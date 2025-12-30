import { state } from './shared.js';

export class Entity {
    constructor(config) {
        this.x = config.x || window.innerWidth + 100;
        this.y = config.y || Math.random() * window.innerHeight;
        this.type = config.type; // 'fish', 'human', 'whale', 'eel', 'jellyfish', 'bullet'
        this.radius = config.radius || 15;
        this.speed = config.speed || 2;
        this.sinOffset = Math.random() * Math.PI * 2;
        this.dead = false;

        // Stats
        this.points = config.points || 0;
        this.hpValue = config.hpValue || 0;
        this.damage = config.damage || 0;
        this.symbol = config.symbol || '🐟';
        this.color = config.color || 'white';

        // Behavioral
        this.angle = config.angle || 0;
        this.isDangerous = config.isDangerous || false;
        this.hasBullet = false; // For boats/humans
    }

    update(dt, playerSpeed) {
        // Move across the screen relative to shark speed
        this.x -= (this.speed + playerSpeed);

        // Oscillation for some types
        if (this.type === 'jellyfish' || this.type === 'eel') {
            this.y += Math.sin(Date.now() / 500 + this.sinOffset) * 2;
        }

        // Offscreen check
        if (this.x < -100) {
            this.dead = true;
        }
    }

    draw(ctx) {
        if (this.dead) return;

        ctx.save();
        ctx.translate(this.x, this.y);
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';

        // Draw Shadow/Glow
        if (this.isDangerous) {
            ctx.shadowBlur = 15;
            ctx.shadowColor = this.type === 'eel' ? '#00f2ff' : '#e74c3c';
        }

        ctx.font = `${this.radius * 2}px Arial`;
        ctx.fillStyle = this.color;
        ctx.fillText(this.symbol, 0, 0);

        ctx.restore();
    }
}
