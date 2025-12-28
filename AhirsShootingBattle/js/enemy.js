import { Projectile } from './projectile.js';
import { state } from './shared.js';

export class Enemy {
    constructor(config) {
        this.difficulty = config.difficulty;

        this.x = window.innerWidth - 100;
        this.y = 100;
        this.radius = 20;
        this.speed = this.difficulty.speed;
        this.accuracy = this.difficulty.accuracy;
        this.angle = Math.PI; // Facing left

        this.health = 100;
        this.money = 0;
        this.isEnemy = true;
        this.lastFireTime = 0;
        this.fireRate = 1000; // Constant base fire rate for AI

        this.state = 'WANDERING'; // WANDERING, CHASING_VAULT, ATTACKING
        this.target = null;
    }

    update(dt, player, map, canvas) {
        if (this.health <= 0) return;

        // --- AI Logic ---
        this.think(player, map);
        this.move(map, canvas);
        this.attack(player);
    }

    think(player, map) {
        // Simple priority: 1. Attack Player if close, 2. Chase Vault if exists, 3. Wander
        const distToPlayer = Math.sqrt((this.x - player.x) ** 2 + (this.y - player.y) ** 2);

        if (distToPlayer < 400) {
            this.state = 'ATTACKING';
            this.target = player;
        } else {
            const nearestVault = this.findNearestVault(map);
            if (nearestVault) {
                this.state = 'CHASING_VAULT';
                this.target = nearestVault;
            } else {
                this.state = 'WANDERING';
                this.target = null;
            }
        }
    }

    findNearestVault(map) {
        let minDesc = Infinity;
        let nearest = null;
        map.vaults.forEach(v => {
            if (v.collected) return;
            const d = Math.sqrt((this.x - v.x) ** 2 + (this.y - v.y) ** 2);
            if (d < minDesc) {
                minDesc = d;
                nearest = v;
            }
        });
        return nearest;
    }

    move(map, canvas) {
        if (!this.target && this.state !== 'WANDERING') return;

        let tx = this.x;
        let ty = this.y;

        if (this.state === 'WANDERING') {
            // Slight random movement or towards center
            tx = canvas.width / 2;
            ty = canvas.height / 2;
        } else {
            tx = this.target.x;
            ty = this.target.y;
        }

        const dist = Math.sqrt((tx - this.x) ** 2 + (ty - this.y) ** 2);
        const angle = Math.atan2(ty - this.y, tx - this.x);
        this.angle = angle;

        // Tactical Distance Maintenance
        if (this.state === 'ATTACKING' || (this.target && (this.target.isPlayer || this.target.isDecoy))) {
            const preferredDist = 200; // Keep 200px distance
            const hasLOS = map.hasLineOfSight(this.x, this.y, this.target.x, this.target.y);

            if (hasLOS) {
                if (dist < preferredDist - 20) {
                    // Too close! Move away
                    const moveAngle = angle + Math.PI;
                    const bdx = Math.cos(moveAngle) * this.speed;
                    const bdy = Math.sin(moveAngle) * this.speed;

                    if (!map.checkWallCollision(this.x + bdx, this.y, this.radius)) {
                        this.x += bdx;
                    }
                    if (!map.checkWallCollision(this.x, this.y + bdy, this.radius)) {
                        this.y += bdy;
                    }
                    return;
                } else if (dist < preferredDist + 20) {
                    // Sweet spot, stop moving
                    return;
                }
            }
        }

        const dx = Math.cos(angle) * this.speed;
        const dy = Math.sin(angle) * this.speed;

        const nextX = this.x + dx;
        const nextY = this.y + dy;

        // Collision Check
        if (!map.checkWallCollision(nextX, this.y, this.radius)) {
            this.x = nextX;
        }
        if (!map.checkWallCollision(this.x, nextY, this.radius)) {
            this.y = nextY;
        }
    }

    attack(player) {
        const now = Date.now();
        if (now - this.lastFireTime < this.fireRate) return;

        // Check line of sight (Simplified: just distance and accuracy)
        const dist = Math.sqrt((this.x - player.x) ** 2 + (this.y - player.y) ** 2);
        if (dist > 500) return;

        // Accuracy Roll
        const error = (1 - this.accuracy) * (Math.random() - 0.5) * 0.5;
        const fireAngle = Math.atan2(player.y - this.y, player.x - this.x) + error;

        state.projectiles.push(new Projectile({
            x: this.x,
            y: this.y,
            angle: fireAngle,
            speed: 12,
            dmg: 10,
            owner: 'enemy',
            color: '#e74c3c'
        }));

        this.lastFireTime = now;
    }

    takeDamage(dmg) {
        this.health -= dmg;
        if (this.health <= 0) {
            this.health = 0;
            this.die();
        }
    }

    die() {
        // Logic for enemy death, boneuses to player
    }

    draw(ctx) {
        if (this.health <= 0) return;

        ctx.save();
        ctx.translate(this.x, this.y);
        ctx.rotate(this.angle);

        // Body
        ctx.fillStyle = '#e74c3c'; // Military Red
        ctx.beginPath();
        ctx.arc(0, 0, this.radius, 0, Math.PI * 2);
        ctx.fill();

        // Gun
        ctx.fillStyle = '#333';
        ctx.fillRect(this.radius - 5, -5, 15, 10);

        // Avatar
        ctx.font = '20px Arial';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.rotate(-this.angle);
        ctx.fillText('🤖', 0, 0);

        ctx.restore();

        // HP Bar (Micro)
        ctx.fillStyle = 'rgba(0,0,0,0.5)';
        ctx.fillRect(this.x - 20, this.y - 35, 40, 5);
        ctx.fillStyle = '#e74c3c';
        ctx.fillRect(this.x - 20, this.y - 35, 40 * (this.health / 100), 5);
    }
}
