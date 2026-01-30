export class Player {
    constructor(avatar, startCol, startRow) {
        this.avatar = avatar;
        this.col = startCol;
        this.row = startRow;
        this.x = 0; // Pixel coordinates, set later
        this.y = 0;
        this.size = 0.6; // Player size relative to cell size
        this.speed = 0.05; // Cells per frame (approx)
        this.health = 100;
        this.dead = false;

        // Physics
        this.radius = 0; // Computed
    }

    reset(c, r) {
        this.col = c;
        this.row = r;
        this.health = 100;
        this.dead = false;
    }

    update(input, maze, cellSize, offsetX, offsetY) {
        if (this.dead) return;

        // Ensure coords are set (lazy init for update loop)
        if (this.x === 0 && this.y === 0) {
            this.x = offsetX + (this.col + 0.5) * cellSize;
            this.y = offsetY + (this.row + 0.5) * cellSize;
        }

        // Convert pixel metrics
        let pixelSpeed = this.speed * cellSize;
        this.radius = (cellSize * this.size) / 2;

        // Proposed new position
        let dx = 0;
        let dy = 0;

        if (input.up) dy -= pixelSpeed;
        if (input.down) dy += pixelSpeed;
        if (input.left) dx -= pixelSpeed;
        if (input.right) dx += pixelSpeed;

        // Normalize diagonal
        if (dx !== 0 && dy !== 0) {
            dx *= 0.707;
            dy *= 0.707;
        }

        // Apply movement with collision
        this.move(dx, dy, maze, cellSize, offsetX, offsetY);
    }

    move(dx, dy, maze, cellSize, offsetX, offsetY) {
        // Current absolute position
        let nextX = this.x + dx;
        let nextY = this.y + dy;

        // Check collisions for X
        if (!this.checkCollision(nextX, this.y, maze, cellSize, offsetX, offsetY)) {
            this.x = nextX;
        }

        // Check collisions for Y
        if (!this.checkCollision(this.x, nextY, maze, cellSize, offsetX, offsetY)) {
            this.y = nextY;
        }

        // Update Logical Grid Coordinates (Center of player)
        this.col = Math.floor((this.x - offsetX) / cellSize);
        this.row = Math.floor((this.y - offsetY) / cellSize);
    }

    checkCollision(newX, newY, maze, cellSize, offsetX, offsetY) {
        // Simple circle-wall collision or bounding box
        // We check the 4 corners of the player's bounding box against walls

        // Player center relative to maze
        let relX = newX - offsetX;
        let relY = newY - offsetY;

        // Player Bounding Box (slightly smaller than visual radius for forgiveness)
        let r = this.radius * 0.8;

        let checkpoints = [
            { x: relX - r, y: relY - r }, // Top-Left
            { x: relX + r, y: relY - r }, // Top-Right
            { x: relX - r, y: relY + r }, // Bottom-Left
            { x: relX + r, y: relY + r }  // Bottom-Right
        ];

        for (let p of checkpoints) {
            let col = Math.floor(p.x / cellSize);
            let row = Math.floor(p.y / cellSize);

            // Check out of bounds
            if (col < 0 || col >= maze.cols || row < 0 || row >= maze.rows) return true;

            let walls = maze.getWalls(col, row);

            // Check specific wall collisions within this cell
            let cellLeft = col * cellSize;
            let cellRight = (col + 1) * cellSize;
            let cellTop = row * cellSize;
            let cellBottom = (row + 1) * cellSize;

            if (walls.left && p.x < cellLeft + 2) return true; // +2 buffer
            if (walls.right && p.x > cellRight - 2) return true;
            if (walls.top && p.y < cellTop + 2) return true;
            if (walls.bottom && p.y > cellBottom - 2) return true;
        }

        return false;
    }

    draw(ctx, cellSize, offsetX, offsetY) {
        // First frame initialization of position if needed
        if (this.x === 0 && this.y === 0) {
            this.x = offsetX + (this.col + 0.5) * cellSize;
            this.y = offsetY + (this.row + 0.5) * cellSize;
        }

        // ensure coords follow resize if game resizes (re-calc based on cr/cl if needed? No, continuous pos)

        ctx.font = `${cellSize * 0.7}px serif`;
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";
        ctx.fillText(this.avatar, this.x, this.y);
    }
}
