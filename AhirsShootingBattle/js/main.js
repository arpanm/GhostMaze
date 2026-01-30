import { Map } from './map.js';
import { Player } from './player.js';
import { Enemy } from './enemy.js';
import { WeaponSystem } from './weapon.js';
import { state, input, CONFIG, DIFFICULTY_SETTINGS } from './shared.js';
import { economy } from './economy.js';

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
        // Economy Check
        if (!economy.hasEnoughBalance(10)) {
            document.getElementById('low-balance-modal').classList.remove('hidden');
            return;
        }

        initAudio(); // Initialize audio context on user interaction
        economy.spendCoins(10, 'Shooting Battle Entry');
        updateBalanceDisplay();
        initBattle();
    });

    document.getElementById('close-low-balance').addEventListener('click', () => {
        document.getElementById('low-balance-modal').classList.add('hidden');
    });

    function updateBalanceDisplay() {
        const el = document.getElementById('menu-coin-balance');
        if (el) el.textContent = economy.getBalance();
    }
    updateBalanceDisplay();

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
    document.getElementById('restart-btn').addEventListener('click', () => {
        if (!economy.hasEnoughBalance(10)) {
            document.getElementById('low-balance-modal').classList.remove('hidden');
            return;
        }
        economy.spendCoins(10, 'Shooting Battle Restart');
        updateBalanceDisplay();
        initBattle();
    });
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
    state.vaultSpawnTimer = 0;
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

    // Dynamic Vaults
    state.map.update(dt);
    state.vaultSpawnTimer += dt;
    if (state.vaultSpawnTimer > 5000) { // Every 5 seconds
        state.vaultSpawnTimer = 0;
        state.map.spawnVault(500 + Math.floor(Math.random() * 1000), 15000); // New vaults last 15s
    }
}

function endGame(result) {
    state.active = false;
    if (state.timerInterval) clearInterval(state.timerInterval);

    showScreen('game-over-screen');

    const hpBonus = result === 'win' ? state.player.health * CONFIG.SURVIVAL_MULTIPLIER : 0;
    const winBonus = result === 'win' ? CONFIG.WIN_BONUS : 0;
    const moneyCollected = state.player.money;
    const weaponValue = state.player.weaponValue || 0;
    const total = hpBonus + winBonus + moneyCollected + weaponValue;

    document.getElementById('game-over-title').innerText = result === 'win' ? 'MISSION ACCOMPLISHED' : 'MISSION FAILED';
    document.getElementById('result-badge').innerText = result === 'win' ? '🏆' : '💀';
    document.getElementById('breakdown-health').innerText = hpBonus;
    document.getElementById('breakdown-win').innerText = winBonus;
    document.getElementById('breakdown-money').innerText = moneyCollected;
    document.getElementById('breakdown-weapon').innerText = weaponValue;
    document.getElementById('total-score').innerText = total;

    // Reward Logic - Removed per requirement
    /*
    const coinsEarned = Math.floor(total / 500);
    if (coinsEarned > 0) {
        economy.addCoins(coinsEarned, 'Shooting Battle Reward');
        updateBalanceDisplay();
    }
    document.getElementById('game-over-reason').insertAdjacentHTML('beforeend', `<br><span style="color:gold; font-size:1.2rem;">Earned ${coinsEarned} Coins! 🪙</span>`);
    */

    saveScore(total, {
        hpBonus, winBonus, moneyCollected, weaponValue,
        difficulty: state.difficulty,
        avatar: state.player.avatar,
        color: state.player.color,
        weapon: state.player.weapon.name,
        name: state.player.name
    });
}

function saveScore(total, details) {
    const raw = localStorage.getItem('ahirs_shooting_leaderboard');
    let data = raw ? JSON.parse(raw) : [];

    data.push({
        name: details.name || 'UNKNOWN SOLDIER',
        score: total || 0,
        hpBonus: details.hpBonus || 0,
        winBonus: details.winBonus || 0,
        moneyCollected: details.moneyCollected || 0,
        weaponValue: details.weaponValue || 0,
        difficulty: details.difficulty || 'medium',
        avatar: details.avatar || '🪖',
        date: new Date().toISOString()
    });

    data.sort((a, b) => b.score - a.score);
    data = data.slice(0, 10);
    localStorage.setItem('ahirs_shooting_leaderboard', JSON.stringify(data));
}

function showLeaderboard() {
    showScreen('leaderboard-screen');
    const tableBody = document.getElementById('leaderboard-body');
    tableBody.innerHTML = '';

    const raw = localStorage.getItem('ahirs_shooting_leaderboard');
    const data = raw ? JSON.parse(raw) : [];

    if (data.length === 0) {
        tableBody.innerHTML = '<tr><td colspan="6" class="no-records">NO BATTLE RECORDS YET</td></tr>';
    } else {
        data.forEach((entry, idx) => {
            if (!entry) return;
            const row = document.createElement('tr');

            // Format bonuses for display with safe checks
            const hpBN = (entry.hpBonus || 0).toLocaleString();
            const winBN = (entry.winBonus || 0).toLocaleString();
            const econ = ((entry.moneyCollected || 0) + (entry.weaponValue || 0)).toLocaleString();
            const totalScore = (entry.score || 0).toLocaleString();
            const soldierName = entry.name || 'SOLDIER';
            const difficulty = entry.difficulty || 'Unknown';
            const dateStr = entry.date ? new Date(entry.date).toLocaleDateString() : 'Unknown Date';

            row.innerHTML = `
                <td class="rank-cell">#${idx + 1}</td>
                <td class="soldier-cell">
                    <span>${entry.avatar || '🪖'}</span>
                    <div>
                        <strong>${soldierName}</strong>
                        <div style="font-size: 0.6rem; color: var(--text-muted)">${difficulty} • ${dateStr}</div>
                    </div>
                </td>
                <td class="bonus-cell">${hpBN}</td>
                <td class="bonus-cell">${winBN}</td>
                <td class="bonus-cell">${econ}</td>
                <td class="total-cell">${totalScore}</td>
            `;
            tableBody.appendChild(row);
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
        if (result.type === 'heal') {
            state.player.money -= result.cost;
            state.player.health = Math.min(100, state.player.health + 10);
        } else if (result.type === 'decoy') {
            state.player.money -= result.cost;
            state.player.decoyCharges += result.charges;
        } else if (result.type === 'weapon') {
            const isOwned = state.player.inventory.find(w => w.id === itemId);
            if (!isOwned) {
                state.player.money -= result.cost;
                state.player.weaponValue = (state.player.weaponValue || 0) + result.item.price;
                state.player.addWeapon(result.item);
            }
            state.player.equipWeapon(itemId);
        }
        updateStore();
        updateHUD();
        playMoneySound();
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
        if (e.key === 'e' || e.key === 'E') {
            if (state.player && state.player.decoyCharges > 0) {
                state.player.spawnDecoy();
            }
        }
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

    // Update Decoy Count
    const decoyCountEl = document.getElementById('decoy-count');
    if (decoyCountEl) decoyCountEl.innerText = state.player.decoyCharges;
    const topDecoyCountEl = document.getElementById('top-decoy-count');
    if (topDecoyCountEl) topDecoyCountEl.innerText = state.player.decoyCharges;

    document.getElementById('enemy-health-val').innerText = Math.max(0, state.enemy.health);
    document.getElementById('enemy-health-bar').style.width = state.enemy.health + '%';
    document.getElementById('enemy-money-val').innerText = state.enemy.money;

    // Update Top HUD Weapon Display
    const weaponDisp = document.getElementById('user-weapon-disp');
    if (weaponDisp && state.player) {
        weaponDisp.innerText = state.player.weapon.name;
    }

    // Update Weapon Inventory Selector
    const invHud = document.getElementById('weapon-inventory-hud');
    if (invHud && state.player) {
        invHud.innerHTML = '';
        state.player.inventory.forEach(weapon => {
            const div = document.createElement('div');
            div.className = `inventory-item ${state.player.weapon.id === weapon.id ? 'active' : ''}`;
            div.innerText = weapon.symbol;
            div.title = weapon.name;
            div.onclick = (e) => {
                e.stopPropagation();
                state.player.equipWeapon(weapon.id);
                updateHUD();
                playMoneySound(); // Feedback for switch
            };
            invHud.appendChild(div);
        });
    }
}

function updateStore() {
    const playerMoney = state.player.money;
    document.getElementById('store-money-val').innerText = playerMoney.toLocaleString();

    document.querySelectorAll('.store-item').forEach(item => {
        const type = item.dataset.id;
        const price = parseInt(item.dataset.price);
        const buyBtn = item.querySelector('.buy-btn');

        // Clear existing messages
        const oldMsg = item.querySelector('.insufficient-funds-msg');
        if (oldMsg) oldMsg.remove();

        const isOwned = state.player.inventory.find(w => w.id === type);
        const isActive = state.player.weapon.id === type;

        if (type !== 'heal' && type !== 'decoy' && isOwned) {
            if (isActive) {
                buyBtn.innerText = 'EQUIPPED';
                buyBtn.className = 'buy-btn equipped';
                buyBtn.style.opacity = '0.5';
                buyBtn.style.cursor = 'default';
            } else {
                buyBtn.innerText = 'EQUIP';
                buyBtn.className = 'buy-btn equip';
                buyBtn.style.opacity = '1';
                buyBtn.style.cursor = 'pointer';
            }
        } else if (playerMoney < price) {
            buyBtn.innerText = type === 'heal' ? 'HEAL' : 'BUY';
            buyBtn.className = 'buy-btn';
            buyBtn.style.opacity = '0.5';
            buyBtn.style.cursor = 'not-allowed';

            const msg = document.createElement('div');
            msg.className = 'insufficient-funds-msg';
            msg.innerText = 'Collect more fund to buy';
            item.appendChild(msg);
        } else {
            buyBtn.innerText = type === 'heal' ? 'HEAL' : 'BUY';
            buyBtn.className = 'buy-btn';
            buyBtn.style.opacity = '1';
            buyBtn.style.cursor = 'pointer';
        }
    });
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

import { initAudio, playFireSound, playMoneySound, playHitSound } from './audio.js';
export { initAudio, playFireSound, playMoneySound, playHitSound };
