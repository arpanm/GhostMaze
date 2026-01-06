import { ChessGame } from './chess.js';
import { UIManager } from './ui.js';
import { ChessAI } from './ai.js';

class Main {
    constructor() {
        this.game = new ChessGame();
        this.ui = new UIManager(document.getElementById('chess-board'), this.game);
        this.ai = new ChessAI(this.game);

        this.gameState = 'MENU'; // MENU, PLAY, PAUSE, END
        this.options = {
            side: 'white',
            difficulty: 'easy',
            format: 'rapid', // 10m
            time: 600, // seconds
        };

        this.timers = { w: 600, b: 600 };
        this.timerInterval = null;

        this.initListeners();
    }

    initListeners() {
        document.getElementById('start-btn').addEventListener('click', () => this.startGame());

        // Options
        document.querySelectorAll('#side-select .toggle-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                document.querySelectorAll('#side-select .toggle-btn').forEach(b => b.classList.remove('selected'));
                e.target.classList.add('selected');
                this.options.side = e.target.dataset.side;
            });
        });

        // Difficulty
        document.querySelectorAll('#difficulty-select .toggle-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                document.querySelectorAll('#difficulty-select .toggle-btn').forEach(b => b.classList.remove('selected'));
                e.target.classList.add('selected');
                this.options.difficulty = e.target.dataset.diff;
            });
        });

        // Format
        document.getElementById('format-select').addEventListener('change', (e) => {
            const formats = {
                classical: 5400, // 90m
                rapid: 600, // 10m
                blitz: 300, // 5m
                bullet: 60 // 1m
            };
            this.options.format = e.target.value;
            this.options.time = formats[e.target.value];
        });

        // Style
        document.querySelectorAll('#style-select .toggle-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                document.querySelectorAll('#style-select .toggle-btn').forEach(b => b.classList.remove('selected'));
                e.target.classList.add('selected');
                this.ui.pieceTheme = e.target.dataset.style;
                if (this.gameState === 'PLAY') this.ui.drawBoard(); // Redraw if checking theme mid-game
            });
        });

        // Board interactions
        const boardEl = document.getElementById('chess-board');
        boardEl.addEventListener('click', (e) => this.handleBoardClick(e));

        // Pause/Exit
        document.getElementById('pause-btn').addEventListener('click', () => this.pauseGame());
        document.getElementById('resume-btn').addEventListener('click', () => this.resumeGame());
        document.getElementById('restart-btn').addEventListener('click', () => {
            this.showScreen('hud'); // Hide pause
            this.startGame();
        });
        document.getElementById('exit-btn').addEventListener('click', () => location.reload()); // Simple exit

        // Menu Buttons
        document.getElementById('leaderboard-btn').addEventListener('click', () => this.showScreen('leaderboard-screen'));
        document.getElementById('back-from-leaderboard').addEventListener('click', () => this.showScreen('start-screen'));
        document.getElementById('credits-btn').addEventListener('click', () => this.showScreen('credits-screen'));
        document.getElementById('back-from-credits').addEventListener('click', () => this.showScreen('start-screen'));
        document.getElementById('play-again-btn').addEventListener('click', () => this.startGame());
        document.getElementById('menu-btn').addEventListener('click', () => this.showScreen('start-screen'));

        // Helper to show screens
        this.showScreen('start-screen');

        // Load Leaderboard initially
        this.updateLeaderboard();
    }

    showScreen(id) {
        document.querySelectorAll('.screen').forEach(s => s.classList.remove('active', 'hidden'));
        document.querySelectorAll('.screen').forEach(s => s.classList.add('hidden'));

        const target = document.getElementById(id);
        if (target) {
            target.classList.remove('hidden');
            target.classList.add('active');
        }

        if (id === 'hud') { // special case
            document.getElementById('ui-layer').style.pointerEvents = 'none'; // click through
        } else {
            document.getElementById('ui-layer').style.pointerEvents = 'all';
        }
    }

    startGame() {
        const name = document.getElementById('player-name').value.trim();
        if (!name) {
            document.getElementById('name-error').classList.remove('hidden');
            return;
        }
        document.getElementById('name-error').classList.add('hidden');
        document.getElementById('player-name-display').textContent = name;

        // Reset
        this.game.reset();
        this.game.playerName = name;

        // Timers
        this.timers = { w: this.options.time, b: this.options.time };
        this.updateTimerDisplay();
        this.startTimerLoop();

        // Setup UI
        this.ui.flipped = this.options.side === 'black'; // Play as black?
        this.ui.drawBoard();

        document.getElementById('game-area').classList.remove('hidden');
        this.showScreen('hud'); // Actually effectively hides all screens
        document.getElementById('ui-layer').dataset.active = "false"; // helper

        this.gameState = 'PLAY';

        if (this.options.side === 'black') {
            // AI Move
            setTimeout(() => this.makeAIMove(), 1000);
        }
    }

    startTimerLoop() {
        if (this.timerInterval) clearInterval(this.timerInterval);
        this.timerInterval = setInterval(() => {
            if (this.gameState !== 'PLAY') return;

            const turn = this.game.turn;
            this.timers[turn]--;

            if (this.timers[turn] <= 0) {
                this.timers[turn] = 0;
                this.game.isGameOver = true;
                this.game.winner = turn === 'w' ? 'black' : 'white'; // Opponent wins on time
                this.checkGameOver(true);
            }
            this.updateTimerDisplay();
        }, 1000);
    }

    handleBoardClick(e) {
        if (this.gameState !== 'PLAY') return;

        const square = e.target.closest('.square');
        if (!square) return;

        const r = parseInt(square.dataset.r);
        const c = parseInt(square.dataset.c);
        const coords = { r, c };

        // 1. If piece selected, try to move
        if (this.ui.selectedSquare) {
            const from = this.ui.selectedSquare;
            // Trying to move to (r, c)
            if (this.game.makeMove(from, coords)) {
                // Valid move!
                this.endTurn();
                return;
            } else {
                // Invalid move. 
                // If clicked on another own piece, select it instead.
                const piece = this.game.getPiece(r, c);
                if (piece && piece.color === this.game.turn) {
                    this.selectSquare(coords);
                    return;
                }
                // Else deselect
                this.deselect();
            }
        } else {
            // 2. No selection. Select if own piece
            const piece = this.game.getPiece(r, c);
            if (piece && piece.color === this.game.turn) {
                // Check if it's user's turn
                const userColor = this.options.side === 'white' ? 'w' : 'b';
                if (this.options.difficulty !== 'human_vs_human' && this.game.turn !== userColor) {
                    return; // Not your turn
                }
                this.selectSquare(coords);
            }
        }
    }

    selectSquare(coords) {
        this.ui.selectedSquare = coords;
        const moves = this.game.getMoves(coords.r, coords.c);
        this.ui.drawBoard(); // Redraw to clear previous
        this.ui.highlightMoves(moves);
        this.ui.highlightSelected(coords);
    }

    deselect() {
        this.ui.selectedSquare = null;
        this.ui.drawBoard();
    }

    endTurn() {
        this.deselect();
        this.ui.drawBoard();
        this.checkGameOver();

        if (this.gameState === 'PLAY' && !this.game.isGameOver) {
            const userColor = this.options.side === 'white' ? 'w' : 'b';
            if (this.game.turn !== userColor) {
                // AI Turn
                setTimeout(() => this.makeAIMove(), 100);
            }
        }
    }

    checkGameOver(timeout = false) {
        if (this.game.isGameOver) {
            this.gameState = 'END';
            clearInterval(this.timerInterval);

            let title = 'GAME OVER';
            let msg = '';

            if (timeout) {
                title = 'TIME EXPIRED';
                msg = this.game.winner === 'white' ? 'White wins on time' : 'Black wins on time';
            } else if (this.game.winner === 'draw') {
                title = 'DRAW';
                msg = 'Stalemate';
            } else {
                title = 'CHECKMATE';
                msg = this.game.winner === 'white' ? 'White Wins!' : 'Black Wins!';
            }

            document.getElementById('game-result-title').textContent = title;
            document.getElementById('game-result-msg').textContent = msg;

            // Stats
            document.getElementById('stat-moves').textContent = this.game.fullMoveNumber;
            // Time Remaining (User's time)
            const userSide = this.options.side === 'white' ? 'w' : 'b';
            const time = this.timers[userSide];
            const m = Math.floor(time / 60);
            const s = time % 60;
            document.getElementById('stat-time').textContent = `${m}:${s < 10 ? '0' + s : s}`;

            // Save Score
            this.saveScore(this.game.winner === 'white' ? 'w' : 'b'); // Winner color

            this.showScreen('game-over-screen');
        }
    }

    saveScore(winnerColor) {
        const userColor = this.options.side === 'white' ? 'w' : 'b';
        let result = 'loss';
        if (this.game.winner === 'draw') result = 'draw';
        else if (winnerColor === userColor) result = 'win';

        const record = {
            name: this.game.playerName,
            result: result,
            difficulty: this.options.difficulty,
            format: this.options.format,
            date: new Date().toISOString()
        };

        const key = 'AhirsChess_Scores';
        const scores = JSON.parse(localStorage.getItem(key) || '[]');
        scores.push(record);
        localStorage.setItem(key, JSON.stringify(scores));

        this.updateLeaderboard(scores);
    }

    updateLeaderboard(scores) {
        // Also call this on menu load
        const list = document.getElementById('leaderboard-list');
        if (!list) return;
        list.innerHTML = '';

        // Handle undefined scores
        if (!scores) return;

        // Filter last 10 or best? Just show recent list for now
        scores.slice(-10).reverse().forEach(s => {
            const row = document.createElement('div');
            row.className = 'score-row';
            row.innerHTML = `<span>${s.name} (${s.difficulty})</span> <span>${s.result.toUpperCase()}</span>`;
            list.appendChild(row);
        });
    }

    makeAIMove() {
        const color = this.game.turn;
        // Use difficulty from options
        // For UI responsiveness, we might want to make this async or web worker, but for basic JS it's fine
        const bestMove = this.ai.getBestMove(color, this.options.difficulty);

        if (bestMove) {
            this.game.makeMove(bestMove.from, bestMove.to);
            this.endTurn();
        } else {
            this.checkGameOver();
        }
    }

    updateTimerDisplay() {
        const format = (s) => {
            const m = Math.floor(s / 60);
            const sec = s % 60;
            return `${m}:${sec < 10 ? '0' + sec : sec}`;
        };

        const userSide = this.options.side === 'white' ? 'w' : 'b';
        const oppSide = userSide === 'w' ? 'b' : 'w';

        const userTime = this.timers[userSide];
        const oppTime = this.timers[oppSide];

        const pt = document.getElementById('player-timer');
        const ot = document.getElementById('opponent-timer');

        if (pt) pt.textContent = format(userTime);
        if (ot) ot.textContent = format(oppTime);

        if (this.game.turn === userSide) {
            if (pt) pt.classList.add('active');
            if (ot) ot.classList.remove('active');
        } else {
            if (pt) pt.classList.remove('active');
            if (ot) ot.classList.add('active');
        }
    }

    pauseGame() {
        this.gameState = 'PAUSE';
        this.showScreen('pause-screen');
    }

    resumeGame() {
        this.gameState = 'PLAY';
        document.querySelectorAll('.screen').forEach(s => s.classList.add('hidden'));
    }
}

window.onload = () => new Main();
