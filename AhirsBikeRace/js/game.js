import { images } from './assets.js';
import { SoundManager } from './audio.js';
import Entity from './entities/Entity.js';
import Car from './entities/Car.js';
import Opponent from './entities/Opponent.js';
import Police from './entities/Police.js';


export class Game {
    constructor(canvas, uiCallbacks) {
        this.canvas = canvas;
        this.ctx = canvas.getContext('2d');
        this.ui = uiCallbacks; // { onGameOver: (stats) => {}, onUpdateHud: (data) => {} }

        this.width = canvas.width;
        this.height = canvas.height;

        // Game Constants
        this.fps = 60;
        this.step = 1 / this.fps;
        this.dt = 0;
        this.lastTime = 0;

        // Road Params
        this.segments = [];
        this.segmentLength = 200; // Length of one segment
        this.rumbleLength = 3;    // Number of segments per rumble strip
        this.roadWidth = 2000;    // Logical road width
        this.lanes = 3;
        this.fieldOfView = 100;
        this.cameraHeight = 1000;
        this.cameraDepth = null;  // calculated
        this.drawDistance = 300;  // How many segments to draw
        this.fogDensity = 5;

        // Player Params
        this.player = {
            x: 0,
            y: 0,
            z: 0,
            speed: 0,
            maxSpeed: 12000,
            accel: 12000 / 5,
            breaking: -12000,
            decud: -12000 / 5,
            offRoadDecel: -12000, // Same as full braking
            offRoadLimit: 2000, // Crawl speed
            width: 80 * 3, // scale up pixel art
            height: 80 * 3,
            sprite: "PLAYER"
        };

        this.position = 0; // Camera Z

        // Assets (Sprites)
        this.sprites = {
            TREE: { x: 0, y: 0, w: 48, h: 48, scale: 20 }, // Example logic
            ROCK: { x: 48, y: 0, w: 48, h: 48, scale: 10 }
        };

        // 2. Opponent Entity (From Split Sheet)
        if (images.police) {
            const w = images.police.width / 2;
            const h = images.police.height;
            // OPPONENT uses right half of police-civilion.png
            this.sprites.OPPONENT = { x: 0, y: 0, w: 64, h: 64, sourceX: w, sourceY: 0, sourceW: w, sourceH: h, scale: 5 };
        } else {
            console.warn("Civilian/Police sheet missing, using fallbacks");
            this.sprites.OPPONENT = { ...this.sprites.PLAYER_STRAIGHT };
        }
        // Assets (Sprites)
        this.sprites = {
            PLAYER_STRAIGHT: { x: 0, y: 0, w: 64, h: 64, imageId: 'player' },
            TREE: { x: 0, y: 0, w: 48, h: 48, scale: 20, imageId: 'obstacles' },
            ROCK: { x: 48, y: 0, w: 48, h: 48, scale: 10, imageId: 'obstacles' },
        };

        // Fallback checks
        if (!images.competitor1) this.sprites.COMPETITOR1.imageId = 'player';
        if (!images.competitor2) this.sprites.COMPETITOR2.imageId = 'player';

        this.input = { left: false, right: false, up: false, down: false, attack: false };
        this.paused = false;
        this.running = false;
        this.score = 0;
        this.health = 100;
        this.time = 0;
        this.distance = 0; // Total distance traveled
        this.trackLength = null;
        this.raceDistance = 50000; // 50km equivalent units? (segment 200 * ?)
        // Let's say trackLength is length of generated road loop. Race is multiple laps or one long?
        // Let's make race distance = track length for simplicity of V1 finish line.

        this.entities = []; // Cars, Opponents
        this.police = new Police(0, 0);

        this.sound = new SoundManager();
        this.screenShake = 0; // x, y offset intensity

        // Resize listener
        window.addEventListener('resize', () => this.resize());
        this.resize();
    }

    resize() {
        this.canvas.width = window.innerWidth;
        this.canvas.height = window.innerHeight;
        this.width = this.canvas.width;
        this.height = this.canvas.height;
        // Re-calc camera depth (1 / Math.tan((this.fieldOfView / 2) * Math.PI / 180));
        this.cameraDepth = 1 / Math.tan((this.fieldOfView / 2) * Math.PI / 180);
        // We actually use a simpler projection calculation often: depth = 1 / tan(fov/2) usually means logical screen dist.
        // For standard "Jake Gordon" style:
        this.cameraDepth = 0.8; // tweak manually for look
    }

    start(options) {
        this.options = options; // difficulty etc.
        this.reset();
        this.running = true;
        this.paused = false;

        // Audio
        this.sound.init();
        this.sound.startEngine();

        this.lastTime = performance.now();
        requestAnimationFrame((t) => this.loop(t));
    }

    reset() {
        this.state = 'RUNNING';
        this.segments = [];
        this.createRoad();

        this.player.speed = 0;
        this.player.x = 0;
        this.position = 0;
        this.score = 0;
        this.takedowns = 0;
        this.health = 100;
        this.time = 0;
        this.distance = 0;

        this.entities = [];
        this.police = new Police(0, 0); // Reset police

        // Difficulty Configs
        const difficulty = this.options.difficulty || 'medium';
        let carCount = 30; // Medium
        let minOppSpeed = 6000;
        let speedRange = 3000;

        if (difficulty === 'easy') {
            carCount = 5; // Very very infrequent
            minOppSpeed = 2000; // Really slow
            speedRange = 2000;
        } else if (difficulty === 'hard') {
            carCount = 60; // Frequent
            minOppSpeed = 9000; // Fast
            speedRange = 3500; // Up to 12500 (challenging player max)
            // Note: Player maxSpeed is 12000. 12500 means unbeatable unless you boost?
        } else {
            // Medium
            carCount = 20; // Infrequent
            minOppSpeed = 4000; // Slow but faster than easy
            speedRange = 3000;
        }

        // Spawn Traffic
        for (let i = 0; i < carCount; i++) {
            let z = Math.random() * this.trackLength;
            let speed = 2000 + Math.random() * 5000;
            // Maybe vary car speed too? Keep as is for now.
            this.entities.push(new Car(z, -0.5 + Math.random(), speed));
        }

        // Spawn Opponents
        for (let i = 0; i < 4; i++) {
            // Avoid center lane (0) for player start
            let laneOffset = -0.8 + (i * 0.4);
            if (Math.abs(laneOffset) < 0.1) laneOffset = 0.5; // push center to right

            // Speed based on difficulty
            let oppSpeed = minOppSpeed + Math.random() * speedRange;
            this.entities.push(new Opponent(0, laneOffset, oppSpeed));
        }

    }

    createRoad() {
        // Terrain Colors
        const terrains = {
            hills: { road: '#646464', grass: '#105610', rumble: '#B83422' }, // Dark Green/Red
            city: { road: '#222', grass: '#050510', rumble: '#00FFFF' },   // Neon/Dark
            snow: { road: '#a0a0a0', grass: '#f0f0f0', rumble: '#5555ff' } // White/Blue
        };
        const palette = terrains[this.options.terrain] || terrains.hills;
        this.currentPalette = palette;

        // Generate segments
        // 1. Enter straight
        this.addStraight(50);
        // 2. Low rolling hills
        this.addLowRollingHills(50, 200);
        this.addSCurves();
        this.addHill(100, 400);
        this.addCurve(50, 2);
        this.addStraight(50);
        this.addDownHillToEnd();
        this.addFinishLine();

        this.trackLength = this.segments.length * this.segmentLength;

        // Add sprites randomly
        this.addSprites();
    }

    addSegment(curve, y) {
        let n = this.segments.length;
        const p = this.currentPalette;
        const darkGrass = this.adjustColor(p.grass, -20);
        const lightGrass = p.grass;
        const darkRoad = this.adjustColor(p.road, -10);
        const lightRoad = p.road;

        const isDark = Math.floor(n / this.rumbleLength) % 2;

        this.segments.push({
            index: n,
            p1: { world: { y: this.lastY(), z: n * this.segmentLength }, camera: {}, screen: {} },
            p2: { world: { y: y, z: (n + 1) * this.segmentLength }, camera: {}, screen: {} },
            curve: curve,
            sprites: [],
            cars: [],
            color: isDark ? { road: darkRoad, grass: darkGrass, rumble: '#444' } : { road: lightRoad, grass: lightGrass, rumble: p.rumble },
            isFinish: false // Default
        });
    }

    addFinishLine() {
        // Mark the last 5 segments as finish line
        for (let i = 0; i < 5; i++) {
            this.addSegment(0, this.lastY());
            this.segments[this.segments.length - 1].isFinish = true;
            this.segments[this.segments.length - 1].color.road = '#FFF'; // Start white for potential patterning
        }

    }

    // Helper to darken hex color slightly
    adjustColor(col, amount) {
        return col; // simplification for now, proper hex shading is complex without a lib
    }

    lastY() { return (this.segments.length === 0) ? 0 : this.segments[this.segments.length - 1].p2.world.y; }

    addStraight(num) {
        for (let i = 0; i < num; i++) this.addSegment(0, this.lastY());
    }

    addCurve(num, curve) {
        for (let i = 0; i < num; i++) this.addSegment(curve, this.lastY());
    }

    addHill(num, height) {
        for (let i = 0; i < num; i++) this.addSegment(0, this.lastY() + (height * Math.cos(i / num * Math.PI - Math.PI)));
    }

    addLowRollingHills(num, height) {
        for (let i = 0; i < num; i++) this.addSegment(0, this.lastY() + (height * Math.cos(i / num * Math.PI * 4))); // More frequent ups/downs
    }

    addSCurves() {
        this.addCurve(50, 2);
        this.addCurve(50, -2);
        this.addCurve(50, 3);
        this.addCurve(50, -3);
    }

    addDownHillToEnd() {
        // We need to return the y back to 0 so the loop is continuous.
        let num = 200;
        let startY = this.lastY();
        let endY = 0;

        for (let i = 0; i < num; i++) {
            // Linear interpolation from startY to 0
            let percent = (i + 1) / num;
            // Ease in/out?
            let y = startY + (endY - startY) * percent;
            this.addSegment(0, y);
        }
    }

    addSprites() {
        // Randomly add trees and rocks
        for (let i = 20; i < this.segments.length - 20; i += 5 + Math.floor(Math.random() * 20)) {
            // Left side (Fields)
            if (Math.random() > 0.5) {
                this.segments[i].sprites.push({ source: images.obstacles, ...this.sprites.TREE, offset: -6 - Math.random() * 10 });
            }
            // Right side (Fields)
            if (Math.random() > 0.5) {
                this.segments[i].sprites.push({ source: images.obstacles, ...this.sprites.ROCK, offset: 6 + Math.random() * 10 });
            }
        }

        // Add Finish Line Sprite at end?
        // this.segments[this.segments.length-1].sprites.push(...)
        // We'll draw finish line procedurally for now
    }

    // --- Core Loop ---

    loop(now) {
        if (!this.running) return;

        this.dt = Math.min(1, (now - this.lastTime) / 1000);
        this.lastTime = now;

        if (!this.paused) {
            this.time += this.dt; // Increment time
            try {
                this.update(this.dt);
                this.draw();
            } catch (e) {
                console.error("Game Loop Error:", e);
                this.running = false; // Stop ensuring we don't spam errors
                alert("Game Error: " + e.message); // Inform user
            }
        }

        requestAnimationFrame((t) => this.loop(t));
    }

    update(dt) {
        const playerSegment = this.findSegment(this.position + this.player.z);
        const playerW = this.roadWidth * 0.5; // Approx player hit width relative to road
        const speedPercent = this.player.speed / this.player.maxSpeed;

        this.position = (this.position + this.player.speed * dt);
        if (this.state === 'GAME_OVER_ANIMATION') {
            this.player.speed = this.accel(this.player.speed, -this.player.maxSpeed, this.dt); // Brake hard
            if (this.police) {
                this.police.speed = this.player.speed; // Police matches speed
                this.police.z = this.position + this.player.z - 100; // Police right beside/behind
                // Force offset to be next to player
                let targetOffset = this.player.x + (this.player.x > 0 ? -0.8 : 0.8);
                this.police.offset = this.police.offset + (targetOffset - this.police.offset) * 5 * dt;
            }

            this.gameOverTimer -= dt;
            if (this.gameOverTimer < 0 || Math.abs(this.player.speed) < 100) {
                this.finishRace('BUSTED');
            }
            // Continue rendering but skip player input
            // Update entities slightly?
        } else {
            // Normal Update
            this.updateGameLogic(dt);
        }

        // Draw regardless
        this.draw();
    }

    getRank() {
        let rank = 1;
        // Position on the loop
        let pLocalZ = this.position;

        this.entities.forEach(e => {
            if (!(e instanceof Opponent)) return;
            // Check relative distance in loop
            let dist = e.z - pLocalZ;
            if (dist < -this.trackLength / 2) dist += this.trackLength;
            if (dist > this.trackLength / 2) dist -= this.trackLength;

            // If dist > 0, they are ahead in the loop
            if (dist > 0) rank++;
        });
        return rank;
    }

    updateGameLogic(dt) {
        let playerSegment = this.findSegment(this.position + this.player.z);
        let speedPercent = this.player.speed / this.player.maxSpeed;

        this.position = (this.position + this.player.speed * dt);
        this.distance += this.player.speed * dt;

        // Shake Decay
        if (this.screenShake > 0) this.screenShake -= dt * 30;
        if (this.screenShake < 0) this.screenShake = 0;

        // Finish Line Logic
        if (this.position >= this.trackLength) {
            this.finishRace('FINISHED');
            return; // Stop updating game logic
        }

        while (this.position >= this.trackLength) this.position -= this.trackLength;
        while (this.position < 0) this.position += this.trackLength;

        let dx = this.dt * 2 * (this.player.speed / this.player.maxSpeed); // lateral speed

        if (this.input.left) this.player.x -= dx;
        else if (this.input.right) this.player.x += dx;

        // Centrifugal force
        this.player.x = this.player.x - (dx * speedPercent * playerSegment.curve * 2);

        // Accelerate / Brake
        if (this.input.up) this.player.speed = this.accel(this.player.speed, this.player.accel, this.dt);
        else if (this.input.down) this.player.speed = this.accel(this.player.speed, this.player.breaking, this.dt);
        else this.player.speed = this.accel(this.player.speed, this.player.decud, this.dt);

        // Attack Logic
        if (this.input.attack) {
            // Check for nearby opponents to hit
            [...this.entities, this.police].forEach(e => {
                if (Math.abs(e.z - (this.position + this.player.z)) < 200) { // Close Z
                    if (this.overlap(this.player.x, 1.8, e.offset, 1.0)) { // Widen overlap check for easier hits
                        // HIT!
                        // Push opponent away
                        let pushDir = (e.offset > this.player.x) ? 1 : -1;
                        e.offset += pushDir * 0.1;

                        // Visual/Audio feedback
                        this.ui.onMessage("HIT!");
                        this.sound.playHit();
                        this.screenShake = 10;
                        this.takedowns++;
                        this.score += 200;

                        // Slow them down?
                        if (e.speed) e.speed *= 0.9;
                    }
                }
            });
        }

        // Off-road handling
        if ((this.player.x < -1) || (this.player.x > 1)) {
            if (this.player.speed > this.player.offRoadLimit)
                this.player.speed = this.accel(this.player.speed, this.player.offRoadDecel, this.dt);

            // Collision with static sprites (trees/rocks)
            for (let i = 0; i < playerSegment.sprites.length; i++) {
                let sprite = playerSegment.sprites[i];
                let spriteW = 0.5;
                if (this.overlap(this.player.x, 0.8, sprite.offset, spriteW)) {
                    this.sound.playCrash();
                    this.screenShake = 20;
                    this.crash("CRASHED_STATIC"); // Pass reason
                }
            }
        }

        [...this.entities, this.police].forEach(e => {
            if (!e) return;
            e.update(dt, this);

            // Collision with player
            let playerRealZ = this.position + this.player.z;

            let dist = e.z - playerRealZ;
            while (dist > this.trackLength / 2) dist -= this.trackLength;
            while (dist < -this.trackLength / 2) dist += this.trackLength;

            if (Math.abs(dist) < 100) { // Close Z
                // Ignore collision with IDLE police
                if (e instanceof Police && e.state === 'IDLE') return;

                if (this.overlap(this.player.x, 0.8, e.offset, 0.8)) {
                    // Collision!
                    // If police -> busted
                    if (e instanceof Police && e.state === 'CHASING') {
                        this.onPoliceCatch();
                    } else {
                        // Crash
                        this.sound.playCrash();
                        this.screenShake = 20;
                        this.crash("CRASHED_VEHICLE");
                    }
                }
            }
        });

        // Clamp speed
        this.player.speed = Math.max(0, Math.min(this.player.speed, this.player.maxSpeed));

        // Update HUD
        // Update HUD (Dynamic Rank)
        let totalOpponents = this.entities.length;
        let rank = this.getRank();

        this.ui.onUpdateHud({
            speed: Math.floor(this.player.speed / 100),
            distance: Math.floor(this.distance / 1000),
            score: this.score,
            takedowns: this.takedowns,
            time: this.time,
            position: `${rank}/${totalOpponents + 1}`,
            rank: rank,
            health: this.health
        });
    }

    onPoliceCatch() {
        if (this.state === 'GAME_OVER_ANIMATION') return;
        this.state = 'GAME_OVER_ANIMATION';
        this.gameOverTimer = 2.0;
        this.ui.onMessage("BUSTED! PULL OVER!");
    }

    finishRace(reason = 'FINISHED') {
        this.running = false;
        this.sound.stopEngine();

        let rank = null;
        let finishBonus = 0;

        // 1. Position/Rank Bonus (ONLY if FINISHED)
        if (reason === 'FINISHED') {
            rank = 1;
            // Count opponents ahead
            this.entities.forEach(e => {
                if (!(e instanceof Opponent)) return;
                // If ahead of player
                if (e.z > (this.position + this.player.z)) rank++;
            });

            if (rank === 1) finishBonus = 5000;
            else if (rank === 2) finishBonus = 4000;
            else if (rank === 3) finishBonus = 3000;
            else finishBonus = 500; // Finish but poor rank
        }

        // 2. Health Bonus (Given for all scenarios, based on remaining health)
        let healthBonus = Math.floor(this.health) * 10;

        // 3. Takedown Bonus
        // Note: this.score accumulates 200/hit during play, but we reconstruct here to be safe and consistent.
        let takedownScore = this.takedowns * 200;

        let totalScore = finishBonus + takedownScore + healthBonus;

        this.ui.onGameOver({
            score: totalScore,
            distance: this.distance,
            reason: reason,
            rank: rank,
            takedowns: this.takedowns,
            healthBonus: healthBonus
        });
    }

    accel(v, a, dt) {
        return v + (a * dt);
    }

    overlap(x1, w1, x2, w2) {
        const half1 = w1 / 2;
        const half2 = w2 / 2;
        const min1 = x1 - half1;
        const max1 = x1 + half1;
        const min2 = x2 - half2;
        const max2 = x2 + half2;
        return !((max1 < min2) || (min1 > max2));
    }

    crash(reason = "CRASHED") {
        this.player.speed -= 10;
        this.health -= 1; // reduce health
        this.ui.onMessage("OUCH! Hit!"); // Feedback
        if (this.health <= 0) {
            this.health = 0;
            // Delegate to finishRace
            this.finishRace(reason);
        }
    }

    findSegment(z) {
        let index = Math.floor(z / this.segmentLength) % this.segments.length;
        if (index < 0) index += this.segments.length;
        return this.segments[index];
    }

    // --- Rendering ---

    draw() {
        this.ctx.clearRect(0, 0, this.width, this.height);

        let shakeX = 0;
        let shakeY = 0;
        if (this.screenShake > 0) {
            shakeX = (Math.random() - 0.5) * this.screenShake;
            shakeY = (Math.random() - 0.5) * this.screenShake;
        }

        this.ctx.save();
        this.ctx.translate(shakeX, shakeY);

        // Background - Parallax
        // Simple: draw image tiled
        if (images.background) {
            this.ctx.drawImage(images.background, 0, 0, this.width, this.height); // basic sky
        } else {
            this.ctx.fillStyle = '#72D7EE';
            this.ctx.fillRect(0, 0, this.width, this.height);
        }

        // Render Road
        let baseSegment = this.findSegment(this.position);
        let basePercent = (this.position % this.segmentLength) / this.segmentLength;
        let playerSegment = this.findSegment(this.position + this.player.z);
        let playerPercent = ((this.position + this.player.z) % this.segmentLength) / this.segmentLength;
        let playerY = 0;
        if (playerSegment) {
            playerY = playerSegment.p1.world.y + (playerSegment.p2.world.y - playerSegment.p1.world.y) * playerPercent;
        }

        let dx = - (baseSegment.curve * basePercent);
        let x = 0;
        let maxy = this.height;

        // Render Segments
        for (let n = 0; n < this.drawDistance; n++) {
            let segment = this.segments[(baseSegment.index + n) % this.segments.length];
            segment.looped = segment.index < baseSegment.index;
            // Loop adjustment for Z
            let loopOffset = segment.looped ? this.trackLength : 0;

            // Project
            this.project(segment.p1, (this.player.x * this.roadWidth) - x, playerY + this.cameraHeight, this.position - loopOffset);
            this.project(segment.p2, (this.player.x * this.roadWidth) - x - dx, playerY + this.cameraHeight, this.position - loopOffset);

            x += dx;
            dx += segment.curve;

            if ((segment.p1.camera.z <= this.cameraDepth) || // behind camera
                (segment.p2.screen.y >= maxy) ||             // clipped by nearer segment
                (segment.p2.screen.y >= segment.p1.screen.y)) // backface cull
                continue;

            this.renderSegment(segment);
            maxy = segment.p1.screen.y;
        }

        // Render Sprites (Back to front painter's alg is implicit if we iterate far to near? No, we iterate near to far usually)
        // Correct way: iterate far to near for sprites? OR Draw sprites in the loop above but they need to be sorted.
        // Standard fast way: 
        // 1. Draw all road segments (done above, implicitly handles occlusion via maxy)
        // 2. Draw sprites back-to-front.

        // Render Entities
        // We insert them into the painter's algorithm by checking if they belong to current segment 'n'
        for (let n = this.drawDistance - 1; n > 0; n--) {
            let segment = this.segments[(baseSegment.index + n) % this.segments.length];
            // Render Static Sprites
            for (let i = 0; i < segment.sprites.length; i++) {
                let sprite = segment.sprites[i];
                let scale = segment.p1.screen.scale;
                let sx = segment.p1.screen.x + (scale * sprite.offset * this.roadWidth * this.width / 2);
                let sy = segment.p1.screen.y;
                this.renderSprite(sprite.source, sprite, scale, sx, sy, -0.5, -1, segment.p1.world.y);
            }

            // Check for Dynamic Entities in this segment
            // Entity Z must be within segment range [segment.index * len, (segment.index+1)*len]
            // Handle wrap: if segment.looped ??
            let segmentZStart = segment.index * this.segmentLength;
            let segmentZEnd = segmentZStart + this.segmentLength;

            [...this.entities, this.police].forEach(e => {
                // Handle looping logic for finding segment.
                // It's expensive to iterate all entities for all segments.
                // Optimization: Pre-calculate entity segment index in update?
                // For now, brute force 20 entities is fine.

                // Wrap entity Z for comparison
                let ez = e.z;
                // But wait, segment indices are absolute 0..N.
                // e.z is 0..trackLength.

                if (ez >= segmentZStart && ez < segmentZEnd) {
                    e.render(this.ctx, this, segment);
                }
            });
        }

        // Render Player
        // We want the player to be on the road. 
        // playerY is the world Y of the road segment under the player.
        // We need to project that to screen Y using the standard project function logic.
        // ScreenY = H/2 - (scale * (worldY - cameraY) * H/2).
        // cameraY is (playerY + cameraHeight).
        // So worldY - cameraY = playerY - (playerY + cameraHeight) = -cameraHeight.
        // Wait, if we use that, the player is always at fixed screen Y?

        // Yes! In this pseudo-3D engine, the player's screen Y is effectively constant 
        // relative to the "horizon" if the camera follows the player's Y perfectly.
        // BUT, the visual effect of going up/down a hill comes from the road segments *ahead* moving.

        // However, the user says "player is flying". This implies the road is drawn BELOW the player's feet.
        // This usually happens if the camera smoothing lags or if the elevation change is too steep.

        // Let's stick to a fixed screen Y for the player (standard for these racers) 
        // but ensure the road renders correctly "under" it.
        // The issue might be simply the `this.height - ...` hardcoded math vs the projection math.

        // Let's rely on the updated renderPlayer which now respects destY.
        // We calculate destY properly here:
        // By definition of the camera following playerY, the road under the player is at:
        // CamY = PlayerY + H. P.y = PlayerY.
        // RelY = -H.
        // ScreenY = H/2 - (scale * -H * H/2) ... scale = 1/depth.
        // It simplifies to a constant.

        let destY = (this.height / 2) - (this.cameraDepth / this.player.z * (playerY - (playerY + this.cameraHeight)) * this.height / 2);
        // player.z is 0 in local space?? No.
        // p.screen.scale = cameraDepth / p.camera.z.
        // For the player, p.camera.z is... distance from camera?
        // In "Outrun" style, player is at fixed Z relative to camera.
        // Let's assume absolute fixed screen Y is safer.

        this.renderPlayer(this.width / 2, this.height - 20); // Fixed Y bottom

        // Wait, I just modified renderPlayer to consume destY directly.
        // So if I pass `this.height - 20`, it will draw there.
        // The previous bug was `this.height - targetHeight - bounce - 20`.
        // If I pass `this.height`, renderPlayer (new) does `destY - targetHeight`.
        // So passing `this.height` puts feet at bottom of screen.

        // Let's use `this.height` and let renderPlayer subtract height.

        this.ctx.restore();
    }

    project(p, cameraX, cameraY, cameraZ) {
        p.camera.x = (p.world.x || 0) - cameraX;
        p.camera.y = p.world.y - cameraY;
        p.camera.z = p.world.z - cameraZ;
        p.screen.scale = this.cameraDepth / p.camera.z;
        p.screen.x = Math.round((this.width / 2) + (p.screen.scale * p.camera.x * this.width / 2));
        p.screen.y = Math.round((this.height / 2) - (p.screen.scale * p.camera.y * this.height / 2));
        p.screen.w = Math.round((p.screen.scale * this.roadWidth * this.width / 2));
    }

    renderSegment(segment) {
        let x1 = segment.p1.screen.x;
        let y1 = segment.p1.screen.y;
        let w1 = segment.p1.screen.w;
        let x2 = segment.p2.screen.x;
        let y2 = segment.p2.screen.y;
        let w2 = segment.p2.screen.w;

        let r1 = this.rumbleWidth(w1, this.lanes);
        let r2 = this.rumbleWidth(w2, this.lanes);
        let l1 = this.laneMarkerWidth(w1, this.lanes);
        let l2 = this.laneMarkerWidth(w2, this.lanes);

        this.ctx.fillStyle = segment.color.grass;
        this.ctx.fillRect(0, y2, this.width, y1 - y2);

        this.polygon(x1 - w1 - r1, y1, x1 - w1, y1, x2 - w2, y2, x2 - w2 - r2, y2, segment.color.rumble);
        this.polygon(x1 + w1 + r1, y1, x1 + w1, y1, x2 + w2, y2, x2 + w2 + r2, y2, segment.color.rumble);

        if (segment.isFinish) {
            // Draw Checkered Flag Pattern
            let checkSize = w1 / 6; // approximate
            let rows = 2; // draw 2 rows depth perception? No, just pattern the road quad

            // Simplest: Draw the road white, and then black squares
            this.polygon(x1 - w1, y1, x1 + w1, y1, x2 + w2, y2, x2 - w2, y2, '#FFF'); // Base white

            let lanes = 6;
            let bw1 = w1 * 2 / lanes;
            let bw2 = w2 * 2 / lanes;

            this.ctx.fillStyle = '#000';
            for (let i = 0; i < lanes; i++) {
                // Checkers
                if ((segment.index + i) % 2 === 0) {
                    let bx1 = x1 - w1 + i * bw1;
                    let bx2 = x2 - w2 + i * bw2;
                    this.polygon(bx1, y1, bx1 + bw1, y1, bx2 + bw2, y2, bx2, y2, '#000');
                }
            }
        } else {
            this.polygon(x1 - w1, y1, x1 + w1, y1, x2 + w2, y2, x2 - w2, y2, segment.color.road);
        }

        if (segment.color.lane) {
            let lanew1 = w1 * 2 / this.lanes;
            let lanew2 = w2 * 2 / this.lanes;
            let lanex1 = x1 - w1 + lanew1;
            let lanex2 = x2 - w2 + lanew2;
            for (let lane = 1; lane < this.lanes; lanex1 += lanew1, lanex2 += lanew2, lane++)
                this.polygon(lanex1 - l1 / 2, y1, lanex1 + l1 / 2, y1, lanex2 + l2 / 2, y2, lanex2 - l2 / 2, y2, '#FFF');
        }
    }

    rumbleWidth(projectedRoadWidth, lanes) { return projectedRoadWidth / Math.max(6, 2 * lanes); }
    laneMarkerWidth(projectedRoadWidth, lanes) { return projectedRoadWidth / Math.max(32, 8 * lanes); }

    polygon(x1, y1, x2, y2, x3, y3, x4, y4, color) {
        this.ctx.fillStyle = color;
        this.ctx.beginPath();
        this.ctx.moveTo(x1, y1);
        this.ctx.lineTo(x2, y2);
        this.ctx.lineTo(x3, y3);
        this.ctx.lineTo(x4, y4);
        this.ctx.closePath();
        this.ctx.fill();
    }

    renderSprite(image, spriteDef, scale, destX, destY, offsetX, offsetY) {
        if (!image) return;

        // Normalize scaling. Assume "standard" sprite is 64 logical units.
        // If image is 1024px, we scale it down to match logical size relative to roadWidth (2000).
        let logicalW = spriteDef.w || 64;
        let logicalH = spriteDef.h || 64;
        let spriteScale = spriteDef.scale || 1; // Respect sprite definition scale

        let destW = (logicalW * scale * this.width / 2) * spriteScale * (this.sprites.startScale || 1);
        let destH = (logicalH * scale * this.width / 2) * spriteScale * (this.sprites.startScale || 1);

        // Aspect Ratio Maintenance
        // If actual image (or source rect) aspect ratio differs, preserve it based on destW
        let sw = spriteDef.sourceW || image.width;
        let sh = spriteDef.sourceH || image.height;

        let aspectRatio = sw / sh;
        destH = destW / aspectRatio;

        let sx = spriteDef.sourceX || spriteDef.x || 0;
        let sy = spriteDef.sourceY || spriteDef.y || 0;

        destX += (destW * offsetX);
        destY += (destH * offsetY);

        this.ctx.drawImage(image, sx, sy, sw, sh, destX, destY, destW, destH);
    }

    renderPlayer(destX, destY) {
        // Player bounce based on speed
        let bounce = (1.5 * Math.random() * (this.player.speed / this.player.maxSpeed) * this.width / 800) * 4;

        if (images.player) {
            // Target size: 25% of screen height
            const targetHeight = this.height * 0.25;
            const aspectRatio = images.player.width / images.player.height;
            const targetWidth = targetHeight * aspectRatio;

            // Use destY passed from draw() which accounts for hill elevation
            // But we need to offset it to draw the bottom of the sprite at destY
            // destY is the screen Y of the road surface under the player

            this.ctx.drawImage(images.player,
                destX - targetWidth / 2,
                destY - targetHeight - bounce,
                targetWidth,
                targetHeight
            );
        } else {
            this.ctx.fillStyle = 'red';
            this.ctx.fillRect(destX - 20, destY - 80 - bounce, 40, 80);
        }
    }
}
