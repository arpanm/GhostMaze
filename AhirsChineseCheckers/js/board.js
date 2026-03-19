/**
 * Board class - Manages the hexagonal star grid and hole states.
 * Standard Chinese Checkers: 5-side hexagon core (61 holes) + 6 triangles (10 holes each) = 121 holes.
 */

export class Board {
    constructor() {
        this.holes = new Map(); // Key: "q,r", Value: { q, r, occupant: null, zone, color }
        this.generateBoard();
    }

    generateBoard() {
        for (let q = -8; q <= 8; q++) {
            for (let r = -8; r <= 8; r++) {
                const s = -q - r;
                if (this.isInStar(q, r, s)) {
                    const zone = this.getZone(q, r, s);
                    const color = this.getZoneColor(zone);
                    this.addHole(q, r, color, zone);
                }
            }
        }
    }

    isInStar(q, r, s) {
        const lim = 4;
        // Inner hexagon
        if (Math.abs(q) <= lim && Math.abs(r) <= lim && Math.abs(s) <= lim) return true;

        // Triangles (Must be strictly one coord out of bounds and other two limited)
        if (r < -lim && q > 0 && s > 0 && q <= lim && s <= lim) return true; // Top
        if (r > lim && q < 0 && s < 0 && q >= -lim && s >= -lim) return true; // Bottom
        if (q < -lim && r > 0 && s > 0 && r <= lim && s <= lim) return true; // Bottom-Left
        if (q > lim && r < 0 && s < 0 && r >= -lim && s >= -lim) return true; // Top-Right
        if (s < -lim && q > 0 && r > 0 && q <= lim && r <= lim) return true; // Top-Left
        if (s > lim && q < 0 && r < 0 && q >= -lim && r >= -lim) return true; // Bottom-Right
        
        return false;
    }

    getZone(q, r, s) {
        if (r > 4) return 'PLAYER_1'; // Bottom
        if (r < -4) return 'AI';       // Top
        if (q < -4) return 'ZONE_BL';
        if (q > 4) return 'ZONE_TR';
        if (s < -4) return 'ZONE_TL';
        if (s > 4) return 'ZONE_BR';
        return 'NEUTRAL';
    }

    getZoneColor(zone) {
        switch (zone) {
            case 'PLAYER_1': return 'rgba(0, 255, 136, 0.3)'; // Primary green
            case 'AI': return 'rgba(0, 204, 255, 0.3)';       // Primary blue
            case 'ZONE_BL': return 'rgba(255, 68, 68, 0.2)';   // Red
            case 'ZONE_TR': return 'rgba(255, 170, 0, 0.2)';   // Orange
            case 'ZONE_TL': return 'rgba(187, 102, 255, 0.2)'; // Purple
            case 'ZONE_BR': return 'rgba(255, 255, 0, 0.2)';   // Yellow
            default: return 'rgba(255, 255, 255, 0.05)';
        }
    }

    addHole(q, r, color, zone) {
        this.holes.set(`${q},${r}`, { q, r, occupant: null, zone, color });
    }

    getHole(q, r) {
        return this.holes.get(`${q},${r}`);
    }

    getAllHoles() {
        return Array.from(this.holes.values());
    }

    getOccupant(q, r) {
        const hole = this.getHole(q, r);
        return hole ? hole.occupant : null;
    }

    setOccupant(q, r, piece) {
        const hole = this.getHole(q, r);
        if (hole) {
            hole.occupant = piece;
            if (piece) { piece.q = q; piece.r = r; }
        }
    }

    getNeighbors(q, r) {
        const directions = [
            {q: +1, r:  0}, {q: +1, r: -1}, {q:  0, r: -1},
            {q: -1, r:  0}, {q: -1, r: +1}, {q:  0, r: +1}
        ];
        return directions.map(d => this.getHole(q + d.q, r + d.r)).filter(h => !!h);
    }
}
