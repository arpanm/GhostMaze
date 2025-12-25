export class Maze {
    constructor(cols, rows) {
        this.cols = cols;
        this.rows = rows;
        this.cellSize = 0; // Set by renderer
        this.grid = [];
        this.stack = [];
        
        this.init();
    }

    init() {
        // Initialize grid
        this.grid = [];
        for (let r = 0; r < this.rows; r++) {
            let row = [];
            for (let c = 0; c < this.cols; c++) {
                row.push(new Cell(c, r));
            }
            this.grid.push(row);
        }
        
        // Generate maze
        this.generate();
        
        // Pick random exit
        // Exit should be on the edge usually, or just a specific cell
        this.exitCell = this.grid[Math.floor(Math.random() * this.rows)][Math.floor(Math.random() * this.cols)];
        // Ensure exit is not start (0,0)
        while (this.exitCell.c === 0 && this.exitCell.r === 0) {
            this.exitCell = this.grid[Math.floor(Math.random() * this.rows)][Math.floor(Math.random() * this.cols)];
        }
    }

    generate() {
        let current = this.grid[0][0];
        current.visited = true;
        
        do {
            let next = this.checkNeighbors(current);
            if (next) {
                next.visited = true;
                this.stack.push(current);
                this.removeWalls(current, next);
                current = next;
            } else if (this.stack.length > 0) {
                current = this.stack.pop();
            }
        } while (this.stack.length > 0);
    }

    checkNeighbors(cell) {
        let neighbors = [];
        let top = (cell.r > 0) ? this.grid[cell.r - 1][cell.c] : undefined;
        let right = (cell.c < this.cols - 1) ? this.grid[cell.r][cell.c + 1] : undefined;
        let bottom = (cell.r < this.rows - 1) ? this.grid[cell.r + 1][cell.c] : undefined;
        let left = (cell.c > 0) ? this.grid[cell.r][cell.c - 1] : undefined;

        if (top && !top.visited) neighbors.push(top);
        if (right && !right.visited) neighbors.push(right);
        if (bottom && !bottom.visited) neighbors.push(bottom);
        if (left && !left.visited) neighbors.push(left);

        if (neighbors.length > 0) {
            let r = Math.floor(Math.random() * neighbors.length);
            return neighbors[r];
        } else {
            return undefined;
        }
    }

    removeWalls(a, b) {
        let x = a.c - b.c;
        if (x === 1) { a.walls.left = false; b.walls.right = false; }
        else if (x === -1) { a.walls.right = false; b.walls.left = false; }

        let y = a.r - b.r;
        if (y === 1) { a.walls.top = false; b.walls.bottom = false; }
        else if (y === -1) { a.walls.bottom = false; b.walls.top = false; }
    }

    draw(ctx, width, height) {
        this.cellSize = Math.min(width / this.cols, height / this.rows);
        
        // Centering offset if aspect ratio differs
        let offsetX = (width - this.cols * this.cellSize) / 2;
        let offsetY = (height - this.rows * this.cellSize) / 2;

        ctx.strokeStyle = "#ffffff";
        ctx.lineWidth = 2; // Wall thickness

        for (let r = 0; r < this.rows; r++) {
            for (let c = 0; c < this.cols; c++) {
                let cell = this.grid[r][c];
                let x = offsetX + c * this.cellSize;
                let y = offsetY + r * this.cellSize;

                ctx.beginPath();
                if (cell.walls.top) { ctx.moveTo(x, y); ctx.lineTo(x + this.cellSize, y); }
                if (cell.walls.right) { ctx.moveTo(x + this.cellSize, y); ctx.lineTo(x + this.cellSize, y + this.cellSize); }
                if (cell.walls.bottom) { ctx.moveTo(x + this.cellSize, y + this.cellSize); ctx.lineTo(x, y + this.cellSize); }
                if (cell.walls.left) { ctx.moveTo(x, y + this.cellSize); ctx.lineTo(x, y); }
                ctx.stroke();

                // Draw Exit
                if (cell === this.exitCell) {
                    ctx.fillStyle = "#00ff00"; // Green Exit
                    ctx.font = `${this.cellSize * 0.8}px Arial`;
                    ctx.textAlign = "center";
                    ctx.textBaseline = "middle";
                    ctx.fillText("🚪", x + this.cellSize/2, y + this.cellSize/2);
                }
            }
        }
        
        return { cellSize: this.cellSize, offsetX, offsetY };
    }
    
    getWalls(col, row) {
        if (col < 0 || col >= this.cols || row < 0 || row >= this.rows) return { top: true, right: true, bottom: true, left: true };
        return this.grid[row][col].walls;
    }
}

class Cell {
    constructor(c, r) {
        this.c = c;
        this.r = r;
        this.walls = { top: true, right: true, bottom: true, left: true };
        this.visited = false;
    }
}
