import { Map } from './map.js';
import { Player } from './player.js';
import { Enemy } from './enemy.js';
import { WeaponSystem } from './weapon.js';
import { state, input, CONFIG, DIFFICULTY_SETTINGS } from './shared.js';

// --- Initialization ---
window.onload = () => {
    state.canvas = document.getElementById('game-canvas');
    state.ctx = state.canvas.getContext('2d');

    setupUIListeners();
    setupInputListeners();
    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);
};

function resizeCanvas() {
    state.canvas.width = window.innerWidth;
    state.canvas.height = window.innerHeight;
}

function setupUIListeners() {
    // Start Battle
    document.getElementById('start-btn').addEventListener('click', () => {
        initAudio(); // Initialize audio context on user interaction
        initBattle();
    });

    // Avatar Selection
    document.querySelectorAll('.avatar-option').forEach(el => {
        el.addEventListener('click', (e) => {
            document.querySelectorAll('.avatar-option').forEach(opt => opt.classList.remove('selected'));
            e.target.classList.add('selected');
        });
    });

    // Color Selection
    document.querySelectorAll('.color-option').forEach(el => {
        el.addEventListener('click', (e) => {
            document.querySelectorAll('.color-option').forEach(opt => opt.classList.remove('selected'));
            e.target.classList.add('selected');
        });
    });

    // Difficulty Selection
    document.querySelectorAll('.difficulty-option').forEach(el => {
        el.addEventListener('click', (e) => {
            document.querySelectorAll('.difficulty-option').forEach(opt => opt.classList.remove('selected'));
            e.currentTarget.classList.add('selected');
        });
    });

    // Store
    document.getElementById('open-store-btn').addEventListener('click', () => pauseGame(true));
    document.getElementById('close-store-btn').addEventListener('click', () => pauseGame(false));

    // Store Items
    document.querySelectorAll('.store-item').forEach(item => {
        item.querySelector('button')?.addEventListener('click', () => {
            buyItem(item.dataset.id);
        });
    });

    // Menu Navigation
    document.getElementById('show-leaderboard-btn').addEventListener('click', showLeaderboard);
    document.getElementById('back-to-start-btn').addEventListener('click', () => showScreen('start-screen'));
    document.getElementById('show-credits-btn').addEventListener('click', () => showScreen('credits-screen'));
    document.getElementById('back-from-credits-btn').addEventListener('click', () => showScreen('start-screen'));
    document.getElementById('restart-btn').addEventListener('click', initBattle);
    document.getElementById('menu-btn').addEventListener('click', () => showScreen('start-screen'));
    document.getElementById('clear-leaderboard-btn').addEventListener('click', clearLeaderboard);
}

function clearLeaderboard() {
    if (confirm('Permanently wipe all battle records?')) {
        localStorage.removeItem('ahirs_shooting_leaderboard');
        showLeaderboard();
    }
}

function showScreen(screenId) {
    document.querySelectorAll('.screen').forEach(s => s.classList.add('hidden'));
    document.getElementById(screenId).classList.remove('hidden');
}

function initBattle() {
    const name = document.getElementById('player-name').value.trim();
    if (!name) {
        document.getElementById('name-error').classList.remove('hidden');
        return;
    }

    // Setup State
    state.difficulty = document.querySelector('.difficulty-option.selected').dataset.difficulty;
    const diffCfg = DIFFICULTY_SETTINGS[state.difficulty];

    state.active = true;
    state.paused = false;
    state.projectiles = [];
    state.vaults = [];
    state.decoys = [];
    state.startTime = Date.now();

    // Initialize Classes
    state.map = new Map(diffCfg.vaultCount);
    state.player = new Player({
        name: name,
        avatar: document.querySelector('.avatar-option.selected').dataset.avatar,
        color: document.querySelector('.color-option.selected').dataset.color,
        weapon: WeaponSystem.get('pistol')
    });

    state.enemy = new Enemy({
        difficulty: diffCfg
    });

    // Reset UI
    showScreen('game-hud');
    document.getElementById('controls-layer').classList.remove('hidden');
    updateHUD();

    // Start Loops
    state.lastTime = performance.now();
    requestAnimationFrame(gameLoop);
    startTimer();
}

function pauseGame(paused) {
    state.paused = paused;
    if (paused) {
        showScreen('store-overlay');
        updateStore();
    } else {
        showScreen('game-hud');
    }
}

// --- Game Loop ---
function gameLoop(timestamp) {
    if (!state.active) return;

    const dt = timestamp - state.lastTime;
    state.lastTime = timestamp;

    if (!state.paused) {
        update(dt);
        draw();
    }

    requestAnimationFrame(gameLoop);
}

function update(dt) {
    state.player.update(dt, input, state.map, state.canvas);
    state.enemy.update(dt, state.player, state.map, state.canvas);

    if (state.player.health <= 0) {
        endGame('loss');
        return;
    }
    if (state.enemy.health <= 0) {
        endGame('win');
        return;
    }

    // Update Projectiles
    state.projectiles = state.projectiles.filter(p => !p.dead);
    state.projectiles.forEach(p => p.update(dt, [state.player, state.enemy, ...state.decoys], state.map));

    // Update Decoys
    state.decoys = state.decoys.filter(d => !d.dead);
    state.decoys.forEach(d => d.update(dt, state.map));

    // Collision & Events
    checkMoneyCollection();
    updateHUD();
}

function endGame(result) {
    state.active = false;
    if (state.timerInterval) clearInterval(state.timerInterval);

    showScreen('game-over-screen');

    const hpBonus = result === 'win' ? state.player.health * CONFIG.SURVIVAL_MULTIPLIER : 0;
    const winBonus = result === 'win' ? CONFIG.WIN_BONUS : 0;
    const moneyCollected = state.player.money;
    const weaponValue = state.player.weapon.price;
    const total = hpBonus + winBonus + moneyCollected + weaponValue;

    document.getElementById('game-over-title').innerText = result === 'win' ? 'MISSION ACCOMPLISHED' : 'MISSION FAILED';
    document.getElementById('result-badge').innerText = result === 'win' ? '🏆' : '💀';
    document.getElementById('breakdown-health').innerText = hpBonus;
    document.getElementById('breakdown-win').innerText = winBonus;
    document.getElementById('breakdown-money').innerText = moneyCollected;
    document.getElementById('breakdown-weapon').innerText = weaponValue;
    document.getElementById('total-score').innerText = total;

    saveScore(total, {
        hpBonus, winBonus, moneyCollected, weaponValue,
        difficulty: state.difficulty,
        avatar: state.player.avatar
    });
}

function saveScore(total, details) {
    const raw = localStorage.getItem('ahirs_shooting_leaderboard');
    let data = raw ? JSON.parse(raw) : [];

    data.push({
        name: state.player.name,
        score: total,
        ...details,
        date: new Date().toISOString()
    });

    data.sort((a, b) => b.score - a.score);
    data = data.slice(0, 10);
    localStorage.setItem('ahirs_shooting_leaderboard', JSON.stringify(data));
}

function showLeaderboard() {
    showScreen('leaderboard-screen');
    const list = document.getElementById('leaderboard-list');
    list.innerHTML = '';

    const raw = localStorage.getItem('ahirs_shooting_leaderboard');
    const data = raw ? JSON.parse(raw) : [];

    if (data.length === 0) {
        list.innerHTML = '<li class="no-records">NO BATTLE RECORDS YET</li>';
    } else {
        data.forEach((entry, idx) => {
            const li = document.createElement('li');
            li.innerHTML = `
                <div class="leader-rank">#${idx + 1}</div>
                <div class="leader-info">
                    <strong>${entry.avatar} ${entry.name}</strong>
                    <span>Diff: ${entry.difficulty} • ${new Date(entry.date).toLocaleDateString()}</span>
                </div>
                <div class="leader-score">${entry.score.toLocaleString()}</div>
            `;
            list.appendChild(li);
        });
    }
}

function checkMoneyCollection() {
    state.map.vaults.forEach(v => {
        if (v.collected) return;

        // Player collection
        const distP = Math.sqrt((state.player.x - v.x) ** 2 + (state.player.y - v.y) ** 2);
        if (distP < state.player.radius + v.size) {
            v.collected = true;
            state.player.money += v.amount;
            playMoneySound();
            triggerFlash('collect-flash');
        }

        // Enemy collection
        const distE = Math.sqrt((state.enemy.x - v.x) ** 2 + (state.enemy.y - v.y) ** 2);
        if (distE < state.enemy.radius + v.size) {
            v.collected = true;
            state.enemy.money += v.amount;
        }
    });
}

function triggerFlash(id) {
    const el = document.getElementById(id);
    el.classList.remove('hidden');
    el.classList.add('flash-active');
    setTimeout(() => {
        el.classList.remove('flash-active');
        setTimeout(() => el.classList.add('hidden'), 100);
    }, 100);
}

function buyItem(itemId) {
    const result = WeaponSystem.handlePurchase(state.player.id, itemId, state.player.money);
    if (result.success) {
        state.player.money -= result.cost;
        if (result.type === 'heal') {
            state.player.health = Math.min(100, state.player.health + 10);
        } else if (result.type === 'decoy') {
            state.player.decoyCharges += result.charges;
        } else if (result.type === 'weapon') {
            state.player.weapon = result.item;
        }
        updateStore();
        updateHUD();
        playMoneySound(); // Re-use for feedback
    }
}

function draw() {
    state.ctx.clearRect(0, 0, state.canvas.width, state.canvas.height);

    state.map.draw(state.ctx, state.canvas.width, state.canvas.height);
    state.projectiles.forEach(p => p.draw(state.ctx));
    state.decoys.forEach(d => d.draw(state.ctx));
    state.player.draw(state.ctx);
    state.enemy.draw(state.ctx);
}

// --- Inputs ---
function setupInputListeners() {
    // Keyboard
    window.addEventListener('keydown', e => {
        if (e.key === 'ArrowUp' || e.key === 'w') input.up = true;
        if (e.key === 'ArrowDown' || e.key === 's') input.down = true;
        if (e.key === 'ArrowLeft' || e.key === 'a') input.left = true;
        if (e.key === 'ArrowRight' || e.key === 'd') input.right = true;
        if (e.key === ' ') input.fire = true;
    });

    window.addEventListener('keyup', e => {
        if (e.key === 'ArrowUp' || e.key === 'w') input.up = false;
        if (e.key === 'ArrowDown' || e.key === 's') input.down = false;
        if (e.key === 'ArrowLeft' || e.key === 'a') input.left = false;
        if (e.key === 'ArrowRight' || e.key === 'd') input.right = false;
        if (e.key === ' ') input.fire = false;
    });

    // Desktop: Click to aim/fire
    state.canvas.addEventListener('mousedown', e => {
        if (!state.active || state.paused) return;
        const rect = state.canvas.getBoundingClientRect();
        input.tapPos = { x: e.clientX - rect.left, y: e.clientY - rect.top };
        input.fire = true;
    });

    // Mobile: Joystick
    const zone = document.getElementById('joystick-zone');
    const knob = document.getElementById('joystick-knob');

    const handleJoystick = (e) => {
        if (!state.active || state.paused) return;
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

    const resetJoystick = () => {
        knob.style.transform = 'translate(0, 0)';
        input.joystick.x = 0;
        input.joystick.y = 0;
        input.joystick.active = false;
    };

    zone.addEventListener('touchstart', (e) => { e.preventDefault(); handleJoystick(e); });
    zone.addEventListener('touchmove', (e) => { e.preventDefault(); handleJoystick(e); });
    zone.addEventListener('touchend', resetJoystick);

    // Action Buttons
    document.getElementById('fire-btn')?.addEventListener('touchstart', (e) => {
        e.preventDefault();
        input.fire = true;
    });
    document.getElementById('fire-btn')?.addEventListener('touchend', () => input.fire = false);

    document.getElementById('decoy-btn')?.addEventListener('click', () => {
        if (state.player && state.player.decoyCharges > 0) {
            state.player.spawnDecoy();
        }
    });

    // Global Tap to Shoot
    state.canvas.addEventListener('touchstart', e => {
        if (!state.active || state.paused) return;
        const rect = state.canvas.getBoundingClientRect();
        input.tapPos = { x: e.touches[0].clientX - rect.left, y: e.touches[0].clientY - rect.top };
        input.fire = true;
    });
}

// --- Utils ---
function updateHUD() {
    document.getElementById('user-health-val').innerText = Math.max(0, state.player.health);
    document.getElementById('user-health-bar').style.width = state.player.health + '%';
    document.getElementById('user-money-val').innerText = state.player.money;

    document.getElementById('enemy-health-val').innerText = Math.max(0, state.enemy.health);
    document.getElementById('enemy-health-bar').style.width = state.enemy.health + '%';
    document.getElementById('enemy-money-val').innerText = state.enemy.money;
}

function updateStore() {
    document.getElementById('store-money-val').innerText = state.player.money;
}

function startTimer() {
    if (state.timerInterval) clearInterval(state.timerInterval);
    state.timerInterval = setInterval(() => {
        if (!state.paused && state.active) {
            const elapsed = Date.now() - state.startTime;
            const sec = Math.floor(elapsed / 1000) % 60;
            const min = Math.floor(elapsed / 60000);
            document.querySelector('.battle-timer').innerText =
                `${min.toString().padStart(2, '0')}:${sec.toString().padStart(2, '0')}`;
        }
    }, 1000);
}

// --- Audio ---
let audioCtx = null;

function initAudio() {
    if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    if (audioCtx.state === 'suspended') audioCtx.resume();
}

function playFireSound() {
    if (!audioCtx) return;
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.type = 'sawtooth';
    osc.frequency.setValueAtTime(150, audioCtx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(40, audioCtx.currentTime + 0.1);
    gain.gain.setValueAtTime(0.1, audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.1);
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    osc.start();
    osc.stop(audioCtx.currentTime + 0.1);
}

function playMoneySound() {
    if (!audioCtx) return;
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(880, audioCtx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(1760, audioCtx.currentTime + 0.1);
    gain.gain.setValueAtTime(0.1, audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.2);
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    osc.start();
    osc.stop(audioCtx.currentTime + 0.2);
}

function playHitSound() {
    if (!audioCtx) return;
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.type = 'square';
    osc.frequency.setValueAtTime(100, audioCtx.currentTime);
    gain.gain.setValueAtTime(0.1, audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.1);
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    osc.start();
    osc.stop(audioCtx.currentTime + 0.1);
}

export { playFireSound, playMoneySound, playHitSound };
