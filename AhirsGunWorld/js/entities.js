import { getWeapon } from './weapons.js';

// Base character class
class Character {
    constructor(x, y, team, name, avatar) {
        this.x = x; this.y = y;
        this.team = team; // 'green' or 'red'
        this.name = name || (team === 'green' ? 'Soldier' : 'Enemy');
        this.avatar = avatar || (team === 'green' ? '🪖' : '💀');
        this.radius = 12;
        this.speed = 2;
        this.health = 100;
        this.maxHealth = 100;
        this.alive = true;
        this.weapon = getWeapon('pistol');
        this.inventory = [getWeapon('pistol')];
        this.lastFireTime = 0;
        this.vx = 0; this.vy = 0;
        this.angle = 0; // facing direction
        this.shield = 50;
        this.maxShield = 50;
        this.shieldActive = false;
        this.shieldCooldown = 0;
        this.vehicleMode = null; // null, 'car', 'plane', 'sub'
        this.coins = 0;
        this.kills = 0;
    }

    takeDamage(amount) {
        if (!this.alive) return;
        if (this.shieldActive && this.shield > 0) {
            const absorbed = Math.min(this.shield, amount);
            this.shield -= absorbed;
            amount -= absorbed;
        }
        this.health -= amount;
        if (this.health <= 0) {
            this.health = 0;
            this.alive = false;
        }
    }

    heal(amount) {
        this.health = Math.min(this.maxHealth, this.health + amount);
    }

    canFire(now) {
        return this.alive && (now - this.lastFireTime) >= this.weapon.fireRate;
    }

    fire(now, targetX, targetY, projectiles) {
        if (!this.canFire(now)) return;
        this.lastFireTime = now;
        const angle = Math.atan2(targetY - this.y, targetX - this.x);
        this.angle = angle;

        if (this.weapon.type === 'melee') {
            // Melee attack — check if target is in range
            projectiles.push(new Projectile(this.x, this.y, angle, this.weapon, this.team, true));
        } else if (this.weapon.type === 'beam') {
            projectiles.push(new Projectile(this.x, this.y, angle, this.weapon, this.team, false, true));
        } else {
            projectiles.push(new Projectile(this.x, this.y, angle, this.weapon, this.team));
        }
    }

    move(dx, dy, map) {
        if (!this.alive) return;
        let spd = this.speed;
        if (this.vehicleMode === 'car') spd *= 2;
        if (this.vehicleMode === 'sub') spd *= 0.7;

        const nx = this.x + dx * spd;
        const ny = this.y + dy * spd;

        const canFly = this.vehicleMode === 'plane';
        if (canFly || !map.isWall(nx, this.y, this.radius)) this.x = nx;
        if (canFly || !map.isWall(this.x, ny, this.radius)) this.y = ny;
    }

    equipWeapon(weaponId) {
        const w = this.inventory.find(w => w.id === weaponId);
        if (w) this.weapon = w;
    }

    addWeapon(weapon) {
        if (!this.inventory.find(w => w.id === weapon.id)) {
            this.inventory.push(weapon);
        }
    }

    draw(ctx, camX, camY) {
        if (!this.alive) return;
        const sx = this.x - camX;
        const sy = this.y - camY;

        // Shield glow
        if (this.shieldActive && this.shield > 0) {
            ctx.beginPath();
            ctx.arc(sx, sy, this.radius + 6, 0, Math.PI * 2);
            ctx.strokeStyle = 'rgba(0, 200, 255, 0.5)';
            ctx.lineWidth = 2;
            ctx.stroke();
        }

        // Body
        const bodyColor = this.team === 'green' ? '#2ecc71' : '#c0392b';
        const outlineColor = this.team === 'green' ? '#27ae60' : '#922b21';

        // Vehicle mode visual
        if (this.vehicleMode === 'car') {
            ctx.fillStyle = bodyColor;
            ctx.fillRect(sx - 14, sy - 8, 28, 16);
            ctx.fillStyle = '#333';
            ctx.fillRect(sx - 12, sy + 6, 6, 4);
            ctx.fillRect(sx + 6, sy + 6, 6, 4);
        } else if (this.vehicleMode === 'plane') {
            ctx.fillStyle = bodyColor;
            ctx.beginPath();
            ctx.moveTo(sx + 16, sy);
            ctx.lineTo(sx - 12, sy - 10);
            ctx.lineTo(sx - 12, sy + 10);
            ctx.closePath();
            ctx.fill();
        } else if (this.vehicleMode === 'sub') {
            ctx.fillStyle = bodyColor;
            ctx.beginPath();
            ctx.ellipse(sx, sy, 16, 10, 0, 0, Math.PI * 2);
            ctx.fill();
            ctx.fillStyle = '#555';
            ctx.fillRect(sx - 2, sy - 14, 4, 6);
        } else {
            // Regular soldier
            ctx.beginPath();
            ctx.arc(sx, sy, this.radius, 0, Math.PI * 2);
            ctx.fillStyle = bodyColor;
            ctx.fill();
            ctx.strokeStyle = outlineColor;
            ctx.lineWidth = 2;
            ctx.stroke();

            // Scars for red team
            if (this.team === 'red') {
                ctx.strokeStyle = '#600';
                ctx.lineWidth = 1;
                ctx.beginPath();
                ctx.moveTo(sx - 4, sy - 4);
                ctx.lineTo(sx + 2, sy + 2);
                ctx.moveTo(sx + 2, sy - 5);
                ctx.lineTo(sx - 2, sy + 1);
                ctx.stroke();
            }

            // Direction indicator
            ctx.beginPath();
            ctx.moveTo(sx, sy);
            ctx.lineTo(sx + Math.cos(this.angle) * 18, sy + Math.sin(this.angle) * 18);
            ctx.strokeStyle = this.team === 'green' ? '#fff' : '#faa';
            ctx.lineWidth = 2;
            ctx.stroke();
        }

        // Health bar
        const barW = 24, barH = 3;
        ctx.fillStyle = '#333';
        ctx.fillRect(sx - barW / 2, sy - this.radius - 8, barW, barH);
        ctx.fillStyle = this.health > 30 ? '#2ecc71' : '#e74c3c';
        ctx.fillRect(sx - barW / 2, sy - this.radius - 8, barW * (this.health / this.maxHealth), barH);

        // Shield bar
        if (this.maxShield > 0) {
            ctx.fillStyle = '#333';
            ctx.fillRect(sx - barW / 2, sy - this.radius - 12, barW, 2);
            ctx.fillStyle = '#3498db';
            ctx.fillRect(sx - barW / 2, sy - this.radius - 12, barW * (this.shield / this.maxShield), 2);
        }

        // Name
        ctx.fillStyle = '#fff';
        ctx.font = '9px Arial';
        ctx.textAlign = 'center';
        ctx.fillText(this.name, sx, sy - this.radius - 15);
    }
}

export class Player extends Character {
    constructor(x, y, name, avatar) {
        super(x, y, 'green', name, avatar);
        this.isPlayer = true;
        this.speed = 2.5;
    }

    activateShield() {
        if (this.shieldCooldown <= 0 && this.shield > 0) {
            this.shieldActive = true;
            this.shieldCooldown = 5000; // 5s cooldown after deactivation
        }
    }

    update(dt) {
        if (this.shieldActive && this.shield <= 0) {
            this.shieldActive = false;
        }
        if (!this.shieldActive && this.shieldCooldown > 0) {
            this.shieldCooldown -= dt;
        }
        // Shield regen when not active
        if (!this.shieldActive && this.shieldCooldown <= 0) {
            this.shield = Math.min(this.maxShield, this.shield + 0.02 * dt);
        }
    }
}

export class Teammate extends Character {
    constructor(x, y, name, index) {
        super(x, y, 'green', name, '🪖');
        this.isPlayer = false;
        this.aiState = 'follow';
        this.targetEnemy = null;
        this.stateTimer = 0;
        this.followOffset = { x: (index % 4 - 1.5) * 40, y: Math.floor(index / 4) * 40 + 30 };
    }
}

export class Enemy extends Character {
    constructor(x, y, diffMult, isBoss, name) {
        super(x, y, 'red', name || (isBoss ? 'BOSS' : 'Red Soldier'), isBoss ? '👹' : '💀');
        this.isBoss = isBoss;
        this.health = isBoss ? 200 * diffMult : 60 + 20 * diffMult;
        this.maxHealth = this.health;
        this.speed = 1.5 + 0.3 * diffMult;
        this.shield = isBoss ? 100 : 30;
        this.maxShield = this.shield;
        this.aiState = 'patrol';
        this.targetEntity = null;
        this.stateTimer = 0;
        this.patrolTarget = null;
        this.accuracy = 0.3 + 0.2 * diffMult; // 0.3 to 0.9
        this.reactionTime = 1000 - 300 * diffMult; // smaller = faster

        if (isBoss) {
            this.weapon = getWeapon('rocket');
            this.radius = 16;
        } else if (diffMult > 2) {
            this.weapon = getWeapon('rifle');
        }
    }
}

export class Pet {
    constructor(x, y, team) {
        this.x = x; this.y = y;
        this.team = team;
        this.emoji = team === 'green' ? '🐕' : '🐺';
        this.name = team === 'green' ? 'Rex' : 'Fang';
        this.health = 80;
        this.maxHealth = 80;
        this.alive = true;
        this.radius = 8;
        this.speed = 3;
        this.damage = 8;
        this.attackCooldown = 0;
        this.targetEnemy = null;
    }

    takeDamage(amount) {
        this.health -= amount;
        if (this.health <= 0) { this.health = 0; this.alive = false; }
    }

    heal(amount) {
        this.health = Math.min(this.maxHealth, this.health + amount);
    }

    update(dt, owner, enemies, map) {
        if (!this.alive) return;
        this.attackCooldown -= dt;

        // Find nearest enemy within range
        let nearestDist = 150;
        this.targetEnemy = null;
        for (const e of enemies) {
            if (!e.alive) continue;
            const d = Math.hypot(e.x - this.x, e.y - this.y);
            if (d < nearestDist) {
                nearestDist = d;
                this.targetEnemy = e;
            }
        }

        if (this.targetEnemy) {
            // Move towards enemy
            const dx = this.targetEnemy.x - this.x;
            const dy = this.targetEnemy.y - this.y;
            const dist = Math.hypot(dx, dy);
            if (dist > 25) {
                const nx = this.x + (dx / dist) * this.speed;
                const ny = this.y + (dy / dist) * this.speed;
                if (!map.isWall(nx, this.y, this.radius)) this.x = nx;
                if (!map.isWall(this.x, ny, this.radius)) this.y = ny;
            }
            // Attack
            if (dist < 30 && this.attackCooldown <= 0) {
                this.targetEnemy.takeDamage(this.damage);
                this.attackCooldown = 800;
            }
        } else {
            // Follow owner
            const dx = owner.x - this.x;
            const dy = owner.y + 25 - this.y;
            const dist = Math.hypot(dx, dy);
            if (dist > 35) {
                const nx = this.x + (dx / dist) * this.speed;
                const ny = this.y + (dy / dist) * this.speed;
                if (!map.isWall(nx, this.y, this.radius)) this.x = nx;
                if (!map.isWall(this.x, ny, this.radius)) this.y = ny;
            }
        }
    }

    draw(ctx, camX, camY) {
        if (!this.alive) return;
        const sx = this.x - camX;
        const sy = this.y - camY;
        ctx.font = '16px Arial';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(this.emoji, sx, sy);

        // Health bar
        const barW = 18, barH = 2;
        ctx.fillStyle = '#333';
        ctx.fillRect(sx - barW / 2, sy - 14, barW, barH);
        ctx.fillStyle = this.health > 25 ? '#2ecc71' : '#e74c3c';
        ctx.fillRect(sx - barW / 2, sy - 14, barW * (this.health / this.maxHealth), barH);
    }
}

export class Projectile {
    constructor(x, y, angle, weapon, team, isMelee = false, isBeam = false) {
        this.x = x; this.y = y;
        this.angle = angle;
        this.speed = weapon.speed || 8;
        this.vx = Math.cos(angle) * this.speed;
        this.vy = Math.sin(angle) * this.speed;
        this.damage = weapon.damage;
        this.range = weapon.range;
        this.team = team;
        this.startX = x; this.startY = y;
        this.alive = true;
        this.isMelee = isMelee;
        this.isBeam = isBeam;
        this.radius = isMelee ? 15 : (isBeam ? 3 : 4);
        this.type = weapon.type;
        this.life = isMelee ? 100 : (isBeam ? 150 : 5000);
    }

    update(dt, entities, map) {
        if (!this.alive) return;
        this.life -= dt;
        if (this.life <= 0) { this.alive = false; return; }

        this.x += this.vx;
        this.y += this.vy;

        // Range check
        if (Math.hypot(this.x - this.startX, this.y - this.startY) > this.range) {
            this.alive = false;
            return;
        }

        // Wall collision (not for beam/melee)
        if (!this.isMelee && !this.isBeam && map.isWall(this.x, this.y, 2)) {
            this.alive = false;
            // Damage cover
            for (const cover of map.covers) {
                if (cover.hp > 0 && Math.hypot(this.x - cover.x, this.y - cover.y) < 16) {
                    cover.hp -= this.damage;
                }
            }
            return;
        }

        // Entity collision
        for (const e of entities) {
            if (!e.alive || e.team === this.team) continue;
            if (Math.hypot(this.x - e.x, this.y - e.y) < e.radius + this.radius) {
                e.takeDamage(this.damage);
                this.alive = false;
                return;
            }
        }
    }

    draw(ctx, camX, camY) {
        if (!this.alive) return;
        const sx = this.x - camX;
        const sy = this.y - camY;

        if (this.isBeam) {
            ctx.beginPath();
            ctx.moveTo(this.startX - camX, this.startY - camY);
            ctx.lineTo(sx, sy);
            ctx.strokeStyle = this.team === 'green' ? 'rgba(0, 255, 100, 0.8)' : 'rgba(255, 50, 50, 0.8)';
            ctx.lineWidth = 3;
            ctx.stroke();
        } else if (this.isMelee) {
            ctx.beginPath();
            ctx.arc(sx, sy, this.radius, 0, Math.PI * 2);
            ctx.fillStyle = 'rgba(255, 255, 255, 0.3)';
            ctx.fill();
        } else if (this.type === 'explosive') {
            ctx.font = '12px Arial';
            ctx.textAlign = 'center';
            ctx.fillText('🚀', sx, sy);
        } else {
            ctx.beginPath();
            ctx.arc(sx, sy, this.radius, 0, Math.PI * 2);
            ctx.fillStyle = this.team === 'green' ? '#aaffaa' : '#ffaaaa';
            ctx.fill();
        }
    }
}
