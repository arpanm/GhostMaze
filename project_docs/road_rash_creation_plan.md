# Abir's Road Rash Implementation Plan

## Goal Description
Create a responsive, web-based racing and combat game inspired by "Road Rash". The game will feature a pseudo-3D perspective where players race bikes, fight opponents, dodge obstacles, and avoid police. It will support desktop and mobile controls.

## User Review Required
> [!IMPORTANT]
> I will use a **Pseudo-3D** rendering technique (classic retro racing style) using HTML5 Canvas. This provides the authentic "Road Rash" feel rather than a top-down 2D view.

> [!NOTE]
> Assets will be generated using the AI image generator to ensure a unique and premium look.

## Proposed Changes

### Project Structure
New directory: `AhirsRoadRash`

#### [NEW] [index.html](file:///Users/arpan1.mukherjee/code/GhostMaze/AhirsRoadRash/index.html)
- Main entry point.
- Canvas element for game rendering.
- UI overlays for Start Screen, HUD, Pause Menu, Game Over.

#### [NEW] [style.css](file:///Users/arpan1.mukherjee/code/GhostMaze/AhirsRoadRash/css/style.css)
- Responsive design.
- Game UI styling (menus, buttons, HUD).
- Animations for UI transitions.

#### [NEW] [main.js](file:///Users/arpan1.mukherjee/code/GhostMaze/AhirsRoadRash/js/main.js)
- Game entry point and state management.
- Event listeners (Input handling).

#### [NEW] [game.js](file:///Users/arpan1.mukherjee/code/GhostMaze/AhirsRoadRash/js/game.js)
- Core game loop (Update, Draw).
- `Road` class for pseudo-3D rendering (segments, curves, hills).
- `Player` class (movement, combat state, sprite handling).
- `Opponent` class (AI, aggression, combat).
- `Sprite` class (rendering billboard objects: trees, rocks, cars).

#### [NEW] [assets.js](file:///Users/arpan1.mukherjee/code/GhostMaze/AhirsRoadRash/js/assets.js)
- Asset loading and management.
- Placeholder generation or base64 strings if needed initially.

### Feature Breakdown

1.  **Core Engine**:
    - Segment-based road rendering (Z-mapping).
    - Parallax background scrolling.
    - Centrifugal force on curves.

2.  **Gameplay**:
    - **Player**: Steer, Accelerate, Brake, Punch, Kick.
    - **Health/Stamina**: Health drops on crash/hit. Stamina for fighting.
    - **Physics**: Collision detection with road side objects (fall), cars (crash), and opponents (fight).

3.  **Content**:
    - **Terrains**: Desert (Hills), City (Buildings), Snow (Slippery).
    - **Entities**: Police (chase logic), Pedestrians (avoid), Animals.
    - **Funny Elements**: Jumping pets, clowns/jokers on road.

4.  **UI/UX**:
    - **Start Screen**: Name input, Color selection, Difficulty (Easy/Medium/Hard).
    - **HUD**: Speed, Position, Health, Distance.
    - **Touch Controls**: On-screen buttons for mobile (Steer L/R, Accel, Brake, Attack).

5.  **Data Persistence**:
    - `localStorage` for High Scores.

## Verification Plan

### Automated Tests
- None planned for this visual game.

### Manual Verification
- **Desktop**: Verify Keyboard arrows for steering/speed, Space/Enter for combat.
- **Mobile**: Toggle mobile emulation, check touch button responsiveness.
- **Gameplay**:
    - Complete a race.
    - Crash into a tree (verify fall animation).
    - Kick an opponent (verify reaction).
    - Pause/Resume game.
    - Check High Score saving.
