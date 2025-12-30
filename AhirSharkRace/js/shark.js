import { state, CONFIG } from './shared.js';

export class Shark {
    constructor(config) {
        this.x = config.x || 100;
        this.y = config.y || window.innerHeight / 2;
        this.radius = 30;
        this.color = config.color || '#3498db';
        this.logo = config.logo || '🦈';
        this.name = config.name || 'AI Shark';
        this.isPlayer = config.isPlayer || false;

        this.health = CONFIG.maxHealth;
        this.maxSpeed = CONFIG.baseSpeed;
        this.currentSpeed = 0;
        this.angle = 0;
        this.dead = false;

        // Progress tracking for race
        this.progress = 0;
    }

    update(dt, inputMap) {
        if (this.dead) return;

        // --- Speed Logic (Health Dependent) ---
        // High health = fast, low health = slower
        let healthFactor = this.health / CONFIG.maxHealth;
        let speedMult = 1.0;

        if (healthFactor < 0.3) speedMult = 0.5;
        else if (healthFactor < 0.6) speedMult = 0.8;

        this.currentSpeed = this.maxSpeed * speedMult;

        if (this.isPlayer) {
            this.handlePlayerMovement(inputMap);
        } else {
            this.handleAIMovement();
        }

        // Clamp to screen bounds (only Y axis, X is mostly fixed/scrolling)
        this.y = Math.max(this.radius, Math.min(window.innerHeight - this.radius, this.y));
    }

    handlePlayerMovement(inputMap) {
        let dx = 0;
        let dy = 0;

        // Joystick
        if (inputMap.joystick.active) {
            dx = inputMap.joystick.x;
            dy = inputMap.joystick.y;
        } else {
            // Keyboard
            if (inputMap.up) dy = -1;
            if (inputMap.down) dy = 1;
            if (inputMap.left) dx = -1;
            if (inputMap.right) dx = 1;
        }

        // Apply movement relative to scrolling sea
        // Vertical movement is free
        this.y += dy * this.currentSpeed * 1.5;

        // Horizontal movement adjusts position relative to screen center
        this.x += dx * this.currentSpeed;

        // Constraint: Don't let player leave the left/right too far
        this.x = Math.max(50, Math.min(window.innerWidth * 0.4, this.x));

        // Angle based on vertical movement
        if (dy !== 0 || dx !== 0) {
            this.angle = Math.atan2(dy, dx + 2); // Leaning slightly forward
        } else {
            this.angle *= 0.95; // Return to neutral
        }
    }

    handleAIMovement() {
        // AI sharks just swim forward at their set speed
        // Occasional vertical oscillation
        this.y += Math.sin(Date.now() / 1000 + this.x) * 1;

        // AI sharks generally stay at their relative speed
        this.progress += this.currentSpeed;
    }

    takeDamage(dmg) {
        this.health -= dmg;
        if (this.health <= 0) {
            this.health = 0;
            this.dead = true;
        }
    }

    eat(points, hp) {
        state.score += points * state.difficulty.scoreMult;
        this.health = Math.min(CONFIG.maxHealth, this.health + hp);
    }

    draw(ctx) {
        if (this.dead) return;

        ctx.save();
        ctx.translate(this.x, this.y);
        ctx.rotate(this.angle);

        // Body Shape - Streamlined for racing
        const tailWave = Math.sin(Date.now() / 150) * 10;

        ctx.fillStyle = this.color;

        // Main Body (Torpedo shape)
        ctx.beginPath();
        ctx.ellipse(0, 0, this.radius * 2, this.radius * 0.8, 0, 0, Math.PI * 2);
        ctx.fill();

        // Tail (Dynamic)
        ctx.beginPath();
        ctx.moveTo(-this.radius * 1.5, 0);
        ctx.quadraticCurveTo(-this.radius * 2.5, tailWave, -this.radius * 3, tailWave * 1.5);
        ctx.lineTo(-this.radius * 3, -tailWave * 1.5);
        ctx.quadraticCurveTo(-this.radius * 2.5, -tailWave, -this.radius * 1.5, 0);
        ctx.fill();

        // Fins
        ctx.beginPath();
        ctx.moveTo(0, -this.radius * 0.5);
        ctx.lineTo(this.radius * 0.5, -this.radius * 1.5);
        ctx.lineTo(this.radius * 1.2, -this.radius * 0.5);
        ctx.fill();

        // Logo
        ctx.rotate(-this.angle);
        ctx.fillStyle = 'white';
        ctx.font = '20px Arial';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(this.logo, 0, 0);

        ctx.restore();

        // Health Bar (Minimal)
        if (this.isPlayer) {
            ctx.fillStyle = 'rgba(0,0,0,0.3)';
            ctx.fillRect(this.x - 30, this.y + 40, 60, 4);
            ctx.fillStyle = this.health > 40 ? '#2ecc71' : '#e74c3c';
            ctx.fillRect(this.x - 30, this.y + 40, 60 * (this.health / 100), 4);
        }
    }
}
