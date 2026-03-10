export class Person {
    constructor(x, y, type, avatar) {
        this.x = x;
        this.y = y;
        this.radius = 20;
        this.type = type; // 'SPY', 'KILLER', 'CIVILIAN', 'OWNER'
        this.avatar = avatar;
        this.color = this.getColorByType(type);

        // Movement state
        this.speed = 0.05; // Base speed for AI
        this.vx = (Math.random() - 0.5) * this.speed;
        this.vy = (Math.random() - 0.5) * this.speed;
        this.moveTimer = 0;

        // Game State
        this.isDead = false;
        this.hasNecklace = (type === 'OWNER');

        // Intelligence
        this.questionsAnswered = 0;
        this.maxQuestions = 3;
        this.knowledge = []; // Array of facts they know
        this.isLiar = (type === 'KILLER'); // Killer always lies (or mixes lies)
        this.seenKiller = false;
    }

    getColorByType(type) {
        // Only visible for debug/Spy - Normal people should look same ring color or none?
        // Actually UI requires "Normal people" look same.
        // But for Debug/Spy player, we need to know who is who? No, player shouldn't know!
        // Everyone should have same ring unless inspected?
        if (type === 'SPY') return '#00ff88';
        return '#ffffff'; // Everyone else matches
    }

    update(dt, walls, others, bounds) {
        if (this.isDead) return;

        // Player handled separately usually, but if this is generic person:
        if (this.type === 'SPY') return;

        // AI Random Walk
        this.moveTimer -= dt;
        if (this.moveTimer <= 0) {
            // New direction
            if (Math.random() > 0.3) {
                // Move
                const angle = Math.random() * Math.PI * 2;
                this.vx = Math.cos(angle) * this.speed * dt; // Scale by dt not needed here if applied in pos
                this.vx = Math.cos(angle) * 0.1; // 0.1 px/ms
                this.vy = Math.sin(angle) * 0.1;
                this.moveTimer = 1000 + Math.random() * 2000;
            } else {
                // Stop
                this.vx = 0;
                this.vy = 0;
                this.moveTimer = 500 + Math.random() * 1000;
            }
        }

        this.move(this.vx * dt, this.vy * dt, walls);

        // Keep in bounds
        if (this.x < this.radius) this.x = this.radius;
        if (this.x > bounds.w - this.radius) this.x = bounds.w - this.radius;
        if (this.y < this.radius) this.y = this.radius;
        if (this.y > bounds.h - this.radius) this.y = bounds.h - this.radius;
    }

    move(dx, dy, walls) {
        // X Axis
        this.x += dx;
        if (this.checkCollision(walls)) {
            this.x -= dx;
            this.vx *= -1; // Bounce AI
        }

        // Y Axis
        this.y += dy;
        if (this.checkCollision(walls)) {
            this.y -= dy;
            this.vy *= -1; // Bounce AI
        }
    }

    checkCollision(walls) {
        for (let w of walls) {
            // AABB vs Circle (Simplified to AABB vs Square approx for speed or pure Circle-Rect)
            // Lets do Closest Point Circle-Rect
            const clampX = Math.max(w.x, Math.min(this.x, w.x + w.w));
            const clampY = Math.max(w.y, Math.min(this.y, w.y + w.h));

            const dx = this.x - clampX;
            const dy = this.y - clampY;

            if ((dx * dx + dy * dy) < (this.radius * this.radius)) {
                return true;
            }
        }
        return false;
    }

    draw(ctx) {
        if (this.isDead) return; // Or draw dead body?

        // Shadow
        ctx.fillStyle = "rgba(0,0,0,0.3)";
        ctx.beginPath();
        ctx.ellipse(this.x, this.y + 10, this.radius, this.radius * 0.4, 0, 0, Math.PI * 2);
        ctx.fill();

        // Avatar Body (Circle)
        ctx.fillStyle = this.type === 'SPY' ? '#222' : '#eee'; // Suit for spy?
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
        ctx.fill();

        // Selection/Type Ring
        ctx.strokeStyle = this.color;
        ctx.lineWidth = 3;
        ctx.stroke();

        // Emoji
        ctx.font = "24px Arial";
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";
        ctx.fillText(this.avatar, this.x, this.y);

        // Name/Role Label (Debug or if known)
        // ctx.fillStyle = "white";
        // ctx.font = "10px Arial";
        // ctx.fillText(this.type, this.x, this.y - 30);

        // Necklace Visual (Only for Owner if alive, or maybe subtle hint?)
        // Let's make it a small yellow dot on Owner/Killer if they have it?
        // No, keep it secret.
        // But maybe Owner has a crown/chain visible?
        if (this.type === 'OWNER' && !this.isDead) {
            ctx.fillStyle = "gold";
            ctx.beginPath();
            ctx.arc(this.x + 10, this.y - 10, 5, 0, Math.PI * 2);
            ctx.fill();
        }
    }
}
