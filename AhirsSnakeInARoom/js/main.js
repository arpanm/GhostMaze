import { Game } from './game.js';

const screens = {
    start: document.getElementById('start-screen'),
    gameHUD: document.getElementById('game-hud'),
    pause: document.getElementById('pause-screen'),
    gameOver: document.getElementById('game-over-screen'),
    howToPlay: document.getElementById('how-to-play-screen'),
    leaderboard: document.getElementById('leaderboard-screen'),
    credits: document.getElementById('credits-screen'),
    controls: document.getElementById('controls-layer')
};

const game = new Game('game-canvas');

// Game Config
const state = {
    playerName: '',
    color: '#00ff00',
    playerName: '',
    color: '#00ff00',
    logo: '🐍',
    difficulty: 'easy'
};

// --- Event Listeners ---

// Color Picker
document.querySelectorAll('.color-opt').forEach(opt => {
    opt.addEventListener('click', () => {
        document.querySelectorAll('.color-opt').forEach(c => c.classList.remove('active'));
        opt.classList.add('active');
        state.color = opt.dataset.color;
    });
});

// Logo Picker
document.querySelectorAll('.logo-opt').forEach(opt => {
    opt.addEventListener('click', () => {
        document.querySelectorAll('.logo-opt').forEach(l => l.classList.remove('active'));
        opt.classList.add('active');
        state.logo = opt.dataset.logo;
    });
});

// Difficulty Selector
document.querySelectorAll('.diff-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        document.querySelectorAll('.diff-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        state.difficulty = btn.dataset.diff;
    });
});

// Start Button
document.getElementById('start-btn').addEventListener('click', () => {
    const nameInput = document.getElementById('player-name');
    const nameError = document.getElementById('name-error');

    if (!nameInput.value.trim()) {
        nameError.classList.remove('hidden');
        return;
    }
    nameError.classList.add('hidden');
    state.playerName = nameInput.value.trim();

    startGame();
});

// Navigation
document.getElementById('how-to-play-btn').addEventListener('click', () => showScreen(screens.howToPlay));
document.getElementById('back-from-guide-btn').addEventListener('click', () => showScreen(screens.start));

document.getElementById('leaderboard-btn').addEventListener('click', () => {
    updateLeaderboardView();
    showScreen(screens.leaderboard);
});
document.getElementById('back-to-start-btn').addEventListener('click', () => showScreen(screens.start));
document.getElementById('clear-leaderboard-btn').addEventListener('click', () => {
    localStorage.removeItem('snake_room_leaderboard');
    updateLeaderboardView();
});

document.getElementById('credits-btn').addEventListener('click', () => showScreen(screens.credits));
document.getElementById('back-from-credits-btn').addEventListener('click', () => showScreen(screens.start));

// Pause
document.getElementById('pause-btn').addEventListener('click', () => {
    game.pause();
    document.getElementById('pause-score-display').textContent = `Current Score: ${game.score}`;
    screens.pause.classList.remove('hidden');
});
document.getElementById('resume-btn').addEventListener('click', () => {
    screens.pause.classList.add('hidden');
    game.resume();
});
document.getElementById('restart-pause-btn').addEventListener('click', () => {
    screens.pause.classList.add('hidden');
    startGame();
});
document.getElementById('abandon-btn').addEventListener('click', () => {
    screens.pause.classList.add('hidden');
    saveScore(game.score, game.kills); // Save score on exit
    showScreen(screens.start);
    screens.gameHUD.classList.add('hidden');
    screens.controls.classList.add('hidden');
});

// Game Over Actions
document.getElementById('restart-btn').addEventListener('click', startGame);
document.getElementById('menu-btn').addEventListener('click', () => showScreen(screens.start));


function showScreen(screen) {
    Object.values(screens).forEach(s => s.classList.add('hidden'));
    screen.classList.remove('hidden');
}

function startGame() {
    showScreen(screens.gameHUD);
    // Show screens overlay
    // But gameHUD needs to be visible over canvas.
    // Actually our css hides everything "screen" except the one active.
    // game-canvas is always behind.
    // We need gameHUD and controls-layer visible
    screens.gameHUD.classList.remove('hidden');
    screens.controls.classList.remove('hidden');

    // Update HUD
    document.getElementById('user-name-disp').textContent = state.playerName;
    document.getElementById('user-name-disp').style.color = state.color;

    game.init({
        name: state.playerName,
        color: state.color,
        logo: state.logo,
        difficulty: state.difficulty
    });
}

// Bind Game Callbacks
game.bindUI({
    onScoreUpdate: (score, kills) => {
        document.getElementById('user-score-val').textContent = score;
    },
    onGameOver: (result) => {
        screens.gameHUD.classList.add('hidden');
        screens.controls.classList.add('hidden');
        screens.gameOver.classList.remove('hidden');

        document.getElementById('game-over-title').textContent = result.win ? "WIN: ROOM CLEARED!" : "LOST: GAME OVER";
        document.getElementById('game-over-reason').textContent = result.reason;

        document.getElementById('breakdown-insects').textContent = result.insects * 10;
        document.getElementById('breakdown-kills').textContent = result.kills * 100;
        document.getElementById('breakdown-circle').textContent = result.score - (result.insects * 10 + result.kills * 100);
        document.getElementById('total-score').textContent = result.score;

        saveScore(result.score, result.kills);
    }
});

function saveScore(score, kills) {
    const entry = {
        name: state.playerName,
        color: state.color,
        logo: state.logo,
        difficulty: state.difficulty,
        score: score,
        scoreData: {
            kills: kills,
            insects: game.insectsEaten || 0,
            bonus: (score - (game.insectsEaten * 10 + kills * 100))
        },
        date: new Date().toLocaleDateString()
    };

    let lb = JSON.parse(localStorage.getItem('snake_room_leaderboard') || '[]');
    lb.push(entry);
    lb.sort((a, b) => b.score - a.score);
    lb = lb.slice(0, 10);
    localStorage.setItem('snake_room_leaderboard', JSON.stringify(lb));
}

function updateLeaderboardView() {
    const lb = JSON.parse(localStorage.getItem('snake_room_leaderboard') || '[]');
    const tbody = document.getElementById('leaderboard-body');
    tbody.innerHTML = '';

    if (lb.length === 0) {
        tbody.innerHTML = '<tr><td colspan="4" style="text-align:center">No Records Yet</td></tr>';
        return;
    }

    lb.forEach((entry, index) => {
        const row = document.createElement('tr');

        // Handle legacy data
        const logo = entry.logo || '🐍';
        const color = entry.color || '#00ff00';
        const diff = entry.difficulty ? entry.difficulty.toUpperCase() : 'NORMAL';
        const insects = entry.scoreData ? entry.scoreData.insects : '?';
        const kills = entry.scoreData ? entry.scoreData.kills : (entry.kills || '?');
        const bonus = entry.scoreData ? entry.scoreData.bonus : 0;

        row.innerHTML = `
            <td>#${index + 1}</td>
            <td>
                <div style="display:flex; flex-direction:column; align-items:center; font-size:0.8rem; color:#aaa;">
                    <span style="font-size:1.2rem; filter: drop-shadow(0 0 5px ${color});">${logo}</span>
                    <span>${entry.name}</span>
                    <span>${diff}</span>
                </div>
            </td>
            <td>
                <div style="display:flex; flex-direction:column; font-size:0.8rem; color:#aaa;">
                    <span>🐞 Food: ${insects}</span>
                    <span>☠️ Kills: ${kills}</span>
                    <span>🏆 Bonus: ${bonus}</span>
                </div>
            </td>
            <td style="color: var(--primary-color); font-weight:bold; font-size:1.1rem;">${entry.score}</td>
        `;
        tbody.appendChild(row);
    });
}

// Initial
showScreen(screens.start);
