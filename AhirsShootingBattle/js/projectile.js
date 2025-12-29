import { state } from './shared.js';
import { playMoneySound } from './audio.js';

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
        this.radius = config.radius || 4;
        this.isMelee = config.isMelee || false;
        this.lifetime = config.lifetime || 5000;
        this.aliveTime = 0;
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
        // --- Obstacle Check (Skip for melee sweeps to avoid instant-kill by walls) ---
        if (!this.isMelee && map.checkWallCollision(this.x, this.y, this.radius)) {
            this.dead = true;
            return;
        }

        // --- Lifetime Check ---
        this.aliveTime += dt;
        if (this.aliveTime > this.lifetime) {
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

        // Award money if player hits enemy
        if (this.owner === 'player' && target.isEnemy) {
            state.player.money += 100;
            try { playMoneySound(); } catch (e) { }
            this.triggerCollectEffect();
        }

        // Trigger visual effect
        this.triggerHitEffect();
    }

    triggerHitEffect() {
        const flash = document.getElementById('hit-flash');
        if (!flash) return;
        flash.classList.remove('hidden');
        flash.classList.add('flash-active');
        setTimeout(() => {
            flash.classList.remove('flash-active');
            setTimeout(() => flash.classList.add('hidden'), 100);
        }, 100);
    }

    triggerCollectEffect() {
        const flash = document.getElementById('collect-flash');
        if (!flash) return;
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
        if (this.isMelee) {
            // Draw a faint "sweep" arc instead of a solid circle for melee
            const opacity = 1 - (this.aliveTime / this.lifetime);
            ctx.globalAlpha = opacity * 0.3;
            // Sweep should be centered on player, but for now we draw the circle faintly
            ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
        } else {
            ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
        }
        ctx.fillStyle = this.color;
        ctx.fill();

        // Trail
        ctx.shadowBlur = 10;
        ctx.shadowColor = this.color;

        ctx.restore();
    }
}
