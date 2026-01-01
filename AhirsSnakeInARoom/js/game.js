import { Snake } from './snake.js';
import { Utils } from './utils.js';
import { InputHandler } from './input.js';

export class Game {
    constructor(canvasId) {
        this.canvas = document.getElementById(canvasId);
        this.ctx = this.canvas.getContext('2d');

        // Resize canvas to full screen
        this.resize();
        window.addEventListener('resize', () => this.resize());

        this.input = new InputHandler();

        this.state = 'MENU'; // MENU, PLAYING, PAUSED, GAME_OVER
        this.snakes = [];
        this.insects = [];
        this.particles = []; // For death effects/eating

        this.playerName = "Player";
        this.difficulty = "easy";

        this.lastTime = 0;
        this.score = 0;
        this.kills = 0;
        this.insectsEaten = 0;

        // Game settings
        this.insectMax = 50;
        this.insectSpawnTimer = 0;

        this.uiCallbacks = {};
    }

    bindUI(callbacks) {
        this.uiCallbacks = callbacks;
    }

    resize() {
        this.width = window.innerWidth;
        this.height = window.innerHeight;
        this.canvas.width = this.width;
        this.canvas.height = this.height;
    }

    reset() {
        this.snakes = [];
        this.insects = [];
        this.particles = [];
        this.score = 0;
        this.kills = 0;
        this.insectsEaten = 0;
    }

    init(config) {
        this.reset();
        this.playerName = config.name;
        this.playerColor = config.color;
        this.playerLogo = config.logo || '🐍';

        // Difficulty
        if (config.difficulty === 'medium') {
            this.enemyCount = 7;
            this.baseEnemySpeed = 160;
        } else if (config.difficulty === 'hard') {
            this.enemyCount = 10;
            this.baseEnemySpeed = 190;
        } else {
            // Easy
            this.enemyCount = 5;
            this.baseEnemySpeed = 130;
        }

        // Spawn Player
        this.snakes.push(new Snake(
            this,
            0,
            this.width / 2,
            this.height / 2,
            this.playerColor,
            true,
            this.playerName,
            this.playerLogo
        ));

        // Create AI Snakes
        const aiColors = ['#ff0000', '#0000ff', '#ffff00', '#ff00ff', '#00ffff', '#ffffff', '#ff8800'];
        const aiNames = ['Viper', 'Cobra', 'Python', 'Anaconda', 'Mamba', 'Boa', 'Sidewinder', 'Krait'];

        for (let i = 0; i < this.enemyCount; i++) {
            const x = Utils.random(50, this.width - 50);
            const y = Utils.random(50, this.height - 50);
            const color = aiColors[i % aiColors.length];
            const name = aiNames[i % aiNames.length] + " " + (i + 1);

            const s = new Snake(this, i + 1, x, y, color, false, name);
            s.baseSpeed = this.baseEnemySpeed;
            s.speed = s.baseSpeed;
            this.snakes.push(s);
        }

        // Initial insects
        for (let i = 0; i < 20; i++) this.spawnInsect();

        this.state = 'PLAYING';
        this.lastTime = performance.now();
        requestAnimationFrame((t) => this.loop(t));
    }

    pause() {
        if (this.state === 'PLAYING') this.state = 'PAUSED';
    }

    resume() {
        if (this.state === 'PAUSED') {
            this.state = 'PLAYING';
            this.lastTime = performance.now();
            requestAnimationFrame((t) => this.loop(t));
        }
    }

    spawnInsect(x, y, value) {
        const types = [
            { icon: '🐞', val: 10, color: '#ff4444' }, // Ladybug
            { icon: '🪰', val: 15, color: '#888888' }, // Fly
            { icon: '🦗', val: 20, color: '#44ff44' }, // Grasshopper
            { icon: '🐝', val: 50, color: '#ffff00' }, // Bee (Rare)
            { icon: '🏐', val: 5, color: '#ffffff' }   // Body Orb (from dead snakes)
        ];

        let type = types[Utils.randomInt(0, 3)];
        if (Math.random() > 0.95) type = types[3]; // Rare bee
        if (value) {
            // Drop from dead snake
            type = { icon: '🏐', val: value, color: '#ffffff' };
        }

        this.insects.push({
            x: x || Utils.random(20, this.width - 20),
            y: y || Utils.random(20, this.height - 20),
            radius: 5 + (type.val / 10),
            type: type,
            age: 0
        });
    }

    loop(timestamp) {
        if (this.state !== 'PLAYING') return;

        const dt = (timestamp - this.lastTime) / 1000;
        this.lastTime = timestamp;

        this.update(dt);
        this.render();

        requestAnimationFrame((t) => this.loop(t));
    }

    update(dt) {
        if (this.state !== 'PLAYING') return;

        if (dt > 0.1) dt = 0.1; // Cap dt for lag spikes

        // Spawn Insects
        if (this.insects.length < this.insectMax) {
            this.insectSpawnTimer += dt;
            if (this.insectSpawnTimer > 0.5) { // Spawn every 0.5s if low
                this.spawnInsect();
                this.insectSpawnTimer = 0;
            }
        }

        // Update Snakes
        this.snakes.forEach(s => s.update(dt));

        // Simple AI Logic corrections
        this.snakes.forEach(s => {
            if (!s.isPlayer && s.alive) {
                // Find nearest food
                let nearest = null;
                let minDist = 1000;

                // Look for insects
                for (let food of this.insects) {
                    const d = Utils.getDistance(s.x, s.y, food.x, food.y);
                    if (d < minDist) {
                        minDist = d;
                        nearest = food;
                    }
                }

                // Occasionally change mind or avoid walls
                if (nearest && Math.random() < 0.95) {
                    s.aiTarget = nearest;
                } else {
                    s.aiTarget = { x: Utils.random(0, this.width), y: Utils.random(0, this.height) };
                }
            }

            // Encirclement Check
            if (s.alive) {
                const loopPoly = s.getSelfLoopPolygon();
                if (loopPoly) {
                    // Check if any victim is inside this polygon
                    for (let victim of this.snakes) {
                        if (victim === s || !victim.alive) continue;

                        // Check if victim head is inside
                        if (Utils.pointInPolygon(victim.getHead(), loopPoly)) {
                            // Victim killed by encirclement!
                            victim.alive = false;

                            // Visual feedback
                            // Spawn massive amount of food from victim
                            const victimSegments = victim.getBodySegments();
                            victimSegments.forEach((seg, idx) => {
                                if (idx % 2 === 0)
                                    this.spawnInsect(seg.x, seg.y, 5);
                            });

                            // Attacker bonus
                            s.grow(5); // Big growth

                            if (s.isPlayer) {
                                this.score += 500;
                                this.kills++;
                                // Show message?
                                this.uiCallbacks.onGameOver && this.uiCallbacks.onScoreUpdate(this.score, this.kills); // Update score
                            } else if (victim.isPlayer) {
                                this.endGame(false, "Encercled by " + s.name + "!");
                                return; // Stop update if player died
                            }
                        }
                    }

                    // Also eat all insects inside
                    for (let i = this.insects.length - 1; i >= 0; i--) {
                        const bug = this.insects[i];
                        if (Utils.pointInPolygon(bug, loopPoly)) {
                            s.grow(bug.type.val / 10);
                            this.insects.splice(i, 1);
                            if (s.isPlayer) {
                                this.score += bug.type.val;
                                this.insectsEaten++;
                            }
                        }
                    }
                }
            }
        });

        if (this.state !== 'PLAYING') return; // Exit if game ended in loop

        this.checkCollisions();

        if (this.state !== 'PLAYING') return; // Exit if game ended in collision

        // Cleanup
        this.snakes = this.snakes.filter(s => s.alive);

        // Win/Loss
        const player = this.snakes.find(s => s.isPlayer);
        if (!player) {
            // Should have been caught by checkCollisions or loop check, but just in case
            this.endGame(false, "You were defeated!");
        } else if (this.snakes.length === 1 && player) {
            // Victory if only player remains
            this.score += 5000; // Winning Bonus
            this.endGame(true, "Room Cleared! All Rivals Eliminated.");
        }

        if (player && this.uiCallbacks.onScoreUpdate) {
            this.uiCallbacks.onScoreUpdate(this.score, this.kills);
        }
    }

    checkCollisions() {
        const player = this.snakes.find(s => s.isPlayer);

        // 1. Snake vs Insect
        for (let s of this.snakes) {
            if (!s.alive) continue;
            const head = s.getHead();

            for (let i = this.insects.length - 1; i >= 0; i--) {
                const bug = this.insects[i];
                if (Utils.circleIntersect(head, { x: bug.x, y: bug.y, radius: bug.radius })) {
                    // Eat
                    s.grow(bug.type.val / 10); // Grow logic
                    this.insects.splice(i, 1);
                    if (s.isPlayer) {
                        this.score += bug.type.val;
                        this.insectsEaten++;
                    }
                }
            }
        }

        // 2. Snake vs Snake (Combat)
        for (let s1 of this.snakes) {
            if (!s1.alive) continue;
            const head1 = s1.getHead();

            for (let s2 of this.snakes) {
                if (s1 === s2 || !s2.alive) continue;

                const head2 = s2.getHead();

                // A. Head-to-Head Collision (Bigger wins)
                if (Utils.circleIntersect(head1, head2)) {
                    // Determine winner
                    let winner = null;
                    let loser = null;

                    if (s1.currentLength > s2.currentLength) {
                        winner = s1; loser = s2;
                    } else if (s2.currentLength > s1.currentLength) {
                        winner = s2; loser = s1;
                    } else {
                        // Equal size? Random or both die? Let's say random or just bounce.
                        // For gameplay flow, kill one at random if equal.
                        if (Math.random() < 0.5) { winner = s1; loser = s2; }
                        else { winner = s2; loser = s1; }
                    }

                    if (winner && loser) {
                        loser.alive = false;
                        // Convert loser to food
                        const loserSegments = loser.getBodySegments();
                        loserSegments.forEach((seg, idx) => {
                            if (idx % 2 === 0) this.spawnInsect(seg.x, seg.y, 5);
                        });

                        winner.grow(10); // Bonus for head-on kill
                        if (winner.isPlayer) {
                            this.score += 1000; // Big bonus
                            this.kills++;
                        } else if (loser.isPlayer) {
                            // Player died
                            this.endGame(false, "Devoured by " + winner.name + "!");
                        }
                        continue; // S2 dead, move to next
                    }
                }

                // B. Head-to-Body Collision
                const body2 = s2.getBodySegments();

                for (let seg of body2) {
                    if (Utils.circleIntersect(head1, seg)) {
                        // S1 hit S2's body
                        // "Whichever snake it touches by its face, the remaining portion of the other snake it will eat"
                        // So S2 loses tail from 'seg.index' onwards.

                        // Drop food from cut segments
                        const lostLength = (s2.currentLength - seg.index); // Simple approximation
                        const value = Math.floor(lostLength * 5);

                        // Spawn food burst at cut location
                        for (let k = 0; k < Math.min(10, lostLength); k++) {
                            this.spawnInsect(seg.x + Utils.random(-20, 20), seg.y + Utils.random(-20, 20), 5);
                        }

                        // S2 shrinks
                        s2.targetLength = seg.index;
                        s2.currentLength = seg.index;
                        // Prune history immediately
                        const historyKeep = Math.floor(seg.index * s2.spacing);
                        if (s2.history.length > historyKeep) {
                            s2.history.length = historyKeep;
                        }

                        // If S2 is too small, it dies
                        if (s2.currentLength < 5) {
                            s2.alive = false;
                            // Drop remaining body as food
                            const remSegments = s2.getBodySegments();
                            remSegments.forEach((rseg, idx) => {
                                if (idx % 3 === 0) this.spawnInsect(rseg.x, rseg.y, 5);
                            });

                            if (s1.isPlayer) {
                                this.kills++;
                            }
                        }

                        // S1 bonus? 
                        if (s1.isPlayer) {
                            // "its length will increase"
                            s1.grow(2);
                            this.score += 100;
                        } else if (s2.isPlayer) {
                            // Player was cut!
                            // "if any other snake touches any portion of the player's snake remaining portion of the player snake will be lost"
                            // Handled naturally by symmetry when s2 is player loop
                        }

                        if (s2.isPlayer && !s2.alive) {
                            this.endGame(false, "Cut in half by " + s1.name + "!");
                        }

                        break; // Process one hit per frame per pair
                    }
                }
            }
        }
    }

    render() {
        // Clear
        this.ctx.clearRect(0, 0, this.width, this.height);

        // Draw Insects
        for (let bug of this.insects) {
            this.ctx.font = `${bug.radius * 2}px Serif`;
            this.ctx.textAlign = 'center';
            this.ctx.textBaseline = 'middle';
            this.ctx.fillText(bug.type.icon, bug.x, bug.y);
        }

        // Draw Snakes
        // Sort by y so lower snakes are on top? Or player on top?
        // Player on top usually feels best
        this.snakes.sort((a, b) => (a.isPlayer ? 1 : -1));

        for (let s of this.snakes) {
            s.render(this.ctx);
        }
    }

    endGame(win, reason) {
        if (this.state === 'GAME_OVER') return; // Prevent double trigger
        this.state = 'GAME_OVER';
        if (this.uiCallbacks.onGameOver) {
            this.uiCallbacks.onGameOver({
                win: win,
                reason: reason,
                score: this.score,
                kills: this.kills,
                insects: this.insectsEaten
            });
        }
    }
}
