# Ahir's Ghost Maze - Architecture & Flows Overview

## 🏗 System Architecture
The project is a procedurally generated, canvas-based HTML5 survival maze game built with vanilla JavaScript (ES6 Modules) and CSS3. The core engine resides in the `AhirsGhostMaze/js/` directory.

### Core Components
- **`main.js` (The Orchestrator)**: Handles initialization, the core `requestAnimationFrame` game loop, state management (score, health, active entities, difficulty setting), UI bindings, audio synthesis (for the ghost alarm), and loading/saving the leaderboard to `localStorage`.
- **`maze.js` (Procedural Generation)**: Implements a recursive backtracker algorithm to dynamically map out a grid-based maze. It maintains cell objects with wall states (`top`, `right`, `bottom`, `left`), picks a random exit (the green door), and handles the rendering of walls onto the canvas.
- **`player.js` (Player Entity)**: Manages absolute pixel positioning and logical grid coordinates. It processes movement vectors from input (keyboard or virtual joystick) and calculates bounding-box collisions against the maze's cell walls to prevent out-of-bounds movement.
- **`ghost.js` (Enemy Entity)**: The primary antagonist. Spawns at a random angle and calculated distance from the player. It dictates a state machine (`APPEARING` -> `CHASING` -> `DEAD`). During the `CHASING` state, it calculates an absolute vector toward the player and flies through walls to reach them.
- **`stone.js` (Collectibles)**: Represents gems (`diamond`, `ruby`, `emerald`, `sapphire`) that grant points. Stones have a deterministic lifetime (10 seconds) and expire if not collected.
- **`economy.js` (Virtual Economy)**: A persistent coin tracking system using `localStorage`. It manages the player's balance, requiring an entry fee to start a match, and logs a history of transactions.

---

## 🔄 Key Game Flows

### 1. Game Initialization & Entry
1. The user selects an avatar, difficulty, and enters their name on the UI.
2. Clicking **"Start"** triggers a balance check via `economy.js`. If valid, 10 coins are deducted.
3. Relevant state variables (score, health, active stones, active ghosts) are reset.
4. A new `Maze` is generated, and the `Player` is spawned at cell `(0, 0)`.
5. The `gameLoop` begins overriding the start screen with the active game HUD and canvas.

### 2. The Game Loop (`update` -> `draw`)
The unified update loop handles time-deltas (`dt`) and delegates responsibilities to components:
- **Health Decay**: The player's health steadily decreases by roughly 1.5 HP/second. If it reaches 0, the game triggers a "Life Over" condition.
- **Player Movement**: Pending input controls dictates the `(dx, dy)` vector for the player, processed by `player.move()` to detect wall intersections before confirming coordinates.
- **Item Spawning**: Stones spawn randomly throughout the maze on a timer scaled by the chosen difficulty. Expired stones are spliced out of the active array.
- **Ghost Encounters**: 
  - If no ghost is active, and the respawn interval is met, one is instantiated.
  - The ghost blinks in place (`APPEARING`) for 1 second.
  - It triggers the web audio synthesis alarm and starts tracking the player (`CHASING`).
  - Surviving the full chase duration transitions the ghost to `DEAD`, awarding a "Ghost Escape Bonus" based on the player's distance from the vanishing ghost multiplied by the difficulty multiplier.
  - Touching the ghost immediately triggers the "Ghost Attack" end-game condition.
- **Win Condition Check**: If the player's grid coordinates match the maze's `exitCell` coordinates, victory is triggered.

### 3. End Game & Persistence
1. The `endGame(win, reason)` function ceases the game loop and stops the audio alarm.
2. **Score Calculation**: 
   - Base Score = (Points from Collected Stones)
   - Final Score = Base Score + Ghost Escape Bonuses + (Health * 1000) (if victorious).
3. The new local score is appended to the `ghost_maze_leaderboard` JSON string in `localStorage`. The list is sorted by highest score and truncated to the Top 10.
4. The post-game UI renders the cause of game over, the breakdown of collected gems, and the final leaderboard status.
