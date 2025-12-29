export class Map {
    constructor(vaultCount) {
        this.width = window.innerWidth;
        this.height = window.innerHeight;
        this.obstacles = [];
        this.vaults = [];
        this.generate(vaultCount);
    }

    generate(vaultCount) {
        // Clear previous
        this.obstacles = [];
        this.vaults = [];

        // Generate Obstacles
        const obstacleTypes = [
            { type: 'hill', color: '#4b5563', size: { min: 60, max: 120 }, symbol: '⛰️' },
            { type: 'tree', color: '#065f46', size: { min: 40, max: 80 }, symbol: '🌳' },
            { type: 'stone', color: '#57534e', size: { min: 30, max: 60 }, symbol: '🪨' },
            { type: 'bush', color: '#166534', size: { min: 35, max: 70 }, symbol: '🌿' }
        ];

        // Ensure central corridor is relatively clear for start
        const safeZone = 150;

        for (let i = 0; i < 25; i++) {
            const config = obstacleTypes[Math.floor(Math.random() * obstacleTypes.length)];
            const size = config.size.min + Math.random() * (config.size.max - config.size.min);

            let x, y, tries = 0;
            do {
                x = Math.random() * (this.width - size);
                y = Math.random() * (this.height - size);
                tries++;
            } while (this.isNearEdge(x, y, size) || tries < 10 && this.isNearStart(x, y, safeZone));

            this.obstacles.push({
                x, y, size,
                type: config.type,
                color: config.color,
                symbol: config.symbol
            });
        }

        // Generate Money Vaults
        for (let i = 0; i < vaultCount; i++) {
            this.spawnVault(500 + Math.floor(Math.random() * 1000), 30000); // Initial vaults last 30s
        }
    }

    spawnVault(amount, lifetime = 15000) {
        let x, y, tries = 0;
        do {
            x = 50 + Math.random() * (this.width - 100);
            y = 50 + Math.random() * (this.height - 100);
            tries++;
        } while (this.isColliding(x, y, 30) && tries < 20);

        this.vaults.push({
            x, y,
            size: 30,
            collected: false,
            amount: amount,
            lifetime: lifetime,
            maxLifetime: lifetime
        });
    }

    update(dt) {
        this.vaults = this.vaults.filter(v => {
            if (v.collected) return false;
            v.lifetime -= dt;
            return v.lifetime > 0;
        });
    }

    isNearStart(x, y, zone) {
        // ... (existing code remains same)
        const userStart = { x: 50, y: this.height - 50 };
        const enemyStart = { x: this.width - 50, y: 50 };

        const distUser = Math.sqrt((x - userStart.x) ** 2 + (y - userStart.y) ** 2);
        const distEnemy = Math.sqrt((x - enemyStart.x) ** 2 + (y - enemyStart.y) ** 2);

        return distUser < zone || distEnemy < zone;
    }

    isNearEdge(x, y, size) {
        return x < size || y < size || x > this.width - size || y > this.height - size;
    }

    isColliding(x, y, size) {
        return this.obstacles.some(o => {
            const dist = Math.sqrt((x - o.x) ** 2 + (y - o.y) ** 2);
            return dist < (size + o.size) / 2;
        });
    }

    checkWallCollision(x, y, radius) {
        for (const o of this.obstacles) {
            const dx = x - o.x;
            const dy = y - o.y;
            const dist = Math.sqrt(dx * dx + dy * dy);
            if (dist < radius + o.size / 2.5) {
                return true;
            }
        }
        return false;
    }

    hasLineOfSight(x1, y1, x2, y2) {
        const dist = Math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2);
        const steps = Math.floor(dist / 10);

        for (let i = 1; i < steps; i++) {
            const t = i / steps;
            const px = x1 + (x2 - x1) * t;
            const py = y1 + (y2 - y1) * t;

            if (this.checkWallCollision(px, py, 5)) {
                return false;
            }
        }
        return true;
    }

    draw(ctx, width, height) {
        this.width = width;
        this.height = height;

        // Draw Grass Texture
        ctx.fillStyle = '#101b2d';
        ctx.fillRect(0, 0, width, height);

        // Draw Obstacles
        this.obstacles.forEach(o => {
            ctx.shadowBlur = 10;
            ctx.shadowColor = 'rgba(0,0,0,0.5)';

            ctx.font = `${o.size}px Arial`;
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.fillText(o.symbol, o.x, o.y);

            ctx.shadowBlur = 0;
        });

        // Draw Vaults
        this.vaults.forEach(v => {
            if (v.collected) return;

            // Blinking effect when expiring
            if (v.lifetime < 3000 && Math.floor(Date.now() / 250) % 2 === 0) return;

            ctx.save();
            ctx.beginPath();
            ctx.arc(v.x, v.y, 15, 0, Math.PI * 2);
            ctx.fillStyle = '#f1c40f';
            ctx.fill();

            // Glow
            ctx.shadowBlur = 15;
            ctx.shadowColor = '#f1c40f';
            ctx.strokeStyle = '#fff';
            ctx.lineWidth = 2;
            ctx.stroke();

            ctx.fillStyle = '#b8860b';
            ctx.font = 'bold 12px Arial';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.fillText('$', v.x, v.y);
            ctx.restore();
        });
    }
}
