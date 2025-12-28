import { state } from './shared.js';

export class Projectile {
    constructor(config) {
        this.x = config.x;
        this.y = config.y;
        this.angle = config.angle;
        this.speed = config.speed;
        this.dmg = config.dmg;
        this.owner = config.owner; // 'player' or 'enemy'
        this.color = config.color || 'yellow';
        this.dead = false;
        this.radius = 4;
    }

    update(dt, targets, map) {
        if (this.dead) return;

        this.x += Math.cos(this.angle) * this.speed;
        this.y += Math.sin(this.angle) * this.speed;

        // --- Boundary Check ---
        if (this.x < 0 || this.x > window.innerWidth || this.y < 0 || this.y > window.innerHeight) {
            this.dead = true;
            return;
        }

        // --- Obstacle Check ---
        if (map.checkWallCollision(this.x, this.y, this.radius)) {
            this.dead = true;
            return;
        }

        // --- Target Hit Check ---
        for (const target of targets) {
            if (!target || target.dead) continue;

            // Robust Skip Owner check
            if (this.owner === 'player' && target.isPlayer) continue;
            if (this.owner === 'enemy' && target.isEnemy) continue;

            // Simple Circle Collision
            const dx = this.x - target.x;
            const dy = this.y - target.y;
            const dist = Math.sqrt(dx * dx + dy * dy);

            if (dist < target.radius + this.radius) {
                this.hit(target);
                break;
            }
        }
    }

    hit(target) {
        this.dead = true;
        target.takeDamage(this.dmg);

        // Trigger visual effect (handled in main.js or here?)
        this.triggerHitEffect();
    }

    triggerHitEffect() {
        const flash = document.getElementById('hit-flash');
        flash.classList.remove('hidden');
        flash.classList.add('flash-active');
        setTimeout(() => {
            flash.classList.remove('flash-active');
            setTimeout(() => flash.classList.add('hidden'), 100);
        }, 100);
    }

    draw(ctx) {
        if (this.dead) return;

        ctx.save();
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
        ctx.fillStyle = this.color;
        ctx.fill();

        // Trail
        ctx.shadowBlur = 10;
        ctx.shadowColor = this.color;

        ctx.restore();
    }
}
