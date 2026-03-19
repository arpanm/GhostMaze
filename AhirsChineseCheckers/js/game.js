import { Board } from './board.js';
import { Piece } from './piece.js';

export class Game {
    constructor(ui, economy) {
        this.ui = ui;
        this.economy = economy;
        this.board = new Board();
        this.playerCount = 2;
        this.pieces = [];
        this.selectedPiece = null;
        this.validMoves = [];
        this.turn = 'PLAYER_1'; // PLAYER_1, AI_1, AI_2
        this.isRunning = false;
        this.timer = 0;
        this.lastTime = 0;
        this.aiDifficulty = 'medium';
        this.isAiThinking = false;

        this.canvas = document.getElementById('game-canvas');
        this.ctx = this.canvas.getContext('2d');
        this.resize();
        window.addEventListener('resize', () => this.resize());
    }

    start(config = { playerCount: 2, difficulty: 'medium' }) {
        console.log("Starting game session...");
        this.playerCount = config.playerCount || 2;
        this.aiDifficulty = config.difficulty || 'medium';
        this.board = new Board();
        this.pieces = [];
        this.setupBoard();
        this.turn = 'PLAYER_1';
        this.isRunning = true;
        this.timer = 0;
        this.lastTime = performance.now();
        this.selectedPiece = null;
        this.validMoves = [];
        this.isAiThinking = false;
        
        // Ensure no multiple loops
        if (this.animationId) cancelAnimationFrame(this.animationId);
        this.animate(performance.now());
    }

    setupBoard() {
        if (this.playerCount === 2) {
            // Standard 2-Player: Opposite zones
            this.addPiecesToZone('ZONE_4', 'PLAYER_1', '#00ff88'); // Bottom
            this.addPiecesToZone('ZONE_1', 'AI_1', '#00ccff');     // Top
        } else {
            // Symmetrical 3-Player: Every second triangle
            this.addPiecesToZone('ZONE_4', 'PLAYER_1', '#00ff88'); // Bottom
            this.addPiecesToZone('ZONE_2', 'AI_1', '#ffaa00');     // Top-Right
            this.addPiecesToZone('ZONE_6', 'AI_2', '#bb66ff');     // Top-Left
        }
        console.log(`Setup complete: ${this.pieces.length} pieces on board.`);
    }

    addPiecesToZone(zoneName, owner, color) {
        const holes = this.board.getAllHoles().filter(h => h.zone === zoneName);
        holes.forEach(h => {
            const piece = new Piece(h.q, h.r, owner, color);
            this.pieces.push(piece);
            this.board.setOccupant(h.q, h.r, piece);
        });
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

        this.update();
        this.draw();
        
        const score = this.getScore('PLAYER_1');
        this.ui.updateHUD({
            turn: (this.turn === 'PLAYER_1') ? 'Your Turn' : `${this.turn}'s Turn`,
            score: `${score}/10`,
            timer: Math.floor(this.timer / 1000)
        });

        this.animationId = requestAnimationFrame((t) => this.animate(t));
    }

    update() {
        if (this.turn.startsWith('AI') && this.isRunning && !this.isAiThinking) {
            this.aiTurn();
        }
    }

    aiTurn() {
        this.isAiThinking = true;
        const delay = this.aiDifficulty === 'easy' ? 1500 : 800;

        setTimeout(() => {
            if (!this.isRunning) return;
            const move = this.getBestMove(this.turn);
            if (move) {
                this.executeMove(move.piece, move.target);
            } else {
                this.endTurn();
            }
            this.isAiThinking = false;
        }, delay);
    }

    getBestMove(owner) {
        const myPieces = this.pieces.filter(p => p.owner === owner);
        let best = null;
        let maxScore = -Infinity;

        const targetZoneName = this.getTargetZoneName(owner);

        myPieces.forEach(p => {
            const moves = this.getValidMoves(p);
            moves.forEach(m => {
                const score = this.scoreMove(p, m, targetZoneName);
                if (score > maxScore) {
                    maxScore = score;
                    best = { piece: p, target: m };
                }
            });
        });
        return best;
    }

    getTargetZoneName(owner) {
        if (owner === 'PLAYER_1') return 'ZONE_1';
        if (this.playerCount === 2) {
            return 'ZONE_4'; // AI target is Bottom
        } else {
            // 3p layout: 4->1, 2->5, 6->3
            if (owner === 'AI_1') return 'ZONE_5';
            if (owner === 'AI_2') return 'ZONE_3';
        }
        return 'ZONE_1';
    }

    scoreMove(piece, target, targetZoneName) {
        const targetHoles = this.board.getAllHoles().filter(h => h.zone === targetZoneName);
        if (targetHoles.length === 0) return 0;

        let tQ = 0, tR = 0;
        targetHoles.forEach(h => { tQ += h.q; tR += h.r; });
        tQ /= targetHoles.length;
        tR /= targetHoles.length;

        const oldDist = this.axialDist(piece.q, piece.r, tQ, tR);
        const newDist = this.axialDist(target.q, target.r, tQ, tR);
        
        // Progress toward target centroid
        let score = (oldDist - newDist);
        
        // Bonus for actually reaching the target zone
        const destZone = this.board.getHole(target.q, target.r).zone;
        if (destZone === targetZoneName) score += 10;
        
        // Tiny randomness
        return score + Math.random() * 0.1;
    }

    axialDist(q1, r1, q2, r2) {
        return (Math.abs(q1 - q2) + Math.abs(q1 + r1 - q2 - r2) + Math.abs(r1 - r2)) / 2;
    }

    getValidMoves(piece) {
        const moves = [];
        this.board.getNeighbors(piece.q, piece.r).forEach(h => {
            if (!h.occupant) moves.push({ q: h.q, r: h.r });
        });
        this.getJumpMoves(piece.q, piece.r, [], moves);
        return moves;
    }

    getJumpMoves(q, r, visited, outcomes) {
        const directions = [{q:1,r:0},{q:1,r:-1},{q:0,r:-1},{q:-1,r:0},{q:-1,r:1},{q:0,r:1}];
        directions.forEach(d => {
            const over = this.board.getHole(q + d.q, r + d.r);
            const land = this.board.getHole(q + d.q*2, r + d.r*2);
            if (over?.occupant && land && !land.occupant) {
                const key = `${land.q},${land.r}`;
                if (!visited.includes(key)) {
                    outcomes.push({ q: land.q, r: land.r, isJump: true });
                    visited.push(key);
                    this.getJumpMoves(land.q, land.r, visited, outcomes);
                }
            }
        });
    }

    handleClick(x, y) {
        if (this.turn !== 'PLAYER_1' || !this.isRunning) return;
        const hex = this.pixelToHex(x, y);
        const hole = this.board.getHole(hex.q, hex.r);
        
        if (hole?.occupant && hole.occupant.owner === 'PLAYER_1') {
            this.selectedPiece = hole.occupant;
            this.validMoves = this.getValidMoves(this.selectedPiece);
        } else if (this.selectedPiece) {
            const move = this.validMoves.find(m => m.q === hex.q && m.r === hex.r);
            if (move) {
                this.executeMove(this.selectedPiece, move);
            } else {
                this.selectedPiece = null;
                this.validMoves = [];
            }
        }
    }

    executeMove(piece, target) {
        this.board.setOccupant(piece.q, piece.r, null);
        this.board.setOccupant(target.q, target.r, piece);
        piece.q = target.q;
        piece.r = target.r;
        this.selectedPiece = null;
        this.validMoves = [];
        this.endTurn();
    }

    endTurn() {
        const winner = this.checkWin();
        if (winner) {
            this.isRunning = false;
            this.saveScore(winner);
            this.ui.showGameOver(winner === 'PLAYER_1');
            return;
        }

        if (this.playerCount === 2) {
            this.turn = (this.turn === 'PLAYER_1') ? 'AI_1' : 'PLAYER_1';
        } else {
            if (this.turn === 'PLAYER_1') this.turn = 'AI_1';
            else if (this.turn === 'AI_1') this.turn = 'AI_2';
            else this.turn = 'PLAYER_1';
        }
    }

    checkWin() {
        const players = ['PLAYER_1', 'AI_1', 'AI_2'];
        for (const p of players) {
            const targetZone = this.getTargetZoneName(p);
            const holes = this.board.getAllHoles().filter(h => h.zone === targetZone);
            if (holes.length > 0 && holes.every(h => h.occupant && h.occupant.owner === p)) {
                return p;
            }
        }
        return null;
    }

    getScore(owner) {
        const targetZone = this.getTargetZoneName(owner);
        const holes = this.board.getAllHoles().filter(h => h.zone === targetZone);
        return holes.filter(h => h.occupant && h.occupant.owner === owner).length;
    }

    saveScore(winner) {
        if (winner !== 'PLAYER_1') return;
        const time = Math.floor(this.timer / 1000);
        const scores = JSON.parse(localStorage.getItem('ahirs_cc_scores') || '[]');
        scores.push({ player: "Ahir", time, result: 'Victory ⭐', date: new Date().toISOString() });
        scores.sort((a,b) => a.time - b.time);
        localStorage.setItem('ahirs_cc_scores', JSON.stringify(scores.slice(0, 10)));
    }

    pixelToHex(x, y) {
        const size = this.getHexSize();
        const cx = this.canvas.width / 2, cy = this.canvas.height / 2;
        let q = (2/3 * (x - cx)) / size;
        let r = (-1/3 * (x - cx) + Math.sqrt(3)/3 * (y - cy)) / size;
        return this.axialRound(q, r);
    }

    axialRound(q, r) {
        let s = -q - r;
        let rq = Math.round(q), rr = Math.round(r), rs = Math.round(s);
        const qd = Math.abs(rq-q), rd = Math.abs(rr-r), sd = Math.abs(rs-s);
        if (qd > rd && qd > sd) rq = -rr-rs;
        else if (rd > sd) rr = -rq-rs;
        return { q: rq, r: rr };
    }

    getHexSize() {
        return Math.min(this.canvas.width, this.canvas.height) / 25;
    }

    draw() {
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        const size = this.getHexSize();
        const cx = this.canvas.width / 2, cy = this.canvas.height / 2;

        this.board.getAllHoles().forEach(h => {
            const px = cx + size * (3/2 * h.q);
            const py = cy + size * (Math.sqrt(3)/2 * h.q + Math.sqrt(3) * h.r);
            this.ctx.beginPath();
            this.ctx.arc(px, py, size * 0.42, 0, Math.PI * 2);
            this.ctx.fillStyle = h.color;
            this.ctx.fill();
            if (this.validMoves.some(m => m.q === h.q && m.r === h.r)) {
                this.ctx.fillStyle = 'rgba(255, 255, 0, 0.6)';
                this.ctx.beginPath();
                this.ctx.arc(px, py, size * 0.2, 0, Math.PI * 2);
                this.ctx.fill();
            }
        });

        this.pieces.forEach(p => {
            const px = cx + size * (3/2 * p.q);
            const py = cy + size * (Math.sqrt(3)/2 * p.q + Math.sqrt(3) * p.r);
            this.ctx.save();
            this.ctx.translate(px, py);
            this.ctx.beginPath();
            this.ctx.arc(0, 0, size * 0.38, 0, Math.PI * 2);
            this.ctx.fillStyle = p.color;
            this.ctx.shadowBlur = 15;
            this.ctx.shadowColor = p.color;
            this.ctx.fill();
            if (p === this.selectedPiece) {
                this.ctx.strokeStyle = '#fff';
                this.ctx.lineWidth = 3;
                this.ctx.stroke();
            }
            this.ctx.restore();
        });
    }
}
