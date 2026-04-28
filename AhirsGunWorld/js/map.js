// Map generation for each level
const TERRAIN_THEMES = {
    jungle:     { floor: '#3a6b2a', wall: '#1a3a0e', cover: '#2d5a1e', accent: '#5a9a3e', obstacles: ['🌳','🌿','🪨'] },
    desert:     { floor: '#d4b860', wall: '#8a7030', cover: '#c2a645', accent: '#e8d080', obstacles: ['🪨','🏜️','🌵'] },
    underwater: { floor: '#2a5a7a', wall: '#0d2a3a', cover: '#1a4a6a', accent: '#4a8aaa', obstacles: ['🪸','🐚','⚓'] },
    arctic:     { floor: '#d0e8f0', wall: '#8ab0c0', cover: '#a0c8d8', accent: '#e8f4f8', obstacles: ['🧊','❄️','⛄'] },
    urban:      { floor: '#666666', wall: '#333333', cover: '#555555', accent: '#888888', obstacles: ['🏗️','🚗','📦'] },
    volcano:    { floor: '#5a2a0a', wall: '#2a0a00', cover: '#4a1a0a', accent: '#8a3a1a', obstacles: ['🔥','🪨','💀'] }
};

export class GameMap {
    constructor(width, height, terrain, levelIndex) {
        this.tileSize = 32;
        this.cols = Math.floor(width / this.tileSize);
        this.rows = Math.floor(height / this.tileSize);
        this.theme = TERRAIN_THEMES[terrain] || TERRAIN_THEMES.jungle;
        this.terrain = terrain;
        this.grid = [];
        this.covers = [];
        this.lootCrates = [];
        this.generate(levelIndex);
    }

    generate(levelIndex) {
        // Initialize with floor
        this.grid = Array(this.rows).fill(0).map(() => Array(this.cols).fill(0));

        // Border walls
        for (let r = 0; r < this.rows; r++) {
            this.grid[r][0] = 1;
            this.grid[r][this.cols - 1] = 1;
        }
        for (let c = 0; c < this.cols; c++) {
            this.grid[0][c] = 1;
            this.grid[this.rows - 1][c] = 1;
        }

        // Random wall clusters (more as levels increase)
        const wallCount = 15 + Math.floor(levelIndex * 1.5);
        for (let i = 0; i < wallCount; i++) {
            const cx = 3 + Math.floor(Math.random() * (this.cols - 6));
            const cy = 3 + Math.floor(Math.random() * (this.rows - 6));
            const size = 1 + Math.floor(Math.random() * 3);
            for (let dy = 0; dy < size; dy++) {
                for (let dx = 0; dx < size; dx++) {
                    const r = cy + dy, c = cx + dx;
                    if (r > 0 && r < this.rows - 1 && c > 0 && c < this.cols - 1) {
                        this.grid[r][c] = 1;
                    }
                }
            }
        }

        // Ensure spawn areas are clear (left for green, right for red)
        for (let r = 2; r < 8; r++) {
            for (let c = 2; c < 8; c++) this.grid[r][c] = 0;
            for (let c = this.cols - 8; c < this.cols - 2; c++) this.grid[r][c] = 0;
        }

        // Cover objects (destructible)
        const coverCount = 10 + Math.floor(levelIndex * 0.5);
        for (let i = 0; i < coverCount; i++) {
            const c = 3 + Math.floor(Math.random() * (this.cols - 6));
            const r = 3 + Math.floor(Math.random() * (this.rows - 6));
            if (this.grid[r][c] === 0) {
                this.covers.push({
                    x: c * this.tileSize + this.tileSize / 2,
                    y: r * this.tileSize + this.tileSize / 2,
                    hp: 50,
                    emoji: this.theme.obstacles[Math.floor(Math.random() * this.theme.obstacles.length)]
                });
            }
        }

        // Loot crates
        const lootCount = 5 + Math.floor(levelIndex * 0.3);
        for (let i = 0; i < lootCount; i++) {
            const c = 3 + Math.floor(Math.random() * (this.cols - 6));
            const r = 3 + Math.floor(Math.random() * (this.rows - 6));
            if (this.grid[r][c] === 0) {
                const types = ['health', 'coins', 'ammo'];
                this.lootCrates.push({
                    x: c * this.tileSize + this.tileSize / 2,
                    y: r * this.tileSize + this.tileSize / 2,
                    type: types[Math.floor(Math.random() * types.length)],
                    collected: false
                });
            }
        }
    }

    isWall(px, py, radius) {
        const corners = [
            { x: px - radius, y: py - radius },
            { x: px + radius, y: py - radius },
            { x: px - radius, y: py + radius },
            { x: px + radius, y: py + radius }
        ];
        for (const corner of corners) {
            const c = Math.floor(corner.x / this.tileSize);
            const r = Math.floor(corner.y / this.tileSize);
            if (r < 0 || r >= this.rows || c < 0 || c >= this.cols) return true;
            if (this.grid[r][c] === 1) return true;
        }
        return false;
    }

    getSpawnPos(team) {
        if (team === 'green') {
            return { x: 4 * this.tileSize, y: 4 * this.tileSize };
        } else {
            return { x: (this.cols - 5) * this.tileSize, y: 4 * this.tileSize };
        }
    }

    draw(ctx, camX, camY, canvasW, canvasH) {
        const startC = Math.max(0, Math.floor(camX / this.tileSize));
        const endC = Math.min(this.cols, Math.ceil((camX + canvasW) / this.tileSize));
        const startR = Math.max(0, Math.floor(camY / this.tileSize));
        const endR = Math.min(this.rows, Math.ceil((camY + canvasH) / this.tileSize));

        for (let r = startR; r < endR; r++) {
            for (let c = startC; c < endC; c++) {
                const x = c * this.tileSize - camX;
                const y = r * this.tileSize - camY;
                if (this.grid[r][c] === 1) {
                    ctx.fillStyle = this.theme.wall;
                } else {
                    ctx.fillStyle = this.theme.floor;
                }
                ctx.fillRect(x, y, this.tileSize + 1, this.tileSize + 1);
            }
        }

        // Draw covers
        ctx.font = `${this.tileSize * 0.8}px Arial`;
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        for (const cover of this.covers) {
            if (cover.hp <= 0) continue;
            const sx = cover.x - camX;
            const sy = cover.y - camY;
            if (sx > -50 && sx < canvasW + 50 && sy > -50 && sy < canvasH + 50) {
                ctx.fillText(cover.emoji, sx, sy);
            }
        }

        // Draw loot
        for (const loot of this.lootCrates) {
            if (loot.collected) continue;
            const sx = loot.x - camX;
            const sy = loot.y - camY;
            if (sx > -50 && sx < canvasW + 50 && sy > -50 && sy < canvasH + 50) {
                const emoji = loot.type === 'health' ? '❤️' : loot.type === 'coins' ? '💰' : '📦';
                ctx.fillText(emoji, sx, sy);
            }
        }
    }
}
