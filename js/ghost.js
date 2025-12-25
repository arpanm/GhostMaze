export class Ghost {
    constructor(playerCol, playerRow, mazeCols, mazeRows) {
        // Spawn nearby but not on top
        // Random angle, distance 3-6 cells
        let angle = Math.random() * Math.PI * 2;
        let dist = 3 + Math.random() * 3;

        let c = playerCol + Math.cos(angle) * dist;
        let r = playerRow + Math.sin(angle) * dist;

        // Clamp to maze bounds
        this.col = Math.max(0, Math.min(mazeCols - 1, c));
        this.row = Math.max(0, Math.min(mazeRows - 1, r));

        this.x = 0; // pixel pos set in draw/update
        this.y = 0;

        this.state = 'APPEARING'; // APPEARING, CHASING, DEAD
        this.symbol = '👻';

        this.timer = 0;
        this.appearTime = 1000; // 1 second warning
        this.chaseTime = 3000;  // 3 seconds chase

        this.speed = 0.035; // Slightly slower than player (0.05) or faster? 3 sec is short. Let's make it 0.04.
    }

    update(dt, player, cellSize, offsetX, offsetY) {
        this.timer += dt;

        if (this.state === 'APPEARING') {
            if (this.timer >= this.appearTime) {
                this.state = 'CHASING';
                this.timer = 0;
            }
        } else if (this.state === 'CHASING') {
            if (this.timer >= this.chaseTime) {
                this.state = 'DEAD';
                return;
            }

            // Move towards player (Flying)
            // Calculate absolute positions
            // Ensure ghost coordinates are set
            if (this.x === 0) {
                this.x = offsetX + (this.col + 0.5) * cellSize;
                this.y = offsetY + (this.row + 0.5) * cellSize;
            }

            let px = player.x;
            let py = player.y;

            let dx = px - this.x;
            let dy = py - this.y;
            let dist = Math.sqrt(dx * dx + dy * dy);

            if (dist > 0) {
                let moveDist = this.speed * cellSize; // Speed is in cells per frame roughly, need time scaling? 
                // We'll assume dt is effectively handled by game loop fixed step or just scale by logic 
                // Actually if called per frame, need to normalize speed. 
                // Player speed was 0.05 per frame. 

                let moveX = (dx / dist) * moveDist;
                let moveY = (dy / dist) * moveDist;

                this.x += moveX;
                this.y += moveY;

                // Update grid coords
                this.col = Math.floor((this.x - offsetX) / cellSize);
                this.row = Math.floor((this.y - offsetY) / cellSize);
            }
        }
    }

    draw(ctx, cellSize, offsetX, offsetY) {
        if (this.state === 'DEAD') return;

        // Init pos if fresh
        if (this.x === 0) {
            this.x = offsetX + (this.col + 0.5) * cellSize;
            this.y = offsetY + (this.row + 0.5) * cellSize;
        }

        let alpha = 1;
        if (this.state === 'APPEARING') {
            // Blink
            alpha = Math.floor(Date.now() / 100) % 2 === 0 ? 0.5 : 1;
        }

        ctx.save();
        ctx.globalAlpha = alpha;
        ctx.font = `${cellSize * 0.7}px serif`;
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";
        ctx.fillText(this.symbol, this.x, this.y);
        ctx.restore();
    }

    checkCollision(player, cellSize) {
        if (this.state !== 'CHASING') return false;

        let dx = this.x - player.x;
        let dy = this.y - player.y;
        let dist = Math.sqrt(dx * dx + dy * dy);

        // Hitbox radius
        let r = (cellSize * 0.6) / 2;

        return dist < (r + r); // Touch
    }
}
