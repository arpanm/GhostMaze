const STONE_TYPES = [
    { type: 'diamond', symbol: '💎', points: 50 },
    { type: 'ruby', symbol: '🔴', points: 30 },
    { type: 'emerald', symbol: '🟢', points: 20 },
    { type: 'sapphire', symbol: '🔵', points: 10 }
];

export class Stone {
    constructor(col, row) {
        this.col = col;
        this.row = row;
        let rand = Math.floor(Math.random() * STONE_TYPES.length);
        this.data = STONE_TYPES[rand];
        this.points = this.data.points;
        this.symbol = this.data.symbol;
        this.spawnTime = Date.now();
        this.lifetime = 10000; // 10 seconds
    }

    isExpired() {
        return Date.now() - this.spawnTime > this.lifetime;
    }

    draw(ctx, cellSize, offsetX, offsetY) {
        let x = offsetX + (this.col + 0.5) * cellSize;
        let y = offsetY + (this.row + 0.5) * cellSize;

        ctx.font = `${cellSize * 0.5}px serif`;
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";
        ctx.fillText(this.symbol, x, y);
    }
}
