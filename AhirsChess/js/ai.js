export class ChessAI {
    constructor(game) {
        this.game = game;
        this.positionCount = 0;

        // Piece Values
        this.weights = { p: 100, n: 320, b: 330, r: 500, q: 900, k: 20000 };

        // Piece-Square Tables (simplified)
        // White perspective. For Black, we mirror rows.
        this.pst = {
            p: [
                [0, 0, 0, 0, 0, 0, 0, 0],
                [50, 50, 50, 50, 50, 50, 50, 50],
                [10, 10, 20, 30, 30, 20, 10, 10],
                [5, 5, 10, 25, 25, 10, 5, 5],
                [0, 0, 0, 20, 20, 0, 0, 0],
                [5, -5, -10, 0, 0, -10, -5, 5],
                [5, 10, 10, -20, -20, 10, 10, 5],
                [0, 0, 0, 0, 0, 0, 0, 0]
            ],
            n: [
                [-50, -40, -30, -30, -30, -30, -40, -50],
                [-40, -20, 0, 0, 0, 0, -20, -40],
                [-30, 0, 10, 15, 15, 10, 0, -30],
                [-30, 5, 15, 20, 20, 15, 5, -30],
                [-30, 0, 15, 20, 20, 15, 0, -30],
                [-30, 5, 10, 15, 15, 10, 5, -30],
                [-40, -20, 0, 5, 5, 0, -20, -40],
                [-50, -40, -30, -30, -30, -30, -40, -50]
            ],
            b: [
                [-20, -10, -10, -10, -10, -10, -10, -20],
                [-10, 0, 0, 0, 0, 0, 0, -10],
                [-10, 0, 5, 10, 10, 5, 0, -10],
                [-10, 5, 5, 10, 10, 5, 5, -10],
                [-10, 0, 10, 10, 10, 10, 0, -10],
                [-10, 10, 10, 10, 10, 10, 10, -10],
                [-10, 5, 0, 0, 0, 0, 5, -10],
                [-20, -10, -10, -10, -10, -10, -10, -20]
            ],
            r: [
                [0, 0, 0, 0, 0, 0, 0, 0],
                [5, 10, 10, 10, 10, 10, 10, 5],
                [-5, 0, 0, 0, 0, 0, 0, -5],
                [-5, 0, 0, 0, 0, 0, 0, -5],
                [-5, 0, 0, 0, 0, 0, 0, -5],
                [-5, 0, 0, 0, 0, 0, 0, -5],
                [-5, 0, 0, 0, 0, 0, 0, -5],
                [0, 0, 0, 5, 5, 0, 0, 0]
            ],
            q: [
                [-20, -10, -10, -5, -5, -10, -10, -20],
                [-10, 0, 0, 0, 0, 0, 0, -10],
                [-10, 0, 5, 5, 5, 5, 0, -10],
                [-5, 0, 5, 5, 5, 5, 0, -5],
                [0, 0, 5, 5, 5, 5, 0, -5],
                [-10, 5, 5, 5, 5, 5, 0, -10],
                [-10, 0, 5, 0, 0, 0, 0, -10],
                [-20, -10, -10, -5, -5, -10, -10, -20]
            ],
            k: [
                [-30, -40, -40, -50, -50, -40, -40, -30],
                [-30, -40, -40, -50, -50, -40, -40, -30],
                [-30, -40, -40, -50, -50, -40, -40, -30],
                [-30, -40, -40, -50, -50, -40, -40, -30],
                [-20, -30, -30, -40, -40, -30, -30, -20],
                [-10, -20, -20, -20, -20, -20, -20, -10],
                [20, 20, 0, 0, 0, 0, 20, 20],
                [20, 30, 10, 0, 0, 10, 30, 20]
            ]
        };
    }

    getBestMove(color, difficulty) {
        this.positionCount = 0;
        let depth = 1;
        if (difficulty === 'medium') depth = 3;
        // Proficient/Hard depth 4? Might be slow in JS without optimization. Try 3 for now, verified later.
        if (difficulty === 'hard') depth = 3; // Keep conservatively low for JS

        const moves = this.game.getAllMoves(color);
        if (moves.length === 0) return null;

        // Sort moves to improve pruning? (Captures first)
        // moves.sort(...) 

        let bestMove = null;
        let bestValue = -Infinity;
        let alpha = -Infinity;
        let beta = Infinity;

        // Root Search
        for (const move of moves) {
            const savedState = this.game.saveState();
            this.game.executeMoveInternal(move.from.r, move.from.c, move.to); // Using raw execute to avoid redundant checks

            // Minimax is recursive. If I am 'white' (maximizer), next is 'black' (minimizer).
            // But usually Minimax is implemented as NegaMax or changing evaluation perspective.
            // Let's stick to standard Minimax from maximizing player's POV.
            // If color is 'w', we want MAX score.
            // If color is 'b', we want MIN score? 
            // Better: Always maximize score from own perspective.

            const value = -this.minimax(depth - 1, -beta, -alpha, this.getOppositeColor(color));

            this.game.restoreState(savedState);

            if (value > bestValue) {
                bestValue = value;
                bestMove = move;
            }
            alpha = Math.max(alpha, value);
        }

        console.log(`AI explored ${this.positionCount} positions. Best Value: ${bestValue}`);
        return bestMove;
    }

    minimax(depth, alpha, beta, color) {
        this.positionCount++;

        if (depth === 0) {
            return this.evaluateBoard(color);
        }

        const moves = this.game.getAllMoves(color);
        if (moves.length === 0) {
            if (this.game.isCheck(color)) return -Infinity; // Checkmate (loss)
            return 0; // Stalemate
        }

        let max = -Infinity;
        for (const move of moves) {
            const savedState = this.game.saveState();
            this.game.executeMoveInternal(move.from.r, move.from.c, move.to);

            // Negamax: -minimax(...)
            const val = -this.minimax(depth - 1, -beta, -alpha, this.getOppositeColor(color));

            this.game.restoreState(savedState);

            if (val > max) max = val;
            alpha = Math.max(alpha, val);
            if (alpha >= beta) break; // Pruning
        }
        return max;
    }

    evaluateBoard(color) {
        let score = 0;
        // Evaluate from 'color' perspective
        // Positive score = Good for 'color'

        for (let r = 0; r < 8; r++) {
            for (let c = 0; c < 8; c++) {
                const p = this.game.board[r][c];
                if (!p) continue;

                let val = this.weights[p.type];

                // PST (Piece-Square Table)
                let rPst = r;
                let cPst = c;

                // If white, use PST as is. If black, mirror rows (0->7)
                // Note: My board[0] is Black side, board[7] is White side.
                // The PST is defined for White (starts at bottom, row 7 is backrank).
                // Wait, my PST definition:
                // p[0] is row 0? 
                // Usually PSTs are defined Rank 1 to 8. Rank 1 is index 7.
                // My PST array: index 0 (top) -> index 7 (bottom).
                // Initial board: Black at 0, White at 7.
                // So for White, Row 7 is "home". 
                // My PST: If index 7 has [0,0...], that matches pawn start? 
                // Let's assumes PST index 0 = Board Row 0.

                if (p.color === 'w') {
                    // White is at bottom (rows 6,7). Target is top (row 0).
                    // PST should reward advancing to lower indices.
                    // My PST 'p' row 1 has 50 (promotion). Row 1 is near top. Good.
                    // So for White, use (r, c).
                    rPst = r;
                } else {
                    // Black is at top (rows 0,1). Target is bottom (row 7).
                    // Mirror row index: 7 - r.
                    rPst = 7 - r;
                }

                // Add PST value
                // Note: PSTs types k,q,r,b,n,p need to exist
                if (this.pst[p.type]) {
                    val += this.pst[p.type][rPst][c];
                }

                if (p.color === color) score += val;
                else score -= val;
            }
        }
        return score;
    }

    getOppositeColor(c) {
        return c === 'w' ? 'b' : 'w';
    }
}

