export class Board {
    constructor(ctx) {
        this.ctx = ctx;
        this.tiles = [];
        this.snakes = [];
        this.ladders = [];
        this.w = 0;
        this.h = 0;
        this.tileW = 0;
        this.tileH = 0;

        // Config
        this.cols = 10;
        this.rows = 10;

        // Offset for centering
        this.offsetX = 0;
        this.offsetY = 0;

        // Assets
        this.snakeImg = new Image();
        this.snakeImg.src = new URL('../assets/snake.png', import.meta.url).href;
        this.ladderImg = new Image();
        this.ladderImg.src = new URL('../assets/ladder.png', import.meta.url).href;
    }

    resize(w, h) {
        this.w = w;
        this.h = h;

        // Maintain aspect ratio close to square but fit screen
        const size = Math.min(w, h) * 0.95; // Use more screen space
        this.tileW = size / this.cols;
        this.tileH = size / this.rows;

        this.offsetX = (w - size) / 2;
        this.offsetY = (h - size) / 2;
    }

    getTileCenter(i) {
        // 1-based index i
        if (i < 1) i = 1;
        if (i > 100) i = 100;

        const row = Math.floor((i - 1) / 10); // 0 to 9 (0 is bottom logically)
        const col = (i - 1) % 10; // 0 to 9

        // Visual Layout: Row 0 is at the bottom (index 9 in canvas grid usually, but we draw top-down)
        // Let's say visual grid r goes 0 (top) to 9 (bottom).
        // So visual_r = 9 - row;

        const visual_r = 9 - row;

        // Zigzag:
        // Even logical rows (0, 2, 4...) -> Left to Right (0 -> 9)
        // Odd logical rows (1, 3, 5...) -> Right to Left (9 -> 0)
        let visual_c = col;
        if (row % 2 === 1) {
            visual_c = 9 - col;
        }

        const x = visual_c * this.tileW + this.tileW / 2;
        const y = visual_r * this.tileH + this.tileH / 2;

        return { x, y };
    }

    getEventAt(tile) {
        const snake = this.snakes.find(s => s.from === tile);
        if (snake) return { type: 'SNAKE', to: snake.to };

        const ladder = this.ladders.find(l => l.from === tile);
        if (ladder) return { type: 'LADDER', to: ladder.to };

        return null;
    }

    generate() {
        this.snakes = [];
        this.ladders = [];

        const occupied = new Set(); // Track start/end points to avoid clashes
        const snakeHeads = new Set();

        // Helper to check if tile is free
        const isFree = (tile) => !occupied.has(tile) && tile !== 1 && tile !== 100;
        const getRow = (tile) => Math.floor((tile - 1) / 10);

        // Generate Snakes
        let attempts = 0;
        while (this.snakes.length < 5 && attempts < 1000) {
            attempts++;
            let head = Math.floor(Math.random() * 90) + 11; // 11 to 99
            let tail = Math.floor(Math.random() * (head - 10)) + 1;

            if (isFree(head) && isFree(tail) && getRow(head) > getRow(tail)) {
                this.snakes.push({ from: head, to: tail });
                occupied.add(head);
                occupied.add(tail);
                snakeHeads.add(head);
            }
        }

        // Generate Ladders
        attempts = 0;
        while (this.ladders.length < 5 && attempts < 1000) {
            attempts++;
            let start = Math.floor(Math.random() * 80) + 2;
            let end = Math.floor(Math.random() * (99 - start)) + start + 1;

            if (end > start && isFree(start) && isFree(end) && !snakeHeads.has(end) && getRow(end) > getRow(start)) {
                this.ladders.push({ from: start, to: end });
                occupied.add(start);
                occupied.add(end);
            }
        }
    }

    draw(ctx) {
        ctx.save();
        ctx.translate(this.offsetX, this.offsetY);

        // Draw Grid
        for (let r = 0; r < 10; r++) {
            for (let c = 0; c < 10; c++) {
                // Neon Tile Style
                const isOddRow = (9 - r) % 2 === 1; // logical row
                const isDark = (r + c) % 2 === 0;

                // Checkerboard
                ctx.fillStyle = isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(255, 255, 255, 0.05)';
                ctx.fillRect(c * this.tileW, r * this.tileH, this.tileW, this.tileH);

                // Grid Lines
                ctx.strokeStyle = 'rgba(255, 255, 255, 0.1)';
                ctx.lineWidth = 1;
                ctx.strokeRect(c * this.tileW, r * this.tileH, this.tileW, this.tileH);
            }
        }

        // Numbers
        ctx.font = 'bold 16px Orbitron';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';

        for (let i = 1; i <= 100; i++) {
            const pos = this.getTileCenter(i);

            // Adjust back to local coords (getTileCenter returns global if offset added? 
            // WAIT - getTileCenter logic used visual_c * width. That is logic coord rel to offset IF we translate.
            // My getTileCenter logic returns (x,y) relative to Board (0,0).
            // But getTileCenter is called by Game which likely expects global coords for players?
            // Actually Players call board.getTileCenter.
            // The Board.draw calls ctx.translate(offsetX, offsetY).
            // So inside here, (0,0) is board top-left.
            // getTileCenter returns coordinates relative to board top-left.
            // So we can use them directly here.

            let color = 'rgba(255,255,255,0.4)';
            if (i === 1) color = '#00ff00';
            if (i === 100) color = '#ff00ff';

            ctx.fillStyle = color;
            // Draw number in corner
            ctx.fillText(i, pos.x - this.tileW / 2 + 15, pos.y - this.tileH / 2 + 15);
        }

        const time = performance.now();

        // Draw Ladders
        this.ladders.forEach(l => {
            const start = this.getTileCenter(l.from); // Bottom
            const end = this.getTileCenter(l.to);     // Top

            // Draw Image
            this.drawImageRotated(ctx, this.ladderImg, start, end, 0.6); // Scale width down a bit
        });

        // Draw Snakes
        this.snakes.forEach(s => {
            const start = this.getTileCenter(s.from); // Head
            const end = this.getTileCenter(s.to);     // Tail

            this.drawProceduralSnake(ctx, start, end, time);
        });

        ctx.restore();
    }

    drawProceduralSnake(ctx, p1, p2, time) {
        // Calculate points
        const points = [];
        const segments = 30;
        const dx = p2.x - p1.x;
        const dy = p2.y - p1.y;

        // Control points for a natural curve
        const angle = Math.atan2(dy, dx);
        const perp = angle + Math.PI / 2;

        // Generate backbone points
        for (let i = 0; i <= segments; i++) {
            const t = i / segments;
            const tx = p1.x + dx * t;
            const ty = p1.y + dy * t;

            // Wiggle
            const wave = Math.sin(t * 10 - time * 0.005) * (15 * Math.sin(t * Math.PI)); // Envelope taper at ends and reverse wave direction for forward movement feeling

            const wx = tx + Math.cos(perp) * wave;
            const wy = ty + Math.sin(perp) * wave;

            points.push({ x: wx, y: wy });
        }

        // Draw Body - Thick Line with Pattern
        ctx.lineCap = 'round';
        ctx.lineJoin = 'round';

        // Outer Outline
        ctx.strokeStyle = '#004400';
        ctx.lineWidth = 14;
        ctx.beginPath();
        points.forEach((p, i) => {
            if (i === 0) ctx.moveTo(p.x, p.y);
            else ctx.lineTo(p.x, p.y);
        });
        ctx.stroke();

        // Inner Green Body
        ctx.strokeStyle = '#00BB00';
        ctx.lineWidth = 10;
        ctx.stroke();

        // Draw Scales/Stripes (Yellow)
        ctx.strokeStyle = '#AAFF00';
        ctx.lineWidth = 2;
        points.forEach((p, i) => {
            if (i % 2 === 0 && i > 0 && i < segments) {
                // Approximate normal
                const prev = points[i - 1];
                const next = points[i + 1];
                const a = Math.atan2(next.y - prev.y, next.x - prev.x) + Math.PI / 2;

                const lx = p.x + Math.cos(a) * 4;
                const ly = p.y + Math.sin(a) * 4;
                const rx = p.x - Math.cos(a) * 4;
                const ry = p.y - Math.sin(a) * 4;

                ctx.beginPath();
                ctx.moveTo(lx, ly);
                ctx.lineTo(rx, ry);
                ctx.stroke();
            }
        });

        // Draw Head (at p1)
        const headPos = points[0];
        const nextPos = points[1];
        const headAngle = Math.atan2(nextPos.y - headPos.y, nextPos.x - headPos.x); // To tail

        const headFacing = headAngle + Math.PI;

        ctx.save();
        ctx.translate(headPos.x, headPos.y);
        ctx.rotate(headFacing);

        // Head Shape
        ctx.fillStyle = '#009900';
        ctx.beginPath();
        ctx.ellipse(0, 0, 12, 10, 0, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = '#004400';
        ctx.lineWidth = 1;
        ctx.stroke();

        // Eyes
        ctx.fillStyle = 'white';
        ctx.beginPath();
        ctx.arc(5, -4, 3, 0, Math.PI * 2);
        ctx.arc(5, 4, 3, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = 'black';
        ctx.beginPath();
        ctx.arc(6, -4, 1, 0, Math.PI * 2);
        ctx.arc(6, 4, 1, 0, Math.PI * 2);
        ctx.fill();

        // Tongue
        const tCycle = (Math.sin(time * 0.01) + 1) / 2;
        if (tCycle > 0.8) {
            ctx.strokeStyle = 'red';
            ctx.lineWidth = 1;
            ctx.beginPath();
            ctx.moveTo(10, 0);
            ctx.lineTo(15, 0);
            ctx.lineTo(18, -2);
            ctx.moveTo(15, 0);
            ctx.lineTo(18, 2);
            ctx.stroke();
        }

        ctx.restore();
    }

    // Kept helper if needed for ladders
    drawImageRotated(ctx, img, p1, p2, widthScale, wiggleAngle = 0) {
        if (!img.complete) return;

        const dx = p2.x - p1.x;
        const dy = p2.y - p1.y;
        const length = Math.hypot(dx, dy);
        const angle = Math.atan2(dy, dx);

        const mx = (p1.x + p2.x) / 2;
        const my = (p1.y + p2.y) / 2;

        ctx.save();
        ctx.translate(mx, my);
        ctx.rotate(angle + Math.PI / 2 + wiggleAngle);

        const w = this.tileW * widthScale;
        const h = length + this.tileH * 0.5;

        ctx.drawImage(img, -w / 2, -h / 2, w, h);
        ctx.restore();
    }
}
