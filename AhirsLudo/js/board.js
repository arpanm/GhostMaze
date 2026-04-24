/**
 * Board class - Defines the coordinates for the Ludo path and yards.
 */

export class Board {
    constructor() {
        this.gridSize = 15; // 15x15 grid
        this.paths = {
            green: this.generatePath('green'),
            blue: this.generatePath('blue'),
            yellow: this.generatePath('yellow'),
            red: this.generatePath('red')
        };
        this.safeSquares = [0, 8, 13, 21, 26, 34, 39, 47]; // 0-indexed relative indices
    }

    // Returns a full path for a player from start to home center
    generatePath(player) {
        // Base outer path (52 steps)
        const outer = [
            [6,1],[6,2],[6,3],[6,4],[6,5], // Top-Left vertical down
            [5,6],[4,6],[3,6],[2,6],[1,6],[0,6], // Left horizontal left
            [0,7],[0,8], // Left vertical down (middle)
            [1,8],[2,8],[3,8],[4,8],[5,8], // Left horizontal right
            [6,9],[6,10],[6,11],[6,12],[6,13],[6,14], // Bottom-Left vertical down
            [7,14],[8,14], // Bottom vertical right (middle)
            [8,13],[8,12],[8,11],[8,10],[8,9], // Bottom-Right vertical up
            [9,8],[10,8],[11,8],[12,8],[13,8],[14,8], // Right horizontal right
            [14,7],[14,6], // Right vertical up (middle)
            [13,6],[12,6],[11,6],[10,6],[9,6], // Right horizontal left
            [8,5],[8,4],[8,3],[8,2],[8,1],[8,0], // Top-Right vertical up
            [7,0],[6,0]  // Top vertical left (middle)
        ];

        // Shift path based on player start
        let startIdx = 0;
        if (player === 'red') startIdx = 13;
        if (player === 'yellow') startIdx = 26;
        if (player === 'blue') startIdx = 39;

        const shiftedOuter = [...outer.slice(startIdx), ...outer.slice(0, startIdx)];
        
        // Take 51 steps of outer path (stop before completing circle)
        const gamePath = shiftedOuter.slice(0, 51);

        // Add 6 home run steps
        const homeRuns = {
            green: [[7,1],[7,2],[7,3],[7,4],[7,5],[7,6]],
            blue: [[13,7],[12,7],[11,7],[10,7],[9,7],[8,7]],
            yellow: [[7,13],[7,12],[7,11],[7,10],[7,9],[7,8]],
            red: [[1,7],[2,7],[3,7],[4,7],[5,7],[6,7]]
        };

        return [...gamePath, ...homeRuns[player]];
    }

    getYardPositions(player) {
        const offsets = {
            green: [1, 1],
            blue: [10, 1],
            yellow: [10, 10],
            red: [1, 10]
        };
        const [baseX, baseY] = offsets[player];
        return [
            [baseX+1, baseY+1], [baseX+3, baseY+1],
            [baseX+1, baseY+3], [baseX+3, baseY+3]
        ];
    }
}
