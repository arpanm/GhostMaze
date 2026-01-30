import { Board } from './board.js';
import { Player } from './entities.js';
import { economy } from './economy.js';

export class Game {
    constructor() {
        this.canvas = document.getElementById('game-canvas');
        this.ctx = this.canvas.getContext('2d');

        // State
        this.state = 'START'; // START, ROLL, MOVE, EVENT, END
        this.players = [];
        this.currentPlayerIndex = 0;
        this.opponentCount = 0;

        // Modules
        this.board = new Board(this.ctx);
        // Temp player for setup
        this.playerConfig = { name: 'Player', color: '#00ff00' };

        // Setup
        this.resize();
        this.setupInputs();

        // Loop
        requestAnimationFrame((t) => this.loop(t));
    }

    resize() {
        this.canvas.width = window.innerWidth;
        this.canvas.height = window.innerHeight;
        this.board.resize(this.canvas.width, this.canvas.height);
    }

    setupInputs() {
        window.addEventListener('resize', () => this.resize());

        document.getElementById('close-low-balance').addEventListener('click', () => {
            document.getElementById('low-balance-modal').classList.add('hidden');
        });
        this.updateBalanceDisplay();

        // Start Screen
        document.getElementById('start-btn').addEventListener('click', () => this.startGame());

        // Name & Color
        document.getElementById('player-name').addEventListener('input', (e) => this.playerConfig.name = e.target.value.trim() || 'Player');

        document.querySelectorAll('.color-opt').forEach(el => {
            el.addEventListener('click', (e) => {
                document.querySelectorAll('.color-opt').forEach(c => c.classList.remove('active'));
                e.target.classList.add('active');
                this.playerConfig.color = e.target.dataset.color;
            });
        });

        // Opponent Selector
        document.querySelectorAll('.opt-btn').forEach(el => {
            el.addEventListener('click', (e) => {
                document.querySelectorAll('.opt-btn').forEach(b => b.classList.remove('active'));
                e.target.classList.add('active');
                this.opponentCount = parseInt(e.target.dataset.count);
            });
        });

        // Roll
        document.getElementById('roll-btn').addEventListener('click', () => {
            if (this.players[this.currentPlayerIndex].isBot) return;
            this.rollDice();
        });

        // Pause
        document.getElementById('menu-btn').addEventListener('click', () => {
            document.getElementById('pause-modal').classList.remove('hidden');
        });
        document.getElementById('resume-btn').addEventListener('click', () => {
            document.getElementById('pause-modal').classList.add('hidden');
        });
        document.getElementById('restart-btn').addEventListener('click', () => {
            document.getElementById('pause-modal').classList.add('hidden');
            this.showScreen('start-screen');
            this.state = 'START';
        });
        document.getElementById('exit-btn').addEventListener('click', () => {
            document.getElementById('pause-modal').classList.add('hidden');
            this.showScreen('start-screen');
            this.state = 'START';
        });

        // Win
        document.getElementById('play-again-btn').addEventListener('click', () => location.reload()); // Simple reload for now
        document.getElementById('main-menu-back-btn').addEventListener('click', () => location.reload());

        // Credits / Leaderboard / HTP
        document.getElementById('credits-btn').addEventListener('click', () => this.showScreen('credits-screen'));
        document.getElementById('back-credits-btn').addEventListener('click', () => this.showScreen('start-screen'));

        document.getElementById('how-to-play-btn').addEventListener('click', () => this.showScreen('how-to-play-screen'));
        document.getElementById('back-htp-btn').addEventListener('click', () => this.showScreen('start-screen'));

        document.getElementById('hall-of-fame-btn').addEventListener('click', () => {
            this.loadLeaderboard();
            this.showScreen('leaderboard-screen');
        });
        document.getElementById('back-leaderboard-btn').addEventListener('click', () => this.showScreen('start-screen'));
    }

    loadLeaderboard() {
        const list = document.getElementById('leaderboard-list');
        const msg = document.getElementById('no-records-msg');
        list.innerHTML = '';

        const scores = JSON.parse(localStorage.getItem('ahirs-snake-ladder-scores') || '[]');

        if (scores.length === 0) {
            msg.style.display = 'block';
            return;
        }

        msg.style.display = 'none';
        scores.forEach((s, i) => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>#${i + 1}</td>
                <td>${s.name}</td>
                <td>${s.moves}</td>
                <td>${s.date}</td>
            `;
            list.appendChild(tr);
        });
    }

    showScreen(id) {
        document.querySelectorAll('.screen').forEach(s => s.classList.add('hidden'));
        document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
        document.getElementById(id).classList.remove('hidden');
        document.getElementById(id).classList.add('active');

        if (id === 'hud') {
            document.getElementById('hud').style.pointerEvents = 'none';
        }
    }

    startGame() {
        // Economy Check
        if (!economy.hasEnoughBalance(10)) {
            document.getElementById('low-balance-modal').classList.remove('hidden');
            return;
        }

        economy.spendCoins(10, 'Snake & Ladder Entry');
        this.updateBalanceDisplay();

        this.board.generate();

        // Init Players
        this.players = [];
        this.players.push(new Player(this.playerConfig.name, this.playerConfig.color, false));

        // Add Bots
        // Add Bots
        // Expanded palette matching UI options + extras
        const botColors = ['#00ff00', '#ff00ff', '#00ffff', '#ffff00', '#ff0000', '#0000ff'];
        const occupiedColors = [this.playerConfig.color.toLowerCase()];

        for (let i = 0; i < this.opponentCount; i++) {
            // Find unique color
            let color = botColors.find(c => !occupiedColors.includes(c.toLowerCase()));
            if (!color) color = '#ffffff'; // Fallback

            occupiedColors.push(color.toLowerCase());
            this.players.push(new Player(`Bot ${i + 1}`, color, true));
        }

        this.currentPlayerIndex = 0;

        // UI
        this.showScreen('hud');
        document.getElementById('ui-layer').style.pointerEvents = 'none';

        this.updateHUD();
        this.state = 'ROLL';
        this.log("Game Started! " + this.players[0].name + "'s Turn.");
    }

    updateHUD() {
        const p = this.players[this.currentPlayerIndex];
        document.getElementById('hud-name').textContent = p.name;
        document.getElementById('hud-avatar').textContent = p.name[0].toUpperCase();
        document.getElementById('hud-avatar').style.color = p.color;
        document.getElementById('hud-avatar').style.borderColor = p.color;

        const rollBtn = document.getElementById('roll-btn');
        if (p.isBot) {
            document.getElementById('turn-indicator').textContent = "OPPONENT THINKING...";
            rollBtn.disabled = true;
            // rollBtn.style.opacity = 0.5; // Handled by CSS now
        } else {
            document.getElementById('turn-indicator').textContent = "YOUR TURN";
            // Only enable if state is ROLL (not during move/animation if updateHUD called oddly)
            if (this.state === 'ROLL') {
                rollBtn.disabled = false;
            }
            // rollBtn.style.opacity = 1; // Handled by CSS
        }
    }

    log(msg) {
        document.getElementById('game-log').textContent = msg;
    }

    rollDice() {
        if (this.state !== 'ROLL') return;

        this.state = 'ANIMATING_DICE';
        const dice = document.getElementById('dice-cube');
        document.getElementById('roll-btn').disabled = true; // Prevent double click

        // Reset transform to force animation? No, standard CSS transition takes care of it usually
        // But to ensure it spins every time, we increment rotation
        const rx = Math.floor(Math.random() * 4) * 360 + 360 * 5;
        const ry = Math.floor(Math.random() * 4) * 360 + 360 * 5;
        dice.style.transition = 'transform 1s ease-out';
        dice.style.transform = `rotateX(${rx}deg) rotateY(${ry}deg)`;

        // Play Sound (TODO)

        const val = Math.floor(Math.random() * 6) + 1;

        setTimeout(() => {
            this.handleRollResult(val);
        }, 1100);
    }

    handleRollResult(val) {
        const p = this.players[this.currentPlayerIndex];
        this.log(`${p.name} Rolled a ${val}!`);

        // Fix Dice Orientation
        const dice = document.getElementById('dice-cube');
        dice.style.transition = 'none'; // Instant snap
        // Find rotation module 360 that matches face
        // 1: 0,0 | 6: 180,0 | 2: -90,0 | 5: 90,0 | 3: 0,-90 | 4: 0,90
        // We'll just reset rotation to clean state
        let rot = { x: 0, y: 0 };
        if (val === 1) rot = { x: 0, y: 0 };
        if (val === 6) rot = { x: 0, y: 180 };
        if (val === 2) rot = { x: -90, y: 0 };
        if (val === 5) rot = { x: 90, y: 0 };
        if (val === 3) rot = { x: 0, y: -90 };
        if (val === 4) rot = { x: 0, y: 90 };
        dice.style.transform = `rotateX(${rot.x}deg) rotateY(${rot.y}deg)`;


        if (p.currentTile + val <= 100) {
            p.setTarget(p.currentTile + val);
            p.moves++;
            this.state = 'MOVE';
        } else {
            this.log("Need exact roll!");
            this.endTurn();
        }
    }

    endTurn() {
        if (this.state === 'END') return;

        this.currentPlayerIndex = (this.currentPlayerIndex + 1) % this.players.length;
        this.state = 'ROLL';
        this.updateHUD();

        // AI Check
        const nextP = this.players[this.currentPlayerIndex];
        if (nextP.isBot) {
            setTimeout(() => this.rollDice(), 1000); // 1s Think Time
        }
    }

    loop(t) {
        // Update
        if (this.state === 'MOVE') {
            const p = this.players[this.currentPlayerIndex];
            const finished = p.update();
            if (finished) {
                this.checkTileEvent();
            }
        }

        // Draw
        this.ctx.fillStyle = '#111';
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

        this.board.draw(this.ctx);

        // Draw all players
        this.players.forEach(p => p.draw(this.board, this.ctx));

        requestAnimationFrame((t) => this.loop(t));
    }

    checkTileEvent() {
        const p = this.players[this.currentPlayerIndex];
        const event = this.board.getEventAt(p.currentTile);

        if (event) {
            if (event.type === 'SNAKE') {
                this.log(`${p.name} bitten by Snake!`);
                p.setTarget(event.to);
                this.state = 'MOVE';
                // Play Sound
            } else if (event.type === 'LADDER') {
                this.log(`${p.name} found a Ladder!`);
                p.setTarget(event.to);
                this.state = 'MOVE';
                // Play Sound
            }
        } else {
            // Check Win
            if (p.currentTile === 100) {
                this.winGame(p);
            } else {
                this.endTurn();
            }
        }
    }

    winGame(winner) {
        this.state = 'END';
        document.getElementById('win-screen').classList.remove('hidden');
        document.getElementById('winner-name').textContent = winner.name;
        document.getElementById('winner-moves').textContent = winner.moves;
        document.getElementById('winner-avatar').textContent = "🏆";

        // Save Score only if human
        if (!winner.isBot) {
            this.saveScore(winner.name, winner.moves);
            // economy.addCoins(100, 'Snake & Ladder Win');
            // this.updateBalanceDisplay();
            // document.querySelector('.winner-card').insertAdjacentHTML('beforeend', `<p style="color:gold; font-size:1.2rem; margin-top:10px;">Earned 100 Coins! 🪙</p>`);
        }
    }

    saveScore(name, moves) {
        const scores = JSON.parse(localStorage.getItem('ahirs-snake-ladder-scores') || '[]');
        scores.push({ name, moves, date: new Date().toLocaleDateString() });
        scores.sort((a, b) => a.moves - b.moves); // Sort by fewer moves
        localStorage.setItem('ahirs-snake-ladder-scores', JSON.stringify(scores.slice(0, 5)));
    }

    updateBalanceDisplay() {
        const el = document.getElementById('menu-coin-balance');
        if (el) el.textContent = economy.getBalance();
    }
}
