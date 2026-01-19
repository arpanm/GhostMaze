export class Player {
    constructor(name, color, isBot) {
        this.name = name;
        this.color = color;
        this.isBot = isBot; // Ensure isBot is saved
        this.currentTile = 1;
        this.renderTile = 1; // For smooth animation
        this.targetTile = 1;
        this.moveSpeed = 0.1;

        // Asset
        this.pawnImg = new Image();
        this.pawnImg.src = new URL('../assets/pawn.png', import.meta.url).href;
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
        if (Math.abs(this.renderTile - this.targetTile) > 0.1) {
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
        // Position relative to board grid
        const localPos = board.getTileCenter(this.renderTile);

        // Apply Global Board Offset
        const x = localPos.x + board.offsetX;
        const y = localPos.y + board.offsetY;

        const size = board.tileW * 0.6; // Pawn size relative to tile

        ctx.save();
        ctx.translate(x, y);

        // Draw Player Color Base (Shadow/Glow)
        ctx.shadowColor = this.color;
        ctx.shadowBlur = 15;
        ctx.fillStyle = this.color;

        ctx.beginPath();
        ctx.ellipse(0, size / 2 - 5, size / 2, size / 4, 0, 0, Math.PI * 2); // Oval shadow at base
        ctx.fill();

        ctx.shadowBlur = 0;

        // Draw Pawn Image
        if (this.pawnImg.complete) {
            // Draw image centered horizontally, and sitting on the pivot (bottom aligned to center)
            // Center of tile is (0,0) here. 
            // We want the pawn's base to be at (0,0).
            ctx.drawImage(this.pawnImg, -size / 2, -size + size / 4, size, size); // +size/4 to shift down slightly so base is at handling point

            // Tint
            ctx.globalCompositeOperation = 'source-atop';
            ctx.fillStyle = this.color;
            ctx.globalAlpha = 0.3;
            // ctx.fillRect(-size/2, -size, size, size); 
            ctx.globalAlpha = 1.0;
            ctx.globalCompositeOperation = 'source-over';
        } else {
            // Fallback circle
            ctx.beginPath();
            ctx.fillStyle = this.color;
            ctx.arc(0, 0, 15, 0, Math.PI * 2);
            ctx.fill();
        }

        ctx.restore();
    }
}
