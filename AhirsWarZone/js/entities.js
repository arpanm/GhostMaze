export class Unit {
    constructor(x, y, team, type, color, logo) {
        this.x = x;
        this.y = y;
        this.team = team; // 'red' or 'blue'
        this.type = type; // 'tank' or 'plane'
        this.color = color || (team === 'blue' ? '#3498db' : '#e74c3c');
        this.logo = logo; // Emoji logic
        this.width = 40;
        this.height = 20;
        this.health = 100;
        this.maxHealth = 100;
        this.selected = false;
        this.angle = 0; // Movement angle (for planes mostly, or ground slope)
        this.alive = true;
    }

    takeDamage(amount) {
        this.health -= amount;
        if (this.health <= 0) {
            this.health = 0;
            this.alive = false;
        }
    }

    draw(ctx) {
        // Base Unit Draw (Subclasses override)
        ctx.fillStyle = this.color;
        if (this.selected) {
            ctx.strokeStyle = '#f1c40f';
            ctx.lineWidth = 3;
            ctx.strokeRect(this.x - this.width / 2 - 5, this.y - this.height - 5, this.width + 10, this.height + 10);
        }
    }

    drawLogo(ctx) {
        if (this.logo) {
            ctx.font = '16px serif';
            ctx.fillStyle = '#fff';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            // Draw logo offset a bit above or on the unit
            ctx.fillText(this.logo, 0, -15);
        }
    }
}

export class Tank extends Unit {
    constructor(x, y, team, color, logo) {
        super(x, y, team, 'tank', color, logo);
        this.speed = 2;
        this.turretAngle = team === 'blue' ? -Math.PI / 4 : -Math.PI * 0.75;
    }

    update(terrain, keys, boundsWidth) {
        if (!this.selected && this.team === 'blue') return; // Only update movement if selected (or AI controlled externally)

        if (this.team === 'blue') {
            if (keys['ArrowLeft']) this.move(-1, terrain);
            if (keys['ArrowRight']) this.move(1, terrain);
        }
    }

    move(dir, terrain) {
        this.x += dir * this.speed;
        // Clamp to terrain
        this.y = terrain.getHeightAt(this.x);
        // Calculate angle based on terrain slope
        const nextY = terrain.getHeightAt(this.x + 5);
        this.angle = Math.atan2(nextY - this.y, 5);
    }

    draw(ctx) {
        super.draw(ctx);
        ctx.save();
        ctx.translate(this.x, this.y);
        ctx.rotate(this.angle);

        // Body
        ctx.fillStyle = this.color;
        ctx.fillRect(-15, -10, 30, 10); // Main Body
        ctx.fillRect(-10, -15, 20, 10); // Turret Base

        // Barrel (Independent rotation)
        ctx.rotate(-this.angle); // Cancel body rotation for barrel
        ctx.rotate(this.turretAngle);
        ctx.fillStyle = '#2c3e50';
        ctx.fillRect(0, -3, 25, 6);
        ctx.rotate(-this.turretAngle);
        ctx.rotate(this.angle);

        // Logo
        this.drawLogo(ctx);

        ctx.restore();
    }
}

export class Plane extends Unit {
    constructor(x, y, team, color, logo) {
        super(x, y, team, 'plane', color, logo);
        this.y = 80 + Math.random() * 100; // Fly high
        this.baseY = this.y;
        this.speed = 2.5;
        this.direction = team === 'blue' ? 1 : -1;
        this.time = Math.random() * 100;
    }

    update(terrain, keys) {
        // Controlled via keys if selected and blue
        if (this.team === 'blue' && this.selected) {
            if (keys['ArrowLeft']) { this.x -= this.speed; this.direction = -1; }
            if (keys['ArrowRight']) { this.x += this.speed; this.direction = 1; }
        } else if (this.team === 'red') {
            // AI Movement (Simple patrol)
            this.x += this.speed * this.direction;
            if (this.x > 2000 || this.x < 0) this.direction *= -1;
        }

        // Ensure bounds
        if (this.x < 0) this.x = 0;
        if (this.x > 2000) this.x = 2000; // Assuming world width

        this.time += 0.05;
        this.y = this.baseY + Math.sin(this.time) * 5; // Slight hover effect
    }

    draw(ctx) {
        super.draw(ctx);
        ctx.save();
        ctx.translate(this.x, this.y);
        if (this.direction < 0) ctx.scale(-1, 1);

        ctx.fillStyle = this.color || (this.team === 'blue' ? '#3498db' : '#e74c3c');

        // Simple Plane Shape
        ctx.beginPath();
        ctx.moveTo(15, 0); // Nose
        ctx.lineTo(-10, -10); // Tail top
        ctx.lineTo(-10, 5); // Bottom
        ctx.fill();

        // Wing
        ctx.fillStyle = '#ddd';
        ctx.beginPath();
        ctx.moveTo(5, 0);
        ctx.lineTo(-5, 15);
        ctx.lineTo(0, 0);
        ctx.fill();

        // Logo
        if (this.direction < 0) ctx.scale(-1, 1); // Unflip for text? No, text draws backwards if flipped.
        // If flipped, we need to unflip just for text or draw text separate.
        // Actually, simple fix:
        ctx.scale(this.direction < 0 ? -1 : 1, 1); // Reset
        this.drawLogo(ctx);

        ctx.restore();
    }
}

export class Projectile {
    constructor(x, y, vx, vy, type, team) {
        this.x = x;
        this.y = y;
        this.vx = vx;
        this.vy = vy;
        this.type = type; // 'missile', 'bomb'
        this.team = team; // 'blue' or 'red'
        this.radius = 4;
        this.active = true;
    }

    update(gravity, wind) {
        this.vy += gravity;
        this.vx += wind * 0.05; // Wind effect
        this.x += this.vx;
        this.y += this.vy;
    }

    draw(ctx) {
        if (this.type === 'bomb') {
            // Fire Blast visual
            const gradient = ctx.createRadialGradient(this.x, this.y, 1, this.x, this.y, this.radius * 2);
            gradient.addColorStop(0, '#f1c40f'); // Yellow center
            gradient.addColorStop(0.5, '#e67e22'); // Orange mid
            gradient.addColorStop(1, 'rgba(192, 57, 43, 0)'); // Red/Transparent edge

            ctx.fillStyle = gradient;
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.radius * 2.5, 0, Math.PI * 2); // Larger visual than collider
            ctx.fill();

        } else {
            // Missile
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
            ctx.fillStyle = this.type === 'bomb' ? '#2c3e50' : '#e67e22'; // Fallback
            ctx.fill();
        }
    }
}

export class Structure extends Unit {
    constructor(x, y, team, type, color, logo) {
        super(x, y, team, type, color, logo); // type: 'bunker' or 'tower'
        this.width = type === 'bunker' ? 50 : 30;
        this.height = type === 'bunker' ? 20 : 60;
        this.y -= this.height; // Sit ON terrain
        this.health = type === 'bunker' ? 200 : 150;
        this.maxHealth = this.health;
    }

    update(terrain) {
        // Static
    }

    draw(ctx) {
        // Base
        ctx.fillStyle = this.color;
        ctx.fillRect(this.x - this.width / 2, this.y, this.width, this.height);

        // Detail
        ctx.fillStyle = 'rgba(0,0,0,0.3)';
        if (this.type === 'bunker') {
            // Embrasures
            ctx.fillRect(this.x - 15, this.y + 5, 10, 5);
            ctx.fillRect(this.x + 5, this.y + 5, 10, 5);
        } else {
            // Tower head
            ctx.fillRect(this.x - this.width / 2 - 5, this.y - 10, this.width + 10, 10);
        }

        ctx.save();
        ctx.translate(this.x, this.y);
        this.drawLogo(ctx);
        ctx.restore();

        // Health bar mini
        const hpPct = this.health / this.maxHealth;
        ctx.fillStyle = 'red';
        ctx.fillRect(this.x - this.width / 2, this.y - 10, this.width, 5);
        ctx.fillStyle = '#2ecc71';
        ctx.fillRect(this.x - this.width / 2, this.y - 10, this.width * hpPct, 5);
    }
}

export class Particle {
    constructor(x, y, color, speed, life) {
        this.x = x;
        this.y = y;
        const angle = Math.random() * Math.PI * 2;
        this.vx = Math.cos(angle) * speed;
        this.vy = Math.sin(angle) * speed;
        this.color = color;
        this.life = life; // Frames or time
        this.maxLife = life;
        this.size = Math.random() * 3 + 1;
        this.gravity = 0.1;
    }

    update() {
        this.x += this.vx;
        this.y += this.vy;
        this.vy += this.gravity; // Gravity fall
        this.life--;
        this.size *= 0.95; // Shrink
    }

    draw(ctx) {
        ctx.globalAlpha = this.life / this.maxLife;
        ctx.fillStyle = this.color;
        ctx.beginPath();
        ctx.arc(this.x, this.y, Math.max(0, this.size), 0, Math.PI * 2);
        ctx.fill();
        ctx.globalAlpha = 1.0;
    }
}
