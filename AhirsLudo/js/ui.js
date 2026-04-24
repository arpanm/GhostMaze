/**
 * UIManager class - Manages all UI screens, buttons, and transitions.
 */

export class UIManager {
    constructor(economy) {
        this.economy = economy;
        this.dom = {
            screens: document.querySelectorAll('.screen'),
            startScreen: document.getElementById('start-screen'),
            hud: document.getElementById('game-hud'),
            gameOver: document.getElementById('game-over-screen'),
            legends: document.getElementById('legends-screen'),
            credits: document.getElementById('credits-screen'),
            howToPlay: document.getElementById('how-to-play-screen'),
            
            coinBalance: document.getElementById('menu-coin-balance'),
            playerName: document.getElementById('player-name'),
            nameError: document.getElementById('name-error'),
            
            dice: document.getElementById('dice'),
            diceInstruction: document.getElementById('dice-instruction'),
            aiTalk: document.getElementById('ai-talk'),
            
            turnDisplay: document.getElementById('turn-display'),
            scoreDisplay: document.getElementById('score-display'),
            timerDisplay: document.querySelector('#timer-display span'),
            
            carousel: document.getElementById('other-games-carousel')
        };

        this.init();
    }

    init() {
        this.setupEventListeners();
        this.populateCarousel();
        this.updateMenuBalance(this.economy.getBalance());
    }

    setupEventListeners() {
        // Simple screen toggles
        document.getElementById('how-to-play-btn').onclick = () => this.showScreen('howToPlay');
        document.getElementById('legends-btn').onclick = () => {
            this.populateLegends();
            this.showScreen('legends');
        };
        document.getElementById('credits-btn').onclick = () => this.showScreen('credits');
        
        document.querySelectorAll('.back-btn').forEach(btn => {
            btn.onclick = () => this.showScreen('startScreen');
        });

        document.getElementById('menu-btn').onclick = () => this.showScreen('startScreen');
        document.getElementById('restart-btn').onclick = () => this.onStartBtn();

        // Selections
        this.setupSelections('.avatar-option');
        this.setupSelections('.player-count-option');
        this.setupSelections('.difficulty-option');
    }

    setupSelections(selector) {
        document.querySelectorAll(selector).forEach(el => {
            el.onclick = () => {
                document.querySelectorAll(selector).forEach(opt => opt.classList.remove('selected'));
                el.classList.add('selected');
            };
        });
    }

    bindStartGame(callback) {
        this.onStartGame = callback;
        document.getElementById('start-btn').onclick = () => this.onStartBtn();
    }

    onStartBtn() {
        const name = this.dom.playerName.value.trim();
        if (!name) {
            this.dom.nameError.classList.remove('hidden');
            return;
        }
        this.dom.nameError.classList.add('hidden');
        
        const config = {
            name: name,
            color: document.querySelector('.avatar-option.selected').dataset.color,
            playerCount: parseInt(document.querySelector('.player-count-option.selected').dataset.count),
            difficulty: document.querySelector('.difficulty-option.selected').dataset.difficulty
        };
        this.onStartGame(config);
    }

    bindDiceRoll(callback) {
        document.getElementById('dice-container').onclick = callback;
    }

    setDiceValue(val, rolling = false) {
        this.dom.dice.className = rolling ? 'dice-rolling' : '';
        this.dom.dice.textContent = rolling ? '?' : this.getDiceIcon(val);
        this.dom.diceInstruction.textContent = rolling ? 'Rolling...' : 'Select a Piece';
    }

    getDiceIcon(val) {
        const icons = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅'];
        return icons[val - 1] || val;
    }

    showScreen(key) {
        this.dom.screens.forEach(s => s.classList.add('hidden'));
        this.dom.hud.classList.add('hidden');
        
        if (key === 'hud') {
            this.dom.hud.classList.remove('hidden');
        } else {
            this.dom[key].classList.remove('hidden');
        }
    }

    updateHUD(data) {
        if (data.turn) this.dom.turnDisplay.textContent = data.turn;
        if (data.score) this.dom.scoreDisplay.textContent = data.score;
        if (data.timer !== undefined) this.dom.timerDisplay.textContent = data.timer;
    }

    showAITalk(message) {
        this.dom.aiTalk.textContent = message;
        this.dom.aiTalk.classList.add('active');
        setTimeout(() => this.dom.aiTalk.classList.remove('active'), 3000);
    }

    showGameOver(victory, message) {
        document.getElementById('result-title').textContent = victory ? 'VICTORY 🎉' : 'DEFEAT 💀';
        document.getElementById('result-message').textContent = message;
        this.showScreen('gameOver');
    }

    updateMenuBalance(balance) {
        if (this.dom.coinBalance) this.dom.coinBalance.textContent = balance;
    }

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
        
        this.dom.carousel.innerHTML = '';
        games.forEach(g => {
            const card = document.createElement('a');
            card.href = g.link;
            card.className = 'game-card';
            card.innerHTML = `<span class="card-icon">${g.icon}</span><h5>${g.name}</h5>`;
            this.dom.carousel.appendChild(card);
        });
    }

    populateLegends() {
        const scores = JSON.parse(localStorage.getItem('ahirs_ludo_scores') || '[]');
        const body = document.getElementById('legends-body');
        const msg = document.getElementById('no-legends-msg');
        
        body.innerHTML = '';
        if (scores.length === 0) {
            msg.classList.remove('hidden');
            return;
        }
        msg.classList.add('hidden');
        
        scores.forEach((s, i) => {
            const row = `<tr><td>${i+1}</td><td>${s.player}</td><td>${s.time}s</td><td>${s.result}</td></tr>`;
            body.innerHTML += row;
        });
    }
}
