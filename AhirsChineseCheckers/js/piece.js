/**
 * Piece class - Represents a single marble on the board.
 */

export class Piece {
    constructor(id, q, r, owner, color, name) {
        this.id = id;
        this.q = q;
        this.r = r;
        this.owner = owner; // 'PLAYER_1' or 'AI'
        this.color = color;
        this.name = name; // Funny name like "Speedy McHop"
        this.isDizzy = false;
        this.spinAngle = 0;
    }

    update(dt) {
        if (this.isDizzy) {
            this.spinAngle += 0.01 * dt;
        }
    }
}
