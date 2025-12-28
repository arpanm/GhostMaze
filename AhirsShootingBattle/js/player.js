import { Projectile } from './projectile.js';
import { Decoy } from './decoy.js';
import { state, input } from './shared.js';
import { playFireSound, playHitSound } from './main.js';

export class Player {
    constructor(config) {
        this.name = config.name;
        this.avatar = config.avatar;
        this.color = config.color;
        this.weapon = config.weapon;

        this.x = 100;
        this.y = window.innerHeight - 100;
        this.radius = 20;
        this.speed = 3.5;
        this.angle = 0;

        this.health = 100;
        this.money = 0;
        this.isPlayer = true;
        this.decoyCharges = 0;
        this.lastFireTime = 0;
    }

    update(dt, input, map, canvas) {
        // --- Movement ---
        let dx = 0;
        let dy = 0;

        if (input.up) dy -= this.speed;
        if (input.down) dy += this.speed;
        if (input.left) dx -= this.speed;
        if (input.right) dx += this.speed;

        // Joystick Movement
        if (input.joystick.active) {
            dx = input.joystick.x * this.speed;
            dy = input.joystick.y * this.speed;
        }

        const nextX = this.x + dx;
        const nextY = this.y + dy;

        // Collision Check
        if (!map.checkWallCollision(nextX, this.y, this.radius)) {
            this.x = Math.max(this.radius, Math.min(canvas.width - this.radius, nextX));
        }
        if (!map.checkWallCollision(this.x, nextY, this.radius)) {
            this.y = Math.max(this.radius, Math.min(canvas.height - this.radius, nextY));
        }

        // --- Aiming & Firing ---
        if (input.tapPos) {
            // Calculate angle to tap position
            this.angle = Math.atan2(input.tapPos.y - this.y, input.tapPos.x - this.x);

            // Fire!
            if (input.fire) {
                this.fire(input.tapPos);
                input.fire = false; // Reset fire for single tap
                input.tapPos = null; // Reset tap
            }
        } else if (input.fire) {
            // Spacebar firing (fires in current angle)
            this.fire();
            input.fire = false;
        }
    }

    fire(targetPos = null) {
        const now = Date.now();
        if (now - this.lastFireTime < this.weapon.fireRate) return;

        // Projectile direction
        let angle = this.angle;
        if (targetPos) {
            angle = Math.atan2(targetPos.y - this.y, targetPos.x - this.x);
            this.angle = angle; // Update player angle to face tap
        }

        state.projectiles.push(new Projectile({
            x: this.x,
            y: this.y,
            angle: angle,
            speed: this.weapon.projectileSpeed,
            dmg: this.weapon.dmg,
            owner: 'player',
            color: this.color
        }));

        this.lastFireTime = now;
        playFireSound();
    }

    takeDamage(dmg) {
        this.health -= dmg;
        playHitSound();
        if (this.health <= 0) {
            this.health = 0;
            this.die();
        }
    }

    spawnDecoy() {
        if (this.decoyCharges <= 0) return;
        this.decoyCharges--;
        document.getElementById('decoy-count').innerText = this.decoyCharges;

        // Spawn 3 decoys in different directions
        for (let i = 0; i < 3; i++) {
            const angle = this.angle + (Math.random() - 0.5) * 2;
            state.decoys.push(new Decoy(this.x, this.y, angle, this.color, this.avatar));
        }
    }

    die() {
        // Handled in main.js end game logic
    }

    draw(ctx) {
        ctx.save();
        ctx.translate(this.x, this.y);
        ctx.rotate(this.angle);

        // Body Shadow
        ctx.shadowBlur = 10;
        ctx.shadowColor = 'rgba(0,0,0,0.5)';

        // Drawing Player Shape/Avatar
        ctx.fillStyle = this.color;
        ctx.beginPath();
        ctx.arc(0, 0, this.radius, 0, Math.PI * 2);
        ctx.fill();

        // Direction Indicator (Gun)
        ctx.fillStyle = '#333';
        ctx.fillRect(this.radius - 5, -5, 15, 10);

        // Avatar
        ctx.font = '20px Arial';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.rotate(-this.angle); // Keep avatar upright
        ctx.fillText(this.avatar, 0, 0);

        ctx.restore();

        // Name Tag
        ctx.fillStyle = 'white';
        ctx.font = 'bold 12px Orbitron';
        ctx.textAlign = 'center';
        ctx.fillText(this.name, this.x, this.y - 30);
    }
}
