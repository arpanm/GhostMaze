import { Game } from './game.js';

import { loadAssets } from './assets.js';
import { economy } from './economy.js';

// Elements
const canvas = document.getElementById('gameCanvas');
const startScreen = document.getElementById('start-screen');
const hud = document.getElementById('hud');
const pauseScreen = document.getElementById('pause-screen');
const gameOverScreen = document.getElementById('game-over-screen');
const touchControls = document.getElementById('touch-controls');

// UI Fields
const speedVal = document.getElementById('speed-val');
const scoreVal = document.getElementById('score-val');
// const takedownVal = ... (Removed, queried dynamically to be safe)
const distVal = document.getElementsByClassName('dist-val'); // if any
const healthFill = document.getElementById('health-fill');
const goScore = document.getElementById('go-score');
const goDistance = document.getElementById('go-distance');

let game;
let gameOptions = {
    name: 'Player',
    difficulty: 'medium',
    terrain: 'hills'
};

// Initialize
(async function init() {
    await loadAssets();

    game = new Game(canvas, {
        onGameOver: handleGameOver,
        onUpdateHud: updateHud,
        onMessage: showMessage
    });

    setupEventListeners();
})();

function setupEventListeners() {
    // Start Button
    document.getElementById('start-btn').addEventListener('click', () => {
        // Economy Check
        if (!economy.hasEnoughBalance(10)) {
            document.getElementById('low-balance-modal').classList.remove('hidden');
            return;
        }

        const name = document.getElementById('player-name').value || 'Racer';
        const diff = document.getElementById('difficulty').value;
        const terrain = document.getElementById('terrain').value;

        gameOptions = { name, difficulty: diff, terrain };
        economy.spendCoins(10, 'Bike Race Entry');
        updateBalanceDisplay();
        startGame();
    });

    document.getElementById('close-low-balance').addEventListener('click', () => {
        document.getElementById('low-balance-modal').classList.add('hidden');
    });

    function updateBalanceDisplay() {
        const el = document.getElementById('menu-coin-balance');
        if (el) el.textContent = economy.getBalance();
    }
    updateBalanceDisplay();

    // Pause / Resume
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' || e.key === 'p') {
            togglePause();
        }
    });

    document.getElementById('resume-btn').addEventListener('click', togglePause);
    document.getElementById('restart-btn').addEventListener('click', () => {
        if (!economy.hasEnoughBalance(10)) {
            document.getElementById('low-balance-modal').classList.remove('hidden');
            return;
        }
        economy.spendCoins(10, 'Bike Race Restart');
        updateBalanceDisplay();
        startGame();
    });
    document.getElementById('exit-btn').addEventListener('click', showMainMenu);

    document.getElementById('go-restart-btn').addEventListener('click', () => {
        if (!economy.hasEnoughBalance(10)) {
            document.getElementById('low-balance-modal').classList.remove('hidden');
            return;
        }
        economy.spendCoins(10, 'Bike Race Restart');
        updateBalanceDisplay();
        startGame();
    });
    document.getElementById('go-home-btn').addEventListener('click', showMainMenu);

    // Navigation Buttons
    document.getElementById('instructions-btn').addEventListener('click', () => showScreen('how-to-play-screen'));
    document.getElementById('back-htp-btn').addEventListener('click', () => showScreen('start-screen'));

    document.getElementById('credits-btn').addEventListener('click', () => showScreen('credits-screen'));
    document.getElementById('back-credits-btn').addEventListener('click', () => showScreen('start-screen'));

    document.getElementById('hall-of-fame-btn').addEventListener('click', () => {
        loadLeaderboard();
        showScreen('leaderboard-screen');
    });
    document.getElementById('back-leaderboard-btn').addEventListener('click', () => showScreen('start-screen'));


    // Keyboard Controls
    window.addEventListener('keydown', (e) => {
        if (!game.running) return;
        switch (e.key) {
            case 'ArrowLeft': game.input.left = true; break;
            case 'ArrowRight': game.input.right = true; break;
            case 'ArrowUp': game.input.up = true; break;
            case 'ArrowDown': game.input.down = true; break;
            case ' ':
                e.preventDefault();
                game.input.attack = true;
                break; // Space to attack/honk
        }
    });

    window.addEventListener('keyup', (e) => {
        switch (e.key) {
            case 'ArrowLeft': game.input.left = false; break;
            case 'ArrowRight': game.input.right = false; break;
            case 'ArrowUp': game.input.up = false; break;
            case 'ArrowDown': game.input.down = false; break;
            case ' ': game.input.attack = false; break;
        }
    });

    // Touch Controls
    setupTouchControls();
}

function showScreen(id) {
    document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
    document.querySelectorAll('.screen').forEach(s => s.classList.add('hidden')); // Add hidden for consistency if used in CSS
    const screen = document.getElementById(id);
    if (screen) {
        screen.classList.add('active');
        screen.classList.remove('hidden');
    }
}

function loadLeaderboard() {
    const list = document.getElementById('leaderboard-list');
    const msg = document.getElementById('no-records-msg');

    // Clear list
    list.innerHTML = '';

    const scores = JSON.parse(localStorage.getItem('ahirs-bike-race-scores') || '[]');

    if (scores.length === 0) {
        msg.style.display = 'block';
        return;
    }

    msg.style.display = 'none';

    scores.forEach((s, i) => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>#${i + 1}</td>
            <td>${s.name}</td>
            <td>${s.score}</td>
            <td>${s.difficulty.toUpperCase()}</td>
        `;
        list.appendChild(tr);
    });
}

function setupTouchControls() {
    // Detect touch device roughly
    if ('ontouchstart' in window || navigator.maxTouchPoints > 0) {
        // touchControls.classList.add('active'); // Don't show immediately
        game.isTouchDevice = true; // Store flag in game object or globally
    }

    const bindTouch = (id, key) => {
        const btn = document.getElementById(id);
        if (!btn) return;
        btn.addEventListener('touchstart', (e) => { e.preventDefault(); game.input[key] = true; });
        btn.addEventListener('touchend', (e) => { e.preventDefault(); game.input[key] = false; });
    };

    // Remaining buttons
    bindTouch('btn-brake', 'down');
    bindTouch('btn-attack', 'attack');

    // === Virtual Joystick ===
    const joyContainer = document.getElementById('joystick-container');
    const joyKnob = document.getElementById('joystick-knob');
    let joyStartX = 0;
    let joyStartY = 0;
    let joyActive = false;
    const maxDist = 35; // Max radius joystick can move

    const handleJoystick = (e) => {
        if (!joyActive) return;
        e.preventDefault(); // Prevent scroll

        const touch = e.changedTouches[0];
        const dx = touch.clientX - joyStartX;
        const dy = touch.clientY - joyStartY;

        // Calculate distance and clamp
        const dist = Math.sqrt(dx * dx + dy * dy);
        let clampedDx = dx;
        let clampedDy = dy;

        if (dist > maxDist) {
            const ratio = maxDist / dist;
            clampedDx = dx * ratio;
            clampedDy = dy * ratio;
        }

        // Move Knob Visual
        joyKnob.style.transform = `translate(calc(-50% + ${clampedDx}px), calc(-50% + ${clampedDy}px))`;

        // Logic Mapping
        // X-Axis -> Steering
        const deadzone = 10;

        game.input.left = false;
        game.input.right = false;
        game.input.up = false;
        game.input.down = false; // Joystick down can brake too?

        if (clampedDx < -deadzone) game.input.left = true;
        else if (clampedDx > deadzone) game.input.right = true;

        // Y-Axis -> Acceleration (Up is Negative Y in screen space usually, check?)
        // Touch Y increases downwards. So Up needs Negative relative Y.
        // Wait, drag UP means smaller Y value.
        // So dy < 0 is UP.
        if (clampedDy < -deadzone) {
            game.input.up = true; // Accelerate
        } else if (clampedDy > deadzone) {
            game.input.down = true; // Brake
        }
    };

    joyContainer.addEventListener('touchstart', (e) => {
        e.preventDefault();
        joyActive = true;
        const touch = e.changedTouches[0];
        joyStartX = touch.clientX;
        joyStartY = touch.clientY;

        // Reset Knob (should be center initially, but if touched slightly off center?)
        // Easier: Just track relative movement from touch start? 
        // Or joystick should snap to finger? 
        // Standard virtual joystick: The center is fixed (static joystick). Touch start usually matters relative to center?
        // Let's implement Static Joystick (container is fixed).
        // Wait, joyStartX should be center of container?
        // Correct.
        const rect = joyContainer.getBoundingClientRect();
        joyStartX = rect.left + rect.width / 2;
        joyStartY = rect.top + rect.height / 2;

        // Immediate update
        handleJoystick(e);
    }, { passive: false });

    joyContainer.addEventListener('touchmove', handleJoystick, { passive: false });

    const resetJoystick = (e) => {
        if (!joyActive) return;
        joyActive = false;
        joyKnob.style.transform = `translate(-50%, -50%)`; // Reset to center
        game.input.left = false;
        game.input.right = false;
        game.input.up = false;
        game.input.down = false;
    };

    joyContainer.addEventListener('touchend', resetJoystick);
    joyContainer.addEventListener('touchcancel', resetJoystick);
}

function startGame() {
    document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
    hud.classList.add('active'); // Actually it's just visible by default z-index, but we keep it clear

    // Config Difficulty
    // In game.js we just store options for now, but we should parse them
    game.start(gameOptions);

    if (game.isTouchDevice) {
        touchControls.classList.add('active');
    }
}

function togglePause() {
    if (!game.running) return;
    game.paused = !game.paused;
    if (game.paused) {
        pauseScreen.classList.add('active');
    } else {
        pauseScreen.classList.remove('active');
        game.lastTime = performance.now(); // Reset time delta to avoid jump
    }
}

function showMainMenu() {
    game.running = false;
    document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
    touchControls.classList.remove('active');
    startScreen.classList.add('active');
}

function handleGameOver(stats) {
    game.running = false;
    hud.classList.remove('active');
    touchControls.classList.remove('active');
    gameOverScreen.classList.add('active');

    const titleIdx = gameOverScreen.querySelector('h2');
    let message = "";
    let color = "white";

    const bustedMessages = [
        "BUSTED! You fought the law and the law won.",
        "PULL OVER! No donuts for you tonight.",
        "BAD BOYS, BAD BOYS! watcha gonna do?",
        "BUSTED! That's a hefty fine."
    ];
    const crashMessages = [
        "WIPEOUT! Ouch, that looked expensive.",
        "CRASHED! Did you forget the brakes?",
        "TOTALED! Maybe try a tricycle next time?",
        "OUCH! The asphalt tastes like defeat."
    ];
    const winMessages = [
        "RACE FINISHED! You are speed!",
        "WINNER! Eat my dust!",
        "CHAMPION! The road is yours.",
        "FINISHED! A legendary performance!"
    ];

    if (stats.reason === "BUSTED") {
        message = bustedMessages[Math.floor(Math.random() * bustedMessages.length)];
        color = "red";
    } else if (stats.reason === "FINISHED") {
        message = winMessages[Math.floor(Math.random() * winMessages.length)];
        color = "#00ff00";
    } else {
        // Crash or other
        message = crashMessages[Math.floor(Math.random() * crashMessages.length)];
        color = "orange";
    }

    titleIdx.innerText = message;
    titleIdx.style.color = color;
    titleIdx.style.fontSize = "1.5rem";

    // Add explicit cause if not just generic game over
    let causeText = "";
    switch (stats.reason) {
        case "CRASHED_STATIC": causeText = "Cause: Hit a Tree/Rock (Health Depleted)"; break;
        case "CRASHED_VEHICLE": causeText = "Cause: Traffic Accident (Health Depleted)"; break;
        case "BUSTED": causeText = "Cause: Caught by Police"; break;
        case "FINISHED": causeText = "Result: Race Completed!"; break;
        default: causeText = `Cause: ${stats.reason}`;
    }

    // Create or update subtitle
    let sub = gameOverScreen.querySelector('.go-reason');
    if (!sub) {
        sub = document.createElement('p');
        sub.className = 'go-reason';
        sub.style.color = '#fff';
        sub.style.marginBottom = '20px';
        titleIdx.after(sub);
    }
    sub.innerText = causeText;

    goScore.innerText = stats.score;
    goDistance.innerText = Math.floor(stats.distance / 1000);

    // Reward Logic - Removed per requirement
    /*
    const coinsEarned = Math.floor(stats.score / 500);
    if (coinsEarned > 0) {
        economy.addCoins(coinsEarned, 'Bike Race Reward');
        updateBalanceDisplay();
    }
    document.querySelector('.final-score').insertAdjacentHTML('beforeend', `<br><span style="color:gold; font-size:1.2rem;">Earned ${coinsEarned} Coins! 🪙</span>`);
    */

    // Detailed Stats
    const goRank = document.getElementById('go-rank');
    const goTakedowns = document.getElementById('go-takedowns');
    const goHealth = document.getElementById('go-health');
    const goPosVal = document.getElementById('pos-val');

    if (goRank) goRank.innerText = stats.rank ? `#${stats.rank}` : 'DNF';
    if (goTakedowns) goTakedowns.innerText = stats.takedowns || 0;
    if (goHealth) goHealth.innerText = stats.healthBonus || 0;
    if (goPosVal) goPosVal.innerText = stats.rank ? `#${stats.rank}/5` : 'DNF';

    // Save High Score (Leaderboard List)
    const newEntry = {
        name: gameOptions.name,
        score: stats.score,
        difficulty: gameOptions.difficulty,
        date: new Date().toLocaleDateString()
    };

    const scores = JSON.parse(localStorage.getItem('ahirs-bike-race-scores') || '[]');
    scores.push(newEntry);

    // Sort by score desc, keep top 10
    scores.sort((a, b) => b.score - a.score);
    const topScores = scores.slice(0, 10);

    localStorage.setItem('ahirs-bike-race-scores', JSON.stringify(topScores));

    // Also update legacy single high score key if needed, or deprecate it. Let's keep it for compatibility if referenced elsewhere.
    const diff = gameOptions.difficulty;
    const key = `roadrash_highscore_${diff}`;
    const highScore = localStorage.getItem(key) || 0;
    if (stats.score > highScore) {
        localStorage.setItem(key, stats.score);
    }
}

function updateHud(data) {
    if (speedVal) speedVal.innerText = data.speed;
    if (scoreVal) scoreVal.innerText = data.score;

    const tkElem = document.getElementById('takedowns-val');
    if (tkElem) tkElem.innerText = data.takedowns || 0;

    const timerVal = document.getElementById('time-val');
    if (timerVal) {
        let mins = Math.floor(game.time / 60);
        let secs = Math.floor(game.time % 60);
        timerVal.innerText = `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
    }

    const posVal = document.getElementById('pos-val');
    let posNo = data.rank ? data.rank : (data.rank || 1); // Pass from game or stats? Game has it.
    if (posVal) posVal.innerText = posNo + '/5';

    // Health Bar
    if (healthFill) {
        let hp = Math.max(0, data.health);
        healthFill.style.width = `${hp}%`;
        if (hp < 30) healthFill.style.background = '#ff0000';
        else healthFill.style.background = 'linear-gradient(90deg, #ff3333, #ffaa00, #00ff00)';
    }
}

function showMessage(text) {
    const msgArea = document.getElementById('message-area');
    if (!msgArea) return;

    msgArea.innerText = text;
    msgArea.style.opacity = 1;

    // Clear after 3 seconds
    setTimeout(() => {
        msgArea.style.opacity = 0;
    }, 3000);
}
