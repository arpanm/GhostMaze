# Implementation Plan - Ahir's Shark Race

A high-speed, aquatic racing and survival game featuring dynamic speed, predator-prey ecologies, and progressive level difficulty.

## User Review Required

> [!IMPORTANT]
> - **Game Objective**: Be the first Shark to cross the finish line while maintaining health by eating and avoiding predators/bullets.
> - **Speed Mechanic**: Speed is tied to health. At high HP, the shark is faster. Dropping below specific thresholds (e.g., 50%, 25%) reduces max speed.
> - **Controls**: Universal support for Keyboard (WASD/Arrows), Virtual Joystick (Mobile), and Tap/Swipe navigation.

## Proposed Changes

### 1. 🏗️ Project Structure
- Folder: `/Users/arpan1.mukherjee/code/GhostMaze/AhirSharkRace/`
- Files: `index.html`, `style.css`, `js/main.js`, `js/shark.js`, `js/sea.js`, `js/entity.js`, `js/shared.js`.

### 2. 🎨 UI & Aesthetic System
- **Theme**: Deep Ocean Blue + Neon Accents.
- **Start Screen**: Premium glassmorphism with dynamic bubbles/waves.
- **Customization**: 
    - Shark Color (Steel, Blood Red, Deep Sea Blue).
    - Team Logo (Lightning, Jaw, Wave).

### 3. 🌊 Game Engine (JS Modules)
- **main.js**: Orchestrates the loop, UI states, and race progression.
- **sea.js**: Handles the scrolling ocean environment and entity spawning.
- **shark.js**: Player and AI shark subclasses.
- **entity.js**: Base class for Fish, Obstacles, Humans, and Bullets.
- **shared.js**: Global state and configuration.

### 4. 🦈 Mechanics & Entities
- **Racing**: Side-scrolling race with a progress bar.
- **Combat/Eating**:
    - Small fish (+ points, + HP).
    - Humans (+ big HP).
    - Jellyfish/Eels/Whales (- big HP).
    - Boats (+ HP if destroyed/eaten, - HP if hit by bullets).

### 5. 📉 Progression & Persistence
- **Levels**: Speed of other sharks increases by 10-15% per level; object density increases.
- **Leaderboard**: Survival time and final score (Points + Winning Bonus).

### 6. 🔗 Cross-Game Integration
- Update `GhostMaze` and `AhirsShootingBattle` carousels to include Shark Race.
- Add reciprocal links in Shark Race.

### 7. 💅 Polish & UX Refinement

- **Shark Aesthetics**: Update `Shark.draw` for a sleek, streamlined body with dynamic tail animation.
- **Creature Diversity**: Add `Crab`, `Tortoise`, `Octopus` to `sea.js` and `entity.js`. Use vibrant, category-specific gradients/colors.
- **UI Fixes**:
    - Re-bind `restart-btn` and `menu-btn` listeners to ensure they work after a game ends.
    - Add `margin-top` to the "Dive In" button.
    - Enable scrolling on the Start Screen.
- **Improved Screens**: Use full-screen glassmorphism and animated badges for Success/Game Over screens.

### 8. 📱 Mobile & Difficulty Scaling Fixes

- **Joystick Positioning**: Adjust `#controls-layer` in `style.css` to be higher on mobile viewports to prevent it from going below the screen.
- **Difficulty Logic Enhancement**:
    - Update `shared.js` to include dangerous spawn rates and bullet frequency multipliers in difficulty settings.
    - Update `sea.js` to use these multipliers for creature speed, spawning dangerous entities, and boat bullet frequency.
    - Ensure AI shark speed also scales appropriately.

### 9. 🌊 Territory & Level Progression System

- **Continuous Gameplay**: Instead of ending at 10,000 knots, the player moves to the next "Aquatic Sector".
- **Structure**:
    - 3 Territories per Level (e.g., Sector 1, 2, 3).
    - After Sector 3, Level increases and Sector resets to 1.
- **Difficulty Scaling**: Each Sector increase adds a 1.1x multiplier to speed and danger. Each Level increase adds a 1.2x multiplier.
- **Visual Transitions**:
    - Update `Sea.js` to change background gradients and ambient effects based on Level/Sector.
    - Show "SECTOR CONQUERED" overlay during transition.
- **HUD Update**: Display current Sector and Level clearly.

## Verification Plan

### Automated Tests
- Run `npm run dev` to verify entry point registration.
- Verify collision logic via debug console logs.

### Manual Verification
- Test all input methods (Touch, Keyboard).
- Verify health/speed correlation works as expected.
- Ensure level difficulty curves Up correctly.
- Verify cross-game links navigate successfully.
