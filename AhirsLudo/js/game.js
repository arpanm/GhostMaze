import { Board } from './board.js';
import { Piece } from './piece.js';

export class Game {
    constructor(ui, economy) {
        this.ui = ui;
        this.economy = economy;
        this.board = new Board();
        
        this.playerCount = 2;
        this.playersOrder = ['green', 'blue', 'yellow', 'red'];
        this.activePlayers = [];
        this.turnIndex = 0;
        
        this.diceValue = 0;
        this.rollCount = 0;
        this.state = 'WAITING_ROLL'; // WAITING_ROLL, SELECTING_PIECE, ANIMATING
        
        this.pieces = [];
        this.isRunning = false;
        this.timer = 0;
        this.lastTime = 0;

        this.canvas = document.getElementById('game-canvas');
        this.ctx = this.canvas.getContext('2d');
        this.resize();
        window.addEventListener('resize', () => this.resize());
    }

    start(config) {
        this.playerCount = config.playerCount;
        this.userColor = config.color;
        this.aiDifficulty = config.difficulty;
        
        if (this.playerCount === 2) {
            this.activePlayers = ['green', 'yellow'];
        } else if (this.playerCount === 3) {
            this.activePlayers = ['green', 'yellow', 'red'];
        } else {
            this.activePlayers = ['green', 'blue', 'yellow', 'red'];
        }
        
        this.turnIndex = 0;
        
        this.pieces = [];
        this.activePlayers.forEach(p => {
            const color = this.getColorHex(p);
            for (let i = 0; i < 4; i++) {
                this.pieces.push(new Piece(p, i, color));
            }
        });

        this.isRunning = true;
        this.timer = 0;
        this.lastTime = performance.now();
        this.state = 'WAITING_ROLL';
        
        this.animate(performance.now());
        
        if (this.getCurrentPlayer() !== this.userColor) {
            this.aiRoll();
        }
    }

    getCurrentPlayer() {
        return this.activePlayers[this.turnIndex];
    }

    rollDice() {
        if (this.state !== 'WAITING_ROLL') return;
        
        this.state = 'ANIMATING';
        this.ui.setDiceValue(0, true);
        
        setTimeout(() => {
            this.diceValue = Math.floor(Math.random() * 6) + 1;
            this.ui.setDiceValue(this.diceValue, false);
            
            const moves = this.getLegalMoves(this.getCurrentPlayer(), this.diceValue);
            if (moves.length === 0) {
                setTimeout(() => this.nextTurn(), 1000);
            } else {
                this.state = 'SELECTING_PIECE';
                if (this.getCurrentPlayer() !== this.userColor) {
                    this.aiSelectPiece(moves);
                }
            }
        }, 800);
    }

    getLegalMoves(player, dice) {
        return this.pieces.filter(p => {
            if (p.player !== player || p.isFinished) return false;
            if (p.inYard) return dice === 6;
            return p.pathIndex + dice <= 56;
        });
    }

    handlePieceClick(piece) {
        if (this.state !== 'SELECTING_PIECE' || this.getCurrentPlayer() !== this.userColor) return;
        if (piece.player !== this.userColor) return;
        
        const legal = this.getLegalMoves(this.userColor, this.diceValue);
        if (legal.includes(piece)) {
            this.executeMove(piece, this.diceValue);
        }
    }

    executeMove(piece, dice) {
        this.state = 'ANIMATING';
        
        if (piece.move(dice)) {
            console.log(`Moved piece to index ${piece.pathIndex}`);
        } else {
            console.log("Move failed - invalid step count?");
        }

        // Check for capture
        const capture = this.checkCapture(piece);
        
        // Win check
        if (this.checkWin(piece.player)) {
            this.isRunning = false;
            this.saveScore(piece.player === this.userColor);
            this.ui.showGameOver(piece.player === this.userColor, 
                piece.player === this.userColor ? "You took all pieces home!" : `${piece.player} side wins!`);
            return;
        }

        // Extra turn logic
        const extraTurn = (dice === 6 || capture);
        setTimeout(() => {
            if (extraTurn) {
                this.state = 'WAITING_ROLL';
                if (this.getCurrentPlayer() !== this.userColor) this.aiRoll();
            } else {
                this.nextTurn();
            }
        }, 500);
    }

    checkCapture(piece) {
        if (piece.isFinished) return false;
        
        // Relative to current piece
        const globalPos = this.getGlobalPosition(piece);
        if (this.board.safeSquares.includes(piece.pathIndex)) return false;

        let captured = false;
        this.pieces.forEach(p => {
            if (p.player !== piece.player && !p.inYard && !p.isFinished) {
                const otherPos = this.getGlobalPosition(p);
                if (globalPos[0] === otherPos[0] && globalPos[1] === otherPos[1]) {
                    // Check if other piece is on a safe square for THEIR path
                    if (!this.board.safeSquares.includes(p.pathIndex)) {
                        p.reset();
                        p.isDizzy = true;
                        captured = true;
                        this.ui.showAITalk(`${piece.player} captured ${p.player}!`);
                    }
                }
            }
        });
        return captured;
    }

    nextTurn() {
        this.turnIndex = (this.turnIndex + 1) % this.activePlayers.length;
        this.state = 'WAITING_ROLL';
        this.ui.updateHUD({ turn: `${this.getCurrentPlayer().toUpperCase()}'s Turn` });
        
        if (this.getCurrentPlayer() !== this.userColor) {
            this.aiRoll();
        }
    }

    aiRoll() {
        setTimeout(() => this.rollDice(), 1000);
    }

    aiSelectPiece(moves) {
        setTimeout(() => {
            // Greedy: Prefer capture, then getting out of yard, then moving forward
            let selected = moves[0];
            
            const captureMove = moves.find(m => {
                // Peek capture (simplistic)
                return false; // TODO: Implement deeper lookahead
            });
            
            if (captureMove) selected = captureMove;
            else if (moves.find(m => m.inYard)) selected = moves.find(m => m.inYard);
            else selected = moves.sort((a, b) => b.pathIndex - a.pathIndex)[0];
            
            this.executeMove(selected, this.diceValue);
        }, 1000);
    }

    checkWin(player) {
        return this.pieces.filter(p => p.player === player && p.isFinished).length === 4;
    }

    getScore(player) {
        return this.pieces.filter(p => p.player === player && p.isFinished).length;
    }

    saveScore(victory) {
        if (!victory) return;
        const time = Math.floor(this.timer/1000);
        const scores = JSON.parse(localStorage.getItem('ahirs_ludo_scores') || '[]');
        scores.push({ player: document.getElementById('player-name').value, time, result: 'Champion 🏆', date: new Date().toISOString() });
        scores.sort((a,b) => a.time - b.time);
        localStorage.setItem('ahirs_ludo_scores', JSON.stringify(scores.slice(0, 10)));
    }

    // --- Rendering Helpers ---
    getGlobalPosition(piece) {
        if (piece.inYard) {
            return this.board.getYardPositions(piece.player)[piece.index];
        }
        return this.board.paths[piece.player][piece.pathIndex];
    }

    getColorHex(p) {
        const colors = { green: '#00ff88', blue: '#00ccff', yellow: '#ffaa00', red: '#ff4444' };
        return colors[p];
    }

    resize() {
        this.canvas.width = window.innerWidth;
        this.canvas.height = window.innerHeight;
    }

    animate(time) {
        if (!this.isRunning) return;
        const dt = time - (this.lastTime || time);
        this.lastTime = time;
        this.timer += dt;
        
        this.draw();
        
        this.ui.updateHUD({ 
            score: `${this.getScore(this.userColor)}/4`,
            timer: Math.floor(this.timer/1000)
        });
        
        requestAnimationFrame((t) => this.animate(t));
    }

    handleClick(x, y) {
        if (this.state !== 'SELECTING_PIECE' || this.getCurrentPlayer() !== this.userColor) return;
        
        const size = this.getCellSize();
        const offset = this.getBoardOffset();
        
        const clickedPieces = [];
        this.pieces.filter(p => p.player === this.userColor).forEach(p => {
            const pos = this.getGlobalPosition(p);
            const px = offset.x + pos[0] * size + size/2;
            const py = offset.y + pos[1] * size + size/2;
            
            const dist = Math.sqrt((x - px)**2 + (y - py)**2);
            if (dist < size * 0.6) { // Increased radius from 0.4 to 0.6
                clickedPieces.push(p);
            }
        });

        if (clickedPieces.length > 0) {
            const legal = this.getLegalMoves(this.userColor, this.diceValue);
            console.log("Clicked Pieces:", clickedPieces, "Legal:", legal);
            const selectable = clickedPieces.find(p => legal.includes(p));
            if (selectable) {
                console.log("Executing move for piece:", selectable);
                this.handlePieceClick(selectable);
            }
        }
    }

    getCellSize() {
        return Math.min(this.canvas.width, this.canvas.height) / 16;
    }

    getBoardOffset() {
        const size = this.getCellSize();
        return {
            x: (this.canvas.width - size * 15) / 2,
            y: (this.canvas.height - size * 15) / 2
        };
    }

    draw() {
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        const size = this.getCellSize();
        const offset = this.getBoardOffset();
        
        this.drawBoard(this.ctx, size, offset);
        this.drawPieces(this.ctx, size, offset);
    }
    
    // Split drawing for clarity
    drawBoard(ctx, size, offset) {
        const colors = { yard: '#161b22', empty: '#0d1117', border: '#30363d' };
        
        // Draw Grid
        for (let x = 0; x < 15; x++) {
            for (let y = 0; y < 15; y++) {
                const px = offset.x + x * size;
                const py = offset.y + y * size;
                
                // Determine block type
                let fillColor = colors.empty;
                let isYard = (x < 6 && y < 6) || (x > 8 && y < 6) || (x < 6 && y > 8) || (x > 8 && y > 8);
                if (isYard) fillColor = colors.yard;
                
                // Color home paths
                if (y === 7 && x > 0 && x < 6) fillColor = 'rgba(255, 68, 68, 0.2)'; // Red
                if (y === 7 && x > 8 && x < 14) fillColor = 'rgba(0, 204, 255, 0.2)'; // Blue
                if (x === 7 && y > 0 && y < 6) fillColor = 'rgba(0, 255, 136, 0.2)'; // Green
                if (x === 7 && y > 8 && y < 14) fillColor = 'rgba(255, 170, 0, 0.2)'; // Yellow
                
                // Home Square (Middle 3x3)
                if (x >= 6 && x <= 8 && y >= 6 && y <= 8) fillColor = '#1a1f26';
                
                ctx.fillStyle = fillColor;
                ctx.fillRect(px, py, size, size);
                ctx.strokeStyle = colors.border;
                ctx.strokeRect(px, py, size, size);
                
                // Safe Square Stars
                const relativePos = [x, y];
                // Check if this pos is in safeSquares for any player... 
                // Simplified safe check for visual
            }
        }
    }

    drawPieces(ctx, size, offset) {
        // Group pieces by position to draw stacks
        const groups = {};
        this.pieces.forEach(p => {
            if (p.isFinished) return;
            const pos = this.getGlobalPosition(p);
            const key = `${pos[0]},${pos[1]}`;
            if (!groups[key]) groups[key] = [];
            groups[key].push(p);
        });

        Object.values(groups).forEach(group => {
            group.forEach((p, i) => {
                const pos = this.getGlobalPosition(p);
                let px = offset.x + pos[0] * size + size/2;
                let py = offset.y + pos[1] * size + size/2;
                
                // Stack offset if multiple pieces on same square
                if (group.length > 1) {
                    px += (i - (group.length - 1) / 2) * (size * 0.15);
                    py -= (i - (group.length - 1) / 2) * (size * 0.1);
                }

                this.ctx.save();
                this.ctx.translate(px, py);
                
                if (p.isDizzy) {
                    this.ctx.rotate((Date.now() / 100) % (Math.PI * 2));
                }
                
                // Piece glow
                this.ctx.beginPath();
                this.ctx.arc(0, 0, size * 0.35, 0, Math.PI * 2);
                this.ctx.fillStyle = p.color;
                this.ctx.shadowBlur = 15;
                this.ctx.shadowColor = p.color;
                this.ctx.fill();
                
                // Selection highlight
                const legalMoves = this.getLegalMoves(this.userColor, this.diceValue);
                const isLegal = this.state === 'SELECTING_PIECE' && this.getCurrentPlayer() === this.userColor && legalMoves.includes(p);
                if (isLegal) {
                    this.ctx.strokeStyle = '#fff';
                    this.ctx.lineWidth = 3;
                    this.ctx.stroke();
                    this.ctx.beginPath();
                    this.ctx.arc(0, 0, size * 0.45 + Math.sin(Date.now()/200)*2, 0, Math.PI * 2);
                    this.ctx.stroke();
                }
                
                this.ctx.restore();
            });
        });
    }
}
