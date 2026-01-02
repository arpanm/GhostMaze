export class UIManager {
    constructor() {
        this.elements = {
            score: document.getElementById('score-display'),
            pHealth: document.getElementById('player-health-bar'),
            eHealth: document.getElementById('enemy-health-bar'),
            windForce: document.getElementById('wind-force'),
            windArrow: document.getElementById('wind-arrow'),
            shopCurrency: document.getElementById('shop-currency'),

            // Pause/End details
            pauseScore: document.getElementById('pause-score'),
            pauseKills: document.getElementById('pause-kills'),

            finalKills: document.getElementById('final-kills'),
            finalSurvival: document.getElementById('final-survival'),
            finalEconomy: document.getElementById('final-economy'),
            finalTotal: document.getElementById('final-total'),
            leaderboardList: document.getElementById('leaderboard-list'),
        };
    }

    showScreen(screenId) {
        document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
        const screen = document.getElementById(screenId);
        if (screen) screen.classList.add('active');

        const hud = document.getElementById('hud');
        if (screenId === 'hud') {
            hud.style.display = 'flex'; // Ensure flex for HUD
        } else {
            // HUD is effectively hidden by z-index or opacity usually, but let's be explicit if needed
            // Actually CSS handles .active for screens. HUD has special handling? 
            // In style.css, #hud matches .screen, so .active works.
            // But we might want to ensure it's hidden if not active
        }
    }


    updateHUD(score, pHealth, eHealth, wind, currency) {
        this.elements.score.textContent = `${score} PTS`;
        this.elements.pHealth.style.width = `${Math.max(0, pHealth)}%`;
        this.elements.eHealth.style.width = `${Math.max(0, eHealth)}%`;
        this.elements.shopCurrency.textContent = currency;

        // Wind Update
        this.elements.windForce.textContent = Math.abs(wind.toFixed(1));
        const rotation = wind > 0 ? 0 : 180;
        this.elements.windArrow.style.transform = `rotate(${rotation}deg)`;
    }

    updatePauseScreen(score, kills) {
        this.elements.pauseScore.textContent = score;
        this.elements.pauseKills.textContent = kills;
    }

    updateGameOverScreen(kills, survivalBonus, economyBonus, totalScore) {
        this.elements.finalKills.textContent = kills;
        this.elements.finalSurvival.textContent = survivalBonus;
        this.elements.finalEconomy.textContent = economyBonus;
        this.elements.finalTotal.textContent = totalScore;

        this.updateLeaderboard(totalScore);
    }

    updateLeaderboard(currentScore) {
        // Load from LocalStorage
        const key = 'AhirsWarZone_Leaderboard';
        let scores = JSON.parse(localStorage.getItem(key) || '[]');

        // Display
        this.elements.leaderboardList.innerHTML = '';
        if (scores.length === 0) {
            this.elements.leaderboardList.innerHTML = '<p>No Records Yet. Be the first!</p>';
        } else {
            scores.sort((a, b) => b.score - a.score).slice(0, 5).forEach((entry, i) => {
                const row = document.createElement('div');
                row.className = 'leaderboard-row';
                row.style.display = 'flex';
                row.style.justifyContent = 'space-between';
                row.style.padding = '5px';
                row.style.borderBottom = '1px solid #555';

                row.innerHTML = `
                    <span>#${i + 1} ${entry.logo} ${entry.name}</span>
                    <span>${entry.score} pts (${entry.diff})</span>
                `;
                this.elements.leaderboardList.appendChild(row);
            });
        }
    }
}
