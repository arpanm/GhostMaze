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
                if (Math.random() < state.difficulty.bulletFreq) { // Use difficulty bullet frequency
                    state.entities.push(new Entity({
                        type: 'bullet',
                        symbol: '🌑',
                        x: entity.x,
                        y: entity.y,
                        radius: 5,
                        speed: 8 * state.difficulty.speedMult,
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

        // Adjust dangerous vs safe creature probability based on dangerMult
        // dangerMult = 1.0 is default. 
        // We can skew the 'rand' value to make higher results (usually dangerous) more likely.
        let adjustedRand = rand;
        if (state.difficulty.dangerMult > 1) {
            // Skew upwards: x^(1/n) where n > 1 pushes values towards 1
            adjustedRand = Math.pow(rand, 1 / state.difficulty.dangerMult);
        } else {
            // Skew downwards if easier
            adjustedRand = Math.pow(rand, state.difficulty.dangerMult);
        }

        // Multiplier based on Level/Sector
        const progressionMult = (state.level - 1) * 0.2 + (state.sector - 1) * 0.1 + 1;
        const totalMult = state.difficulty.speedMult * progressionMult;

        if (adjustedRand < 0.3) {
            // High Value Prey: Tropical Fish
            config = { type: 'fish', symbol: '🐠', radius: 10, speed: 2 * totalMult, points: 150, hpValue: 5, color: '#ff9f43' };
        } else if (adjustedRand < 0.45) {
            // Standard Prey: Blue Fish
            config = { type: 'fish', symbol: '🐟', radius: 12, speed: 1.5 * totalMult, points: 100, hpValue: 5, color: '#3498db' };
        } else if (adjustedRand < 0.55) {
            // New: Crab
            config = { type: 'crab', symbol: '🦀', radius: 15, speed: 0.8 * totalMult, points: 200, hpValue: 10, color: '#ee5253' };
        } else if (adjustedRand < 0.62) {
            // New: Tortoise
            config = { type: 'tortoise', symbol: '🐢', radius: 25, speed: 0.5 * totalMult, points: 300, hpValue: 15, color: '#10ac84' };
        } else if (adjustedRand < 0.68) {
            // New: Octopus
            config = { type: 'octopus', symbol: '🐙', radius: 20, speed: 1.2 * totalMult, points: 400, hpValue: 10, color: '#5f27cd' };
        } else if (adjustedRand < 0.78) {
            // Dangerous: Jellyfish
            config = { type: 'jellyfish', symbol: '🪼', radius: 15, speed: 1 * totalMult, damage: 15, isDangerous: true, color: '#ff9ff3' };
        } else if (adjustedRand < 0.88) {
            // Dangerous: Eel
            config = { type: 'eel', symbol: '🐍', radius: 20, speed: 2.5 * totalMult, damage: 25, isDangerous: true, color: '#00d2d3' };
        } else if (adjustedRand < 0.94) {
            // Human Swimmer
            config = { type: 'human', symbol: '🏊', radius: 18, speed: 0.5 * totalMult, points: 500, hpValue: 20, color: '#ffcc00' };
        } else {
            // Extreme Danger: Whale
            config = { type: 'whale', symbol: '🐋', radius: 45, speed: 0.2 * totalMult, damage: 50, isDangerous: true, color: '#54a0ff' };
        }

        state.entities.push(new Entity(config));

        // Occasional Boat - frequency also scales
        if (Math.random() < 0.08 * state.difficulty.dangerMult * progressionMult) {
            state.entities.push(new Entity({ type: 'human', symbol: '🚤', radius: 30, speed: 3 * totalMult, points: 1000, hpValue: 30, color: '#ffffff' }));
        }
    }

    draw(ctx) {
        // Deep Sea Gradient - Changes based on Level/Sector
        const hue = 210 - (state.level - 1) * 20 - (state.sector - 1) * 5;
        const darkness = 20 - (state.level - 1) * 5 - (state.sector - 1) * 10;

        const gradient = ctx.createLinearGradient(0, 0, 0, window.innerHeight);
        gradient.addColorStop(0, `hsl(${hue}, 60%, ${darkness + 10}%)`);
        gradient.addColorStop(1, `hsl(${hue}, 80%, ${darkness}%)`);

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
