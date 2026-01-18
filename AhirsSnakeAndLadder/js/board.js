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
    }

    resize(w, h) {
        this.w = w;
        this.h = h;

        // Maintain aspect ratio close to square but fit screen
        const size = Math.min(w, h) * 0.9;
        this.tileW = size / this.cols;
        this.tileH = size / this.rows;

        this.offsetX = (w - size) / 2;
        this.offsetY = (h - size) / 2;
    }

    generate() {
        this.snakes = [];
        this.ladders = [];

        const occupied = new Set(); // Track start/end points to avoid clashes
        const snakeHeads = new Set();
        const ladderBottoms = new Set();

        // Helper to check if tile is free
        const isFree = (tile) => !occupied.has(tile) && tile !== 1 && tile !== 100;

        // Generate Snakes
        let attempts = 0;
        while (this.snakes.length < 5 && attempts < 1000) {
            attempts++;
            let head = Math.floor(Math.random() * 90) + 11; // 11 to 99
            let tail = Math.floor(Math.random() * (head - 10)) + 1; // At least 10 tiles drop

            if (isFree(head) && isFree(tail)) {
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
            let start = Math.floor(Math.random() * 80) + 2; // 2 to 80
            let end = Math.floor(Math.random() * (99 - start)) + start + 1; // Must go up

            // Critical Rule: Ladder Bottom cannot be Snake Head (Infinite loop prevention is good but mainly for clarity)
            // Also Ladder Top shouldn't be a Snake Head immediately (Or maybe it can? Classic games allow it, but let's avoid for "Fairness")

            if (isFree(start) && isFree(end) && !snakeHeads.has(end)) {
                this.ladders.push({ from: start, to: end });
                occupied.add(start);
                occupied.add(end);
                ladderBottoms.add(start);
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
                const isdark = (r + c) % 2 === 0;
                const fill = isdark ? '#1a1a1a' : '#2a2a2a';

                ctx.fillStyle = fill;
                ctx.fillRect(c * this.tileW, r * this.tileH, this.tileW, this.tileH);

                // Glowy Border
                ctx.strokeStyle = '#333';
                ctx.lineWidth = 1;
                ctx.strokeRect(c * this.tileW, r * this.tileH, this.tileW, this.tileH);
            }
        }
        ctx.restore();

        // Draw Numbers (Global Space logic reused but cleaner)
        ctx.font = 'bold 14px Orbitron';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';

        for (let i = 1; i <= 100; i++) {
            const pos = this.getTileCenter(i);

            // Color logic for special tiles
            let color = 'rgba(255,255,255,0.3)';
            if (i === 1) color = '#00ff00';
            if (i === 100) color = '#ff00ff';

            ctx.fillStyle = color;
            ctx.fillText(i, pos.x - this.tileW / 2 + 10, pos.y - this.tileH / 2 + 10);
        }

        // Draw Ladders (Neon Rails)
        this.ladders.forEach(l => {
            const start = this.getTileCenter(l.from);
            const end = this.getTileCenter(l.to);

            const dx = end.x - start.x;
            const dy = end.y - start.y;
            const angle = Math.atan2(dy, dx);
            const dist = Math.hypot(dx, dy);

            ctx.save();
            ctx.translate(start.x, start.y);
            ctx.rotate(angle);

            const width = 20;

            // Rails
            ctx.strokeStyle = '#00ffff';
            ctx.lineWidth = 3;
            ctx.shadowColor = '#00ffff';
            ctx.shadowBlur = 10;

            ctx.beginPath();
            ctx.moveTo(0, -width / 2);
            ctx.lineTo(dist, -width / 2);
            ctx.stroke();

            ctx.beginPath();
            ctx.moveTo(0, width / 2);
            ctx.lineTo(dist, width / 2);
            ctx.stroke();

            // Rungs
            ctx.shadowBlur = 0;
            ctx.lineWidth = 2;
            ctx.strokeStyle = 'rgba(0,255,255,0.5)';
            const steps = Math.floor(dist / 20);
            for (let i = 1; i < steps; i++) {
                const x = i * 20;
                ctx.beginPath();
                ctx.moveTo(x, -width / 2);
                ctx.lineTo(x, width / 2);
                ctx.stroke();
            }

            ctx.restore();
        });

        // Draw Snakes handled by Game -> Snake Entity usually? 
        // But if Board owns them, we draw here.
        // We will delegate to a helper or just draw fancy here.
        const time = performance.now() * 0.005;

        this.snakes.forEach(s => {
            const start = this.getTileCenter(s.from); // Head
            const end = this.getTileCenter(s.to);     // Tail

            // Calculate Control Points for Quadratic/Bezier wiggles
            const midX = (start.x + end.x) / 2;
            const midY = (start.y + end.y) / 2;

            // Wiggle offset perpendicular to direction
            const angle = Math.atan2(end.y - start.y, end.x - start.x);
            const perp = angle + Math.PI / 2;

            const wiggleAmt = Math.sin(time + start.x) * 20;

            const cp1x = midX + Math.cos(perp) * wiggleAmt;
            const cp1y = midY + Math.sin(perp) * wiggleAmt;

            // Snake Body (Gradient)
            const grad = ctx.createLinearGradient(start.x, start.y, end.x, end.y);
            grad.addColorStop(0, '#ff0000');
            grad.addColorStop(1, '#800000');

            ctx.beginPath();
            ctx.moveTo(start.x, start.y);
            ctx.quadraticCurveTo(cp1x, cp1y, end.x, end.y);

            ctx.strokeStyle = grad;
            ctx.lineWidth = 8 + Math.sin(time * 2) * 2; // Breathing thickness
            ctx.lineCap = 'round';
            ctx.shadowColor = 'red';
            ctx.shadowBlur = 15;
            ctx.stroke();
            ctx.shadowBlur = 0;

            // Head Eyes
            ctx.fillStyle = 'white';
            ctx.beginPath();
            ctx.arc(start.x - 3, start.y - 3, 2, 0, Math.PI * 2);
            ctx.arc(start.x + 3, start.y - 3, 2, 0, Math.PI * 2);
            ctx.fill();
        });
    }
}
