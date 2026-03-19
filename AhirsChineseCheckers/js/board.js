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
        // The 121-hole star is the union of two triangles of side 13
        // Triangle 1: q <= 4, r <= 4, s <= 4
        const inT1 = (q <= 4 && r <= 4 && s <= 4);
        // Triangle 2: q >= -4, r >= -4, s >= -4
        const inT2 = (q >= -4 && r >= -4 && s >= -4);
        return inT1 || inT2;
    }

    getZone(q, r, s) {
        // Return ZONE_1 to ZONE_6 for the 6 points of the star
        // Core is |q|<=4, |r|<=4, |s|<=4
        if (Math.abs(q) <= 4 && Math.abs(r) <= 4 && Math.abs(s) <= 4) return 'NEUTRAL';
        
        if (r < -4) return 'ZONE_1'; // Top
        if (q > 4)  return 'ZONE_2'; // Top-Right
        if (s > 4)  return 'ZONE_3'; // Bottom-Right
        if (r > 4)  return 'ZONE_4'; // Bottom
        if (q < -4) return 'ZONE_5'; // Bottom-Left
        if (s < -4) return 'ZONE_6'; // Top-Left
        
        return 'NEUTRAL';
    }

    getZoneColor(zone) {
        switch (zone) {
            case 'ZONE_4': return 'rgba(0, 255, 136, 0.3)'; // Bottom (P1)
            case 'ZONE_1': return 'rgba(0, 204, 255, 0.3)'; // Top
            case 'ZONE_2': return 'rgba(255, 170, 0, 0.2)';  // TR
            case 'ZONE_5': return 'rgba(255, 68, 68, 0.2)';  // BL
            case 'ZONE_6': return 'rgba(187, 102, 255, 0.2)';// TL
            case 'ZONE_3': return 'rgba(255, 255, 0, 0.2)';  // BR
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
