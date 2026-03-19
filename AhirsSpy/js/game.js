import { Person } from './person.js';
import { Assets } from './assets.js';
import { localLLMService } from '../../shared/js/local_llm_service.js';

export class Game {
    constructor(ui, economy) {
        this.ui = ui;
        this.economy = economy;
        this.canvas = document.getElementById('game-canvas');
        this.ctx = this.canvas.getContext('2d');

        this.isRunning = false;
        this.isPaused = false;
        this.persons = [];
        this.player = null;
        this.score = 1000;
        this.timeElapsed = 0;
        this.lastTime = 0;
        this.lastHintTime = 0;
        this.hintInterval = 30000; // 30 seconds

        this.gameConfig = null;
        this.walls = []; // Defines the map

        // Input state
        this.keys = { ArrowUp: false, ArrowDown: false, ArrowLeft: false, ArrowRight: false, Space: false };
        this.mobileInput = { x: 0, y: 0, shoot: false };

        this.bindEvents();
        this.resize();
        window.addEventListener('resize', () => this.resize());
    }

    bindEvents() {
        window.addEventListener('keydown', (e) => {
            if (e.code === 'Space') {
                // Modified: Space interacts if close, shoots if not (or separate key)
                // For safety: Check if close to someone
                if (this.getClosestPerson()) {
                    this.interact();
                } else {
                    this.shoot();
                }
            }
            if (e.code === 'Enter') {
                this.interact(); // Enter to talk
            }
            if (this.keys.hasOwnProperty(e.code)) this.keys[e.code] = true;
        });
        window.addEventListener('keyup', (e) => {
            if (this.keys.hasOwnProperty(e.code)) this.keys[e.code] = false;
        });

        // Touch Joystick binding would go here or in UI
        const joystickZone = document.getElementById('joystick-zone');
        // ... 

        document.getElementById('shoot-btn').addEventListener('click', () => this.shoot());

        // Click to interact with mouse
        this.canvas.addEventListener('click', (e) => {
            // If click on person -> Interact
            const rect = this.canvas.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            // Check if clicked near a person
            this.persons.forEach(p => {
                const dist = Math.hypot(p.x - x, p.y - y);
                if (dist < 40) {
                    this.ui.openDialog(p);
                }
            });
        });
    }

    resize() {
        this.canvas.width = window.innerWidth;
        this.canvas.height = window.innerHeight;
    }

    start(config) {
        if (!this.economy.spendCoins(10, 'Spy Mission Entry')) {
            this.ui.showLowBalance();
            return;
        }

        this.gameConfig = config;
        this.isRunning = true;
        this.isPaused = false;
        this.score = 1000;
        this.timeElapsed = 0;
        this.lastTime = performance.now();

        // Start loading LLM in background so hints are ready later
        localLLMService.init().catch(() => {});

        this.generateMap();
        this.spawnCharacters();
        this.ui.showHUD();
        this.ui.updateHUD({ score: this.score, time: 100 });

        requestAnimationFrame((t) => this.loop(t));
    }

    restart() {
        if (!this.economy.spendCoins(10, 'Spy Mission Retry')) {
            this.ui.showLowBalance();
            return;
        }
        this.start(this.gameConfig);
    }

    togglePause() {
        if (!this.isRunning) return;
        this.isPaused = !this.isPaused;
        if (this.isPaused) {
            this.ui.showPauseMenu();
        } else {
            this.ui.hidePauseMenu();
            this.lastTime = performance.now();
            requestAnimationFrame((t) => this.loop(t));
        }
    }

    loop(timestamp) {
        if (!this.isRunning || this.isPaused) return;

        const dt = timestamp - this.lastTime;
        this.lastTime = timestamp;

        this.update(dt);
        this.draw();

        requestAnimationFrame((t) => this.loop(t));
    }

    update(dt) {
        // Score Decay: -1 every 5s
        this.timeElapsed += dt;
        if (Math.floor(this.timeElapsed / 1000) > Math.floor((this.timeElapsed - dt) / 1000)) {
            const seconds = Math.floor(this.timeElapsed / 1000);
            if (seconds % 5 === 0) {
                this.score = Math.max(0, this.score - 1);
            }
        }

        // Input Handling for Player
        const speed = 0.2 * dt; // pixels per ms
        let dx = 0;
        let dy = 0;

        // Joystick Input
        if (this.ui.joystick && this.ui.joystick.active) {
            dx = this.ui.joystick.x * speed;
            dy = this.ui.joystick.y * speed;
        }
        // Keyboard Input
        
        if (this.keys.ArrowUp) dy -= speed;
        if (this.keys.ArrowDown) dy += speed;
        if (this.keys.ArrowLeft) dx -= speed;
        if (this.keys.ArrowRight) dx += speed;
        

        if (dx !== 0 || dy !== 0) {
            this.player.move(dx, dy, this.walls);
        }

        // Update Persons (AI)
        this.persons.forEach(p => {
            if (!p.isDead) {
                p.update(dt, this.walls, this.persons.concat([this.player]), { w: this.canvas.width, h: this.canvas.height });
            }
        });

        // Killer AI
        this.updateKillerAI(dt);

        this.ui.updateHUD({
            score: this.score,
            time: Math.floor(this.timeElapsed / 1000)
        });

        // Check Proximity for Interact Hint
        this.checkProximity();

        // LLM Hints Timer
        if (this.timeElapsed - this.lastHintTime > this.hintInterval) {
            this.lastHintTime = this.timeElapsed;
            this.triggerLLMHint();
        }
    }

    updateKillerAI(dt) {
        if (!this.killer || this.killer.isDead) return;

        // 1. If has necklace, flee to exit
        if (this.killer.hasNecklace) {
            // Move towards exit (let's say bottom center)
            const exitX = this.canvas.width / 2;
            const exitY = this.canvas.height - 20; // Near the bottom edge

            const angle = Math.atan2(exitY - this.killer.y, exitX - this.killer.x);
            this.killer.move(Math.cos(angle) * this.killer.speed * dt, Math.sin(angle) * this.killer.speed * dt, this.walls);

            // Reached exit?
            if (this.killer.y > this.canvas.height - 50) {
                this.endGame(false, "Killer escaped with the Necklace!");
            }
            return;
        }

        // 2. Hunt Owner
        if (this.owner && !this.owner.isDead) {
            const dist = Math.hypot(this.owner.x - this.killer.x, this.owner.y - this.killer.y);
            if (dist < 30) { // Close enough to kill
                // Kill Owner
                this.owner.isDead = true;
                this.killer.hasNecklace = true;
                this.score = Math.max(0, this.score - 500); // Penalize
            } else {
                // Move towards owner
                const angle = Math.atan2(this.owner.y - this.killer.y, this.owner.x - this.killer.x);
                if (Math.random() > 0.05) { 
                    this.killer.move(Math.cos(angle) * this.killer.speed * dt * 0.8, Math.sin(angle) * this.killer.speed * dt * 0.8, this.walls);
                }
            }
            return;
        }

        // 3. Killer tries to avoid Spy if too close, but no instant random kill
        const spyDist = Math.hypot(this.player.x - this.killer.x, this.player.y - this.killer.y);
        if (spyDist < 100) { 
            // Move away from Spy slowly
            const angle = Math.atan2(this.killer.y - this.player.y, this.killer.x - this.player.x);
            this.killer.move(Math.cos(angle) * this.killer.speed * dt * 0.5, Math.sin(angle) * this.killer.speed * dt * 0.5, this.walls);
        }
    }

    async triggerLLMHint() {
        if (!this.killer || this.killer.isDead) return;

        // If not loaded yet, provide a static fallback hint based on killer traits
        if (!localLLMService.isLoaded) {
            console.log('[Game] 🤖 AI not ready for hint yet, using static fallback.');
            const traits = this.getKillerTraits();
            const trait = traits[Math.floor(Math.random() * traits.length)];
            const fallbacks = [
                `Look for someone who ${trait}...`,
                `A witness says they noticed someone who ${trait}.`,
                `Suspicious activity caught: Person ${trait}.`,
                `Handler Note: Target ${trait}.`
            ];
            const hint = fallbacks[Math.floor(Math.random() * fallbacks.length)];
            this.ui.showHint(hint + " (AI Loading...)");
            
            // Try to init silently in case it failed or hasn't started
            localLLMService.init().catch(() => {});
            return; 
        }

        console.log('[Game] 🤖 Generating AI LLM Hint...');
        try {
            const traits = this.getKillerTraits();
            const hint = await localLLMService.generateSpyHint(traits);
            this.ui.showHint(hint);
        } catch (error) {
            console.error('[Game] ✗ LLM Hint failed:', error);
        }
    }

    getKillerTraits() {
        // Collect traits of the killer to passed to LLM
        const traits = {
            '👨': ['Man', 'Mustache'], '👩': ['Woman', 'Long Hair'], '👱': ['Light Hair'],
            '👴': ['Old', 'Glasses'], '👵': ['Old', 'Glasses'], '🧔': ['Beard'],
            '👮': ['Hat', 'Uniform'], '👷': ['Hat', 'Helmet'], '👸': ['Crown', 'Woman'],
            '🤴': ['Crown', 'Man'], '🧙': ['Hat', 'Beard'], '🧛': ['Cape']
        };
        return traits[this.killer.avatar] || ['Mysterious'];
    }

    draw() {
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

        // Draw Floor
        this.ctx.fillStyle = "#2c3e50";
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

        // Draw Walls
        this.ctx.fillStyle = "#95a5a6";
        this.ctx.strokeStyle = "#7f8c8d";
        this.ctx.lineWidth = 2;
        this.walls.forEach(w => {
            this.ctx.fillRect(w.x, w.y, w.w, w.h);
            this.ctx.strokeRect(w.x, w.y, w.w, w.h);
        });

        // Draw Room Names (Optional)
        this.ctx.fillStyle = "rgba(255,255,255,0.1)";
        this.ctx.font = "20px Arial";
        // ... (can add room labels later)

        // Draw Persons
        // Sort by Y for depth effect
        const allChars = [...this.persons, this.player].sort((a, b) => a.y - b.y);
        allChars.forEach(c => c.draw(this.ctx));

        // Draw Dead Bodies
        this.persons.filter(p => p.isDead).forEach(p => {
            this.ctx.fillStyle = "rgba(255,0,0,0.5)";
            this.ctx.beginPath();
            this.ctx.arc(p.x, p.y, 15, 0, Math.PI * 2);
            this.ctx.fill();
            this.ctx.fillStyle = "white";
            this.ctx.font = "20px Arial";
            this.ctx.textAlign = "center";
            this.ctx.textBaseline = "middle";
            this.ctx.fillText("💀", p.x, p.y);
        });

        // Lighting / Vision cone (Optional)
    }

    handleAction() {
        // Renamed to check interaction, triggered by Space or Button?
        // Actually bindEvents calls this for 'Space' and 'shoot-btn'
        // Let's split it.
    }

    interact() {
        const closest = this.getClosestPerson();
        if (closest && !closest.isDead) {
            this.ui.openDialog(closest);
        }
    }

    shoot() {
        const closest = this.getClosestPerson();
        if (closest) {
            if (closest.type === 'KILLER') {
                this.endGame(true, "You eliminated the Killer!");
            } else {
                closest.isDead = true; // Visual
                this.endGame(false, "You shot an innocent person! Police arrested you.");
            }
        } else {
            // Missed shot sound?
            this.ui.showNotification("You shot into the air!");
        }
    }

    getClosestPerson() {
        let closest = null;
        let minDist = 60; // Interaction radius
        this.persons.forEach(p => {
            if (p === this.player) return; // Don't interact with self
            const dist = Math.hypot(p.x - this.player.x, p.y - this.player.y);
            if (dist < minDist) {
                minDist = dist;
                closest = p;
            }
        });
        return closest;
    }

    checkProximity() {
        // Show/Hide "Talk" hint or button
        const closest = this.getClosestPerson();
        if (closest && !closest.isDead) {
            this.ui.showInteractHint(true, closest.avatar);
        } else {
            this.ui.showInteractHint(false);
        }
    }

    endGame(win, reason) {
        this.isRunning = false;

        let bonus = 0;
        if (win) {
            bonus += this.score; // Time/Score remaining
            if (this.owner && !this.owner.isDead) bonus += 500; // Owner saved bonus
        } else {
            this.score = 0;
        }

        let finalScore = this.score + bonus;

        // Save Score
        this.saveScore(finalScore, win);

        let killerDetails = null;
        if (!win && this.killer) {
            const traits = {
                '👨': ['Man', 'Mustache'], '👩': ['Woman', 'Long Hair'], '👱': ['Light Hair'],
                '👴': ['Old', 'Glasses'], '👵': ['Old', 'Glasses'], '🧔': ['Beard'],
                '👮': ['Hat', 'Uniform'], '👷': ['Hat', 'Helmet'], '👸': ['Crown', 'Woman'],
                '🤴': ['Crown', 'Man'], '🧙': ['Hat', 'Beard'], '🧛': ['Cape']
            };
            const kt = traits[this.killer.avatar] || ['Unknown'];
            killerDetails = {
                avatar: this.killer.avatar,
                occupation: this.killer.occupation || 'Civilian', // occupation might not be set on person, check logic
                clue: `Looked like a ${kt[0] || 'person'}`
            };
            // Person class doesn't seem to store occupation explicitly other than type 'KILLER'/'OWNER'/'CIVILIAN'. 
            // Logic in spawnCharacters assigns type.
            // Let's us 'Killer' as occupation or keep it generic.
            killerDetails.occupation = 'The Killer';
        }

        this.onGameOver({ success: win, message: reason, score: finalScore, killerDetails });
    }

    saveScore(score, win) {
        // Local Storage Logic
        const key = 'ahirs_spy_scores'; // Use separate key or shared?
        let scores = JSON.parse(localStorage.getItem(key) || '[]');
        scores.push({ score, win, date: new Date().toISOString() });
        scores.sort((a, b) => b.score - a.score); // Sort descending
        localStorage.setItem(key, JSON.stringify(scores.slice(0, 10))); // Keep top 10
    }

    generateMap() {
        // Simple House Layout
        const w = this.canvas.width;
        const h = this.canvas.height;
        const wallThick = 20;

        this.walls = [
            // Outer Walls
            { x: 0, y: 0, w: w, h: wallThick },
            { x: 0, y: h - wallThick, w: w, h: wallThick },
            { x: 0, y: 0, w: wallThick, h: h },
            { x: w - wallThick, y: 0, w: wallThick, h: h },

            // Inner Walls
            // Room 1 (Top Left)
            { x: 0, y: h * 0.4, w: w * 0.3, h: wallThick },
            { x: w * 0.3, y: 0, w: wallThick, h: h * 0.4 },

            // Room 2 (Top Right)
            { x: w * 0.6, y: h * 0.4, w: w * 0.4, h: wallThick },
            { x: w * 0.6, y: 0, w: wallThick, h: h * 0.4 },

            // Room 3 (Bottom Left - Kitchen?)
            { x: 0, y: h * 0.7, w: w * 0.4, h: wallThick },
            { x: w * 0.4, y: h * 0.7, w: wallThick, h: h * 0.3 },

            // Room 4 (Middle Block)
            { x: w * 0.4, y: h * 0.4, w: w * 0.2, h: wallThick * 4 } // A pillar/block
        ];
    }

    spawnCharacters() {
        this.persons = [];
        const w = this.canvas.width;
        const h = this.canvas.height;

        // Spawn Player at a safe location (not in the center pillar)
        let px = w / 2;
        let py = h * 0.8;
        this.player = new Person(px, py, 'SPY', this.gameConfig.avatar || '😎');
        // Ensure not in wall
        while(this.checkCollision(this.player, this.walls)) {
            this.player.x += 10;
        }
        // Setup Characters based on difficulty
        let numCivilians = 4;
        if (this.gameConfig.difficulty === 'medium') numCivilians = 6;
        if (this.gameConfig.difficulty === 'hard') numCivilians = 8;

        let roles = ['OWNER', 'KILLER'];
        for (let i = 0; i < numCivilians; i++) roles.push('CIVILIAN');
        roles.sort(() => Math.random() - 0.5);

        // Avatars
        const avatars = ['👨', '👩', '👱', '👴', '👵', '🧔', '👮', '👷', '👸', '🤴', '🧙', '🧛'];
        // Ensure we have enough avatars
        while (avatars.length < roles.length) avatars.push('👤');

        // Shuffle avatars to randomize who looks like what
        avatars.sort(() => Math.random() - 0.5);

        this.killer = null;
        this.owner = null;

        roles.forEach((role, i) => {
            const rX = Math.random() * (w - 100) + 50;
            const rY = Math.random() * (h - 100) + 50;
            const p = new Person(rX, rY, role, avatars[i]);

            // Basic collision check for spawn
            let attempts = 0;
            while (this.checkCollision(p, this.walls) && attempts < 100) {
                p.x = Math.random() * (w - 100) + 50;
                p.y = Math.random() * (h - 100) + 50;
                attempts++;
            }

            if (role === 'KILLER') this.killer = p;
            if (role === 'OWNER') this.owner = p;

            this.persons.push(p);
        });

        // Init Knowledge
        this.distributeKnowledge();
    }

    distributeKnowledge() {
        const traits = {
            '👨': ['is a man', 'has a mustache'], '👩': ['is a woman', 'has long hair'], '👱': ['has light hair'],
            '👴': ['is an old man', 'wears glasses'], '👵': ['is an old woman', 'wears glasses'], '🧔': ['has a beard'],
            '👮': ['wears a police hat', 'is in uniform'], '👷': ['wears a hard hat', 'is a worker'], '👸': ['wears a crown', 'is a woman'],
            '🤴': ['wears a crown', 'is a man'], '🧙': ['wears a wizard hat', 'has a beard'], '🧛': ['wears a cape', 'looks pale']
        };

        const killerTraits = traits[this.killer.avatar] || ['looks like an ordinary person'];

        // Shuffle civilians to distribute clues evenly
        let civilians = this.persons.filter(p => p.type !== 'KILLER');
        civilians.sort(() => Math.random() - 0.5);

        civilians.forEach((p, index) => {
            // First civilian gives a direct visual clue
            if (index === 0) {
                const trait = killerTraits[Math.floor(Math.random() * killerTraits.length)];
                p.knowledge.push(`I saw someone suspicious. The killer ${trait}.`);
            } 
            // Second civilian gives another visual clue
            else if (index === 1 && killerTraits.length > 1) {
                const trait = killerTraits.find(t => !civilians[0].knowledge[0].includes(t)) || killerTraits[0];
                p.knowledge.push(`Watch out! I noticed the killer ${trait}.`);
            }
            // Others vouch for innocent people or just give generic info
            else {
                // Pick a random other civilian to vouch for
                const innocent = civilians.filter(p2 => p2 !== p)[0];
                if (innocent && Math.random() > 0.3) {
                    p.knowledge.push(`I was chatting with ${innocent.avatar} earlier. They are innocent!`);
                } else {
                    p.knowledge.push(`I heard a noise, but didn't see anyone clearly.`);
                }
            }
        });
    }

    handleAskQuestion(person, qId) {
        this.score -= 10; // Cost to ask

        if (person.type === 'KILLER') {
            // LIE!
            if (qId === 'suspect') return "I think it's the Spy!";
            if (qId === 'killer') {
                // Blame random innocent
                const innocent = this.persons.find(p => p.type !== 'KILLER');
                return `It's definitely ${innocent.avatar}! I saw them!`;
            }
            if (qId === 'location') return "I was just checking the locks.";
            if (qId === 'hat' || qId === 'glasses') return "I don't look at people's faces.";
            return "I don't know anything.";
        }

        // Truth (Civilians/Owner)
        if (qId === 'suspect' || qId === 'killer') {
            if (person.knowledge.length > 0) {
                return person.knowledge[0];
            }
            return "I haven't noticed anything unusual.";
        }
        
        if (qId === 'hat' || qId === 'glasses') {
             if (person.knowledge.length > 0 && (person.knowledge[0].includes('hat') || person.knowledge[0].includes('glasses'))) {
                 return "Yes! " + person.knowledge[0];
             }
             return "I didn't notice any accessories.";
        }

        if (qId === 'location') return "I live here / I am a guest.";

        return "I'm just trying to stay safe.";
    }

    checkCollision(rect, walls) {
        // rect: {x, y, w, h} - person radius approx
        // Person size is roughly 30 radius.
        const r = 20;
        for (let wall of walls) {
            if (rect.x + r > wall.x && rect.x - r < wall.x + wall.w &&
                rect.y + r > wall.y && rect.y - r < wall.y + wall.h) {
                return true;
            }
        }
        return false;
    }

    setGameOverCallback(cb) {
        this.onGameOver = cb;
    }

    handleTargetAction(person, action) {
        if (action === 'catch' || action === 'shoot') {
            if (person.type === 'KILLER') {
                const actionText = action === 'catch' ? 'caught' : 'eliminated';
                this.endGame(true, `You ${actionText} the Killer! Mission Accomplished.`);
            } else {
                person.isDead = true; 
                const actionText = action === 'catch' ? 'arrested' : 'shot';
                this.endGame(false, `You ${actionText} an innocent person! Police arrested you.`);
            }
        }
    }

    // Additional logic for binding UI question handler
    bindUI(ui) {
        ui.bindAskQuestion((p, q) => this.handleAskQuestion(p, q));
        ui.bindCatch((p) => this.handleTargetAction(p, 'catch'));
        ui.bindShootTarget((p) => this.handleTargetAction(p, 'shoot'));
    }
}
