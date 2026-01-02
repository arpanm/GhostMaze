# Ahirs War Zone - Retrospective & Documentation

**Date:** January 2, 2026
**Status:** Initial Implementation Complete

## 1. Project Overview
"Ahirs War Zone" is a real-time, responsive artillery/strategy game developed as part of the Ghost Maze Arcade Suite. Two teams (Red vs Blue) battle using tanks and planes in a physics-based environment affected by wind and gravity.

### Key Features
- **Teams**: Blue (Player) vs Red (AI).
- **Units**:
    - **Tanks**: Ground units with adjustable aim and power (Slingshot/Angry Birds style mechanics).
    - **Planes**: Air support units that drop vertical bombs.
- **Environment**: Procedurally generated terrain and dynamic Wind system affecting projectiles.
- **AI**: Three difficulty levels (Easy, Medium, Hard) featuring:
    - **Aiming**: Error adjustment based on difficulty.
    - **Evasion**: Danger sensing for incoming missiles (Hard/Medium).
    - **Economy**: AI purchases reinforcements based on funds.
- **Economy**: Shop system to buy units and repairs using Score/Currency.
- **UI**: Full responsive overlay with Start Screen, HUD, Pause, and Win/Loss screens.

## 2. Implementation Plan (Executed)

### Tech Stack
- **HTML5 Canvas**: Rendering engine.
- **Vanilla JavaScript**: Game logic.
- **CSS3**: UI Overlays.

### Architecture
- `Game` class: Orchestrates the Game Loop, State Management, and global systems.
- `AIController`: Manages enemy decision making.
- `Terrain`: Generates 1D noise heightmap.
- `InputHandler`: Unified Touch/Mouse/Keyboard handling.
- `Unit` / `Projectile`: Entity classes with physics `update()` methods.

### Files Created
- `AhirsWarZone/index.html`
- `AhirsWarZone/css/style.css`
- `AhirsWarZone/js/main.js`
- `AhirsWarZone/js/entities.js`
- `AhirsWarZone/js/terrain.js`
- `AhirsWarZone/js/input.js`
- `AhirsWarZone/js/ai.js`
- `AhirsWarZone/js/ui.js`

## 3. Task List (Completed)

### Setup & Engine
- [x] Directory structure and Vite config update.
- [x] Game Loop and Canvas resizing.
- [x] Input Manager (Touch, Mouse, Keyboard).

### Game Logic
- [x] **Terrain**: Random generation.
- [x] **Wind**: Dynamic force vector.
- [x] **Entities**: Tank, Plane, Projectile classes.
- [x] **Physics**: Gravity + Wind + Velocity.
- [x] **Combat**: Collision detection (Ground/Unit), Damage, Destruction.

### AI & Difficulty
- [x] **Easy**: Poor aim, static behavior.
- [x] **Medium**: Better aim, occasional evasion.
- [x] **Hard**: Precise aim (Wind calc), active dodging, aggressive buying.

### Meta & UI
- [x] **Economy**: Score/Currency tracking, Shop system.
- [x] **Start Screen**: Name, Color, Logo, Difficulty.
- [x] **HUD**: Health bars, Score, Wind Indicator.
- [x] **Screens**: Pause, Game Over (Win/Loss), Leaderboard.
- [x] **Leaderboard**: LocalStorage persistence.

## 4. How to Play
1.  **Select**: Click/Tap your unit (Blue Team).
2.  **Move**: Use Keyboard Arrows or On-screen Buttons.
3.  **Fire (Tank)**: Drag backwards from the tank (Slingshot style) to aim and power up, then release to fire.
4.  **Fire (Plane)**: Tap 'FIRE' or drag/release to drop bomb.
5.  **Shop**: Open Shop to spend points on reinforcements.
6.  **Win**: Destroy all Red Team units.

## 5. Future Improvements (Backlog)
- [ ] **Multiplayer**: Add WebSocket support for PvP.
- [ ] **Campaign**: Progressive levels with varied terrain.
- [ ] **Weapons**: Add different missile types (Triple shot, Homing).
