import { state, CONFIG } from './shared.js';
import { Entity } from './entity.js';

export class Sea {
    constructor() {
        this.spawnTimer = 0;
        this.bubbles = [];
        for (let i = 0; i < 30; i++) {
            this.bubbles.push({
                x: Math.random() * window.innerWidth,
                y: Math.random() * window.innerHeight,
                r: Math.random() * 3 + 1,
                s: Math.random() * 2 + 1
            });
        }
    }

    update(dt, playerSpeed) {
        // --- Spawning Logic ---
        this.spawnTimer += dt;
        const spawnDelay = 1000 * state.difficulty.spawnRate;

        if (this.spawnTimer > spawnDelay) {
            this.spawnEntity();
            this.spawnTimer = 0;
        }

        // Update Bubbles
        this.bubbles.forEach(b => {
            b.x -= (b.s + playerSpeed * 0.5);
            if (b.x < 0) b.x = window.innerWidth;
        });

        // Firing Logic for Humans in Boats
        state.entities.forEach(entity => {
            if (entity.symbol === '🚤' && !entity.dead) {
                if (Math.random() < 0.01) { // Chance to fire
                    state.entities.push(new Entity({
                        type: 'bullet',
                        symbol: '🌑',
                        x: entity.x,
                        y: entity.y,
                        radius: 5,
                        speed: 8,
                        damage: 10,
                        isDangerous: true
                    }));
                }
            }
        });
    }

    spawnEntity() {
        const rand = Math.random();
        let config = {};

        if (rand < 0.4) {
            // High Value Prey: Tropical Fish
            config = { type: 'fish', symbol: '🐠', radius: 10, speed: 2, points: 150, hpValue: 5, color: '#ff9f43' };
        } else if (rand < 0.55) {
            // Standard Prey: Blue Fish
            config = { type: 'fish', symbol: '🐟', radius: 12, speed: 1.5, points: 100, hpValue: 5, color: '#3498db' };
        } else if (rand < 0.65) {
            // New: Crab (Bottom dweller behavior later maybe, for now just floating)
            config = { type: 'crab', symbol: '🦀', radius: 15, speed: 0.8, points: 200, hpValue: 10, color: '#ee5253' };
        } else if (rand < 0.72) {
            // New: Tortoise
            config = { type: 'tortoise', symbol: '🐢', radius: 25, speed: 0.5, points: 300, hpValue: 15, color: '#10ac84' };
        } else if (rand < 0.78) {
            // New: Octopus
            config = { type: 'octopus', symbol: '🐙', radius: 20, speed: 1.2, points: 400, hpValue: 10, color: '#5f27cd' };
        } else if (rand < 0.84) {
            // Dangerous: Jellyfish
            config = { type: 'jellyfish', symbol: '🪼', radius: 15, speed: 1, damage: 15, isDangerous: true, color: '#ff9ff3' };
        } else if (rand < 0.90) {
            // Dangerous: Eel
            config = { type: 'eel', symbol: '🐍', radius: 20, speed: 2.5, damage: 25, isDangerous: true, color: '#00d2d3' };
        } else if (rand < 0.96) {
            // Human Swimmer
            config = { type: 'human', symbol: '🏊', radius: 18, speed: 0.5, points: 500, hpValue: 20, color: '#ffcc00' };
        } else {
            // Extreme Danger: Whale
            config = { type: 'whale', symbol: '🐋', radius: 45, speed: 0.2, damage: 50, isDangerous: true, color: '#54a0ff' };
        }

        state.entities.push(new Entity(config));

        // Occasional Boat
        if (Math.random() < 0.08) {
            state.entities.push(new Entity({ type: 'human', symbol: '🚤', radius: 30, speed: 3, points: 1000, hpValue: 30, color: '#ffffff' }));
        }
    }

    draw(ctx) {
        // Deep Sea Gradient
        const gradient = ctx.createLinearGradient(0, 0, 0, window.innerHeight);
        gradient.addColorStop(0, '#0a192f');
        gradient.addColorStop(1, '#020c1b');
        ctx.fillStyle = gradient;
        ctx.fillRect(0, 0, window.innerWidth, window.innerHeight);

        // Bubbles
        ctx.fillStyle = 'rgba(255, 255, 255, 0.2)';
        this.bubbles.forEach(b => {
            ctx.beginPath();
            ctx.arc(b.x, b.y, b.r, 0, Math.PI * 2);
            ctx.fill();
        });
    }
}
