import { InputHandler } from './input.js';
import { Terrain } from './terrain.js';
import { Tank, Plane, Projectile, Structure, Particle } from './entities.js';
import { AIController } from './ai.js';
import { UIManager } from './ui.js';

export class Game {
    constructor() {
        this.canvas = document.getElementById('game-canvas');
        this.ctx = this.canvas.getContext('2d');
        this.resize();

        // Modules
        this.ui = new UIManager();
        this.input = new InputHandler(this.canvas, this);

        // Game State
        this.state = 'START'; // START, PLAY, PAUSE, GAMEOVER, SHOP
        this.lastTime = 0;

        // Game Data
        this.player = { name: 'Commander', color: '#3498db', logo: '🦅' };
        this.difficulty = 'medium';
        this.score = 0;
        this.currency = 0; // Points to buy stuff
        this.kills = 0;

        // World
        this.gravity = 0.2;
        this.wind = 0;
        this.windTimer = 0;

        // Entities
        this.terrain = null;
        // Entities
        this.terrain = null;
        this.units = [];
        this.structures = []; // Static objects drawn first
        this.projectiles = [];
        this.particles = [];

        this.setupEventListeners();
        window.addEventListener('resize', () => this.resize());

        // Initial Loop
        requestAnimationFrame((t) => this.loop(t));
    }

    resize() {
        this.canvas.width = window.innerWidth;
        this.canvas.height = window.innerHeight;
    }

    setupEventListeners() {
        // ... (existing listeners remain same, no change needed here yet) ...
        // UI Buttons
        document.getElementById('start-btn').addEventListener('click', () => this.initGame());
        // ...
        document.getElementById('pause-btn').addEventListener('click', () => this.togglePause());
        document.getElementById('resume-btn').addEventListener('click', () => this.togglePause());
        document.getElementById('restart-btn').addEventListener('click', () => {
            this.togglePause();
            this.initGame();
        });
        document.getElementById('exit-btn').addEventListener('click', () => location.reload());

        document.getElementById('play-again-btn').addEventListener('click', () => this.initGame());

        // Menu Navigation
        document.getElementById('leaderboard-btn').addEventListener('click', () => {
            this.ui.updateLeaderboard(null, 'leaderboard-full-list');
            this.ui.showScreen('leaderboard-screen');
        });
        document.getElementById('back-from-leaderboard').addEventListener('click', () => this.ui.showScreen('start-screen'));

        document.getElementById('credits-btn').addEventListener('click', () => this.ui.showScreen('credits-screen'));
        document.getElementById('back-from-credits').addEventListener('click', () => this.ui.showScreen('start-screen'));

        // Shop
        document.getElementById('shop-btn').addEventListener('click', () => this.toggleShop());
        document.getElementById('close-shop-btn').addEventListener('click', () => this.toggleShop());

        document.querySelectorAll('.shop-item').forEach(item => {
            item.addEventListener('click', () => this.buyItem(item.dataset.type, parseInt(item.dataset.cost)));
        });

        // Config Selectors
        document.querySelectorAll('.color-option').forEach(el => {
            el.addEventListener('click', () => {
                document.querySelectorAll('.color-option').forEach(e => e.classList.remove('selected'));
                el.classList.add('selected');
                this.player.color = el.dataset.color;
                console.log("Selected Color:", this.player.color);
            });
        });

        document.querySelectorAll('.logo-option').forEach(el => {
            el.addEventListener('click', () => {
                document.querySelectorAll('.logo-option').forEach(e => e.classList.remove('selected'));
                el.classList.add('selected');
                this.player.logo = el.dataset.logo;
            });
        });

        document.getElementById('how-to-play-btn').addEventListener('click', () => this.ui.showScreen('how-to-play-screen'));
        document.getElementById('back-from-help').addEventListener('click', () => this.ui.showScreen('start-screen'));
        document.getElementById('back-from-game-over').addEventListener('click', () => this.ui.showScreen('start-screen'));

        document.querySelectorAll('.diff-btn').forEach(el => {
            el.addEventListener('click', () => {
                document.querySelectorAll('.diff-btn').forEach(b => b.classList.remove('selected'));
                el.classList.add('selected');
                this.difficulty = el.dataset.diff;
            });
        });

        // Controls
        document.getElementById('fire-btn').addEventListener('click', () => this.fireSelectedUnit());

        // Manual Move bindings for UI buttons (touch/mouse)
        const updateKey = (code, down) => {
            if (down) this.input.keys[code] = true;
            else delete this.input.keys[code];
        };

        ['mousedown', 'touchstart'].forEach(evt => {
            document.getElementById('move-left').addEventListener(evt, (e) => { e.preventDefault(); updateKey('ArrowLeft', true); });
            document.getElementById('move-right').addEventListener(evt, (e) => { e.preventDefault(); updateKey('ArrowRight', true); });
        });

        ['mouseup', 'touchend', 'mouseleave'].forEach(evt => {
            document.getElementById('move-left').addEventListener(evt, (e) => { e.preventDefault(); updateKey('ArrowLeft', false); });
            document.getElementById('move-right').addEventListener(evt, (e) => { e.preventDefault(); updateKey('ArrowRight', false); });
        });

        // Space to Fire
        window.addEventListener('keydown', (e) => {
            if (e.code === 'Space') {
                this.fireSelectedUnit();
            }
        });
    }

    initGame() {
        const nameInput = document.getElementById('player-name');
        const errorMsg = document.getElementById('name-error');
        const name = nameInput.value.trim();

        if (!name) {
            errorMsg.style.display = 'block';
            nameInput.style.border = '2px solid #e74c3c';
            return; // Stop initialization
        }

        errorMsg.style.display = 'none';
        nameInput.style.border = 'none';
        this.player.name = name;
        // Reset Stats
        this.score = 0;
        this.currency = 500;
        this.kills = 0;
        this.wind = (Math.random() - 0.5) * 2;

        // Create World
        this.terrain = new Terrain(this.canvas.width, this.canvas.height);
        this.units = [];
        this.structures = [];
        this.projectiles = [];

        // Spawn Initial Units
        this.spawnUnit('tank', 'blue', 100);
        this.spawnUnit('plane', 'blue', 150);
        this.spawnUnit('tank', 'red', this.canvas.width - 100);
        this.spawnUnit('plane', 'red', this.canvas.width - 50);

        // Default Selection: Plane
        this.units.forEach(u => {
            if (u.team === 'blue' && u.type === 'plane') {
                u.selected = true;
            } else {
                u.selected = false;
            }
        });

        // Spawn Structures (Smartly) - Enemy (Red)
        for (let i = 0; i < 4; i++) {
            let attempts = 0;
            let success = false;
            while (attempts < 10 && !success) {
                const x = this.canvas.width / 2 + Math.random() * (this.canvas.width / 2 - 100);
                if (this.isSpotClear(x)) {
                    const type = Math.random() > 0.5 ? 'bunker' : 'tower';
                    this.spawnStructure(type, 'red', x);
                    success = true;
                }
                attempts++;
            }
        }

        // Spawn Structures (Smartly) - Friendly (Blue)
        for (let i = 0; i < 3; i++) { // Fewer friendly ones
            let attempts = 0;
            let success = false;
            while (attempts < 10 && !success) {
                const x = 50 + Math.random() * (this.canvas.width / 2 - 150); // Left side
                if (this.isSpotClear(x)) {
                    const type = Math.random() > 0.5 ? 'bunker' : 'tower';
                    this.spawnStructure(type, 'blue', x);
                    success = true;
                }
                attempts++;
            }
        }


        // AI
        this.ai = new AIController(this, this.difficulty);
        this.enemyCurrency = 500;

        this.state = 'PLAY';
        this.ui.showScreen('hud');
        this.ui.updatePlayerLogo(this.player.logo); // Update Logo
        this.ui.updateHUD(this.score, 100, 100, this.wind, this.currency); // Initial HUD update
    }

    // ...

    spawnUnit(type, team, x) {
        let unit;
        let y = this.terrain.getHeightAt(x);

        // Use player custom color/logo if team is blue
        const color = team === 'blue' ? this.player.color : null;
        const logo = team === 'blue' ? this.player.logo : null;

        console.log(`Spawning ${type} for ${team} with color: ${color}, logo: ${logo}, PlayerColor: ${this.player.color}`);

        if (type === 'tank') {
            unit = new Tank(x, y, team, color, logo);
        } else if (type === 'plane') {
            unit = new Plane(x, 0, team, color, logo); // Plane determines its own Y
        }
        this.units.push(unit);
    }

    togglePause() {
        if (this.state === 'PLAY') {
            this.state = 'PAUSE';
            this.ui.showScreen('pause-screen');
        } else if (this.state === 'PAUSE') {
            this.state = 'PLAY';
            this.ui.showScreen('hud');
            this.lastTime = performance.now();
            requestAnimationFrame((t) => this.loop(t));
        }
    }

    toggleShop() {
        if (this.state === 'PLAY') {
            this.state = 'SHOP';
            this.ui.showScreen('shop-screen');
        } else if (this.state === 'SHOP') {
            this.state = 'PLAY';
            this.ui.showScreen('hud');
            this.lastTime = performance.now();
            requestAnimationFrame((t) => this.loop(t));
        }
    }

    buyItem(type, cost) {
        if (this.currency >= cost) {
            this.currency -= cost;
            // Spawn logic
            if (type === 'tank') this.spawnUnit('tank', 'blue', 100);
            if (type === 'plane') this.spawnUnit('plane', 'blue', 150);
            if (type === 'repair') {
                this.units.forEach(u => {
                    if (u.team === 'blue') u.health = Math.min(u.health + 50, u.maxHealth);
                });
            }
            if (type === 'nuke') {
                // Kill all enemies
                this.units.forEach(u => { if (u.team === 'red') u.takeDamage(1000); });
                this.structures.forEach(s => { if (s.team === 'red') s.health = 0; }); // Destroy structures too
            }

            this.ui.updateHUD(this.score, this.getPlayerHealthAvg(), this.getEnemyHealthAvg(), this.wind, this.currency);
            alert("Purchased: " + type);
        } else {
            alert("Not enough funds!");
        }
    }

    isSpotClear(x) {
        const safeDist = 60;
        for (let u of this.units) if (Math.abs(u.x - x) < safeDist) return false;
        for (let s of this.structures) if (Math.abs(s.x - x) < safeDist) return false;
        return true;
    }



    spawnStructure(type, team, x) {
        let y = this.terrain.getHeightAt(x);
        this.structures.push(new Structure(x, y, team, type));
    }


    // Input Hooks
    handleTap(x, y) {
        if (this.state !== 'PLAY') return;

        // Track where drag started for Swipe vs Aim logic
        this.dragStartedOnUnit = false;

        // Selection Logic
        let clickedUnit = null;
        this.units.forEach(u => {
            if (u.team === 'blue') {
                const dist = Math.hypot(u.x - x, u.y - y);
                if (dist < 50) { // Hitbox slightly larger for touch
                    clickedUnit = u;
                }
            }
        });

        if (clickedUnit) {
            this.dragStartedOnUnit = true; // Started on a unit
            // Select it
            this.units.forEach(unit => unit.selected = false);
            clickedUnit.selected = true;
        } else {
            // Tapped empty space
            // Keep selection? Yes.
        }
    }

    handleClick(x, y) {
        if (this.state !== 'PLAY') return;

        const selected = this.units.find(u => u.selected && u.team === 'blue');
        if (selected && selected.type === 'plane') {
            // Tap to drop bomb (if not tapping a button/UI - UI stops propagation usually)
            // But canvas click implies game action.
            this.fireSelectedUnit();
        }
    }

    handleDragRelease(start, end) {
        if (this.state !== 'PLAY') return;

        const selected = this.units.find(u => u.selected && u.team === 'blue');
        if (!selected) return;

        // Only fire if we started dragging ON the tank (Aiming)
        if (selected.type === 'tank' && this.dragStartedOnUnit) {
            const dx = start.x - end.x;
            const dy = start.y - end.y;

            const power = Math.min(Math.hypot(dx, dy) * 0.15, 20);
            const angle = Math.atan2(dy, dx);

            this.fireProjectile(selected, angle, power);
        }
    }

    fireSelectedUnit() {
        const selected = this.units.find(u => u.selected && u.team === 'blue');
        if (!selected) return;

        if (selected.type === 'plane') {
            this.fireProjectile(selected, Math.PI / 2, 0);
        } else if (selected.type === 'tank') {
            // Spacebar for Tank? Standard shot
            this.fireProjectile(selected, -Math.PI / 4, 15);
        }
    }

    fireProjectile(unit, angle, power) {
        // Cooldown check could go here

        let vx = Math.cos(angle) * power;
        let vy = Math.sin(angle) * power;

        // If plane dropping bomb, inherit velocity?
        if (unit.type === 'plane') {
            vx = 0; // Drop straight
            vy = 5; // Faster initial push
        } else {
            // Tank: spawn from turret tip
            // Offset
        }

        this.projectiles.push(new Projectile(unit.x, unit.y - 20, vx, vy, unit.type === 'plane' ? 'bomb' : 'missile', unit.team));
    }

    update(dt) {
        // Wind Dynamics
        this.windTimer += dt;
        if (this.windTimer > 5) { // Every 5 sec change wind
            this.wind += (Math.random() - 0.5) * 0.5;
            // Clamp wind
            this.wind = Math.max(-2, Math.min(2, this.wind));
            this.wind = Math.max(-2, Math.min(2, this.wind));
            this.windTimer = 0;
        }

        // Dynamic Structures (Randomly added)
        if (Math.random() < 0.001) { // Low chance per frame (~once per 16s at 60fps? 0.001 * 60 = 0.06/sec. Wait 1/0.001 frames = 1000 frames = 16s. Reasonable)
            // Enemy Structure
            const type = Math.random() > 0.5 ? 'bunker' : 'tower';
            this.spawnStructure(type, 'red', this.canvas.width / 2 + Math.random() * (this.canvas.width / 2 - 100));
        }

        // AI
        this.ai.update(performance.now());

        // Entities
        this.units = this.units.filter(u => u.alive);
        this.units.forEach(u => {
            // Combine Input for Swipe
            let keys = { ...this.input.keys };
            if (this.input.isDragging && !this.dragStartedOnUnit) {
                const dx = this.input.dragCurrent.x - this.input.dragStart.x;
                if (dx < -20) keys['ArrowLeft'] = true;
                if (dx > 20) keys['ArrowRight'] = true;
            }
            u.update(this.terrain, keys);
        });

        this.structures = this.structures.filter(s => s.alive); // Structures can die too

        // Particles
        this.particles = this.particles.filter(p => p.life > 0);
        this.particles.forEach(p => p.update());

        // Projectiles
        this.projectiles = this.projectiles.filter(p => p.active);
        this.projectiles.forEach(p => {
            p.update(this.gravity, this.wind);

            // Ground Collision
            if (p.x >= 0 && p.x <= this.canvas.width && p.y > this.terrain.getHeightAt(p.x)) {
                p.active = false;
                this.createExplosion(p.x, p.y, '#f1c40f', 10); // Explode on ground
            }

            // Unit Collision
            this.units.forEach(u => {
                // Friendly Fire Check: Only hit enemies
                if (u.alive && u.team !== p.team && Math.abs(u.x - p.x) < 20 && Math.abs(u.y - p.y) < 20) {
                    this.hitUnit(u, p);
                }
            });

            // Structure Collision
            this.structures.forEach(s => {
                // Friendly Fire Check for structures too
                if (s.alive && s.team !== p.team &&
                    p.x > s.x - s.width / 2 && p.x < s.x + s.width / 2 &&
                    p.y > s.y && p.y < s.y + s.height) {
                    this.hitUnit(s, p);
                }
            });

            // Bounds check
            if (p.x < 0 || p.x > this.canvas.width) p.active = false;
        });

        // Win/Loss
        const blueAlive = this.units.some(u => u.team === 'blue');
        // const redAlive = this.units.some(u => u.team === 'red'); // Structures don't count for win condition?
        // Actually destroying everything Red is fun. Let's keep it to Units for now to end game.
        // OR: All red units dead = Win.

        if (!blueAlive) this.gameOver(false); // Loss

        // Red units check
        const redUnitsAlive = this.units.some(u => u.team === 'red');
        const redStructuresAlive = this.structures.some(s => s.team === 'red');

        if (!redUnitsAlive && !redStructuresAlive) {
            this.gameOver(true); // Win!
        } else {
            this.ui.updateHUD(this.score, this.getPlayerHealthAvg(), this.getEnemyHealthAvg(), this.wind, this.currency);
        }
    }

    createExplosion(x, y, color, count = 15) {
        for (let i = 0; i < count; i++) {
            // Random color variation
            let c = color;
            if (color === 'fire') {
                c = Math.random() > 0.5 ? '#f1c40f' : '#e74c3c';
            }
            this.particles.push(new Particle(x, y, c, Math.random() * 5, 30 + Math.random() * 15));
        }
    }

    hitUnit(u, p) {
        const damage = p.type === 'bomb' ? 40 : 20;
        u.takeDamage(damage);
        p.active = false;

        this.createExplosion(p.x, p.y, 'fire', 8); // Small hit

        // Score
        if (u.health <= 0) {
            this.createExplosion(u.x, u.y, 'fire', 40); // Big Explosion
            if (u.team === 'red') {
                let pts = 100;
                if (u.type === 'tank') pts = 200;
                else if (u.type === 'plane') pts = 300;
                else if (u.type === 'bunker') pts = 150;
                else if (u.type === 'tower') pts = 100;

                this.score += pts;
                this.currency += 100;
                if (u.type !== 'bunker' && u.type !== 'tower') this.kills++;
            }
        }
    }

    getPlayerHealthAvg() {
        const units = this.units.filter(u => u.team === 'blue');
        if (units.length === 0) return 0;
        return units.reduce((acc, u) => acc + u.health, 0) / units.length;
    }
    getEnemyHealthAvg() {
        const units = this.units.filter(u => u.team === 'red');
        if (units.length === 0) return 0;
        return units.reduce((acc, u) => acc + u.health, 0) / units.length;
    }

    draw() {
        // Sky
        this.ctx.fillStyle = "#8dc6ff";
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

        // Terrain
        if (this.terrain) this.terrain.draw(this.ctx);

        // Structures (Behind units)
        this.structures.forEach(s => s.draw(this.ctx));

        // Units
        this.units.forEach(u => u.draw(this.ctx));


        // Projectiles
        this.projectiles.forEach(p => p.draw(this.ctx));

        // Particles
        this.particles.forEach(p => p.draw(this.ctx));

        // Aim Line (Drag)
        if (this.input.isDragging && this.state === 'PLAY' && this.dragStartedOnUnit) {
            const selected = this.units.find(u => u.selected && u.team === 'blue');
            if (selected && selected.type === 'tank') {
                this.ctx.strokeStyle = "rgba(255, 255, 255, 0.5)";
                this.ctx.lineWidth = 2;
                this.ctx.beginPath();
                this.ctx.moveTo(selected.x, selected.y - 10);
                // Visualizing aim (Drag back = Shoot forward)
                // Start: DragStart, Cur: DragCurrent. Vector: Cur - Start.
                // Shot Vector: Start - Cur.
                const aimX = this.input.dragStart.x - this.input.dragCurrent.x;
                const aimY = this.input.dragStart.y - this.input.dragCurrent.y;

                this.ctx.lineTo(selected.x + aimX, selected.y - 10 + aimY);
                this.ctx.stroke();
            }
        }
    }

    loop(t) {
        if (this.state === 'PLAY') {
            const dt = (t - this.lastTime) / 1000;
            this.update(dt || 0.016);
            this.draw();
        }
        this.lastTime = t;
        requestAnimationFrame((t) => this.loop(t));
    }

    gameOver(win) {
        this.state = 'GAMEOVER';

        const survivalBonus = win ? this.getPlayerHealthAvg() * 10 : 0;
        const economyBonus = this.currency;
        const totalScore = Math.floor(this.score + survivalBonus + economyBonus);

        // Save Score
        const record = {
            name: this.player.name,
            logo: this.player.logo,
            score: totalScore,
            diff: this.difficulty,
            date: new Date().toISOString()
        };

        const key = 'AhirsWarZone_Leaderboard';
        const scores = JSON.parse(localStorage.getItem(key) || '[]');
        scores.push(record);
        localStorage.setItem(key, JSON.stringify(scores));

        // Update Screens
        if (win) {
            document.getElementById('game-over-title').textContent = "MISSION ACCOMPLISHED";
            document.getElementById('game-over-title').style.color = "#2ecc71";
        } else {
            document.getElementById('game-over-title').textContent = "MISSION FAILED";
            document.getElementById('game-over-title').style.color = "#e74c3c";
        }

        this.ui.updateGameOverScreen(this.kills, this.score, Math.floor(survivalBonus), economyBonus, totalScore);
        this.ui.showScreen('game-over-screen');
    }
}

// Start
window.addEventListener('load', () => {
    new Game();
});
