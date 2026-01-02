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
            playerLogo: document.getElementById('player-logo-display'),
        };
    }

    updatePlayerLogo(logo) {
        if (this.elements.playerLogo) this.elements.playerLogo.textContent = logo;
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

    updateGameOverScreen(kills, combatScore, survivalBonus, economyBonus, totalScore) {
        this.elements.finalKills.textContent = `${kills} (${combatScore} PTS)`; // Show both kills and the points from them
        this.elements.finalSurvival.textContent = survivalBonus;
        this.elements.finalEconomy.textContent = economyBonus;
        this.elements.finalTotal.textContent = totalScore;

        this.updateLeaderboard(totalScore);
    }

    updateLeaderboard(currentScore, containerId = 'leaderboard-list') {
        const key = 'AhirsWarZone_Leaderboard';
        let scores = [];
        try {
            scores = JSON.parse(localStorage.getItem(key) || '[]');
        } catch (e) {
            console.error("Leaderboard Parse Error", e);
            scores = [];
        }

        // Display
        const container = document.getElementById(containerId);
        if (!container) {
            console.warn(`Leaderboard container #${containerId} not found`);
            return;
        }

        container.innerHTML = '';
        if (scores.length === 0) {
            container.innerHTML = '<p style="text-align:center; padding:10px; color:#bdc3c7;">No Records Yet. Play a mission!</p>';
        } else {
            scores.sort((a, b) => b.score - a.score).slice(0, 10).forEach((entry, i) => {
                const row = document.createElement('div');
                row.className = 'leaderboard-row';
                row.style.display = 'flex';
                row.style.justifyContent = 'space-between';
                row.style.padding = '8px';
                row.style.borderBottom = '1px solid rgba(255,255,255,0.1)';
                row.style.fontSize = '0.9em';

                row.innerHTML = `
                    <span><span style="color:#f1c40f; width:20px; display:inline-block;">#${i + 1}</span> ${entry.logo} ${entry.name} <span style="font-size:0.8em; color:#95a5a6;">(${entry.diff.toUpperCase()})</span></span>
                    <span>${entry.score}</span>
                `;
                container.appendChild(row);
            });
        }
    }
}
