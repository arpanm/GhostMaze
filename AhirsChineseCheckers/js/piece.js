/**
 * Piece class - Represents a single marble on the board.
 */

export class Piece {
    constructor(q, r, owner, color) {
        this.q = q;
        this.r = r;
        this.owner = owner; // 'PLAYER_1', 'AI_1', 'AI_2'
        this.color = color;
        this.isDizzy = false;
    }
}
