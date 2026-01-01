import { Utils } from './utils.js';

export class Snake {
    constructor(game, id, x, y, color, isPlayer = false, name = "Snake", logo = null) {
        this.game = game;
        this.id = id;
        this.x = x;
        this.y = y;
        this.color = color;
        this.isPlayer = isPlayer;
        this.name = name;
        this.logo = logo;

        this.angle = Math.random() * Math.PI * 2;
        this.baseSpeed = isPlayer ? 180 : 150; // pixels per second
        this.speed = this.baseSpeed;
        this.turnSpeed = 4; // Radians per second of turning capability

        // Body
        this.radius = 10;
        this.spacing = 6; // Distance between segments in history
        this.history = []; // Array of {x, y} positions
        this.historyLimit = 0; // Max history length needed

        // Growth
        this.targetLength = 20; // Initial segments
        this.currentLength = 20;

        // State
        this.alive = true;
        this.boostActive = false;

        // Initialize history
        for (let i = 0; i < this.targetLength * this.spacing; i++) {
            this.history.push({ x: x, y: y });
        }
    }

    update(dt) {
        if (!this.alive) return;

        // 1. Steering
        let targetAngle = this.angle;

        if (this.isPlayer) {
            const inputDir = this.game.input.getInputDirection();
            if (inputDir.x !== 0 || inputDir.y !== 0) {
                targetAngle = Math.atan2(inputDir.y, inputDir.x);
            }
        } else {
            // Simple AI: Wander or Chase
            // Implemented in AI Controller or here? Let's keep basic wander here for now
            // Or better, let Game class set a target for AI
            if (this.aiTarget) {
                const dx = this.aiTarget.x - this.x;
                const dy = this.aiTarget.y - this.y;
                targetAngle = Math.atan2(dy, dx);
            } else {
                // Wander wiggle
                targetAngle += Utils.random(-0.1, 0.1);
            }
        }

        // Smooth turning
        const diff = targetAngle - this.angle;
        // Normalize diff to -PI to PI
        let d = diff % (Math.PI * 2);
        if (d < -Math.PI) d += Math.PI * 2;
        if (d > Math.PI) d -= Math.PI * 2;

        const maxTurn = this.turnSpeed * dt;
        if (Math.abs(d) < maxTurn) {
            this.angle = targetAngle;
        } else {
            this.angle += Math.sign(d) * maxTurn;
        }

        // 2. Move Head
        const moveDist = this.speed * dt;
        this.x += Math.cos(this.angle) * moveDist;
        this.y += Math.sin(this.angle) * moveDist;

        // 3. Wall Collision (Bounce)
        this.checkWallCollision();

        // 4. Update History
        // We push new head position to front
        // We assume we move enough every frame. If dt is small, interpolation might be better
        // Simple approach: Always push head. Prune tail based on length.
        this.history.unshift({ x: this.x, y: this.y });

        // Calculate required history length based on segments & spacing
        this.historyLimit = Math.ceil(this.currentLength * this.spacing) + 1;

        // Prune
        if (this.history.length > this.historyLimit) {
            this.history.length = this.historyLimit;
        }

        // Growth animation
        if (this.currentLength < this.targetLength) {
            this.currentLength += 10 * dt; // Grow speed
        }
    }

    checkWallCollision() {
        const margin = this.radius;
        let hit = false;

        let newAngle = this.angle;

        if (this.x < margin) {
            this.x = margin;
            hit = true;
            // Force turn to right (0) or slightly up/down
            newAngle = Utils.random(-1, 1);
        } else if (this.x > this.game.width - margin) {
            this.x = this.game.width - margin;
            hit = true;
            // Force turn left (PI)
            newAngle = Math.PI + Utils.random(-1, 1);
        }

        if (this.y < margin) {
            this.y = margin;
            hit = true;
            // Force turn down (PI/2)
            newAngle = Math.PI / 2 + Utils.random(-1, 1);
        } else if (this.y > this.game.height - margin) {
            this.y = this.game.height - margin;
            hit = true;
            // Force turn up (-PI/2)
            newAngle = -Math.PI / 2 + Utils.random(-1, 1);
        }

        if (hit) {
            // Smoothly curve towards new angle or snap?
            // Snapping prevents getting stuck better
            this.angle = newAngle;
        }
    }

    // Check if head touches own body (approximate loop)
    getSelfLoopPolygon() {
        // Return array of points {x,y} if loop formed, else null
        const head = this.getHead();
        const historyLen = this.history.length;
        const minLoopSize = 20; // Must be at least this many segments long to be a loop

        // Check collision with older history
        // history[0] is head
        for (let i = minLoopSize * this.spacing; i < historyLen; i += this.spacing) {
            const pos = this.history[i];
            const dist = Utils.getDistance(head.x, head.y, pos.x, pos.y);

            if (dist < this.radius * 2) {
                // Loop found!
                // Extract polygon from 0 to i
                // Downsample for performance (every 5th point)
                const poly = [];
                for (let k = 0; k < i; k += 5) {
                    poly.push(this.history[k]);
                }
                return poly;
            }
        }
        return null;
    }

    render(ctx) {
        if (!this.alive) return;

        ctx.save();

        // Draw segments
        // We draw from tail to head so head is on top
        const segmentsToDraw = Math.floor(this.currentLength);

        for (let i = segmentsToDraw - 1; i >= 0; i--) {
            const historyIndex = Math.min(i * this.spacing, this.history.length - 1);
            const pos = this.history[historyIndex];
            if (!pos) continue;

            // visual radius
            let r = this.radius;
            // Taper tail
            if (i > segmentsToDraw - 5) {
                r *= (segmentsToDraw - i) / 5;
            }

            ctx.beginPath();
            ctx.arc(pos.x, pos.y, r, 0, Math.PI * 2);
            ctx.fillStyle = this.color;
            ctx.fill();

            // Border for clarity
            ctx.strokeStyle = "rgba(0,0,0,0.2)";
            ctx.lineWidth = 1;
            ctx.stroke();
        }

        // Draw Logo or Eyes on head
        const headX = this.x;
        const headY = this.y;

        if (this.logo) {
            ctx.save();
            ctx.translate(headX, headY);
            ctx.rotate(this.angle + Math.PI / 2); // Rotate text to match direction (facing 'up' usually for text?)
            // Actually snake moves in 'angle'. Text is usually upright. 
            // If we want the logo to rotate with head:
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.font = `${this.radius * 3.5}px Arial`;
            // Emojis might need checking if they center well
            ctx.fillStyle = "#fff"; // Not really used for emoji but good practice
            ctx.fillText(this.logo, 0, 0);
            ctx.restore();
        } else {
            // Fallback Eyes
            const eyeOffset = this.radius * 0.6;
            const eyeSize = this.radius * 0.3;

            // Eye positions relative to angle
            const lx = headX + Math.cos(this.angle - 0.5) * eyeOffset;
            const ly = headY + Math.sin(this.angle - 0.5) * eyeOffset;
            const rx = headX + Math.cos(this.angle + 0.5) * eyeOffset;
            const ry = headY + Math.sin(this.angle + 0.5) * eyeOffset;

            ctx.fillStyle = "white";
            ctx.beginPath(); ctx.arc(lx, ly, eyeSize, 0, Math.PI * 2); ctx.fill();
            ctx.beginPath(); ctx.arc(rx, ry, eyeSize, 0, Math.PI * 2); ctx.fill();

            ctx.fillStyle = "black";
            ctx.beginPath(); ctx.arc(lx, ly, eyeSize / 2, 0, Math.PI * 2); ctx.fill();
            ctx.beginPath(); ctx.arc(rx, ry, eyeSize / 2, 0, Math.PI * 2); ctx.fill();
        }

        // Name tag
        if (this.name) {
            ctx.fillStyle = "white";
            ctx.font = "10px sans-serif";
            ctx.textAlign = "center";
            ctx.fillText(this.name, headX, headY - this.radius - 5);
        }

        ctx.restore();
    }

    grow(amount) {
        this.targetLength += amount;
        this.radius = Math.min(25, 10 + (this.targetLength / 100)); // Cap size logic
    }

    // Get array of body circles for collision
    getBodySegments() {
        const segments = [];
        const count = Math.floor(this.currentLength);
        // Skip head (index 0) usually, but for general collision we might want it?
        // Usually body collision checking ignores the first few segments to prevent self-collision
        for (let i = 2; i < count; i++) { // Skip first 2 close to head
            const idx = Math.min(i * this.spacing, this.history.length - 1);
            segments.push({
                x: this.history[idx].x,
                y: this.history[idx].y,
                radius: this.radius,
                index: i // useful for cutting
            });
        }
        return segments;
    }

    getHead() {
        return { x: this.x, y: this.y, radius: this.radius };
    }
}
