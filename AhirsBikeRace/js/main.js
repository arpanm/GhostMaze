import { Game } from './game.js';
import { loadAssets } from './assets.js';

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
        const name = document.getElementById('player-name').value || 'Racer';
        const diff = document.getElementById('difficulty').value;
        const terrain = document.getElementById('terrain').value;

        gameOptions = { name, difficulty: diff, terrain };
        startGame();
    });

    // Pause / Resume
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' || e.key === 'p') {
            togglePause();
        }
    });

    document.getElementById('resume-btn').addEventListener('click', togglePause);
    document.getElementById('restart-btn').addEventListener('click', startGame);
    document.getElementById('exit-btn').addEventListener('click', showMainMenu);

    document.getElementById('go-restart-btn').addEventListener('click', startGame);
    document.getElementById('go-home-btn').addEventListener('click', showMainMenu);

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

function setupTouchControls() {
    // Detect touch device roughly
    if ('ontouchstart' in window || navigator.maxTouchPoints > 0) {
        touchControls.classList.add('active');
    }

    const bindTouch = (id, key) => {
        const btn = document.getElementById(id);
        btn.addEventListener('touchstart', (e) => { e.preventDefault(); game.input[key] = true; });
        btn.addEventListener('touchend', (e) => { e.preventDefault(); game.input[key] = false; });
    };

    bindTouch('btn-left', 'left');
    bindTouch('btn-right', 'right');
    bindTouch('btn-accel', 'up');
    bindTouch('btn-brake', 'down');
    bindTouch('btn-attack', 'attack');
}

function startGame() {
    startScreen.classList.remove('active');
    pauseScreen.classList.remove('active');
    gameOverScreen.classList.remove('active');
    hud.classList.add('active'); // Actually it's just visible by default z-index, but we keep it clear

    // Config Difficulty
    // In game.js we just store options for now, but we should parse them
    game.start(gameOptions);
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
    pauseScreen.classList.remove('active');
    gameOverScreen.classList.remove('active');
    startScreen.classList.add('active');
}

function handleGameOver(stats) {
    game.running = false;
    hud.classList.remove('active');
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

    // Save High Score
    const diff = gameOptions.difficulty;
    const key = `roadrash_highscore_${diff}`;
    const highScore = localStorage.getItem(key) || 0;
    if (stats.score > highScore) {
        localStorage.setItem(key, stats.score);
        // Show New Record msg?
    }
}

function updateHud(data) {
    speedVal.innerText = data.speed;
    scoreVal.innerText = data.score;
    document.getElementById('pos-val').innerText = '1/12'; // Mock position for now

    // Health Bar
    healthFill.style.width = `${data.health}%`;
    if (data.health < 30) healthFill.style.background = '#ff0000';
    else healthFill.style.background = 'linear-gradient(90deg, #ff3333, #ffaa00, #00ff00)';
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
