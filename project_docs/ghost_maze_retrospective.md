# Ghost Maze - Retrospective Documentation

> [!NOTE]
> This documentation covers the full scope of the original Ghost Maze game.

## Game Overview
**Ghost Maze** is a survival-horror puzzle game where you navigate a darkened maze to find the exit before your life force runs out or you are caught by spirits.

### Objective
- **Escape:** Find the exit cell (visualized as a light/portal) in the maze.
- **Survive:** Maintain your health, which decays over time (`-1.5 HP/sec`).
- **Score:** Collect stones (💎, 🔴, 🟢, 🔵) for points.

## Core Mechanics

### 1. The Maze & Player
- **Grid:** A 15x15 procedurally generated maze using DFS (Depth-First Search) or similar algorithm (implied by `maze.js`).
- **Visibility:** The player has limited vision (fog of war effect via `canvas` masking, though code suggests simple rendering of cells).

### 2. The Ghosts
Ghosts are the primary antagonist.
- **Spawn Logic:** Ghosts spawn periodically at a distance from the player (determined by difficulty).
- **Behavior Loop:**
    1.  **APPEARING:** Gives a warning (blinking) for 1 second.
    2.  **CHASING:** Flies directly through walls towards the player for `3-5 seconds`.
    3.  **VANISH:** If the player survives the chase, the ghost disappears.
- **Collision:** Touching a ghost results in instant Game Over.

### 3. Difficulty Levels
Configured in `main.js`:
- **Easy:** Ghosts spawn far (8-12 tiles), Chase for 3s. High score multiplier (10x).
- **Medium:** Ghosts spawn closer (4-7 tiles), Chase for 4s. 100x multiplier.
- **Hard:** Ghosts spawn very close (1-3 tiles), Chase for 5s. 1000x multiplier.

## Controls
- **Movement:** `Arrow Keys`, `WASD` (Desktop) or `Virtual Joystick` (Mobile).
- **UI:** Difficulty selection, Avatar selection.

## Technical Architecture

### File Structure
- **`main.js`**: Core controller. Handles game loop, difficulty settings, and "Director AI" for spawning ghosts/stones.
- **`maze.js`**: Generates the grid structure and validates the path.
- **`player.js`**: Handles player physics and collision with walls.
- **`ghost.js`**: State machine for Ghost behavior (Appear -> Chase -> Die).
- **`stone.js`**: Simple collectible logic.

### Audio System
- Uses `AudioContext` for procedural sound generation (e.g., the "Alarm" sound during a chase is a `sawtooth` oscillator modulated by a `sine` LFO).

## Credits
The original game that started the arcade suite.
