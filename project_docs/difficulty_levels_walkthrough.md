# Ghost-Maze Walkthrough

## Overview
Ghost-Maze is a browser-based survival maze game. The player must navigate a procedurally generated maze, collect gemstones, and escape before their health runs out or they are caught by ghosts.

## Features
-   **Procedural Maze**: A new random maze is generated every game.
-   **Entities**:
    -   **Stones**: Collect to gain points (tracked by type: 💎 Diamond, 🔴 Ruby, 🟢 Emerald, 🔵 Sapphire).
    -   **Ghosts**: Randomly appear, give a warning (Red Light), and chase the player.
    -   **Ghost Bonus**: Surviving a ghost chase yields points (100 * distance from ghost).
-   **Audio/Visual**:
    -   **Favicon**: Spooky Ghost Icon.
    -   **Game Over**: Detailed stats (Stones vs Health vs Ghosts) and Cause of Death icons (👻/⏳/💀).
-   **Controls**:
    -   **Keyboard**: Arrow Keys or WASD/HJKL.
    -   **Touch/Mouse**: Virtual Joystick on screen.
-   **Progression**: Escape the maze to win. Score is based on remaining health and collected stones.
-   **Leaderboard**: High scores are saved locally with detailed breakdown (Stones 💎, Ghosts 👻, Health ❤️).
-   **Difficulty Levels**: Three difficulty modes with varying ghost behavior:
    -   **Easy 🟢**: Ghosts spawn far (8-12 cells), chase for 3s, appear every 5s, 10x score multiplier
    -   **Medium 🟡**: Ghosts spawn medium distance (4-7 cells), chase for 4s, appear every 4s, 100x score multiplier
    -   **Hard 🔴**: Ghosts spawn nearby (1-3 cells), chase for 5s, appear every 3s, 1000x score multiplier
-   **Story & Credits**: A dedicated screen sharing the heart-warming story behind the game's creation.
-   **Validation**: Name entry is now mandatory with inline error feedback.

## Verification
-   [x] **Difficulty Levels**: Implemented (Easy, Medium, Hard).
-   [x] **Ghost Timing**: Spawn interval resets only after ghost vanishes.
-   [x] **Credits Screen**: Accessible from the main menu with a scrollable story.
-   [x] **Name Validation**: Inline error message provided if name is missing.

### How to Run
#### Development
1.  Run `npm install`
2.  Run `npm run dev`
3.  Open the localhost URL provided.

#### Production Build
1.  Run `npm run build`
2.  Serve the `dist` folder: `npm run preview`

## Gameplay Guide
1.  **Start Screen**: Enter Name, Pick Avatar.
2.  **The Maze**: You are the Avatar. Wall collision is active.
3.  **Objective**: Find the GREEN EXIT symbol `🚪`.
4.  **Hazards**:
    -   **Health**: Decays over time! Move fast.
    -   **Ghosts**: If the screen flashes RED and alarm sounds, RUN! A ghost is chasing you.
5.  **Game Over**: If Health hits 0 or Ghost touches you.
