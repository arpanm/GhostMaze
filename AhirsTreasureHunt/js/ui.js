export class UIManager {
    constructor(economy) {
        this.economy = economy;
        this.dom = {
            start: document.getElementById('start-screen'),
            gameContainer: document.getElementById('game-container'),
            hud: document.getElementById('game-hud'),
            gameOver: document.getElementById('game-over-screen'),
            pause: document.getElementById('pause-screen'),
            coinBalance: document.getElementById('menu-coin-balance'),
            lowBalance: document.getElementById('low-balance-modal'),
            howToPlay: document.getElementById('how-to-play-screen'),
            legends: document.getElementById('legends-screen'),
            credits: document.getElementById('credits-screen')
        };

        this.setupEventListeners();
    }

    setupEventListeners() {
        // Start Game
        const startBtn = document.getElementById('start-btn');
        if (startBtn) {
            startBtn.addEventListener('click', () => {
                const nameInput = document.getElementById('player-name');
                const name = nameInput ? nameInput.value.trim() : 'Explorer';
                if (!name) {
                    const err = document.getElementById('name-error');
                    if (err) err.classList.remove('hidden');
                    return;
                }

                const shapeEl = document.querySelector('.shape-option.selected');
                const shape = shapeEl ? shapeEl.dataset.shape : 'circle';

                const diffEl = document.querySelector('.difficulty-option.selected');
                const difficulty = diffEl ? diffEl.dataset.difficulty : 'easy';

                const oppInput = document.getElementById('opponent-count');
                let opponents = oppInput ? parseInt(oppInput.value, 10) : 3;
                if (isNaN(opponents) || opponents < 1) opponents = 1;
                if (opponents > 5) opponents = 5;

                if (this.onStartGame) {
                    this.onStartGame({ name, shape, difficulty, opponents });
                }
            });
        }

        // Shape Selection
        document.querySelectorAll('.shape-option').forEach(el => {
            el.addEventListener('click', (e) => {
                document.querySelectorAll('.shape-option').forEach(opt => opt.classList.remove('selected'));
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
        document.getElementById('how-to-play-btn')?.addEventListener('click', () => this.showScreen('how-to-play'));
        document.getElementById('legends-btn')?.addEventListener('click', () => {
            this.populateLegends();
            this.showScreen('legends');
        });
        document.getElementById('credits-btn')?.addEventListener('click', () => this.showScreen('credits'));

        // Back Buttons
        document.querySelectorAll('.back-btn').forEach(b => {
            b.addEventListener('click', () => this.showScreen('start'));
        });

        document.getElementById('menu-btn')?.addEventListener('click', () => {
            location.reload();
        });

        const closeLowBalance = document.getElementById('close-low-balance');
        if (closeLowBalance) {
            closeLowBalance.addEventListener('click', () => {
                this.hideLowBalanceModal();
            });
        }

        this.setupJoystick();
    }

    setupJoystick() {
        const zone = document.getElementById('joystick-zone');
        const knob = document.getElementById('joystick-knob');
        if (!zone || !knob) return;

        this.joystick = { active: false, x: 0, y: 0 };

        let startX, startY;

        const handleStart = (clientX, clientY) => {
            if (this.onInteractionStart) this.onInteractionStart();
            this.joystick.active = true;
            startX = clientX;
            startY = clientY;
            knob.style.transition = 'none';
        };

        const handleMove = (clientX, clientY) => {
            if (!this.joystick.active) return;
            const maxDist = 40;
            let dx = clientX - startX;
            let dy = clientY - startY;
            const dist = Math.sqrt(dx * dx + dy * dy);

            if (dist > maxDist) {
                dx = (dx / dist) * maxDist;
                dy = (dy / dist) * maxDist;
            }

            knob.style.transform = `translate(${dx}px, ${dy}px)`;
            this.joystick.x = dx / maxDist;
            this.joystick.y = dy / maxDist;
        };

        const handleEnd = () => {
            this.joystick.active = false;
            this.joystick.x = 0;
            this.joystick.y = 0;
            knob.style.transform = `translate(0px, 0px)`;
            knob.style.transition = 'transform 0.2s';
        };

        zone.addEventListener('mousedown', e => handleStart(e.clientX, e.clientY));
        window.addEventListener('mousemove', e => handleMove(e.clientX, e.clientY));
        window.addEventListener('mouseup', handleEnd);

        zone.addEventListener('touchstart', e => {
            e.preventDefault();
            handleStart(e.touches[0].clientX, e.touches[0].clientY);
        }, { passive: false });
        zone.addEventListener('touchmove', e => {
            e.preventDefault();
            handleMove(e.touches[0].clientX, e.touches[0].clientY);
        }, { passive: false });
        zone.addEventListener('touchend', handleEnd);
    }

    bindStartGame(cb) { this.onStartGame = cb; }
    bindPauseGame(cb) { document.getElementById('pause-btn')?.addEventListener('click', cb); }
    bindResumeGame(cb) { document.getElementById('resume-btn')?.addEventListener('click', cb); }
    bindRestartGame(cb) { document.getElementById('restart-btn')?.addEventListener('click', cb); }
    bindQuitGame(cb) { document.getElementById('quit-btn')?.addEventListener('click', cb); }

    showScreen(screenName) {
        // Hide all screens
        Object.values(this.dom).forEach(el => {
            if (el && el.classList?.contains('screen')) el.classList.add('hidden');
        });
        this.dom.hud.classList.add('hidden');
        this.dom.gameContainer.classList.add('hidden');

        if (screenName === 'game') {
            this.dom.hud.classList.remove('hidden');
            this.dom.gameContainer.classList.remove('hidden');
        } else if (screenName === 'start') {
            this.dom.start.classList.remove('hidden');
            this.updateMenuBalance();
        } else if (screenName === 'how-to-play') {
            this.dom.howToPlay.classList.remove('hidden');
        } else if (screenName === 'legends') {
            this.dom.legends.classList.remove('hidden');
        } else if (screenName === 'credits') {
            this.dom.credits.classList.remove('hidden');
        } else if (screenName === 'game-over') {
            this.dom.gameOver.classList.remove('hidden');
        }
    }

    updateHUD(data) {
        if (data.score !== undefined) document.getElementById('score-display').innerText = data.score;
        if (data.time !== undefined) document.getElementById('timer-display').querySelector('span').innerText = data.time;
        if (data.health !== undefined) document.getElementById('health-display').innerText = Math.max(0, Math.floor(data.health));
    }

    showGameOver(result) {
        this.showScreen('game-over');

        const title = document.getElementById('result-title');
        const icon = document.getElementById('result-icon');
        const msg = document.getElementById('result-message');

        if (result.success) {
            title.textContent = "MISSION ACCOMPLISHED";
            title.style.color = "#00ff88";
            icon.textContent = "💎";
        } else {
            title.textContent = "MISSION FAILED";
            title.style.color = "#da3633";
            icon.textContent = "💀";
        }
        msg.textContent = result.message;
        document.getElementById('final-score').textContent = result.score;
        document.getElementById('time-taken').textContent = result.time;
    }

    showPauseMenu() {
        this.dom.pause.classList.remove('hidden');
    }

    hidePauseMenu() {
        this.dom.pause.classList.add('hidden');
    }

    populateLegends() {
        const tbody = document.getElementById('legends-body');
        const msg = document.getElementById('no-legends-msg');
        if (!tbody) return;

        tbody.innerHTML = '';

        const scores = JSON.parse(localStorage.getItem('ahirs_treasure_scores') || '[]');

        if (scores.length === 0) {
            msg.style.display = 'block';
            return;
        }
        msg.style.display = 'none';

        scores.sort((a, b) => b.score - a.score).slice(0, 10).forEach((s, i) => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>#${i + 1}</td>
                <td>${s.name}</td>
                <td>${s.score}</td>
                <td>${s.win ? '🏆' : '💀'}</td>
            `;
            tbody.appendChild(tr);
        });
    }

    updateMenuBalance() {
        if (this.dom.coinBalance) {
            this.dom.coinBalance.innerText = this.economy.getBalance();
        }
    }

    showLowBalanceModal() {
        if (this.dom.lowBalance) this.dom.lowBalance.classList.remove('hidden');
    }

    hideLowBalanceModal() {
        if (this.dom.lowBalance) this.dom.lowBalance.classList.add('hidden');
    }

    showHint(msg) {
        const hintEl = document.createElement('div');
        hintEl.className = 'llm-hint';
        hintEl.style.position = 'absolute';
        hintEl.style.top = '10%';
        hintEl.style.left = '50%';
        hintEl.style.transform = 'translateX(-50%)';
        hintEl.style.background = 'rgba(0, 255, 136, 0.9)';
        hintEl.style.color = '#000';
        hintEl.style.padding = '10px 20px';
        hintEl.style.borderRadius = '5px';
        hintEl.style.zIndex = '1100';
        hintEl.style.fontWeight = 'bold';
        hintEl.style.boxShadow = '0 0 15px rgba(0, 255, 136, 0.5)';
        hintEl.style.borderLeft = '5px solid #000';
        hintEl.innerHTML = `<span style="font-size: 1.2em; margin-right: 10px;">💡</span> ${msg}`;
        
        document.body.appendChild(hintEl);

        setTimeout(() => {
            hintEl.style.opacity = '0';
            hintEl.style.transition = 'opacity 0.5s ease';
            setTimeout(() => hintEl.remove(), 500);
        }, 4000);
    }
}
