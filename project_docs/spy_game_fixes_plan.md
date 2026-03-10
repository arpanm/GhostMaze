# Implementation Plan - Low Balance Check for AhirsSpy

The goal is to prevent the game from starting if the user has 0 coins and prompt them to visit the Academy to earn more.

## User Review Required
> [!IMPORTANT]
> I will assume the minimum required balance is > 0. If there is a specific entry fee (e.g. 10 coins), please verify logic in `main.js`. currently strict `balance <= 0` check will be used as requested.

## Proposed Changes

### AhirsSpy

#### [MODIFY] [index.html](file:///Users/arpan1.mukherjee/code/GhostMaze/AhirsSpy/index.html)
- Add the `low-balance-modal` HTML structure at the end of the body, similar to `AhirsSnakeAndLadder`.

#### [MODIFY] [js/ui.js](file:///Users/arpan1.mukherjee/code/GhostMaze/AhirsSpy/js/ui.js)
- Update `constructor` to cache `low-balance-modal` and its close button.
- Add `showLowBalanceModal()` and `hideLowBalanceModal()` methods.
- Bind the close button event in `bindEvents` or `constructor`.

#### [MODIFY] [js/main.js](file:///Users/arpan1.mukherjee/code/GhostMaze/AhirsSpy/js/main.js)
- Update the `ui.bindStartGame` callback.
- Before calling `game.start()`, check `economy.getBalance()`.
- If `balance <= 0`, call `ui.showLowBalanceModal()`.
- Otherwise, proceed with `game.start()`.

### Mission Failed Details

#### [MODIFY] [js/game.js](file:///Users/arpan1.mukherjee/code/GhostMaze/AhirsSpy/js/game.js)
- Update `gameOver` method.
- When calling `this.onGameOver`, pass an object containing `success`, `message`, and `killerDetails` (if failed).
- `killerDetails` should include `avatar`, `occupation`, and a clue/trait.

#### [MODIFY] [js/ui.js](file:///Users/arpan1.mukherjee/code/GhostMaze/AhirsSpy/js/ui.js)
- Update `showGameOver(result)` method.
- Check if `result.success` is false.
- If false and `result.killerDetails` is present, display a new section in the Game Over screen showing the killer's avatar and traits.
- If true, hide this section.

#### [MODIFY] [index.html](file:///Users/arpan1.mukherjee/code/GhostMaze/AhirsSpy/index.html)
- Add a container in the `#game-over-screen` to display the "Killer Identity" section.
- This container will be populated dynamically by `ui.js`.

## Verification Plan

### Manual Verification
1.  **Set Low Balance**: Manually set `localStorage.setItem('ahir_coin_balance', '0')` in the browser console (or via code temporary).
2.  **Try to Start**: Click the "Start Game" button.
3.  **Expectation**: The "Low Balance" modal should appear. Game should NOT start.
4.  **Check Links**: Click "Go to Academy" button in modal; should navigate to Academy.
5.  **Check Close**: Click "Close" button; modal should close.
6.  **Set High Balance**: Set balance to 100.
7.  **Try to Start**: Click "Start Game".
8.  **Expectation**: Game starts normally.
