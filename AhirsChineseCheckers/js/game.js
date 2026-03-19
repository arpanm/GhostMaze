import { Board } from './board.js';
import { Piece } from './piece.js';

export class Game {
    constructor(ui, economy) {
        this.ui = ui;
        this.economy = economy;
        this.board = new Board();
        this.pieces = [];
        this.selectedPiece = null;
        this.validMoves = [];
        this.turn = 'PLAYER_1'; // Player starts
        this.isRunning = false;
        this.timer = 0;
        this.lastTime = 0;

        this.canvas = document.getElementById('game-canvas');
        this.ctx = this.canvas.getContext('2d');
        this.setupBoard();
        this.resize();
        window.addEventListener('resize', () => this.resize());
    }

    setupBoard() {
        const p1Names = ["Speedy McHop", "Jumpin' Joe", "Lily Pad", "Bouncy Bob", "Skippy", "Hopper", "Springy", "Leapy Larry", "Frogger", "Rocket"];
        const aiNames = ["Dull Dino", "Slow Sam", "Stuck Steve", "Heavy Herb", "Lazy Larry", "Procrastinator", "Wait-a-Bit", "Turtle Tom", "Snail Sally", "Glacial Greg"];

        // Setup Player 1 and AI
        let p1Count = 0;
        let aiCount = 0;
        this.board.getAllHoles().forEach(h => {
             if (h.zone === 'PLAYER_1') {
                 const p = new Piece(`p1_${p1Count}`, h.q, h.r, 'PLAYER_1', '#00ff88', p1Names[p1Count]);
                 this.pieces.push(p);
                 this.board.setOccupant(h.q, h.r, p);
                 p1Count++;
             }
             if (h.zone === 'AI') {
                 const p = new Piece(`ai_${aiCount}`, h.q, h.r, 'AI', '#00ccff', aiNames[aiCount]);
                 this.pieces.push(p);
                 this.board.setOccupant(h.q, h.r, p);
                 aiCount++;
             }
        });
    }

    resize() {
        this.canvas.width = window.innerWidth;
        this.canvas.height = window.innerHeight;
        this.draw();
    }

    start() {
        this.isRunning = true;
        this.lastTime = performance.now();
        requestAnimationFrame((t) => this.loop(t));
    }

    loop(timestamp) {
        if (!this.isRunning) return;
        const dt = timestamp - this.lastTime;
        this.lastTime = timestamp;
        this.timer += dt;
        
        this.update(dt);
        this.draw();
        requestAnimationFrame((t) => this.loop(t));
    }

    update(dt) {
        this.pieces.forEach(p => p.update(dt));
        this.ui.updateHUD({
            turn: this.turn,
            timer: Math.floor(this.timer / 1000),
            score: this.calculateProgress('PLAYER_1')
        });
    }

    handleInput(clientX, clientY) {
        if (this.turn !== 'PLAYER_1' || !this.isRunning) return;
        
        const pos = this.screenToHex(clientX, clientY);
        const hole = this.board.getHole(pos.q, pos.r);
        
        if (!hole) return;

        if (hole.occupant && hole.occupant.owner === 'PLAYER_1') {
            this.selectedPiece = hole.occupant;
            this.validMoves = this.calculateValidMoves(hole.q, hole.r);
        } else if (this.selectedPiece && this.validMoves.some(m => m.q === pos.q && m.r === pos.r)) {
            this.movePiece(this.selectedPiece, pos.q, pos.r);
            this.endTurn();
        } else {
            this.selectedPiece = null;
            this.validMoves = [];
        }
    }

    calculateValidMoves(q, r) {
        const moves = [];
        // 1. Single steps
        const neighbors = this.board.getNeighbors(q, r);
        neighbors.forEach(n => {
            if (!n.occupant) moves.push({q: n.q, r: n.r, type: 'step'});
        });

        // 2. Jumps (Recursive)
        const jumpMoves = [];
        this.findJumpMoves(q, r, [], jumpMoves);
        return moves.concat(jumpMoves);
    }

    findJumpMoves(q, r, visited, results) {
        const dirs = [
            {q: +1, r:  0}, {q: +1, r: -1}, {q:  0, r: -1},
            {q: -1, r:  0}, {q: -1, r: +1}, {q:  0, r: +1}
        ];

        dirs.forEach(d => {
            const adjacent = this.board.getHole(q + d.q, r + d.r);
            if (adjacent && adjacent.occupant) {
                const target = this.board.getHole(q + 2*d.q, r + 2*d.r);
                if (target && !target.occupant) {
                    const key = `${target.q},${target.r}`;
                    if (!visited.includes(key)) {
                        visited.push(key);
                        results.push({q: target.q, r: target.r, type: 'jump'});
                        this.findJumpMoves(target.q, target.r, visited, results);
                    }
                }
            }
        });
    }

    movePiece(piece, targetQ, targetR) {
        this.board.setOccupant(piece.q, piece.r, null);
        this.board.setOccupant(targetQ, targetR, piece);
        this.selectedPiece = null;
        this.validMoves = [];
        
        // Funny element: Randomly make piece dizzy
        if (Math.random() < 0.1) piece.isDizzy = true;
        setTimeout(() => piece.isDizzy = false, 2000);
    }

    endTurn() {
        if (this.checkVictory('PLAYER_1')) {
            this.isRunning = false;
            this.saveScore('PLAYER_1');
            this.ui.showGameOver(true);
            return;
        }

        this.turn = 'AI';
        this.ui.showAITalk("AI: 'Thinking... and you won't like it!'");
        setTimeout(() => this.aiTurn(), 1000);
    }

    aiTurn() {
        const aiPieces = this.pieces.filter(p => p.owner === 'AI');
        let bestMove = null;
        let bestPiece = null;
        let maxScore = -Infinity;

        aiPieces.forEach(p => {
            const moves = this.calculateValidMoves(p.q, p.r);
            moves.forEach(m => {
                const score = this.scoreMove('AI', p, m);
                if (score > maxScore) {
                    maxScore = score;
                    bestMove = m;
                    bestPiece = p;
                }
            });
        });

        if (bestPiece && bestMove) {
            this.movePiece(bestPiece, bestMove.q, bestMove.r);
            if (this.checkVictory('AI')) {
                this.isRunning = false;
                this.saveScore('AI');
                this.ui.showGameOver(false);
            } else {
                this.turn = 'PLAYER_1';
                this.ui.showAITalk("AI: 'Your turn, if you dare!'");
            }
        }
    }

    scoreMove(owner, piece, move) {
        // Target for AI is bottom triangle center: r=7, q=-3
        const targetQ = owner === 'AI' ? -3 : 3;
        const targetR = owner === 'AI' ? 7 : -7;

        const oldDist = this.axialDist(piece.q, piece.r, targetQ, targetR);
        const newDist = this.axialDist(move.q, move.r, targetQ, targetR);
        
        let score = (oldDist - newDist);
        if (move.type === 'jump') score += 0.5; // Bonus for jumps
        return score;
    }

    saveScore(winner) {
        if (winner === 'AI') return; 
        const timeStr = Math.floor(this.timer / 1000);
        const scores = JSON.parse(localStorage.getItem('ahirs_cc_scores') || '[]');
        scores.push({ 
            player: "Ahir", 
            time: timeStr, 
            result: 'Victory ⭐',
            date: new Date().toISOString() 
        });
        scores.sort((a, b) => a.time - b.time); 
        localStorage.setItem('ahirs_cc_scores', JSON.stringify(scores.slice(0, 10)));
    }

    axialDist(q1, r1, q2, r2) {
        return (Math.abs(q1 - q2) + Math.abs(q1 + r1 - q2 - r2) + Math.abs(r1 - r2)) / 2;
    }

    checkVictory(owner) {
        const targetZone = owner === 'PLAYER_1' ? 'AI' : 'PLAYER_1';
        const piecesInTarget = this.pieces.filter(p => p.owner === owner && this.board.getHole(p.q, p.r).zone === targetZone);
        return piecesInTarget.length === 10;
    }

    calculateProgress(owner) {
        const targetZone = owner === 'PLAYER_1' ? 'AI' : 'PLAYER_1';
        return this.pieces.filter(p => p.owner === owner && this.board.getHole(p.q, p.r).zone === targetZone).length;
    }

    screenToHex(x, y) {
        const centerX = this.canvas.width / 2;
        const centerY = this.canvas.height / 2;
        const size = 30; 
        
        const relX = x - centerX;
        const relY = y - centerY;
        
        const q = (Math.sqrt(3)/3 * relX - 1/3 * relY) / size;
        const r = (2/3 * relY) / size;
        
        return this.hexRound(q, r);
    }

    hexToScreen(q, r) {
        const size = 30;
        const x = size * (Math.sqrt(3) * q + Math.sqrt(3)/2 * r);
        const y = size * (3/2 * r);
        return { x: x + this.canvas.width/2, y: y + this.canvas.height/2 };
    }

    hexRound(q, r) {
        let s = -q - r;
        let rq = Math.round(q);
        let rr = Math.round(r);
        let rs = Math.round(s);
        const dq = Math.abs(rq - q);
        const dr = Math.abs(rr - r);
        const ds = Math.abs(rs - s);
        if (dq > dr && dq > ds) rq = -rr - rs;
        else if (dr > ds) rr = -rq - rs;
        return { q: rq, r: rr };
    }

    draw() {
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        
        // Draw Board
        this.board.getAllHoles().forEach(h => {
            const pos = this.hexToScreen(h.q, h.r);
            this.ctx.beginPath();
            this.ctx.arc(pos.x, pos.y, 12, 0, Math.PI * 2);
            this.ctx.fillStyle = h.color;
            this.ctx.fill();
            
            if (this.validMoves.some(m => m.q === h.q && m.r === h.r)) {
                this.ctx.beginPath();
                this.ctx.arc(pos.x, pos.y, 6, 0, Math.PI * 2);
                this.ctx.fillStyle = 'rgba(255, 255, 0, 0.5)';
                this.ctx.fill();
            }
        });

        // Draw Pieces
        this.pieces.forEach(p => {
            const pos = this.hexToScreen(p.q, p.r);
            this.ctx.save();
            this.ctx.translate(pos.x, pos.y);
            if (p.isDizzy) this.ctx.rotate(p.spinAngle);
            
            this.ctx.beginPath();
            this.ctx.arc(0, 0, 10, 0, Math.PI * 2);
            this.ctx.fillStyle = p.color;
            this.ctx.fill();
            
            // Highlight selected
            if (this.selectedPiece === p) {
                this.ctx.beginPath();
                this.ctx.arc(0, 0, 14, 0, Math.PI * 2);
                this.ctx.strokeStyle = '#ffffff';
                this.ctx.lineWidth = 2;
                this.ctx.stroke();
            }
            this.ctx.restore();
        });
    }
}
