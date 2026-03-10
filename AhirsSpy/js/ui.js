export class UIManager {
    constructor(economy) {
        this.economy = economy;
        this.dom = {
            start: document.getElementById('start-screen'),
            hud: document.getElementById('game-hud'),
            gameOver: document.getElementById('game-over-screen'),
            pause: document.getElementById('pause-screen'),
            dialog: document.getElementById('dialog-modal'),
            coinBalance: document.getElementById('menu-coin-balance'),
            lowBalance: document.getElementById('low-balance-modal'),
            carousel: document.getElementById('other-games-carousel'),
            howToPlay: document.getElementById('how-to-play-screen'),
            legends: document.getElementById('legends-screen'),
            credits: document.getElementById('credits-screen'),
            lowBalance: document.getElementById('low-balance-modal'),
            killerReveal: document.getElementById('killer-reveal-section'),
            killerAvatar: document.getElementById('killer-reveal-avatar'),
            killerIdentity: document.getElementById('killer-reveal-identity'),
            killerClue: document.getElementById('killer-reveal-clue')
        };

        this.setupEventListeners();
        this.populateCarousel();
    }

    // Dialog System
    openDialog(person) {
        if (person.isDead) return;
        this.dom.dialog.classList.remove('hidden');

        let title = "Suspect";
        if (person.type === 'OWNER') title = "Home Owner";
        if (person.type === 'CIVILIAN') title = "Guest";

        document.getElementById('dialog-name').innerText = title;
        document.getElementById('dialog-avatar').innerText = person.avatar;

        const remaining = person.maxQuestions - person.questionsAnswered;
        document.getElementById('dialog-text').innerText = `Hello... can I help? (${remaining} questions left)`;

        const optionsContainer = document.getElementById('dialog-options');
        optionsContainer.innerHTML = '';

        if (remaining <= 0) {
            document.getElementById('dialog-text').innerText = "I've told you everything I know!";
            return;
        }

        // Questions Pool
        const questions = [
            { id: 'suspect', text: 'Did you see anyone suspicious?' },
            { id: 'location', text: 'Where were you recently?' },
            { id: 'killer', text: 'Who do you think is the Killer?' },
            { id: 'hat', text: 'Did you see someone with a Hat?' },
            { id: 'glasses', text: 'Did you see someone with Glasses?' }
        ];

        questions.forEach(q => {
            const btn = document.createElement('button');
            btn.className = 'dialog-option-btn';
            btn.innerText = q.text;
            btn.onclick = () => {
                this.handleQuestion(person, q);
            };
            optionsContainer.appendChild(btn);
        });
    }

    handleQuestion(person, question) {
        if (person.questionsAnswered >= person.maxQuestions) return;

        person.questionsAnswered++;
        // Deduct score/coin if needed via callback, or just logic
        // TODO: Callback for score penalty

        const answer = this.generateAnswer(person, question);
        document.getElementById('dialog-text').innerText = `"${answer}"`;

        // Remove options after asking one (to prevent spamming same interaction?)
        // Or refresh list. For now, let's keep it open but update count.
        const remaining = person.maxQuestions - person.questionsAnswered;
        if (remaining <= 0) {
            document.getElementById('dialog-options').innerHTML = ''; // Clear options
        } else {
            document.getElementById('dialog-text').innerText += `\n\n(rem: ${remaining})`;
        }
    }

    generateAnswer(person, question) {
        // Simple Logic for now
        // Real logic needs access to Game State (who is killer, etc.)
        // This probably should be in Game.js, not UI.js. 
        // But UI has the reference. Let's delegate.
        if (this.onAskQuestion) {
            return this.onAskQuestion(person, question.id);
        }
        return "I'm not sure...";
    }

    bindAskQuestion(cb) { this.onAskQuestion = cb; }

    bindInteract(cb) {
        const hint = document.getElementById('action-hint');
        const talkBtn = document.getElementById('talk-btn');
        if (hint) hint.addEventListener('click', cb);
        if (talkBtn) talkBtn.addEventListener('click', cb);

        // Make hint clickable
        if (hint) hint.style.cursor = 'pointer';
    }

    closeDialog() {
        this.dom.dialog.classList.add('hidden');
    }

    showInteractHint(active, avatar) {
        const hint = document.getElementById('action-hint');
        const talkBtn = document.getElementById('talk-btn');

        if (active) {
            if (hint) {
                hint.innerHTML = `Talk to ${avatar} <span style="font-size:0.8em">(Space/Click)</span>`;
                hint.style.display = 'block';
                hint.style.background = 'rgba(0, 255, 136, 0.2)';
                hint.style.border = '1px solid #00ff88';
            }
            if (talkBtn) talkBtn.classList.remove('hidden');
        } else {
            if (hint) {
                hint.innerHTML = 'Walk up to someone to interact';
                hint.style.background = 'rgba(0,0,0,0.5)';
                hint.style.border = 'none';
            }
            if (talkBtn) talkBtn.classList.add('hidden');
        }
    }

    showNotification(msg) {
        // Simple toast or reuse hint?
        // Let's create a toast element dynamically or reuse hint
        const toast = document.createElement('div');
        toast.style.position = 'absolute';
        toast.style.top = '20%';
        toast.style.left = '50%';
        toast.style.transform = 'translate(-50%, -50%)';
        toast.style.background = 'rgba(0,0,0,0.8)';
        toast.style.color = 'white';
        toast.style.padding = '10px 20px';
        toast.style.borderRadius = '20px';
        toast.style.zIndex = '1000';
        toast.style.border = '1px solid white';
        toast.innerText = msg;
        document.body.appendChild(toast);

        // Remove after 2s
        setTimeout(() => {
            toast.remove();
        }, 2000);
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

            this.onStartGame({ name, avatar, difficulty });

            // showHUD is called by Game.start usually, but we can prevent double call or just rely on Game.js
            // Game.js calls this.ui.showHUD() which we need to implement.
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
        document.getElementById('how-to-play-btn').addEventListener('click', () => this.showScreen('how-to-play'));
        document.getElementById('legends-btn').addEventListener('click', () => {
            this.populateLegends();
            this.showScreen('legends');
        });
        document.getElementById('credits-btn').addEventListener('click', () => this.showScreen('credits'));

        // Back Buttons
        document.querySelectorAll('.back-btn').forEach(b => {
            b.addEventListener('click', () => this.showScreen('start'));
        });

        // Pause/Game Over Buttons
        document.getElementById('resume-btn').addEventListener('click', () => {
            // Handled by bindResumeGame, but good to have safeguard or remove duplicate?
            // Main.js binds it.
        });
        document.getElementById('menu-btn').addEventListener('click', () => {
            // Reload page or properly reset? Main.js handles quit.
            // We can trigger the bound quit callback.
            // But simpler:
            location.reload();
        });

        document.getElementById('close-low-balance').addEventListener('click', () => {
            this.dom.lowBalance.classList.add('hidden');
        });

        document.getElementById('close-dialog-btn').addEventListener('click', () => this.closeDialog());

        const closeLowBalance = document.getElementById('close-low-balance');
        if (closeLowBalance) {
            closeLowBalance.addEventListener('click', () => {
                this.hideLowBalanceModal();
            });
        }

        // Joystick Logic
        this.setupJoystick();
    }

    showLowBalanceModal() {
        if (this.dom.lowBalance) this.dom.lowBalance.classList.remove('hidden');
    }

    hideLowBalanceModal() {
        if (this.dom.lowBalance) this.dom.lowBalance.classList.add('hidden');
    }

    showHUD() {
        this.showScreen('hud');
    }

    setupJoystick() {
        const zone = document.getElementById('joystick-zone');
        const knob = document.getElementById('joystick-knob');
        if (!zone || !knob) return;

        this.joystick = { active: false, x: 0, y: 0 };

        let startX, startY;

        const handleStart = (clientX, clientY) => {
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
    bindPauseGame(cb) { document.getElementById('pause-btn').addEventListener('click', cb); }
    bindResumeGame(cb) { document.getElementById('resume-btn').addEventListener('click', cb); }
    bindRestartGame(cb) { document.getElementById('restart-btn').addEventListener('click', cb); }
    bindQuitGame(cb) { document.getElementById('quit-btn').addEventListener('click', cb); }

    showScreen(screenName) {
        // Hide all screens
        Object.values(this.dom).forEach(el => {
            if (el && el.classList.contains('screen')) el.classList.add('hidden');
        });
        this.dom.hud.classList.add('hidden');
        this.dom.gameOver.classList.add('hidden');

        if (screenName === 'hud') {
            this.dom.hud.classList.remove('hidden');
        } else if (screenName === 'start') {
            this.dom.start.classList.remove('hidden');
            this.updateMenuBalance();
        } else if (screenName === 'how-to-play') {
            this.dom.howToPlay.classList.remove('hidden');
        } else if (screenName === 'legends') {
            this.dom.legends.classList.remove('hidden');
        } else if (screenName === 'credits') {
            this.dom.credits.classList.remove('hidden');
        }
    }

    updateHUD(data) {
        document.getElementById('score-display').innerText = data.score;
        document.getElementById('timer-display').querySelector('span').innerText = data.time;
    }

    showGameOver(result) {
        this.dom.hud.classList.add('hidden');
        this.dom.gameOver.classList.remove('hidden');

        const title = document.getElementById('result-title');
        const icon = document.getElementById('result-icon');
        const msg = document.getElementById('result-message');

        if (result.success) {
            title.textContent = "MISSION ACCOMPLISHED";
            title.style.color = "#00ff88";
            icon.textContent = "🏆";
            if (this.dom.killerReveal) this.dom.killerReveal.classList.add('hidden');
        } else {
            title.textContent = "MISSION FAILED";
            title.style.color = "#da3633";
            icon.textContent = "💀";

            // Show Killer Reveal
            if (this.dom.killerReveal && result.killerDetails) {
                this.dom.killerReveal.classList.remove('hidden');
                this.dom.killerAvatar.textContent = result.killerDetails.avatar || '❓';
                this.dom.killerIdentity.textContent = result.killerDetails.occupation || 'Unknown';
                this.dom.killerClue.textContent = result.killerDetails.clue ? `"${result.killerDetails.clue}"` : '';
            }
        }
        msg.textContent = result.message;
        document.getElementById('final-score').textContent = result.score;
        document.getElementById('time-bonus').textContent = result.timeBonus || 0;
    }

    showPauseMenu() {
        this.dom.pause.classList.remove('hidden');
    }

    populateLegends() {
        const tbody = document.getElementById('legends-body');
        const msg = document.getElementById('no-legends-msg');
        if (!tbody) return;

        tbody.innerHTML = '';

        // Fetch from LocalStorage
        const scores = JSON.parse(localStorage.getItem('ahirs_spy_scores') || '[]');

        if (scores.length === 0) {
            msg.style.display = 'block';
            return;
        }
        msg.style.display = 'none';

        scores.forEach((s, i) => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>#${i + 1}</td>
                <td>Agent</td>
                <td>${s.score}</td>
                <td>${s.win ? '🏆' : '💀'}</td>
            `;
            tbody.appendChild(tr);
        });
    }

    hidePauseMenu() { this.dom.pause.classList.add('hidden'); }

    updateMenuBalance() {
        this.dom.coinBalance.innerText = this.economy.getBalance();
    }

    showLowBalance() {
        this.dom.lowBalance.classList.remove('hidden');
    }

    populateCarousel() {
        // List of other games
        const games = [
            { name: "Ghost Maze", icon: "👻", link: "../AhirsGhostMaze/index.html" },
            { name: "Snake Room", icon: "🐍", link: "../AhirsSnakeInARoom/index.html" },
            { name: "Shark Race", icon: "🦈", link: "../AhirSharkRace/index.html" },
            { name: "Shooting", icon: "🔫", link: "../AhirsShootingBattle/index.html" },
            { name: "War Zone", icon: "⚔️", link: "../AhirsWarZone/index.html" },
            { name: "Chess", icon: "♟", link: "../AhirsChess/index.html" },
            { name: "Snake & Ladder", icon: "🎲", link: "../AhirsSnakeAndLadder/index.html" },
            { name: "Bike Race", icon: "🚲", link: "../AhirsBikeRace/index.html" }
        ];

        const container = this.dom.carousel;
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
