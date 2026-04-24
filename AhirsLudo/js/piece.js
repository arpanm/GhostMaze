/**
 * Piece class - Represents a single Ludo marble.
 */

export class Piece {
    constructor(player, index, color) {
        this.player = player; // 'green', 'blue', 'yellow', 'red'
        this.index = index;   // 0-3 within team
        this.color = color;
        
        this.inYard = true;
        this.pathIndex = -1; // -1 if in yard, 0-56 if on path
        this.isFinished = false;
        
        this.isDizzy = false;
        this.spinAngle = 0;
    }

    move(steps) {
        if (this.inYard) {
            if (steps === 6) {
                this.inYard = false;
                this.pathIndex = 0;
                return true;
            }
            return false;
        }
        if (this.pathIndex + steps > 56) return false;
        
        this.pathIndex += steps;
        if (this.pathIndex === 56) {
            this.isFinished = true;
        }
        return true;
    }

    reset() {
        this.inYard = true;
        this.pathIndex = -1;
        this.isFinished = false;
    }
}
