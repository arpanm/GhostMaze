import { Maze } from './maze.js';
import { Player } from './player.js';
import { Stone } from './stone.js';
import { Ghost } from './ghost.js';

// --- Configuration ---
const MAZE_COLS = 15;
const MAZE_ROWS = 15;

// --- State ---
let canvas, ctx;
let lastTime = 0;
let maze, player;
let stones = [];
let ghosts = [];
let gameActive = false;
let score = 0;
let health = 100;
let lastStoneTime = 0;
let lastGhostTime = 0;
let stonesCollectedCount = 0;
let stonesDetails = {};
let ghostEscapeScore = 0;

// Input State
const input = {
    up: false,
    down: false,
    left: false,
    right: false
};

// Joystick State
let joystickData = {
    active: false,
    originX: 0,
    originY: 0,
    currentX: 0,
    currentY: 0,
    vectorX: 0,
    vectorY: 0
};

// Audio
let audioCtx;
let alarmOscillator = null;

// User Data
let playerName = "Player";
let playerAvatar = "😎";

// --- Initialization ---
window.onload = () => {
    canvas = document.getElementById('game-canvas');
    ctx = canvas.getContext('2d');

    // Resize handling
    window.addEventListener('resize', resizeCanvas);
    resizeCanvas();

    // UI Bindings
    document.getElementById('start-btn').addEventListener('click', startGame);
    document.getElementById('show-leaderboard-btn').addEventListener('click', showLeaderboard);
    document.getElementById('back-to-start-btn').addEventListener('click', showStartScreen);
    document.getElementById('restart-btn').addEventListener('click', startGame);
    document.getElementById('menu-btn').addEventListener('click', showStartScreen);

    // Avatar Selection
    document.querySelectorAll('.avatar-option').forEach(el => {
        el.addEventListener('click', (e) => {
            document.querySelectorAll('.avatar-option').forEach(opt => opt.classList.remove('selected'));
            e.target.classList.add('selected');
            playerAvatar = e.target.dataset.avatar;
        });
    });

    // Inputs
    setupControls();

    // Start Loop
    requestAnimationFrame(gameLoop);
};

function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
}

function setupControls() {
    // Keyboard
    window.addEventListener('keydown', (e) => {
        if (!gameActive) return;
        switch (e.key) {
            case 'ArrowUp': case 'k': input.up = true; break;
            case 'ArrowDown': case 'j': input.down = true; break;
            case 'ArrowLeft': case 'h': input.left = true; break;
            case 'ArrowRight': case 'l': input.right = true; break;
        }
    });

    window.addEventListener('keyup', (e) => {
        switch (e.key) {
            case 'ArrowUp': case 'k': input.up = false; break;
            case 'ArrowDown': case 'j': input.down = false; break;
            case 'ArrowLeft': case 'h': input.left = false; break;
            case 'ArrowRight': case 'l': input.right = false; break;
        }
    });

    // Joystick
    const zone = document.getElementById('joystick-zone');
    const knob = document.getElementById('joystick-knob');

    const handleStart = (x, y) => {
        if (!gameActive) return;
        joystickData.active = true;

        const rect = zone.getBoundingClientRect();
        // Center of joystick zone
        joystickData.originX = rect.left + rect.width / 2;
        joystickData.originY = rect.top + rect.height / 2;

        handleMove(x, y);
    };

    const handleMove = (x, y) => {
        if (!joystickData.active) return;

        // Prevent scrolling on touch

        let dx = x - joystickData.originX;
        let dy = y - joystickData.originY;

        const radius = 60; // Max radius
        const distance = Math.sqrt(dx * dx + dy * dy);

        if (distance > radius) {
            dx = (dx / distance) * radius;
            dy = (dy / distance) * radius;
        }

        knob.style.transform = `translate(${dx}px, ${dy}px)`;

        // Normalize Vector (-1 to 1)
        joystickData.vectorX = dx / radius;
        joystickData.vectorY = dy / radius;

        // Map to Input
        const threshold = 0.2;
        input.right = joystickData.vectorX > threshold;
        input.left = joystickData.vectorX < -threshold;
        input.down = joystickData.vectorY > threshold;
        input.up = joystickData.vectorY < -threshold;
    };

    const handleEnd = () => {
        joystickData.active = false;
        joystickData.vectorX = 0;
        joystickData.vectorY = 0;
        knob.style.transform = `translate(0px, 0px)`;
        // Reset inputs
        input.up = input.down = input.left = input.right = false;
    };

    // Touch
    zone.addEventListener('touchstart', (e) => {
        e.preventDefault();
        handleStart(e.touches[0].clientX, e.touches[0].clientY);
    });
    zone.addEventListener('touchmove', (e) => {
        e.preventDefault();
        handleMove(e.touches[0].clientX, e.touches[0].clientY);
    });
    zone.addEventListener('touchend', handleEnd);

    // Mouse (for desktop testing of joystick)
    zone.addEventListener('mousedown', (e) => {
        handleStart(e.clientX, e.clientY);
    });
    window.addEventListener('mousemove', (e) => {
        handleMove(e.clientX, e.clientY);
    });
    window.addEventListener('mouseup', handleEnd);
}

// --- Game Logic ---

function startGame() {
    const nameInput = document.getElementById('player-name').value;
    if (nameInput.trim()) playerName = nameInput.trim();

    // Reset State
    gameActive = true;
    score = 0;
    health = 100;
    stones = [];
    ghosts = [];
    lastStoneTime = Date.now();
    lastGhostTime = Date.now();
    stonesCollectedCount = 0;
    stonesDetails = { diamond: 0, ruby: 0, emerald: 0, sapphire: 0 };
    ghostEscapeScore = 0;

    // Gen Maze
    maze = new Maze(MAZE_COLS, MAZE_ROWS);

    // Gen Player (Start at 0,0)
    player = new Player(playerAvatar, 0, 0);

    // Init Audio
    if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    if (audioCtx.state === 'suspended') audioCtx.resume();

    // UI
    document.querySelectorAll('.screen').forEach(s => s.classList.add('hidden'));
    document.getElementById('game-hud').classList.remove('hidden');
    document.getElementById('controls-layer').classList.remove('hidden');
    document.getElementById('alarm-overlay').classList.add('hidden'); // Ensure off
    updateHUD();
}

function updateHUD() {
    const sVal = document.getElementById('score-val');
    const hVal = document.getElementById('health-val');

    if (sVal) sVal.innerText = score;
    if (hVal) hVal.innerText = Math.floor(health);

    // Update individual stone counts
    if (stonesDetails) {
        if (document.getElementById('stone-c-diamond')) document.getElementById('stone-c-diamond').innerText = stonesDetails.diamond;
        if (document.getElementById('stone-c-ruby')) document.getElementById('stone-c-ruby').innerText = stonesDetails.ruby;
        if (document.getElementById('stone-c-emerald')) document.getElementById('stone-c-emerald').innerText = stonesDetails.emerald;
        if (document.getElementById('stone-c-sapphire')) document.getElementById('stone-c-sapphire').innerText = stonesDetails.sapphire;
    }
}


function gameLoop(timestamp) {
    let dt = timestamp - lastTime;
    lastTime = timestamp;

    if (gameActive) {
        update(dt);
        draw();
    }

    requestAnimationFrame(gameLoop);
}

function update(dt) {
    if (!gameActive) return;

    // Health Decay (e.g. 50 seconds to death if idle?)
    // Let's degrade 2 health per second (50s limit)
    health -= (dt / 1000) * 1.5;
    if (health <= 0) {
        health = 0;
        endGame(false, "HEALTH");
        return;
    }
    updateHUD();

    // Calculate Grid Metrics
    let cellSize = Math.min(canvas.width / MAZE_COLS, canvas.height / MAZE_ROWS);
    let offsetX = (canvas.width - MAZE_COLS * cellSize) / 2;
    let offsetY = (canvas.height - MAZE_ROWS * cellSize) / 2;

    // Player
    player.update(input, maze, cellSize, offsetX, offsetY);

    // Check Win (Exit)
    if (player.col === maze.exitCell.c && player.row === maze.exitCell.r) {
        let dx = player.x - (offsetX + (maze.exitCell.c + 0.5) * cellSize);
        let dy = player.y - (offsetY + (maze.exitCell.r + 0.5) * cellSize);
        if (Math.sqrt(dx * dx + dy * dy) < cellSize * 0.4) {
            endGame(true);
            return;
        }
    }

    // Stones
    // Spawn
    if (Date.now() - lastStoneTime > 2000) {
        if (stones.length < 10) {
            let r = Math.floor(Math.random() * MAZE_ROWS);
            let c = Math.floor(Math.random() * MAZE_COLS);
            // Avoid spawning in walls? No, maze logic has walls between cells.
            // Need to ensure it's not player pos
            stones.push(new Stone(c, r));
        }
        lastStoneTime = Date.now();
    }
    // Collect/Expire
    for (let i = stones.length - 1; i >= 0; i--) {
        let s = stones[i];
        if (s.isExpired()) {
            stones.splice(i, 1);
            continue;
        }
        // Collision
        if (s.col === player.col && s.row === player.row) {
            score += s.points;
            stonesCollectedCount++;
            if (stonesDetails[s.data.type] !== undefined) {
                stonesDetails[s.data.type]++;
            }
            stones.splice(i, 1);
        }
    }

    // Ghosts
    // Spawn
    if (Date.now() - lastGhostTime > 5000) {
        if (Math.random() > 0.4) {
            ghosts.push(new Ghost(player.col, player.row, MAZE_COLS, MAZE_ROWS));
            lastGhostTime = Date.now();
        }
    }

    let isChasing = false;
    for (let i = ghosts.length - 1; i >= 0; i--) {
        let g = ghosts[i];
        let wasChasing = (g.state === 'CHASING');
        g.update(dt, player, cellSize, offsetX, offsetY);

        if (g.state === 'DEAD') {
            if (wasChasing) {
                // Ghost just vanished! Calculate bonus.
                // Distance in grid cells
                let dx = player.col - g.col;
                let dy = player.row - g.row;
                let dist = Math.sqrt(dx * dx + dy * dy);
                let bonus = Math.floor(dist * 100);
                score += bonus;
                ghostEscapeScore += bonus;
                // Optional: Show floating text? For now just score update.
            }
            ghosts.splice(i, 1);
            continue;
        }

        if (g.state === 'CHASING') isChasing = true;

        // Touch Player
        if (g.checkCollision(player, cellSize)) {
            endGame(false, "GHOST");
            return;
        }


    }
    updateAlarm(isChasing);
}

function updateAlarm(active) {
    const overlay = document.getElementById('alarm-overlay');
    if (active) {
        if (overlay.classList.contains('hidden')) {
            overlay.classList.remove('hidden');
            startAlarmSound();
        }
    } else {
        if (!overlay.classList.contains('hidden')) {
            overlay.classList.add('hidden');
            stopAlarmSound();
        }
    }
}

function startAlarmSound() {
    if (!audioCtx) return;
    if (alarmOscillator) return;

    try {
        alarmOscillator = audioCtx.createOscillator();
        alarmOscillator.type = 'sawtooth';
        alarmOscillator.frequency.setValueAtTime(440, audioCtx.currentTime);

        // LFO
        const lfo = audioCtx.createOscillator();
        lfo.type = 'sine';
        lfo.frequency.setValueAtTime(5, audioCtx.currentTime); // Faster pulse

        const gain = audioCtx.createGain();
        gain.gain.setValueAtTime(100, audioCtx.currentTime);

        lfo.connect(gain);
        gain.connect(alarmOscillator.frequency);

        const masterGain = audioCtx.createGain();
        masterGain.gain.setValueAtTime(0.05, audioCtx.currentTime);

        alarmOscillator.connect(masterGain);
        masterGain.connect(audioCtx.destination);

        lfo.start();
        alarmOscillator.start();

        alarmOscillator.stopRef = () => {
            alarmOscillator.stop();
            lfo.stop();
        };
    } catch (e) {
        console.warn("Audio error", e);
        alarmOscillator = null;
    }
}

function stopAlarmSound() {
    if (alarmOscillator) {
        try {
            alarmOscillator.stopRef();
        } catch (e) { }
        alarmOscillator = null;
    }
}

function draw() {
    // Clear
    ctx.fillStyle = "#1a1a1a";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    if (!maze) return;

    let res = maze.draw(ctx, canvas.width, canvas.height);
    let { cellSize, offsetX, offsetY } = res;

    stones.forEach(s => s.draw(ctx, cellSize, offsetX, offsetY));
    player.draw(ctx, cellSize, offsetX, offsetY);
    ghosts.forEach(g => g.draw(ctx, cellSize, offsetX, offsetY));
}

function endGame(win, reason = "UNKNOWN") {
    gameActive = false;
    stopAlarmSound();
    updateAlarm(false);

    let finalScore = 0;
    let healthBonus = 0;

    // Always count collected stones as base score
    finalScore = score;

    if (win) {
        healthBonus = Math.floor(health * 1000);
        finalScore += healthBonus;
    } else {
        health = 0;
        healthBonus = 0;
    }

    saveScore(finalScore);

    document.getElementById('game-hud').classList.add('hidden');
    document.getElementById('controls-layer').classList.add('hidden');
    document.getElementById('game-over-screen').classList.remove('hidden');

    let title = "";
    let msg = "";
    let icon = "";

    if (win) {
        title = "YOU ESCAPED!";
        msg = "Successfully Exited the Maze!";
        icon = "🏆";
    } else {
        title = "GAME OVER";
        if (reason === "GHOST") {
            msg = "Ghost Attack! The spirits caught you.";
            icon = "👻";
        } else if (reason === "HEALTH") {
            msg = "Life Over! You ran out of energy.";
            icon = "⏳";
        } else {
            msg = "You succumbed to the maze.";
            icon = "💀";
        }
    }

    document.getElementById('game-result-icon').innerText = icon;
    document.getElementById('game-over-title').innerText = title;
    document.getElementById('game-over-reason').innerText = msg;
    document.getElementById('final-score').innerText = finalScore;


    document.getElementById('end-diamond').innerText = stonesDetails.diamond;
    document.getElementById('end-ruby').innerText = stonesDetails.ruby;
    document.getElementById('end-emerald').innerText = stonesDetails.emerald;
    document.getElementById('end-sapphire').innerText = stonesDetails.sapphire;

    document.getElementById('breakdown-ghosts').innerText = ghostEscapeScore;
    document.getElementById('breakdown-health').innerText = healthBonus;
    updateHUD();
}



// Storage
function saveScore(points) {
    let raw = localStorage.getItem('ghost_maze_leaderboard');
    let data = raw ? JSON.parse(raw) : [];

    // Recalculate healthBonus locally since it's not global
    // Actually we need to pass these or use globals. Global `health` is available.
    // stone points = score.
    // health bonus = points - score.
    // Wait, end game logic: finalScore = score + healthBonus.

    let bonus = Math.max(0, points - score);

    data.push({
        name: playerName,
        avatar: playerAvatar,
        score: points,
        stones: score - ghostEscapeScore,
        ghostBonus: ghostEscapeScore,
        healthBonus: bonus,
        date: new Date().toISOString()
    });

    data.sort((a, b) => b.score - a.score);
    data = data.slice(0, 10);

    localStorage.setItem('ghost_maze_leaderboard', JSON.stringify(data));
}

function showLeaderboard() {
    document.getElementById('start-screen').classList.add('hidden');
    document.getElementById('leaderboard-screen').classList.remove('hidden');

    let list = document.getElementById('leaderboard-list');
    list.innerHTML = '';

    let raw = localStorage.getItem('ghost_maze_leaderboard');
    let data = raw ? JSON.parse(raw) : [];

    if (data.length === 0) {
        list.innerHTML = '<li><span>No records yet</span></li>';
    } else {
        data.forEach((entry, idx) => {
            let li = document.createElement('li');
            // Safe access for old data
            let stoneScore = entry.stones || 0;
            let hpBonus = entry.healthBonus || 0;
            let ghostScore = entry.ghostBonus || 0;

            li.innerHTML = `
                <span>#${idx + 1} ${entry.avatar} ${entry.name}</span>
                <span class="leaderboard-stats">
                    <span title="Stones">💎${stoneScore}</span>
                    <span title="Ghosts">👻${ghostScore}</span>
                    <span title="Health">❤️${hpBonus}</span>
                    <span class="total-score">🌟${entry.score}</span>
                </span>`;
            if (idx === 0) li.style.color = 'gold';
            list.appendChild(li);
        });
    }
}

function showStartScreen() {
    document.querySelectorAll('.screen').forEach(s => s.classList.add('hidden'));
    document.getElementById('start-screen').classList.remove('hidden');
}
