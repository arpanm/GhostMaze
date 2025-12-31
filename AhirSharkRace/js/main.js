import { state, CONFIG, input } from './shared.js';
import { Shark } from './shark.js';
import { Sea } from './sea.js';
import { playSound } from './audio.js';

// --- Initialization ---
function init() {
    state.canvas = document.getElementById('game-canvas');
    state.ctx = state.canvas.getContext('2d');
    resize();
    window.addEventListener('resize', resize);

    setupUI();
    setupInput();
}

function resize() {
    state.canvas.width = window.innerWidth;
    state.canvas.height = window.innerHeight;
}

function setupUI() {
    const startBtn = document.getElementById('start-btn');
    const nameInput = document.getElementById('player-name');
    const nameError = document.getElementById('name-error');

    // Color/Logo Pickers
    document.querySelectorAll('.color-opt').forEach(opt => {
        opt.onclick = () => {
            document.querySelectorAll('.color-opt').forEach(o => o.classList.remove('active'));
            opt.classList.add('active');
        };
    });

    document.querySelectorAll('.logo-opt').forEach(opt => {
        opt.onclick = () => {
            document.querySelectorAll('.logo-opt').forEach(o => o.classList.remove('active'));
            opt.classList.add('active');
        };
    });

    // Difficulty
    document.querySelectorAll('.diff-btn').forEach(btn => {
        btn.onclick = () => {
            document.querySelectorAll('.diff-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            state.difficulty = CONFIG.diffs[btn.dataset.diff];
        };
    });

    startBtn.onclick = () => {
        if (!nameInput.value.trim()) {
            nameError.classList.remove('hidden');
            return;
        }

        const color = document.querySelector('.color-opt.active').dataset.color;
        const logo = document.querySelector('.logo-opt.active').dataset.logo;

        startGame(nameInput.value, color, logo);
    };

    document.getElementById('leaderboard-btn').onclick = () => showLeaderboard();
    document.getElementById('credits-btn').onclick = () => {
        document.getElementById('start-screen').classList.add('hidden');
        document.getElementById('credits-screen').classList.remove('hidden');
    };
    document.getElementById('back-from-credits-btn').onclick = () => {
        document.getElementById('credits-screen').classList.add('hidden');
        document.getElementById('start-screen').classList.remove('hidden');
    };
    document.getElementById('back-to-start-btn').onclick = () => {
        document.getElementById('leaderboard-screen').classList.add('hidden');
        document.getElementById('start-screen').classList.remove('hidden');
    };

    document.getElementById('clear-leaderboard-btn').onclick = () => {
        if (confirm('Are you sure you want to wipe all aquatic records?')) {
            localStorage.removeItem('ahir_shark_race_records');
            showLeaderboard();
        }
    };

    // Game Over / Restart Listeners
    document.getElementById('restart-btn').onclick = () => {
        state.active = false;
        startGame(state.player.name, state.player.color, state.player.logo);
    };
    document.getElementById('menu-btn').onclick = () => {
        location.reload();
    };
}

function setupInput() {
    // Keyboard
    window.addEventListener('keydown', e => {
        if (e.key === 'ArrowUp' || e.key === 'w') input.up = true;
        if (e.key === 'ArrowDown' || e.key === 's') input.down = true;
        if (e.key === 'ArrowLeft' || e.key === 'a') input.left = true;
        if (e.key === 'ArrowRight' || e.key === 'd') input.right = true;
    });
    window.addEventListener('keyup', e => {
        if (e.key === 'ArrowUp' || e.key === 'w') input.up = false;
        if (e.key === 'ArrowDown' || e.key === 's') input.down = false;
        if (e.key === 'ArrowLeft' || e.key === 'a') input.left = false;
        if (e.key === 'ArrowRight' || e.key === 'd') input.right = false;
    });

    // Mobile Joystick
    const zone = document.getElementById('joystick-zone');
    const knob = document.getElementById('joystick-knob');

    const handleJoystick = (e) => {
        const rect = zone.getBoundingClientRect();
        const centerX = rect.left + rect.width / 2;
        const centerY = rect.top + rect.height / 2;

        let clientX = e.touches ? e.touches[0].clientX : e.clientX;
        let clientY = e.touches ? e.touches[0].clientY : e.clientY;

        let dx = clientX - centerX;
        let dy = clientY - centerY;
        const dist = Math.sqrt(dx * dx + dy * dy);
        const maxDist = 40;

        if (dist > maxDist) {
            dx = (dx / dist) * maxDist;
            dy = (dy / dist) * maxDist;
        }

        knob.style.transform = `translate(${dx}px, ${dy}px)`;
        input.joystick.x = dx / maxDist;
        input.joystick.y = dy / maxDist;
        input.joystick.active = true;
    };

    zone.addEventListener('touchstart', (e) => {
        e.preventDefault();
        handleJoystick(e);
    });
    zone.addEventListener('touchmove', (e) => {
        e.preventDefault();
        handleJoystick(e);
    });
    zone.addEventListener('touchend', () => {
        knob.style.transform = 'translate(0, 0)';
        input.joystick.active = false;
    });
}

function startGame(name, color, logo) {
    state.active = true;
    state.score = 0;
    state.distanceTravelled = 0;
    state.entities = [];
    state.enemies = [];

    state.player = new Shark({ name, color, logo, isPlayer: true });
    state.sea = new Sea();

    // Spawn AI Competitors
    for (let i = 0; i < 3; i++) {
        state.enemies.push(new Shark({
            name: `AI Shark ${i + 1}`,
            color: '#7f8c8d',
            logo: '🦈',
            y: (window.innerHeight / 4) * (i + 1),
            x: -100 // Start from behind
        }));
    }

    document.getElementById('start-screen').classList.add('hidden');
    document.getElementById('game-over-screen').classList.add('hidden');
    document.getElementById('game-hud').classList.remove('hidden');
    document.getElementById('controls-layer').classList.remove('hidden');

    requestAnimationFrame(gameLoop);
}

function gameLoop(timestamp) {
    if (!state.active) return;

    const dt = timestamp - state.lastTime;
    state.lastTime = timestamp;

    update(dt);
    draw();

    requestAnimationFrame(gameLoop);
}

function update(dt) {
    if (isNaN(dt)) return;

    // Update Player & Sea
    const pSpeed = state.player.currentSpeed;
    state.player.update(dt, input);
    state.sea.update(dt, pSpeed);

    state.distanceTravelled += pSpeed;

    // Update Competitors
    state.enemies.forEach(e => e.update(dt, {}));

    // Update Entities & Collisions
    state.entities.forEach(entity => {
        entity.update(dt, pSpeed);

        // Collision with Shark
        const dx = entity.x - state.player.x;
        const dy = entity.y - state.player.y;
        const dist = Math.sqrt(dx * dx + dy * dy);

        if (dist < state.player.radius + entity.radius) {
            handleCollision(entity);
        }
    });

    state.entities = state.entities.filter(e => !e.dead);

    updateHUD();
    checkEndConditions();
}

function handleCollision(entity) {
    if (entity.dead) return;

    if (entity.isDangerous) {
        state.player.takeDamage(entity.damage);
        playSound('hit');
    } else {
        state.player.eat(entity.points, entity.hpValue);
        playSound('eat');
    }
    entity.dead = true;
}

function updateHUD() {
    document.getElementById('user-health-bar').style.width = state.player.health + '%';
    document.getElementById('user-health-val').innerText = Math.round(state.player.health);
    document.getElementById('user-score-val').innerText = Math.floor(state.score);
    document.getElementById('speed-val').innerText = Math.round(state.player.currentSpeed * 10);

    const progress = (state.distanceTravelled / CONFIG.raceDistance) * 100;
    document.getElementById('race-progress').style.width = Math.min(100, progress) + '%';
}

function checkEndConditions() {
    if (state.player.dead) {
        endGame('EATEN BY THE OCEAN', 'Your HP reached zero...');
    } else if (state.distanceTravelled >= CONFIG.raceDistance) {
        // Winning bonus
        state.score += state.difficulty.finishBonus;
        endGame('RACE WON!', 'You crossed the finish line first!');
    }
}

function endGame(title, reason) {
    state.active = false;
    document.getElementById('game-over-screen').classList.remove('hidden');
    document.getElementById('game-over-title').innerText = title;
    document.getElementById('game-over-reason').innerText = reason;

    document.getElementById('breakdown-health').innerText = state.player.health * 10;
    document.getElementById('breakdown-fish').innerText = state.score - (state.distanceTravelled >= CONFIG.raceDistance ? state.difficulty.finishBonus : 0);
    document.getElementById('breakdown-finish').innerText = state.distanceTravelled >= CONFIG.raceDistance ? state.difficulty.finishBonus : 0;
    document.getElementById('total-score').innerText = (state.player.health * 10) + state.score;

    saveScore();
}

function saveScore() {
    const total = (state.player.health * 10) + state.score;
    const records = JSON.parse(localStorage.getItem('ahir_shark_race_records') || '[]');
    records.push({
        name: state.player.name,
        health: state.player.health,
        score: state.score,
        finishBonus: state.distanceTravelled >= CONFIG.raceDistance ? state.difficulty.finishBonus : 0,
        total: total,
        date: new Date().toLocaleDateString()
    });
    records.sort((a, b) => b.total - a.total);
    localStorage.setItem('ahir_shark_race_records', JSON.stringify(records.slice(0, 10)));
}

function draw() {
    state.ctx.clearRect(0, 0, state.canvas.width, state.canvas.height);

    state.sea.draw(state.ctx);
    state.entities.forEach(e => e.draw(state.ctx));
    state.enemies.forEach(e => e.draw(state.ctx));
    state.player.draw(state.ctx);
}

init();

function showLeaderboard() {
    document.getElementById('start-screen').classList.add('hidden');
    document.getElementById('leaderboard-screen').classList.remove('hidden');

    const body = document.getElementById('leaderboard-body');
    const records = JSON.parse(localStorage.getItem('ahir_shark_race_records') || '[]');

    body.innerHTML = records.map((r, i) => `
        <tr>
            <td>${i + 1}</td>
            <td>${r.name}</td>
            <td>${r.health * 10}</td>
            <td>${r.score - (r.finishBonus || 0)}</td>
            <td>${r.finishBonus || 0}</td>
            <td class="total-cell">${r.total}</td>
        </tr>
    `).join('');
}
