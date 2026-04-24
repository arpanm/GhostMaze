export class Game {
    constructor(ui, economy) {
        this.ui = ui;
        this.economy = economy;
        this.canvas = document.getElementById('game-canvas');
        this.ctx = this.canvas.getContext('2d');
        
        this.tileSize = 40;
        this.mapWidth = 50;
        this.mapHeight = 50;
        
        this.state = 'idle'; // idle, playing, paused, gameover
        this.lastTime = 0;
        this.camera = { x: 0, y: 0 };
        
        // Input
        this.keys = {};
        window.addEventListener('keydown', e => this.keys[e.code] = true);
        window.addEventListener('keyup', e => this.keys[e.code] = false);

        // Bind resize
        window.addEventListener('resize', () => this.resizeCanvas());
        this.resizeCanvas();
    }

    resizeCanvas() {
        if (!this.canvas) return;
        this.canvas.width = window.innerWidth;
        this.canvas.height = window.innerHeight;
    }

    start(config) {
        this.config = config;
        
        // Setup stats based on difficulty
        const diffMult = config.difficulty === 'hard' ? 1.5 : (config.difficulty === 'medium' ? 1 : 0.5);
        this.stats = {
            score: 0,
            health: 100,
            maxHealth: 100,
            time: 0,
            hazardDamage: 10 * diffMult,
            botSpeed: 1.5 * diffMult
        };

        this.generateMap();
        this.spawnEntities();
        
        this.startTime = Date.now();
        this.lastHintTime = Date.now();
        this.state = 'playing';
        this.ui.showScreen('game');
        
        requestAnimationFrame((t) => this.loop(t));
    }

    generateMap() {
        this.map = Array(this.mapHeight).fill(0).map(() => Array(this.mapWidth).fill(0)); // 0 = wall
        
        // Simple random walk to carve paths
        let x = Math.floor(this.mapWidth / 2);
        let y = Math.floor(this.mapHeight / 2);
        let floorCount = 0;
        const targetFloorCount = (this.mapWidth * this.mapHeight) * 0.4;
        
        this.map[y][x] = 1; // 1 = floor
        floorCount++;
        
        const dirs = [[0,1],[1,0],[0,-1],[-1,0]];
        
        while(floorCount < targetFloorCount) {
            const d = dirs[Math.floor(Math.random() * dirs.length)];
            x += d[0];
            y += d[1];
            
            // Keep in bounds with margin
            x = Math.max(2, Math.min(this.mapWidth - 3, x));
            y = Math.max(2, Math.min(this.mapHeight - 3, y));
            
            if (this.map[y][x] === 0) {
                this.map[y][x] = 1;
                floorCount++;
            }
        }
        
        this.floorTiles = [];
        for(let r = 0; r < this.mapHeight; r++) {
            for(let c = 0; c < this.mapWidth; c++) {
                if (this.map[r][c] === 1) this.floorTiles.push({x: c, y: r});
            }
        }
    }

    getRandomFloorPos() {
        return this.floorTiles[Math.floor(Math.random() * this.floorTiles.length)];
    }

    spawnEntities() {
        this.items = [];
        this.hazards = [];
        this.bots = [];

        // Spawn Player close to center
        let pPos = this.getClosestFloor(Math.floor(this.mapWidth/2), Math.floor(this.mapHeight/2));
        this.player = {
            x: pPos.x * this.tileSize + this.tileSize/2,
            y: pPos.y * this.tileSize + this.tileSize/2,
            speed: 4,
            radius: 12
        };

        // Spawn Main Treasure far away
        const farTiles = this.floorTiles.filter(t => Math.hypot(t.x - pPos.x, t.y - pPos.y) > 20);
        const tPos = farTiles.length > 0 ? farTiles[Math.floor(Math.random() * farTiles.length)] : this.getRandomFloorPos();
        this.items.push({ type: 'treasure', x: tPos.x * this.tileSize + this.tileSize/2, y: tPos.y * this.tileSize + this.tileSize/2, radius: 15 });

        // Spawn Potions & Coins
        for(let i=0; i<15; i++) {
            let pos = this.getRandomFloorPos();
            this.items.push({ type: 'coin', x: pos.x * this.tileSize + this.tileSize/2, y: pos.y * this.tileSize + this.tileSize/2, radius: 8 });
        }
        for(let i=0; i<8; i++) {
            let pos = this.getRandomFloorPos();
            this.items.push({ type: 'potion', x: pos.x * this.tileSize + this.tileSize/2, y: pos.y * this.tileSize + this.tileSize/2, radius: 10 });
        }

        // Spawn Hazards (Traps and Ghosts)
        for(let i=0; i<10; i++) {
            let pos = this.getRandomFloorPos();
            this.hazards.push({ type: 'trap', x: pos.x * this.tileSize + this.tileSize/2, y: pos.y * this.tileSize + this.tileSize/2, radius: 15 });
        }
        for(let i=0; i<5; i++) {
            let pos = this.getRandomFloorPos();
            this.hazards.push({ 
                type: 'ghost', 
                x: pos.x * this.tileSize + this.tileSize/2, 
                y: pos.y * this.tileSize + this.tileSize/2, 
                radius: 14,
                vx: (Math.random()-0.5)*2,
                vy: (Math.random()-0.5)*2
            });
        }

        // Spawn Bots
        for(let i=0; i < this.config.opponents; i++) {
            let pos = this.getRandomFloorPos();
            this.bots.push({
                x: pos.x * this.tileSize + this.tileSize/2,
                y: pos.y * this.tileSize + this.tileSize/2,
                radius: 12,
                vx: 0, vy: 0,
                target: null // Will pathfind to treasure or random
            });
        }
    }

    getClosestFloor(cx, cy) {
        let best = this.floorTiles[0];
        let minDist = Infinity;
        for(let t of this.floorTiles) {
            let d = Math.hypot(t.x - cx, t.y - cy);
            if(d < minDist) { minDist = d; best = t; }
        }
        return best;
    }

    togglePause() {
        if (this.state === 'playing') {
            this.state = 'paused';
            this.ui.showPauseMenu();
        } else if (this.state === 'paused') {
            this.state = 'playing';
            this.ui.hidePauseMenu();
            this.lastTime = performance.now();
            requestAnimationFrame((t) => this.loop(t));
        }
    }

    endGame(success, reason) {
        this.state = 'gameover';
        
        let finalScore = this.stats.score;
        if (success) {
            // Time bonus
            let timeBonus = Math.max(0, 300 - this.stats.time) * 10;
            finalScore += 5000 + timeBonus; // 5000 for winning
            this.economy.addCoins(50, "Treasure Found!");
        }

        this.saveScore(finalScore, success);

        this.ui.showGameOver({
            success,
            message: reason,
            score: finalScore,
            time: this.stats.time
        });
    }

    saveScore(score, win) {
        const scores = JSON.parse(localStorage.getItem('ahirs_treasure_scores') || '[]');
        scores.push({
            name: this.config.name,
            score: score,
            win: win,
            date: new Date().toISOString()
        });
        localStorage.setItem('ahirs_treasure_scores', JSON.stringify(scores));
    }

    loop(timestamp) {
        if (this.state !== 'playing') return;
        
        const dt = (timestamp - this.lastTime) / 1000;
        this.lastTime = timestamp;
        
        if (dt > 0.1) {
            requestAnimationFrame((t) => this.loop(t));
            return; // Prevent huge jumps
        }

        this.update(dt);
        this.render();

        if (this.state === 'playing') {
            requestAnimationFrame((t) => this.loop(t));
        }
    }

    update(dt) {
        this.stats.time = Math.floor((Date.now() - this.startTime) / 1000);

        // Hint Logic
        if (Date.now() - this.lastHintTime > 15000) {
            const mainTreasure = this.items.find(i => i.type === 'treasure');
            let msgs = [
                "Keep exploring! Watch out for ghosts.",
                "Potions will restore your health.",
                "Bots are also looking for the treasure!"
            ];
            if (mainTreasure) {
                let dx = mainTreasure.x - this.player.x;
                let dy = mainTreasure.y - this.player.y;
                let dirX = dx > 0 ? 'East' : 'West';
                let dirY = dy > 0 ? 'South' : 'North';
                if (Math.abs(dx) > Math.abs(dy)) {
                   msgs.push(`My compass points ${dirX}!`);
                } else {
                   msgs.push(`I feel a chill from the ${dirY}!`);
                }
            }
            let hint = msgs[Math.floor(Math.random() * msgs.length)];
            this.ui.showHint(hint);
            this.lastHintTime = Date.now();
        }

        this.updatePlayer(dt);
        this.updateBots(dt);
        this.updateHazards(dt);
        this.checkCollisions(dt);

        this.ui.updateHUD({
            score: this.stats.score,
            health: this.stats.health,
            time: this.stats.time
        });

        if (this.stats.health <= 0) {
            this.endGame(false, "You succumbed to the hazards!");
        }

        // Camera follow player smoothly
        const targetCamX = this.player.x - this.canvas.width / 2;
        const targetCamY = this.player.y - this.canvas.height / 2;
        this.camera.x += (targetCamX - this.camera.x) * 5 * dt;
        this.camera.y += (targetCamY - this.camera.y) * 5 * dt;
    }

    updatePlayer(dt) {
        let dx = 0, dy = 0;

        if (this.keys['ArrowUp'] || this.keys['KeyW']) dy -= 1;
        if (this.keys['ArrowDown'] || this.keys['KeyS']) dy += 1;
        if (this.keys['ArrowLeft'] || this.keys['KeyA']) dx -= 1;
        if (this.keys['ArrowRight'] || this.keys['KeyD']) dx += 1;

        if (this.ui.joystick && this.ui.joystick.active) {
            dx = this.ui.joystick.x;
            dy = this.ui.joystick.y;
        }

        if (dx !== 0 || dy !== 0) {
            const mag = Math.hypot(dx, dy);
            dx /= mag; dy /= mag;
            
            const pSpeed = this.player.speed * (dt * 60);

            let newX = this.player.x + dx * pSpeed;
            let newY = this.player.y + dy * pSpeed;

            if (!this.isWallCollision(newX, this.player.y, this.player.radius)) this.player.x = newX;
            if (!this.isWallCollision(this.player.x, newY, this.player.radius)) this.player.y = newY;
        }
    }

    updateBots(dt) {
        // Find main treasure
        const mainTreasure = this.items.find(i => i.type === 'treasure');
        
        for (let bot of this.bots) {
            if (mainTreasure) {
                // Move towards treasure (ignoring walls for simplicity, but will slide)
                let hx = mainTreasure.x - bot.x;
                let hy = mainTreasure.y - bot.y;
                let mag = Math.hypot(hx, hy);
                if (mag > 0) {
                    bot.vx = (hx / mag) * this.stats.botSpeed * (dt * 60);
                    bot.vy = (hy / mag) * this.stats.botSpeed * (dt * 60);
                }
            }
            
            let newX = bot.x + bot.vx;
            let newY = bot.y + bot.vy;
            let collidedX = this.isWallCollision(newX, bot.y, bot.radius);
            let collidedY = this.isWallCollision(bot.x, newY, bot.radius);
            
            if (!collidedX) bot.x = newX;
            else bot.vx *= -1; // bounce logic to get unstuck slightly
            
            if (!collidedY) bot.y = newY;
            else bot.vy *= -1;

            // Check if bot got treasure
            if (mainTreasure && Math.hypot(bot.x - mainTreasure.x, bot.y - mainTreasure.y) < bot.radius + mainTreasure.radius) {
                this.endGame(false, "An opponent found the treasure first!");
            }
        }
    }

    updateHazards(dt) {
        for (let h of this.hazards) {
            if (h.type === 'ghost') {
                let newX = h.x + h.vx * (dt * 60);
                let newY = h.y + h.vy * (dt * 60);

                if (this.isWallCollision(newX, h.y, h.radius)) h.vx *= -1;
                else h.x = newX;

                if (this.isWallCollision(h.x, newY, h.radius)) h.vy *= -1;
                else h.y = newY;
            }
        }
    }

    checkCollisions(dt) {
        // Items
        for (let i = this.items.length - 1; i >= 0; i--) {
            let item = this.items[i];
            let dist = Math.hypot(this.player.x - item.x, this.player.y - item.y);
            if (dist < this.player.radius + item.radius) {
                if (item.type === 'coin') {
                    this.stats.score += 100;
                    this.items.splice(i, 1);
                } else if (item.type === 'potion') {
                    this.stats.health = Math.min(this.stats.maxHealth, this.stats.health + 25);
                    this.items.splice(i, 1);
                } else if (item.type === 'treasure') {
                    this.items.splice(i, 1);
                    this.endGame(true, "You found the Treasure!");
                }
            }
        }

        // Hazards
        for (let h of this.hazards) {
            let dist = Math.hypot(this.player.x - h.x, this.player.y - h.y);
            // Proximity damage
            if (dist < this.player.radius + h.radius + 20) {
                // Damage scales with distance
                let intensity = 1 - (dist / (this.player.radius + h.radius + 20));
                this.stats.health -= this.stats.hazardDamage * intensity * dt;
                
                // Visual feedback via shake effect in UI
                const timerEl = document.getElementById('timer-display');
                if (timerEl) {
                    timerEl.classList.add('error-shake');
                    setTimeout(() => timerEl.classList.remove('error-shake'), 200);
                }
            }
        }
    }

    isWallCollision(x, y, r) {
        // Check grid corners of bounding box
        const corners = [
            { x: x - r, y: y - r },
            { x: x + r, y: y - r },
            { x: x - r, y: y + r },
            { x: x + r, y: y + r }
        ];

        for (let c of corners) {
            let tx = Math.floor(c.x / this.tileSize);
            let ty = Math.floor(c.y / this.tileSize);
            
            if (tx < 0 || tx >= this.mapWidth || ty < 0 || ty >= this.mapHeight) return true;
            if (this.map[ty][tx] === 0) return true;
        }
        return false;
    }

    render() {
        this.ctx.fillStyle = '#111';
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

        this.ctx.save();
        this.ctx.translate(-this.camera.x, -this.camera.y);

        // Render Map
        const startC = Math.max(0, Math.floor(this.camera.x / this.tileSize));
        const endC = Math.min(this.mapWidth, Math.ceil((this.camera.x + this.canvas.width) / this.tileSize));
        const startR = Math.max(0, Math.floor(this.camera.y / this.tileSize));
        const endR = Math.min(this.mapHeight, Math.ceil((this.camera.y + this.canvas.height) / this.tileSize));

        for (let r = startR; r < endR; r++) {
            for (let c = startC; c < endC; c++) {
                if (this.map[r][c] === 0) {
                    this.ctx.fillStyle = '#222';
                    this.ctx.fillRect(c * this.tileSize, r * this.tileSize, this.tileSize + 1, this.tileSize + 1);
                    this.ctx.strokeStyle = '#333';
                    this.ctx.strokeRect(c * this.tileSize, r * this.tileSize, this.tileSize, this.tileSize);
                } else {
                    this.ctx.fillStyle = '#3a503a'; // Floor color
                    this.ctx.fillRect(c * this.tileSize, r * this.tileSize, this.tileSize + 1, this.tileSize + 1);
                }
            }
        }

        // Render Items
        this.ctx.textAlign = 'center';
        this.ctx.textBaseline = 'middle';
        for (let item of this.items) {
            let fontSize = item.radius * 1.5;
            this.ctx.font = `${fontSize}px Arial`;
            
            if (item.type === 'coin') {
                this.ctx.fillText('💰', item.x, item.y);
            } else if (item.type === 'potion') {
                this.ctx.fillText('🧪', item.x, item.y);
            } else if (item.type === 'treasure') {
                fontSize = item.radius * 2;
                this.ctx.font = `${fontSize}px Arial`;
                this.ctx.fillText('💎', item.x, item.y);
            }
        }

        // Render Hazards
        for (let h of this.hazards) {
            this.ctx.beginPath();
            this.ctx.arc(h.x, h.y, h.radius, 0, Math.PI * 2);
            if (h.type === 'trap') {
                this.ctx.fillStyle = '#ff4400'; // Fire/trap
                this.ctx.fill();
                this.ctx.fillStyle = '#fff';
                this.ctx.fillText('🔥', h.x-7, h.y+5);
            } else if (h.type === 'ghost') {
                this.ctx.fillStyle = 'rgba(200, 200, 255, 0.6)';
                this.ctx.fill();
                this.ctx.fillStyle = '#000';
                this.ctx.fillText('👻', h.x-7, h.y+5);
            }
        }

        // Render Bots
        for (let bot of this.bots) {
            this.ctx.beginPath();
            this.ctx.arc(bot.x, bot.y, bot.radius, 0, Math.PI * 2);
            this.ctx.fillStyle = '#ff0044'; // Enemy color
            this.ctx.fill();
        }

        // Render Player
        this.ctx.save();
        this.ctx.translate(this.player.x, this.player.y);
        this.ctx.fillStyle = '#00ff88';

        if (this.config.shape === 'circle') {
            this.ctx.beginPath();
            this.ctx.arc(0, 0, this.player.radius, 0, Math.PI * 2);
            this.ctx.fill();
        } else if (this.config.shape === 'square') {
            this.ctx.fillRect(-this.player.radius, -this.player.radius, this.player.radius*2, this.player.radius*2);
        } else if (this.config.shape === 'triangle') {
            this.ctx.beginPath();
            this.ctx.moveTo(0, -this.player.radius);
            this.ctx.lineTo(this.player.radius, this.player.radius);
            this.ctx.lineTo(-this.player.radius, this.player.radius);
            this.ctx.closePath();
            this.ctx.fill();
        } else if (this.config.shape === 'star') {
            this.ctx.font = '20px sans-serif';
            this.ctx.textAlign = 'center';
            this.ctx.textBaseline = 'middle';
            this.ctx.fillText('⭐', 0, 0);
        }

        this.ctx.restore();
        
        // Render Player Name Above
        this.ctx.fillStyle = 'white';
        this.ctx.font = '12px Arial';
        this.ctx.textAlign = 'center';
        this.ctx.fillText(this.config.name, this.player.x, this.player.y - this.player.radius - 5);

        this.ctx.restore();
    }
}
