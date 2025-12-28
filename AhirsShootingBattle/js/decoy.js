export class Decoy {
    constructor(x, y, angle, color, avatar) {
        this.x = x;
        this.y = y;
        this.angle = angle;
        this.color = color;
        this.avatar = avatar;
        this.radius = 20;
        this.speed = 3;
        this.dead = false;
        this.health = 30; // Decoys are fragile
        this.spawnTime = Date.now();
        this.lifespan = 5000; // 5 seconds
    }

    update(dt, map) {
        if (this.dead) return;

        // Move in a constant direction
        const nextX = this.x + Math.cos(this.angle) * this.speed;
        const nextY = this.y + Math.sin(this.angle) * this.speed;

        if (map.checkWallCollision(nextX, nextY, this.radius) ||
            nextX < 0 || nextX > window.innerWidth ||
            nextY < 0 || nextY > window.innerHeight ||
            Date.now() - this.spawnTime > this.lifespan) {
            this.dead = true;
        } else {
            this.x = nextX;
            this.y = nextY;
        }
    }

    takeDamage(dmg) {
        this.health -= dmg;
        if (this.health <= 0) this.dead = true;
    }

    draw(ctx) {
        if (this.dead) return;

        ctx.save();
        ctx.translate(this.x, this.y);
        ctx.rotate(this.angle);
        ctx.globalAlpha = 0.6; // Slightly transparent

        ctx.fillStyle = this.color;
        ctx.beginPath();
        ctx.arc(0, 0, this.radius, 0, Math.PI * 2);
        ctx.fill();

        ctx.font = '20px Arial';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.rotate(-this.angle);
        ctx.fillText(this.avatar, 0, 0);

        ctx.restore();
    }
}
