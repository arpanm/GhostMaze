# Implementation Plan - Ahirs Snake & Ladder

## Goal Description
Build a dynamic, "ultra fun" Snake & Ladder game.
Features:
- **Procedural Board**: Every game has unique snake/ladder positions.
- **Visuals**: Canvas-based rendering for smooth animations (snakes breathing/wiggling).
- **Audio/FX**: Rich sensory feedback.
- **System**: Standard project integration (Scores, Credits, Cross-linking).

## User Review Required
> [!NOTE]
> - **Visual Style**: We will use a neon/dark theme consistent with other "Ahirs" games (WarZone/SharkRace) but with vibrant board colors.
> - **Snakes**: Will be procedurally drawn using Bézier curves on Canvas to allow them to "wiggle".
> - **Dice**: A 3D CSS cube animation for the rolling effect.

## Proposed Changes

### Structure
New Directory: `AhirsSnakeAndLadder`

### Files

#### [NEW] [index.html](file:///Users/arpan1.mukherjee/code/GhostMaze/AhirsSnakeAndLadder/index.html)
- Canvas container.
- UI Overlays: Start Screen (Name/Color), HUD (Dice, Log), Win Modal.

#### [NEW] [style.css](file:///Users/arpan1.mukherjee/code/GhostMaze/AhirsSnakeAndLadder/css/style.css)
- Layout handling.
- **3D Dice CSS**: Keyframes for rolling.
- Background animations.

#### [NEW] [js/main.js](file:///Users/arpan1.mukherjee/code/GhostMaze/AhirsSnakeAndLadder/js/main.js)
- Entry point.
- Init loop.
- Event listeners.

#### [NEW] [js/game.js](file:///Users/arpan1.mukherjee/code/GhostMaze/AhirsSnakeAndLadder/js/game.js)
- Core state machine (ROLL_DICE -> MOVING -> CHECK_TILE -> END_TURN).
- Score saving logic.

#### [NEW] [js/board.js](file:///Users/arpan1.mukherjee/code/GhostMaze/AhirsSnakeAndLadder/js/board.js)
- `generateBoard()`: Logic to place N snakes and M ladders ensuring playability.
- [draw(ctx)](file:///Users/arpan1.mukherjee/code/GhostMaze/AhirsWarZone/js/main.js#535-575): Render grid, numbers, static/dynamic elements.

#### [NEW] [js/entities.js](file:///Users/arpan1.mukherjee/code/GhostMaze/AhirsSnakeAndLadder/js/entities.js)
- `Snake`: Logic for drawing wiggly curves.
- [Player](file:///Users/arpan1.mukherjee/code/GhostMaze/AhirsWarZone/js/main.js#524-529): Position interpolation logic (smooth hopping between tiles).

#### [MODIFY] [vite.config.js](file:///Users/arpan1.mukherjee/code/GhostMaze/vite.config.js)
- Add build entry.

#### [MODIFY] [All Other Games](file:///Users/arpan1.mukherjee/code/GhostMaze/)
- Update [index.html](file:///Users/arpan1.mukherjee/code/GhostMaze/index.html) carousels to include this game.

## Verification Plan
1.  **Board Gen**: Verify no "impossible" loops (snake tail on ladder start etc - though classically allow, we avoid infinite loops).
2.  **Gameplay**: Auto-play simulation mode to check for crashes.
3.  **UI**: Mobile responsiveness check.
