# Ahir's Snake in a Room - Implementation Plan

## Goal Description
Create a responsive web-based game "Ahir's Snake in a Room" where the player controls a snake to eat insects and other snakes while avoiding being eaten or encircled.

## User Review Required
- **Collision Logic**: "Head-to-Head" collision resolution is assumed to favor the player or the larger snake.
- **Encirclement**: I will implement a check to see if a loop is formed by the snake's body and if enemies are inside that closed polygon.

## Proposed Changes

### Directory Structure
New directory: `/Users/arpan1.mukherjee/code/GhostMaze/AhirsSnakeInARoom`

### Logic
1.  **Game Loop**: Standard requestAnimationFrame loop.
2.  **Entities**:
    - `Snake`: properties (id, color, segments, speed, state). methods (move, grow, shrink, checkCollision).
    - `Insect`: properties (position, type, score).
3.  **collision.js**:
    - Handle `Head` vs `Food` (Eat).
    - Handle `Head` vs `Enemy Body` (Enemy cuts).
    - Handle `Head` vs `Wall` (Turn or Die? User said "no one will be able to leave the room", implies walls. I'll make them bounce or slide, or just die/stop. User said "no one will be able to leave", implies solid walls).
    - **Encirclement Check**: When snake head touches own body, run a flood fill or polygon inclusion algorithm to find trapped enemies.

### Files

#### [NEW] [index.html](file:///Users/arpan1.mukherjee/code/GhostMaze/AhirsSnakeInARoom/index.html)
- Standard HTML5 boilerplate.
- Sections:
    - `#start-screen`: Name input, Color picker, Difficulty (Speed, AI count), Buttons.
    - `#game-canvas`: Main rendering area.
    - `#hud`: Score, Rank, Joystick overlay (mobile).
    - `#game-over-screen`: Result, Breakdown.
    - `#how-to-play-screen`: Instructions.
    - `#leaderboard-screen`: Hall of Fame.
    - `#credits-screen`: Story.

#### [NEW] [style.css](file:///Users/arpan1.mukherjee/code/GhostMaze/AhirsSnakeInARoom/style.css)
- Responsive design.
- Dark/Room theme.
- CSS for UI overlays (glassmorphism).

#### [NEW] [logo_selector_and_leaderboard](file:///Users/arpan1.mukherjee/.gemini/antigravity/brain/85aeb9a0-cb4b-4a17-a086-52606d138940/implementation_plan.md)
*   **Logo Selector:**
    *   Add logo options (e.g., 🐍, ☠️, ⚡, 👑, 👁️) to the start screen.
    *   Store selected logo in game state.
    *   Render logo on snake's head.
*   **Enhanced Leaderboard:**
    *   Update `saveScore` to store logo, color, difficulty, and breakdown stats.
    *   Update `updateLeaderboardView` to a table format showing:
        *   Rank
                *   Player (Icon + Name)
        *   Difficulty (Icon)
        *   Breakdown (Insects/Kills/Bonus)
        *   Total Score

### [AhirsSnakeInARoom]
#### [MODIFY] [index.html](file:///Users/arpan1.mukherjee/code/GhostMaze/AhirsSnakeInARoom/index.html)
- Add Logo Selector HTML.
- Update Leaderboard HTML structure.

#### [MODIFY] [style.css](file:///Users/arpan1.mukherjee/code/GhostMaze/AhirsSnakeInARoom/style.css)
- Add styles for logo selector.
- Add styles for enhanced leaderboard table.

#### [MODIFY] [js/main.js](file:///Users/arpan1.mukherjee/code/GhostMaze/AhirsSnakeInARoom/js/main.js)
- Handle logo selection.
- Update `saveScore` and leaderboard rendering logic.

#### [MODIFY] [js/game.js](file:///Users/arpan1.mukherjee/code/GhostMaze/AhirsSnakeInARoom/js/game.js)
- Pass logo to `Snake`.

#### [MODIFY] [js/snake.js](file:///Users/arpan1.mukherjee/code/GhostMaze/AhirsSnakeInARoom/js/snake.js)
- Render selected logo on snake head.

#### [NEW] [js/main.js](file:///Users/arpan1.mukherjee/code/GhostMaze/AhirsSnakeInARoom/js/main.js)
- Entry point.
- State management (screen switching).
- Game loop initialization.

#### [NEW] [js/game.js](file:///Users/arpan1.mukherjee/code/GhostMaze/AhirsSnakeInARoom/js/game.js)
- `Game` class.
- Manages `Snake` instances, `Insect` spawner.
- Physics update loop.

#### [NEW] [js/snake.js](file:///Users/arpan1.mukherjee/code/GhostMaze/AhirsSnakeInARoom/js/snake.js)
- `Snake` class.
- Movement logic (history of positions).
- Input handling (User: Keys/Joystick, AI: Heuristic/Random).

#### [NEW] [js/utils.js](file:///Users/arpan1.mukherjee/code/GhostMaze/AhirsSnakeInARoom/js/utils.js)
- Helper functions (math, random, collision detection algorithms, local storage).

## Verification Plan

### Automated Tests
- None (Visual Game).

### Manual Verification
1.  **Responsiveness**: Test on Desktop (Resize) and simulate Mobile (Touch/Swipe).
2.  **Controls**: Verify WASD/Arrow keys on Desktop. Verify Joystick/Touch on Mobile simulation.
3.  **Gameplay**:
    - Eat insect -> Grow.
    - Head hits Enemy Body -> Enemy shrinks/Player eats parts.
    - Enemy Head hits Player Body -> Player shrinks.
    - Self-collision (encircle) -> Kill enemies inside.
    - Win/Loss screens show correct scores.
