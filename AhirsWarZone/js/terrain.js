export class Terrain {
    constructor(width, height) {
        this.width = width;
        this.height = height;
        this.points = [];
        this.generate();
    }

    generate() {
        this.points = [];
        // Simple random terrain / noise
        let y = this.height * 0.7;
        const segmentLength = 20;

        for (let x = 0; x <= this.width; x += segmentLength) {
            this.points.push({ x, y });
            // Random walk
            y += (Math.random() - 0.5) * 40;
            // Clamp
            if (y > this.height - 20) y = this.height - 20;
            if (y < this.height * 0.4) y = this.height * 0.4;
        }
        // Ensure last point matches width
        this.points[this.points.length - 1].x = this.width;
    }

    getHeightAt(x) {
        // Linear interpolation
        for (let i = 0; i < this.points.length - 1; i++) {
            if (x >= this.points[i].x && x <= this.points[i + 1].x) {
                const img = (x - this.points[i].x) / (this.points[i + 1].x - this.points[i].x);
                return this.points[i].y + (this.points[i + 1].y - this.points[i].y) * img;
            }
        }
        return this.height; // Fallback
    }

    draw(ctx) {
        ctx.fillStyle = "#27ae60"; // Grass color
        ctx.beginPath();
        if (this.points.length === 0) return;

        ctx.moveTo(0, this.height);
        ctx.lineTo(this.points[0].x, this.points[0].y);

        for (let i = 1; i < this.points.length; i++) {
            ctx.lineTo(this.points[i].x, this.points[i].y);
        }

        ctx.lineTo(this.width, this.height);
        ctx.closePath();
        ctx.fill();

        // Ground detail (dirt)
        ctx.strokeStyle = "#2ecc71";
        ctx.lineWidth = 5;
        ctx.stroke();
    }
}
