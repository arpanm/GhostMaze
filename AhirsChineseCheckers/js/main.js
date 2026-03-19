import { Game } from './game.js';
import { UIManager } from './ui.js';
import { Economy } from './economy.js';

window.addEventListener('load', () => {
    const economy = new Economy();
    const ui = new UIManager(economy);
    const game = new Game(ui, economy);

    ui.bindStartGame((config) => {
        if (economy.spendCoins(10, 'Chinese Checkers Mission')) {
            ui.showScreen('hud');
            game.start(config);
            ui.updateMenuBalance(economy.getBalance());
        } else {
            ui.showLowBalance();
        }
    });

    // Handle Clicks
    const canvas = document.getElementById('game-canvas');
    canvas.addEventListener('click', (e) => {
        const rect = canvas.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        game.handleClick(x, y);
    });

    // Initial Balance
    ui.updateMenuBalance(economy.getBalance());
});
