export class ChessGame {
    constructor() {
        this.board = [];
        this.turn = 'w'; // 'w' or 'b'
        this.castlingRights = { w: { k: true, q: true }, b: { k: true, q: true } };
        this.enPassantTarget = null; // Square like 'e3' or null
        this.halfMoveClock = 0; // For 50 move rule
        this.fullMoveNumber = 1;
        this.history = []; // History of moves
        this.isGameOver = false;
        this.winner = null;

        this.reset();
    }

    reset() {
        this.board = this.createInitialBoard();
        this.turn = 'w';
        this.castlingRights = { w: { k: true, q: true }, b: { k: true, q: true } };
        this.enPassantTarget = null;
        this.halfMoveClock = 0;
        this.fullMoveNumber = 1;
        this.history = [];
        this.isGameOver = false;
        this.winner = null;
    }

    createInitialBoard() {
        const board = Array(8).fill(null).map(() => Array(8).fill(null));
        const pieces = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'];

        for (let i = 0; i < 8; i++) {
            board[0][i] = { type: pieces[i], color: 'b' };
            board[1][i] = { type: 'p', color: 'b' };
            board[6][i] = { type: 'p', color: 'w' };
            board[7][i] = { type: pieces[i], color: 'w' };
        }
        return board;
    }

    // Convert 'e2' to {r: 6, c: 4}
    squareToCoords(square) {
        const col = square.charCodeAt(0) - 'a'.charCodeAt(0);
        const row = 8 - parseInt(square[1]);
        return { r: row, c: col };
    }

    coordsToSquare(r, c) {
        const col = String.fromCharCode('a'.charCodeAt(0) + c);
        const row = 8 - r;
        return `${col}${row}`;
    }

    getPiece(r, c) {
        if (r < 0 || r > 7 || c < 0 || c > 7) return null;
        return this.board[r][c];
    }

    // Generate pseudo-legal moves for a piece at (r,c)
    getMoves(r, c, checkCheck = true) {
        const piece = this.board[r][c];
        if (!piece) return [];
        const moves = [];
        const self = this;

        function addMove(tr, tc) {
            if (tr >= 0 && tr < 8 && tc >= 0 && tc < 8) {
                const target = self.board[tr][tc];
                if (!target || target.color !== piece.color) {
                    moves.push({ r: tr, c: tc });
                    return !target; // Continue sliding if empty
                }
            }
            return false; // Stop sliding
        }

        // 1. Pawn Moves
        if (piece.type === 'p') {
            const dir = piece.color === 'w' ? -1 : 1;
            const startRow = piece.color === 'w' ? 6 : 1;

            // Forward 1
            if (!this.board[r + dir][c]) {
                moves.push({ r: r + dir, c: c });
                // Forward 2
                if (r === startRow && !this.board[r + dir * 2][c]) {
                    moves.push({ r: r + dir * 2, c: c });
                }
            }
            // Captures
            [[r + dir, c - 1], [r + dir, c + 1]].forEach(([tr, tc]) => {
                if (tr >= 0 && tr < 8 && tc >= 0 && tc < 8) {
                    const target = this.board[tr][tc];
                    if (target && target.color !== piece.color) {
                        moves.push({ r: tr, c: tc });
                    }
                    // En Passant
                    if (this.enPassantTarget && this.enPassantTarget.r === tr && this.enPassantTarget.c === tc) {
                        moves.push({ r: tr, c: tc, special: 'enpassant' });
                    }
                }
            });
        }

        // 2. Knight Moves
        if (piece.type === 'n') {
            const offsets = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]];
            offsets.forEach(([dr, dc]) => addMove(r + dr, c + dc)); // Knights don't slide, but addMove handles boundaries/captures correctly assuming single step
            // Actually addMove returns bool for sliding, but here we just ignore return
        }

        // 3. Sliding Pieces (Bishop, Rook, Queen)
        const directions = [];
        if (piece.type === 'b' || piece.type === 'q') directions.push([-1, -1], [-1, 1], [1, -1], [1, 1]);
        if (piece.type === 'r' || piece.type === 'q') directions.push([-1, 0], [1, 0], [0, -1], [0, 1]);

        directions.forEach(([dr, dc]) => {
            let tr = r + dr, tc = c + dc;
            while (tr >= 0 && tr < 8 && tc >= 0 && tc < 8) {
                const target = this.board[tr][tc];
                if (!target) {
                    moves.push({ r: tr, c: tc });
                } else {
                    if (target.color !== piece.color) moves.push({ r: tr, c: tc });
                    break;
                }
                tr += dr; tc += dc;
            }
        });

        // 4. King Moves
        if (piece.type === 'k') {
            [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]].forEach(([dr, dc]) => {
                const tr = r + dr, tc = c + dc;
                if (tr >= 0 && tr < 8 && tc >= 0 && tc < 8) {
                    const target = this.board[tr][tc];
                    if (!target || target.color !== piece.color) moves.push({ r: tr, c: tc });
                }
            });

            // Castling
            if (checkCheck && !this.isCheck(piece.color)) {
                // Kingside
                if (this.castlingRights[piece.color].k) {
                    if (!this.board[r][c + 1] && !this.board[r][c + 2]) {
                        if (!this.isSquareAttacked(r, c + 1, piece.color) && !this.isSquareAttacked(r, c + 2, piece.color))
                            moves.push({ r: r, c: c + 2, special: 'castle-k' });
                    }
                }
                // Queenside
                if (this.castlingRights[piece.color].q) {
                    if (!this.board[r][c - 1] && !this.board[r][c - 2] && !this.board[r][c - 3]) {
                        if (!this.isSquareAttacked(r, c - 1, piece.color) && !this.isSquareAttacked(r, c - 2, piece.color))
                            moves.push({ r: r, c: c - 2, special: 'castle-q' });
                    }
                }
            }
        }

        // Filter moves that leave king in check
        if (checkCheck) {
            return moves.filter(m => {
                // Simulate move
                const savedState = this.saveState();
                this.executeMoveInternal(r, c, m);
                const inCheck = this.isCheck(piece.color);
                this.restoreState(savedState);
                return !inCheck;
            });
        }

        return moves;
    }

    saveState() {
        return {
            board: this.cloneBoard(),
            castlingRights: JSON.parse(JSON.stringify(this.castlingRights)),
            enPassantTarget: this.enPassantTarget ? { ...this.enPassantTarget } : null,
            whiteToMove: this.turn === 'w'
        };
    }

    restoreState(state) {
        this.board = state.board;
        this.castlingRights = state.castlingRights;
        this.enPassantTarget = state.enPassantTarget;
        // Turn is typically swapped back manually or not changed if just simple validation
    }

    cloneBoard() {
        return this.board.map(row => row.map(p => p ? { ...p } : null));
    }


    isSquareAttacked(r, c, color) {
        // Check if any enemy piece can move to (r,c)
        // Optimization: check from (r,c) perspective for pawn/knight/sliding attacks
        const enemyColor = color === 'w' ? 'b' : 'w';

        // 1. Pawn attacks
        const pawnDir = color === 'w' ? -1 : 1; // Enemy pawns come from opposite
        // Actually, "is attacked BY enemy". So if I am White, enemy is Black (pawnDir = 1 from their perspective, implies r-1 is where they are? No. Black pawns are at r-1 attacking r)
        // Let's just iterate all enemy pieces for simplicity first, optimize later if needed.
        for (let i = 0; i < 8; i++) {
            for (let j = 0; j < 8; j++) {
                const p = this.board[i][j];
                if (p && p.color === enemyColor) {
                    const moves = this.getMoves(i, j, false); // No recursion
                    if (moves.some(m => m.r === r && m.c === c)) return true;
                }
            }
        }
        return false;
    }

    isCheck(color) {
        // Find King
        let kr, kc;
        for (let i = 0; i < 8; i++) {
            for (let j = 0; j < 8; j++) {
                if (this.board[i][j] && this.board[i][j].type === 'k' && this.board[i][j].color === color) {
                    kr = i; kc = j; break;
                }
            }
        }
        return this.isSquareAttacked(kr, kc, color);
    }

    makeMove(from, to) {
        // Validate
        const moves = this.getMoves(from.r, from.c);
        const move = moves.find(m => m.r === to.r && m.c === to.c);
        if (!move) return false;

        this.executeMoveInternal(from.r, from.c, move);

        // Update State
        if (this.turn === 'b') this.fullMoveNumber++;
        this.turn = this.turn === 'w' ? 'b' : 'w';

        // History
        this.history.push(move); // Track history for stats if needed


        // Checkmate detection
        if (this.getAllMoves(this.turn).length === 0) {
            if (this.isCheck(this.turn)) {
                this.isGameOver = true;
                this.winner = this.turn === 'w' ? 'black' : 'white';
            } else {
                this.isGameOver = true;
                this.winner = 'draw'; // Stalemate
            }
        }

        return true;
    }

    executeMoveInternal(fr, fc, move) {
        const piece = this.board[fr][fc];
        const target = this.board[move.r][move.c];

        // Capture?
        // En Passant
        if (move.special === 'enpassant') {
            const dir = piece.color === 'w' ? 1 : -1; // captured pawn is behind target square
            this.board[move.r + dir][move.c] = null;
        }

        // Move
        this.board[move.r][move.c] = piece;
        this.board[fr][fc] = null;

        // Castling
        if (move.special === 'castle-k') {
            const rook = this.board[fr][7];
            this.board[fr][5] = rook;
            this.board[fr][7] = null;
        }
        if (move.special === 'castle-q') {
            const rook = this.board[fr][0];
            this.board[fr][3] = rook;
            this.board[fr][0] = null;
        }

        // Update Rights (naive - fix later for specific rook moves)
        if (piece.type === 'k') this.castlingRights[piece.color] = { k: false, q: false };
        if (piece.type === 'r') {
            if (fc === 0) this.castlingRights[piece.color].q = false;
            if (fc === 7) this.castlingRights[piece.color].k = false;
        }

        // Promotion (Auto to Queen for now)
        if (piece.type === 'p' && (move.r === 0 || move.r === 7)) {
            piece.type = 'q';
        }

        // Update En Passant Target
        this.enPassantTarget = null;
        if (piece.type === 'p' && Math.abs(move.r - fr) === 2) {
            const midR = (move.r + fr) / 2;
            this.enPassantTarget = { r: midR, c: fc };
        }
    }

    getAllMoves(color) {
        let moves = [];
        for (let i = 0; i < 8; i++) {
            for (let j = 0; j < 8; j++) {
                const p = this.board[i][j];
                if (p && p.color === color) {
                    const pieceMoves = this.getMoves(i, j);
                    // Add 'from' to each move
                    pieceMoves.forEach(m => {
                        moves.push({ from: { r: i, c: j }, to: { r: m.r, c: m.c }, special: m.special });
                    });
                }
            }
        }
        return moves;
    }

}
