import { economy } from './economy.js';
import { STORY, getLevelData, CHAPTERS } from './story.js';
import { getWeapon, STORE_ITEMS, applyMod, WEAPONS } from './weapons.js';
import { Player, Teammate, Enemy, Pet, Projectile } from './entities.js';
import { FriendlyAI, EnemyAI } from './ai.js';
import { GameMap } from './map.js';

const STATE = { canvas: null, ctx: null };
let game = null;

class Game {
    constructor() {
        STATE.canvas = document.getElementById('game-canvas');
        STATE.ctx = STATE.canvas.getContext('2d');
        this.resize();
        window.addEventListener('resize', () => this.resize());

        this.screen = 'start';
        this.currentLevel = 0;
        this.totalScore = 0;
        this.totalKills = 0;
        this.totalCoins = 0;
        this.paused = false;
        this.active = false;
        this.lastTime = 0;
        this.keys = {};
        this.joystick = { active: false, x: 0, y: 0 };
        this.aimPos = null;
        this.config = { name: 'Commander', avatar: '🪖', petCount: 1, difficulty: 'medium', teamNames: [] };

        // Game entities
        this.player = null;
        this.teammates = [];
        this.enemies = [];
        this.pets = [];
        this.enemyPets = [];
        this.projectiles = [];
        this.map = null;
        this.camera = { x: 0, y: 0 };
        this.friendlyAI = new FriendlyAI();
        this.enemyAI = new EnemyAI();
        this.levelTimer = 0;

        this.setupUI();
        this.setupInput();
        this.updateBalanceDisplay();
    }

    resize() {
        STATE.canvas.width = window.innerWidth;
        STATE.canvas.height = window.innerHeight;
    }

    // ---- UI SETUP ----
    setupUI() {
        // Start button
        document.getElementById('start-btn').addEventListener('click', () => this.handleStart());
        document.getElementById('close-low-balance').addEventListener('click', () => {
            document.getElementById('low-balance-modal').classList.add('hidden');
        });

        // Menu nav
        document.getElementById('how-to-play-btn').addEventListener('click', () => this.showScreen('how-to-play-screen'));
        document.getElementById('legends-btn').addEventListener('click', () => { this.populateLegends(); this.showScreen('legends-screen'); });
        document.getElementById('credits-btn').addEventListener('click', () => this.showScreen('credits-screen'));
        document.querySelectorAll('.back-btn').forEach(b => b.addEventListener('click', () => this.showScreen('start-screen')));

        // In-game
        document.getElementById('pause-btn').addEventListener('click', () => this.togglePause());
        document.getElementById('resume-btn').addEventListener('click', () => this.togglePause());
        document.getElementById('quit-btn').addEventListener('click', () => location.reload());
        document.getElementById('store-btn').addEventListener('click', () => this.openStore());
        document.getElementById('close-store-btn').addEventListener('click', () => this.closeStore());

        // Game over
        document.getElementById('restart-btn').addEventListener('click', () => {
            if (!economy.hasEnoughBalance(10)) {
                document.getElementById('low-balance-modal').classList.remove('hidden');
                return;
            }
            economy.spendCoins(10, 'Gun World Restart');
            this.updateBalanceDisplay();
            this.currentLevel = 0;
            this.totalScore = 0;
            this.totalKills = 0;
            this.startLevel();
        });
        document.getElementById('menu-btn').addEventListener('click', () => location.reload());

        // Story continue
        document.getElementById('story-continue-btn').addEventListener('click', () => this.startLevel());

        // Avatar selection
        document.querySelectorAll('.avatar-option').forEach(el => {
            el.addEventListener('click', () => {
                document.querySelectorAll('.avatar-option').forEach(o => o.classList.remove('selected'));
                el.classList.add('selected');
            });
        });

        // Difficulty
        document.querySelectorAll('.difficulty-option').forEach(el => {
            el.addEventListener('click', () => {
                document.querySelectorAll('.difficulty-option').forEach(o => o.classList.remove('selected'));
                el.classList.add('selected');
            });
        });

        // Vehicle buttons
        document.getElementById('vehicle-car')?.addEventListener('click', () => this.toggleVehicle('car'));
        document.getElementById('vehicle-plane')?.addEventListener('click', () => this.toggleVehicle('plane'));
        document.getElementById('vehicle-sub')?.addEventListener('click', () => this.toggleVehicle('sub'));
        document.getElementById('shield-btn')?.addEventListener('click', () => { if (this.player) this.player.activateShield(); });

        // Store items
        document.getElementById('store-grid')?.addEventListener('click', (e) => {
            const btn = e.target.closest('.buy-btn');
            if (!btn) return;
            const itemId = btn.dataset.id;
            this.buyItem(itemId);
        });

        // Mobile fire
        document.getElementById('fire-btn')?.addEventListener('touchstart', (e) => { e.preventDefault(); this.mobileFireStart(); });
        document.getElementById('fire-btn')?.addEventListener('touchend', () => this.mobileFireEnd());
    }

    handleStart() {
        const nameInput = document.getElementById('player-name');
        const name = nameInput.value.trim();
        if (!name) {
            document.getElementById('name-error').classList.remove('hidden');
            return;
        }
        document.getElementById('name-error').classList.add('hidden');

        if (!economy.hasEnoughBalance(10)) {
            document.getElementById('low-balance-modal').classList.remove('hidden');
            return;
        }
        economy.spendCoins(10, 'Gun World Entry');
        this.updateBalanceDisplay();

        this.config.name = name;
        this.config.avatar = document.querySelector('.avatar-option.selected')?.dataset?.avatar || '🪖';
        this.config.petCount = parseInt(document.getElementById('pet-count')?.value || '1');
        if (this.config.petCount < 1) this.config.petCount = 1;
        if (this.config.petCount > 2) this.config.petCount = 2;
        this.config.difficulty = document.querySelector('.difficulty-option.selected')?.dataset?.difficulty || 'medium';

        this.currentLevel = 0;
        this.totalScore = 0;
        this.totalKills = 0;

        // Show opening story
        this.showStory(STORY.opening, 'MISSION BRIEFING');
    }

    showStory(text, title) {
        document.getElementById('story-title').textContent = title || 'INTEL';
        document.getElementById('story-text').textContent = text;
        this.showScreen('story-screen');
    }

    startLevel() {
        const levelData = getLevelData(this.currentLevel);
        if (levelData.chapterIntro) {
            // Show chapter intro first, then start actual level
            document.getElementById('story-title').textContent = `Chapter ${levelData.chapterIndex + 1}: ${levelData.chapterName}`;
            document.getElementById('story-text').textContent = levelData.chapterIntro + '\n\n📋 ' + levelData.title + ': ' + levelData.brief;
            document.getElementById('story-continue-btn').onclick = () => this.initLevel(levelData);
            this.showScreen('story-screen');
            return;
        }
        this.initLevel(levelData);
    }

    initLevel(levelData) {
        // Create map
        this.map = new GameMap(1600, 1200, levelData.terrain, levelData.levelIndex);

        // Spawn player
        const greenSpawn = this.map.getSpawnPos('green');
        this.player = new Player(greenSpawn.x, greenSpawn.y, this.config.name, this.config.avatar);

        // Spawn teammates
        this.teammates = [];
        const teamNames = ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot', 'Golf'];
        for (let i = 0; i < 7; i++) {
            const t = new Teammate(
                greenSpawn.x + (i % 4 - 1.5) * 35,
                greenSpawn.y + Math.floor(i / 4) * 35 + 30,
                teamNames[i], i
            );
            this.teammates.push(t);
        }

        // Spawn enemies
        this.enemies = [];
        const redSpawn = this.map.getSpawnPos('red');
        for (let i = 0; i < levelData.enemyCount; i++) {
            const isBoss = levelData.isBoss && i === 0;
            const bossNames = ['Commander Fang', 'General Blaze', 'Admiral Depth', 'Dr. Frost', 'Warlord Steel', 'The Scar'];
            const name = isBoss ? bossNames[levelData.chapterIndex] : `Red-${i + 1}`;
            const ex = redSpawn.x + (Math.random() - 0.5) * 200;
            const ey = redSpawn.y + (Math.random() - 0.5) * 200;
            this.enemies.push(new Enemy(ex, ey, levelData.diffMultiplier, isBoss, name));
        }

        // Spawn pets
        this.pets = [];
        for (let i = 0; i < this.config.petCount; i++) {
            this.pets.push(new Pet(greenSpawn.x + 20, greenSpawn.y + 20 + i * 20, 'green'));
        }
        this.enemyPets = [new Pet(redSpawn.x - 20, redSpawn.y, 'red')];

        this.projectiles = [];
        this.levelTimer = 0;
        this.active = true;
        this.paused = false;

        // Update HUD
        document.getElementById('level-display').textContent = `Lv.${levelData.levelIndex + 1}: ${levelData.title}`;
        document.getElementById('chapter-display').textContent = levelData.chapterName;

        this.showScreen('game-hud');
        this.lastTime = performance.now();
        requestAnimationFrame((t) => this.loop(t));
    }

    // ---- INPUT ----
    setupInput() {
        window.addEventListener('keydown', (e) => {
            this.keys[e.code] = true;
            if (e.code === 'Escape') this.togglePause();
            if (e.code === 'KeyQ') this.toggleVehicle('car');
            if (e.code === 'KeyE') this.toggleVehicle('plane');
            if (e.code === 'KeyR') this.toggleVehicle('sub');
            if (e.code === 'KeyF') { if (this.player) this.player.activateShield(); }
        });
        window.addEventListener('keyup', (e) => this.keys[e.code] = false);

        // Mouse aim/fire
        STATE.canvas.addEventListener('mousedown', (e) => {
            if (!this.active || this.paused) return;
            const rect = STATE.canvas.getBoundingClientRect();
            this.aimPos = { x: e.clientX - rect.left + this.camera.x, y: e.clientY - rect.top + this.camera.y };
            this.firing = true;
        });
        STATE.canvas.addEventListener('mousemove', (e) => {
            if (!this.firing) return;
            const rect = STATE.canvas.getBoundingClientRect();
            this.aimPos = { x: e.clientX - rect.left + this.camera.x, y: e.clientY - rect.top + this.camera.y };
        });
        STATE.canvas.addEventListener('mouseup', () => this.firing = false);

        // Touch aim/fire on canvas
        STATE.canvas.addEventListener('touchstart', (e) => {
            if (!this.active || this.paused) return;
            const rect = STATE.canvas.getBoundingClientRect();
            this.aimPos = { x: e.touches[0].clientX - rect.left + this.camera.x, y: e.touches[0].clientY - rect.top + this.camera.y };
            this.firing = true;
        }, { passive: true });
        STATE.canvas.addEventListener('touchend', () => this.firing = false);

        // Joystick
        const zone = document.getElementById('joystick-zone');
        const knob = document.getElementById('joystick-knob');
        if (zone && knob) {
            const handleJoystick = (cx, cy) => {
                const rect = zone.getBoundingClientRect();
                const centerX = rect.left + rect.width / 2;
                const centerY = rect.top + rect.height / 2;
                let dx = cx - centerX, dy = cy - centerY;
                const dist = Math.hypot(dx, dy);
                const maxDist = 40;
                if (dist > maxDist) { dx = (dx / dist) * maxDist; dy = (dy / dist) * maxDist; }
                knob.style.transform = `translate(${dx}px, ${dy}px)`;
                this.joystick.x = dx / maxDist;
                this.joystick.y = dy / maxDist;
                this.joystick.active = true;
            };
            const resetJoystick = () => {
                knob.style.transform = 'translate(0,0)';
                this.joystick = { active: false, x: 0, y: 0 };
            };
            zone.addEventListener('touchstart', (e) => { e.preventDefault(); handleJoystick(e.touches[0].clientX, e.touches[0].clientY); }, { passive: false });
            zone.addEventListener('touchmove', (e) => { e.preventDefault(); handleJoystick(e.touches[0].clientX, e.touches[0].clientY); }, { passive: false });
            zone.addEventListener('touchend', resetJoystick);
        }
    }

    mobileFireStart() {
        if (!this.active || this.paused || !this.player) return;
        // Fire in the direction player is facing
        this.firing = true;
        this.aimPos = {
            x: this.player.x + Math.cos(this.player.angle) * 200,
            y: this.player.y + Math.sin(this.player.angle) * 200
        };
    }
    mobileFireEnd() { this.firing = false; }

    toggleVehicle(mode) {
        if (!this.player) return;
        this.player.vehicleMode = this.player.vehicleMode === mode ? null : mode;
    }

    // ---- GAME LOOP ----
    loop(timestamp) {
        if (!this.active) return;
        const dt = timestamp - this.lastTime;
        this.lastTime = timestamp;
        if (dt > 100) { requestAnimationFrame((t) => this.loop(t)); return; }
        if (!this.paused) {
            this.update(dt);
            this.draw();
        }
        requestAnimationFrame((t) => this.loop(t));
    }

    update(dt) {
        const now = performance.now();
        this.levelTimer += dt;

        // Player movement
        let dx = 0, dy = 0;
        if (this.keys['ArrowUp'] || this.keys['KeyW']) dy -= 1;
        if (this.keys['ArrowDown'] || this.keys['KeyS']) dy += 1;
        if (this.keys['ArrowLeft'] || this.keys['KeyA']) dx -= 1;
        if (this.keys['ArrowRight'] || this.keys['KeyD']) dx += 1;
        if (this.joystick.active) { dx = this.joystick.x; dy = this.joystick.y; }
        if (dx !== 0 || dy !== 0) {
            const mag = Math.hypot(dx, dy);
            this.player.move(dx / mag, dy / mag, this.map);
            this.player.angle = Math.atan2(dy, dx);
        }

        // Player fire
        if (this.firing && this.aimPos && this.player.alive) {
            this.player.fire(now, this.aimPos.x, this.aimPos.y, this.projectiles);
        }

        this.player.update(dt);

        // All entities for collision
        const allGreen = [this.player, ...this.teammates.filter(t => t.alive), ...this.pets.filter(p => p.alive)];
        const allRed = [...this.enemies.filter(e => e.alive), ...this.enemyPets.filter(p => p.alive)];
        const allEntities = [...allGreen, ...allRed];

        // Friendly AI
        for (const t of this.teammates) {
            this.friendlyAI.update(dt, t, this.player, this.enemies, this.projectiles, this.map, now);
        }

        // Enemy AI
        for (const e of this.enemies) {
            this.enemyAI.update(dt, e, allGreen, this.projectiles, this.map, now);
        }

        // Pets
        for (const pet of this.pets) pet.update(dt, this.player, allRed, this.map);
        for (const pet of this.enemyPets) {
            const nearestRed = this.enemies.find(e => e.alive);
            if (nearestRed) pet.update(dt, nearestRed, allGreen, this.map);
        }

        // Projectiles
        this.projectiles = this.projectiles.filter(p => p.alive);
        for (const p of this.projectiles) p.update(dt, allEntities, this.map);

        // Loot collection
        for (const loot of this.map.lootCrates) {
            if (loot.collected) continue;
            if (Math.hypot(this.player.x - loot.x, this.player.y - loot.y) < 20) {
                loot.collected = true;
                if (loot.type === 'health') this.player.heal(20);
                else if (loot.type === 'coins') { this.player.coins += 100; this.totalCoins += 100; }
            }
        }

        // Kill tracking
        for (const e of this.enemies) {
            if (!e.alive && !e._counted) {
                e._counted = true;
                this.player.coins += 50;
                this.totalCoins += 50;
                this.totalKills++;
                this.player.kills++;
                this.totalScore += e.isBoss ? 500 : 100;
            }
        }

        // Camera follow
        const targetCamX = this.player.x - STATE.canvas.width / 2;
        const targetCamY = this.player.y - STATE.canvas.height / 2;
        this.camera.x += (targetCamX - this.camera.x) * 0.08;
        this.camera.y += (targetCamY - this.camera.y) * 0.08;

        // Update HUD
        this.updateHUD();

        // Win/Loss check
        if (!this.player.alive) {
            this.endGame(false, 'You were eliminated!');
        } else if (this.enemies.every(e => !e.alive)) {
            this.levelComplete();
        }
    }

    levelComplete() {
        this.active = false;
        const levelData = getLevelData(this.currentLevel);
        const timeBonus = Math.max(0, 300 - Math.floor(this.levelTimer / 1000)) * 10;
        this.totalScore += timeBonus;

        if (levelData.storyAfter) {
            // Chapter end story
            this.currentLevel++;
            if (levelData.isFinalLevel) {
                this.showStory(STORY.ending, 'THE END');
                document.getElementById('story-continue-btn').onclick = () => this.endGame(true, 'All 30 levels completed!');
            } else {
                this.showStory(levelData.storyAfter, `${levelData.title} — Complete`);
                document.getElementById('story-continue-btn').onclick = () => this.startLevel();
            }
        } else {
            this.currentLevel++;
            if (this.currentLevel >= 30) {
                this.showStory(STORY.ending, 'THE END');
                document.getElementById('story-continue-btn').onclick = () => this.endGame(true, 'All 30 levels completed!');
            } else {
                // Brief level transition
                const next = getLevelData(this.currentLevel);
                this.showStory(`✅ Level complete! Score: +${timeBonus} time bonus\n\nNext: ${next.title}\n${next.brief}`, 'MISSION UPDATE');
                document.getElementById('story-continue-btn').onclick = () => this.startLevel();
            }
        }
    }

    endGame(won, reason) {
        this.active = false;
        const title = document.getElementById('result-title');
        const icon = document.getElementById('result-icon');
        const msg = document.getElementById('result-message');

        title.textContent = won ? 'MISSION ACCOMPLISHED' : 'MISSION FAILED';
        title.style.color = won ? '#2ecc71' : '#e74c3c';
        icon.textContent = won ? '🏆' : '💀';
        msg.textContent = reason;

        document.getElementById('final-score').textContent = this.totalScore;
        document.getElementById('final-kills').textContent = this.totalKills;
        document.getElementById('final-level').textContent = `Level ${this.currentLevel + 1} / 30`;
        document.getElementById('final-coins').textContent = this.totalCoins;

        this.saveScore(won);
        this.showScreen('game-over-screen');
    }

    saveScore(won) {
        const scores = JSON.parse(localStorage.getItem('ahirs_gunworld_scores') || '[]');
        scores.push({
            name: this.config.name,
            score: this.totalScore,
            kills: this.totalKills,
            level: this.currentLevel + 1,
            won,
            date: new Date().toISOString()
        });
        scores.sort((a, b) => b.score - a.score);
        if (scores.length > 20) scores.length = 20;
        localStorage.setItem('ahirs_gunworld_scores', JSON.stringify(scores));
    }

    // ---- STORE ----
    openStore() {
        this.paused = true;
        const grid = document.getElementById('store-grid');
        grid.innerHTML = '';
        document.getElementById('store-coins').textContent = this.player.coins;
        for (const item of STORE_ITEMS) {
            const owned = item.type === 'weapon' && this.player.inventory.find(w => w.id === item.id);
            const div = document.createElement('div');
            div.className = 'store-item';
            div.innerHTML = `
                <div class="item-icon">${item.symbol}</div>
                <div class="item-info"><h4>${item.name}</h4><p>${item.desc}</p><span class="price">${item.cost} coins</span></div>
                <button class="buy-btn" data-id="${item.id}" ${owned ? 'disabled' : ''}>${owned ? 'OWNED' : 'BUY'}</button>
            `;
            grid.appendChild(div);
        }
        this.showScreen('store-screen');
    }

    closeStore() {
        this.paused = false;
        this.showScreen('game-hud');
        this.lastTime = performance.now();
    }

    buyItem(itemId) {
        const item = STORE_ITEMS.find(i => i.id === itemId);
        if (!item || this.player.coins < item.cost) return;
        this.player.coins -= item.cost;

        if (item.type === 'weapon') {
            const w = getWeapon(itemId);
            this.player.addWeapon(w);
            this.player.equipWeapon(itemId);
        } else if (item.type === 'mod') {
            this.player.weapon = applyMod(this.player.weapon, itemId);
        } else if (itemId === 'heal') {
            this.player.heal(30);
        } else if (itemId === 'shield_boost') {
            this.player.shield = this.player.maxShield;
        } else if (itemId === 'pet_heal') {
            for (const p of this.pets) p.heal(50);
        }
        document.getElementById('store-coins').textContent = this.player.coins;
        this.openStore(); // Refresh store
    }

    // ---- DRAW ----
    draw() {
        const ctx = STATE.ctx;
        const cw = STATE.canvas.width;
        const ch = STATE.canvas.height;

        ctx.fillStyle = '#111';
        ctx.fillRect(0, 0, cw, ch);

        // Map
        this.map.draw(ctx, this.camera.x, this.camera.y, cw, ch);

        // Entities
        for (const t of this.teammates) t.draw(ctx, this.camera.x, this.camera.y);
        for (const e of this.enemies) e.draw(ctx, this.camera.x, this.camera.y);
        for (const p of this.pets) p.draw(ctx, this.camera.x, this.camera.y);
        for (const p of this.enemyPets) p.draw(ctx, this.camera.x, this.camera.y);
        this.player.draw(ctx, this.camera.x, this.camera.y);

        // Projectiles
        for (const p of this.projectiles) p.draw(ctx, this.camera.x, this.camera.y);

        // Crosshair
        if (this.aimPos) {
            const ax = this.aimPos.x - this.camera.x;
            const ay = this.aimPos.y - this.camera.y;
            ctx.strokeStyle = 'rgba(255,255,255,0.4)';
            ctx.lineWidth = 1;
            ctx.beginPath();
            ctx.moveTo(ax - 10, ay); ctx.lineTo(ax + 10, ay);
            ctx.moveTo(ax, ay - 10); ctx.lineTo(ax, ay + 10);
            ctx.stroke();
        }
    }

    // ---- HUD ----
    updateHUD() {
        if (!this.player) return;
        document.getElementById('health-val').textContent = Math.max(0, Math.floor(this.player.health));
        document.getElementById('health-bar').style.width = this.player.health + '%';
        document.getElementById('shield-val').textContent = Math.max(0, Math.floor(this.player.shield));
        document.getElementById('shield-bar').style.width = (this.player.shield / this.player.maxShield * 100) + '%';
        document.getElementById('coins-val').textContent = this.player.coins;
        document.getElementById('kills-val').textContent = this.player.kills;
        document.getElementById('weapon-val').textContent = this.player.weapon.name;
        document.getElementById('vehicle-val').textContent = this.player.vehicleMode ? this.player.vehicleMode.toUpperCase() : 'NONE';

        const alive = this.enemies.filter(e => e.alive).length;
        document.getElementById('enemies-val').textContent = `${alive}`;

        // Timer
        const sec = Math.floor(this.levelTimer / 1000);
        const min = Math.floor(sec / 60);
        document.getElementById('timer-val').textContent = `${min.toString().padStart(2, '0')}:${(sec % 60).toString().padStart(2, '0')}`;

        // Pet status
        const petEl = document.getElementById('pet-status');
        if (petEl) {
            petEl.textContent = this.pets.filter(p => p.alive).map(p => `🐕${Math.floor(p.health)}`).join(' ');
        }

        // Team alive count
        const teamAlive = this.teammates.filter(t => t.alive).length + 1;
        document.getElementById('team-val').textContent = `${teamAlive}/8`;
    }

    togglePause() {
        if (this.screen === 'game-hud') {
            this.paused = true;
            this.showScreen('pause-screen');
        } else if (this.screen === 'pause-screen') {
            this.paused = false;
            this.showScreen('game-hud');
            this.lastTime = performance.now();
        }
    }

    populateLegends() {
        const tbody = document.getElementById('legends-body');
        if (!tbody) return;
        tbody.innerHTML = '';
        const scores = JSON.parse(localStorage.getItem('ahirs_gunworld_scores') || '[]');
        if (scores.length === 0) {
            tbody.innerHTML = '<tr><td colspan="5" style="text-align:center;padding:20px;">No records yet</td></tr>';
            return;
        }
        scores.slice(0, 10).forEach((s, i) => {
            const tr = document.createElement('tr');
            tr.innerHTML = `<td>#${i + 1}</td><td>${s.name}</td><td>${s.score}</td><td>Lv.${s.level}</td><td>${s.won ? '🏆' : '💀'}</td>`;
            tbody.appendChild(tr);
        });
    }

    showScreen(id) {
        this.screen = id;
        document.querySelectorAll('.screen').forEach(s => s.classList.add('hidden'));
        const el = document.getElementById(id);
        if (el) el.classList.remove('hidden');
        // Show/hide canvas
        if (id === 'game-hud') {
            document.getElementById('game-canvas-wrap').classList.remove('hidden');
            document.getElementById('mobile-controls').classList.remove('hidden');
        } else {
            document.getElementById('game-canvas-wrap').classList.add('hidden');
            document.getElementById('mobile-controls').classList.add('hidden');
        }
    }

    updateBalanceDisplay() {
        const el = document.getElementById('menu-coin-balance');
        if (el) el.textContent = economy.getBalance();
    }
}

window.addEventListener('load', () => { game = new Game(); });
