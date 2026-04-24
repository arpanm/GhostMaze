import { Economy } from './economy.js';
import { UIManager } from './ui.js';
import { Game } from './game.js';

window.addEventListener('load', () => {
    // Initialize Economy
    const economy = new Economy();

    // Initialize UI
    const ui = new UIManager(economy);

    // Initialize Game Engine
    const game = new Game(ui, economy);

    // Bind UI actions to Game Engine
    ui.bindStartGame((config) => {
        const cost = 10;
        if (!economy.hasEnoughBalance(cost)) {
            ui.showLowBalanceModal();
            return;
        }
        
        if (economy.spendCoins(cost, "Started Treasure Hunt Mission")) {
            ui.updateMenuBalance();
            game.start(config);
        }
    });

    ui.bindPauseGame(() => game.togglePause());
    ui.bindResumeGame(() => game.togglePause());
    
    ui.bindRestartGame(() => {
        // Simple restart logic by reloading the page so it goes back to menu to take coins
        location.reload();
    });

    // Setup initial state
    ui.updateMenuBalance();
});
