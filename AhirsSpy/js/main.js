
import { Game } from './game.js';
import { UIManager } from './ui.js';
import { Economy } from './economy.js';

window.addEventListener('load', () => {
    // Initialize Economy
    const economy = new Economy(); // Reuse or duplicate Logic from other games

    // Initialize UI
    const ui = new UIManager(economy);

    // Initialize Game engine
    const game = new Game(ui, economy);

    // Bind UI Loop to Game Loop
    ui.bindStartGame((config) => {
        if (economy.getBalance() <= 0) {
            ui.showLowBalanceModal();
            return;
        }
        game.start(config);
    });
    ui.bindPauseGame(() => game.togglePause());
    ui.bindResumeGame(() => game.togglePause()); // Resume is also toggle
    ui.bindRestartGame(() => game.restart());
    ui.bindQuitGame(() => location.reload()); // Simple reload for main menu for now

    game.bindUI(ui); // Bind Q&A Logic
    ui.bindInteract(() => game.interact());

    game.setGameOverCallback((result) => ui.showGameOver(result));

    // Expose for LLM Service status updates
    window.app = {
        updateLoadingStatus: (status) => {
            console.log(`[AhirsSpy] AI Status: ${status}`);
            // Don't show notifications for background loading to avoid noise
        }
    };

    // Update Menu Balance on Load
    ui.updateMenuBalance();

    // Populate Carousel
    ui.populateCarousel();
});
