export class UIManager {
    constructor(economy) {
        this.economy = economy;
        this.dom = {
            start: document.getElementById('start-screen'),
            hud: document.getElementById('game-hud'),
            gameOver: document.getElementById('game-over-screen'),
            howToPlay: document.getElementById('how-to-play-screen'),
            legends: document.getElementById('legends-screen'),
            credits: document.getElementById('credits-screen'),
            lowBalance: document.getElementById('low-balance-modal'),
            carousel: document.getElementById('other-games-carousel')
        };
        this.setupEventListeners();
        this.populateCarousel();
    }

    setupEventListeners() {
        // Start Game
        document.getElementById('start-btn').addEventListener('click', () => {
            const name = document.getElementById('player-name').value;
            if (!name) {
                document.getElementById('name-error').classList.remove('hidden');
                return;
            }
            const avatar = document.querySelector('.avatar-option.selected').dataset.avatar;
            const difficulty = document.querySelector('.difficulty-option.selected').dataset.difficulty;
            const playerCount = parseInt(document.querySelector('.player-count-option.selected').dataset.count);
            this.onStartGame({ name, avatar, difficulty, playerCount });
        });

        // Player Count Selection
        document.querySelectorAll('.player-count-option').forEach(el => {
            el.addEventListener('click', (e) => {
                document.querySelectorAll('.player-count-option').forEach(opt => opt.classList.remove('selected'));
                e.currentTarget.classList.add('selected');
            });
        });

        // Avatar Selection
        document.querySelectorAll('.avatar-option').forEach(el => {
            el.addEventListener('click', (e) => {
                document.querySelectorAll('.avatar-option').forEach(opt => opt.classList.remove('selected'));
                e.currentTarget.classList.add('selected');
            });
        });

        // Difficulty Selection
        document.querySelectorAll('.difficulty-option').forEach(el => {
            el.addEventListener('click', (e) => {
                document.querySelectorAll('.difficulty-option').forEach(opt => opt.classList.remove('selected'));
                e.currentTarget.classList.add('selected');
            });
        });

        // Menu Buttons
        document.getElementById('how-to-play-btn').addEventListener('click', () => {
            this.showScreen('howToPlay');
        });
        document.getElementById('legends-btn').addEventListener('click', () => {
            this.populateLegends();
            this.showScreen('legends');
        });
        document.getElementById('credits-btn').addEventListener('click', () => {
            this.showScreen('credits');
        });
        
        document.querySelectorAll('.back-btn').forEach(btn => {
            btn.addEventListener('click', () => this.showScreen('start'));
        });

        document.getElementById('close-low-balance').addEventListener('click', () => {
            this.dom.lowBalance.classList.add('hidden');
        });

        document.getElementById('menu-btn').addEventListener('click', () => location.reload());
        document.getElementById('restart-btn').addEventListener('click', () => location.reload());
    }

    showScreen(name) {
        // Hide all screens
        Object.values(this.dom).forEach(el => el?.classList.add('hidden'));
        
        // Show target screen
        if (name === 'hud') {
            this.dom.hud.classList.remove('hidden');
        } else {
            this.dom[name]?.classList.remove('hidden');
        }

        if (name === 'start') {
            this.updateMenuBalance(this.economy.getBalance());
        }
    }

    updateHUD(data) {
        document.getElementById('turn-display').innerText = data.turn === 'PLAYER_1' ? "Your Turn" : "AI Thinking...";
        document.getElementById('score-display').innerText = `${data.score}/10`;
        document.getElementById('timer-display').querySelector('span').innerText = data.timer;
    }

    showAITalk(msg) {
        const el = document.getElementById('ai-talk');
        el.innerText = msg;
        el.classList.remove('hidden');
        el.style.display = 'block';
        setTimeout(() => el.style.display = 'none', 3000);
    }

    showGameOver(win) {
        this.showScreen('gameOver');
        const title = document.getElementById('result-title');
        const msg = document.getElementById('result-message');
        if (win) {
            title.innerText = "STRATEGIC VICTORY! ⭐";
            title.style.color = "#00ff88";
            msg.innerText = "You outmaneuvered the AI with superior tactics!";
        } else {
            title.innerText = "DEFEAT";
            title.style.color = "#ff4444";
            msg.innerText = "The AI anticipates your every move. Rematch?";
        }
    }

    populateLegends() {
        const tbody = document.getElementById('legends-body');
        const msg = document.getElementById('no-legends-msg');
        if (!tbody) return;

        tbody.innerHTML = '';
        const scores = JSON.parse(localStorage.getItem('ahirs_cc_scores') || '[]');

        if (scores.length === 0) {
            msg.style.display = 'block';
            return;
        }
        msg.style.display = 'none';

        scores.forEach((s, i) => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>#${i + 1}</td>
                <td>${s.player}</td>
                <td>${s.time}s</td>
                <td>${s.result}</td>
            `;
            tbody.appendChild(tr);
        });
    }

    showLowBalance() {
        this.dom.lowBalance.classList.remove('hidden');
    }

    updateMenuBalance(balance) {
        const el = document.getElementById('menu-coin-balance');
        if (el) el.innerText = balance;
    }

    bindStartGame(cb) { this.onStartGame = cb; }

    populateCarousel() {
        const games = [
            { name: "Ludo", icon: "🎲", link: "../AhirsLudo/index.html" },
            { name: "Chinese Checkers", icon: "⭐", link: "../AhirsChineseCheckers/index.html" },
            { name: "Spy Mission", icon: "🕵️", link: "../AhirsSpy/index.html" },
            { name: "Ghost Maze", icon: "👻", link: "../AhirsGhostMaze/index.html" },
            { name: "Academy", icon: "🎓", link: "../AhirsAcademy/index.html" },
            { name: "Snake Room", icon: "🐍", link: "../AhirsSnakeInARoom/index.html" },
            { name: "Shark Race", icon: "🦈", link: "../AhirSharkRace/index.html" },
            { name: "Shooting", icon: "🔫", link: "../AhirsShootingBattle/index.html" },
            { name: "War Zone", icon: "⚔️", link: "../AhirsWarZone/index.html" },
            { name: "Chess", icon: "♟", link: "../AhirsChess/index.html" },
            { name: "Snake & Ladder", icon: "🎲", link: "../AhirsSnakeAndLadder/index.html" },
            { name: "Bike Race", icon: "🚲", link: "../AhirsBikeRace/index.html" }
        ];
        const container = this.dom.carousel;
        if (!container) return;
        container.innerHTML = '';
        games.forEach(g => {
            const a = document.createElement('a');
            a.href = g.link;
            a.className = 'game-card';
            a.innerHTML = `<span class="card-icon">${g.icon}</span><h5>${g.name}</h5>`;
            container.appendChild(a);
        });
    }
}
