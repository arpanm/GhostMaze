# Walkthrough: Ahir's Snake in a Room

## Features Checklist
- [x] **Responsive UI:** Works on Desktop (WASD/Arrows) and Mobile (Joystick/Touch).
- [x] **Detailed Start Screen:** 
    - [x] Name input, Color Picker, Difficulty Selection.
    - [x] **Logo Selector:** Choose a custom emoji (🐍, ☠️, ⚡, 👑, 👁️) for your snake.
- [x] **Core IO Mechanics:**
    - [x] Snake movement with smooth turning.
    - [x] Growth by eating insects.
    - [x] Head-to-Head combat: Bigger snake eats smaller snake.
    - [x] Head-to-Body combat: Hitting a body cuts the tail off.
    - [x] Encirclement: Surrounding an area kills all enemies inside.
    - [x] Wall collision: Snake turns away from walls to avoid getting stuck.
- [x] **HUD & Feedback:** 
    - [x] Score, Kills, sector progression (visual), Game Over stats.
    - [x] Pause Screen shows current score.
- [x] **Persistent Leaderboard:** 
    - [x] LocalStorage based Hall of Fame.
    - [x] **Enhanced View:** Shows Rank, Player (Name+Logo+Color), Difficulty, Detailed Score Breakdown.
    - [x] Aborting game from Pause screen saves score correctly.
    - [x] Winning bonus awards 5000 points if you are the last snake standing.
- [x] **Cross-Game Integration:** 
    - [x] Snake Room is linked in Ghost Maze, Shark Race, and Shooting Battle carousels.

## Verification Steps

### 1. Initial Setup
1.  Open `AhirsSnakeInARoom/index.html` in a browser.
2.  **Logo Test:** Select different logos (e.g., ☠️). Verify the selection highlight works.
3.  Enter a name, pick a color (e.g., Blue), and start.

### 2. Gameplay & Visuals
-   **Logo Rendering:** Check your snake's head. It should display the selected emoji (☠️) instead of generic eyes.
-   **Rotation:** Turn the snake. Ensure the logo rotates or stays readable (as per design choice).

### 3. Leaderboard check
-   Play a short game, eat some insects, maybe kill one enemy.
-   End the game (die or exit via pause).
-   **Hall of Fame:**
    -   Open the leaderboard.
    -   Verify your entry shows:
        -   Your Name alongside your Logo and Name Color.
        -   The correct Difficulty icon/text.
        -   A breakdown of "Food", "Kills", and "Bonus".
        -   The correct Total Score.

## Known Limitations
-   Encirclement polygon check is approximate (uses point-in-polygon on body history). Very fast movements might glitch through thin loops.
-   AI acts randomly or seeks food; it does not actively try to encircle the player (too complex for MVP).
