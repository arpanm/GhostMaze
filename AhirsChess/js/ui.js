export class UIManager {
    constructor(gameElement, game) {
        this.gameElement = gameElement; // #chess-board
        this.game = game;
        this.selectedSquare = null;
        this.draggedPiece = null;
        this.flipped = false; // If playing black, board should flip?
        this.pieceTheme = 'classic'; // 'classic' or 'funny'

        this.pieceSymbols = {
            classic: {
                w: { k: '♔', q: '♕', r: '♖', b: '♗', n: '♘', p: '♙' },
                b: { k: '♚', q: '♛', r: '♜', b: '♝', n: '♞', p: '♟' }
            },
            funny: {
                w: { k: '🤴', q: '👸', r: '🏰', b: '🧙‍♂️', n: '🦄', p: '👶' },
                b: { k: '🧛', q: '🧙‍♀️', r: '🏯', b: '🦹', n: '🦖', p: '🧟' }
            }
        };
    }

    drawBoard() {
        this.gameElement.innerHTML = '';
        const board = this.game.board;

        for (let r = 0; r < 8; r++) {
            for (let c = 0; c < 8; c++) {
                // visual row/col depends on flipped state
                const vr = this.flipped ? 7 - r : r;
                const vc = this.flipped ? 7 - c : c;

                const squareDiv = document.createElement('div');
                squareDiv.className = `square ${(vr + vc) % 2 === 0 ? 'light' : 'dark'}`;
                squareDiv.dataset.r = vr;
                squareDiv.dataset.c = vc;
                squareDiv.dataset.square = this.game.coordsToSquare(vr, vc);

                const piece = board[vr][vc];
                if (piece) {
                    const pieceDiv = document.createElement('div');
                    pieceDiv.className = `piece ${piece.color === 'w' ? 'white' : 'black'}`;
                    pieceDiv.textContent = this.pieceSymbols[this.pieceTheme][piece.color][piece.type];
                    // Draggable
                    pieceDiv.setAttribute('draggable', true);
                    squareDiv.appendChild(pieceDiv);
                }

                this.gameElement.appendChild(squareDiv);
            }
        }
    }

    highlightMoves(moves) {
        document.querySelectorAll('.square').forEach(el => el.classList.remove('hint', 'capture-hint'));
        moves.forEach(m => {
            // m is target {r, c}
            const selector = `.square[data-r="${m.r}"][data-c="${m.c}"]`;
            const el = document.querySelector(selector);
            if (el) {
                if (this.game.getPiece(m.r, m.c)) el.classList.add('capture-hint');
                else el.classList.add('hint');
            }
        });
    }

    highlightSelected(coords) {
        document.querySelectorAll('.square').forEach(el => el.classList.remove('selected'));
        if (coords) {
            const selector = `.square[data-r="${coords.r}"][data-c="${coords.c}"]`;
            const el = document.querySelector(selector);
            if (el) el.classList.add('selected');
        }
    }
}
