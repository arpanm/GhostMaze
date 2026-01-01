export class Utils {
    static random(min, max) {
        return Math.random() * (max - min) + min;
    }

    static randomInt(min, max) {
        return Math.floor(Math.random() * (max - min + 1)) + min;
    }

    static getDistance(x1, y1, x2, y2) {
        const dx = x2 - x1;
        const dy = y2 - y1;
        return Math.sqrt(dx * dx + dy * dy);
    }

    static circleIntersect(c1, c2) {
        // c1, c2 = {x, y, radius}
        const dist = this.getDistance(c1.x, c1.y, c2.x, c2.y);
        return dist < (c1.radius + c2.radius);
    }

    // Ray-casting algorithm for Point in Polygon
    static pointInPolygon(point, polygon) {
        // point: {x, y}, polygon: [{x, y}, {x, y}, ...]
        let inside = false;
        for (let i = 0, j = polygon.length - 1; i < polygon.length; j = i++) {
            const xi = polygon[i].x, yi = polygon[i].y;
            const xj = polygon[j].x, yj = polygon[j].y;

            const intersect = ((yi > point.y) !== (yj > point.y))
                && (point.x < (xj - xi) * (point.y - yi) / (yj - yi) + xi);
            if (intersect) inside = !inside;
        }
        return inside;
    }

    static lerp(start, end, t) {
        return start * (1 - t) + end * t;
    }

    // Normalize vector
    static normalize(x, y) {
        const len = Math.sqrt(x * x + y * y);
        if (len === 0) return { x: 0, y: 0 };
        return { x: x / len, y: y / len };
    }
}
