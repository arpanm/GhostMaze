export class Player {
    constructor(name, color) {
        this.name = name;
        this.color = color;
        this.currentTile = 1;
        this.renderTile = 1; // For smooth animation
        this.targetTile = 1;
        this.moveSpeed = 0.1; // Tiles per frame? No, interpolation factor
    }

    reset() {
        this.currentTile = 1;
        this.renderTile = 1;
        this.targetTile = 1;
    }

    setTarget(tile) {
        this.targetTile = tile;
    }

    update() {
        // Simple lerp for now, can improve to hop tile by tile
        if (Math.abs(this.renderTile - this.targetTile) > 0.1) {
            const di = this.targetTile > this.renderTile ? 1 : -1;
            // Move 0.2 tiles per frame
            // this.renderTile += 0.2 * di;

            // Lerp approach
            this.renderTile += (this.targetTile - this.renderTile) * 0.1;

            if (Math.abs(this.renderTile - this.targetTile) < 0.1) {
                this.renderTile = this.targetTile;
                this.currentTile = this.targetTile;
                return true; // Finished moving
            }
            return false; // Still moving
        }
        return true; // Not moving
    }

    draw(board, ctx) {
        const pos = board.getTileCenter(Math.round(this.renderTile));

        ctx.beginPath();
        ctx.fillStyle = this.color;
        ctx.arc(pos.x, pos.y, 15, 0, Math.PI * 2);
        ctx.fill();

        ctx.strokeStyle = 'white';
        ctx.lineWidth = 2;
        ctx.stroke();

        // Pulse effect
        ctx.beginPath();
        ctx.strokeStyle = `rgba(${this.color === '#00ff00' ? '0,255,0' : '255,255,255'}, 0.5)`;
        ctx.arc(pos.x, pos.y, 20 + Math.sin(performance.now() * 0.01) * 2, 0, Math.PI * 2);
        ctx.stroke();
    }
}
