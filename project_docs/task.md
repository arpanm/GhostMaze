# Ghost Maze Arcade Suite - Project Roadmap & Task List

This document tracks all planned improvements, technical debt, and feature requests across the entire suite of games.

## 🚨 Critical Fixes (High Priority)
- [ ] **Global:** Fix `AudioContext` warnings. Ensure AudioContext is only resumed *after* a user gesture interaction (click/touch) across all games.
- [ ] **Ghost Maze:** Verify mobile joystick responsiveness. It feels "stiffer" than the Snake/Shooting implementation.
- [ ] **Shooting Battle:** Fix potential "Infinite Loop" in `findNearestVault` if no vaults are present (add fallback).

## 👻 Ghost Maze
- [ ] **Refactor:** Move `DIFFICULTY_SETTINGS` to a shared config file if possible, or ensure it matches the `shared.js` pattern used in other games to reduce duplication.
- [ ] **UI:** Add a "Transition Animation" when moving between difficulty levels or restarting.
- [ ] **Gameplay:** Add a visual indicator for the "Ghost Chase Timer" (e.g., a progress bar above the ghost) so players know how long they need to survive.

## 🐍 Snake Room
- [ ] **Balance:** AI Snakes sometimes spawn too close to walls. Add a buffer zone to spawn coordinates.
- [ ] **Visuals:** Improve "Encirclement" feedback. When a loop is formed, flash the polygon area to clearly show the "Kill Zone".
- [ ] **Physics:** The "Bounce" off walls is abrupt. Add a slight "squash and stretch" effect or particle impact.

## 🦈 Shark Race
- [ ] **Balance:** "Health = Speed" mechanic can be too punishing for beginners. Considerations:
    - Add a "Minimum Speed" floor (e.g., 50% instead of 30%) for Easy mode.
- [ ] **Content:** Add more variety to the "Sea" background (e.g., shipwrecks, coral reefs) in later Sectors.
- [ ] **Code:** `shark.js` has hardcoded movement constants. Move these to `CONFIG` in `shared.js`.

## 🔫 Shooting Battle
- [ ] **AI:** Refactor `Enemy.think()` method. It's becoming a "God Method". Split into `findTarget()`, `decideState()`, and `executeAction()`.
- [ ] **Economy:** Add a "Daily Bonus" or "Start Bonus" for returning players (localStorage).
- [ ] **Audio:** Add specific sound effects for "Boss Appearance" and "Store Purchase".

## 🏰 Ahirs War Zone
- [x] **Initial Release:** Core gameplay, AI, Economy, and Responsive UI implemented.
- [ ] **Fix:** Spawn Player (Blue) Plane.
- [ ] **Fix:** Main Menu button behavior (return to start).
- [ ] **Fix:** Hall of Fame display on start.
- [ ] **Fix:** Carousel alignment.
- [ ] **Feature:** Add Bunkers and Watch Towers.
- [ ] **Polish:** Add particle effects for explosions.


## 🛠️ General / Infrastructure
- [ ] **Navigation:** Unify the "Home" / "Back" button logic. Some games use `../index.html` hardcoded, others might use absolute paths. Ensure consistent routing.
- [ ] **Styles:** Extract common CSS (buttons, glassmorphism panels) into a `common/style.css` to reduce duplication in `style.css` of each game.
- [ ] **PWA:** Consider adding a `manifest.json` to make the suite installable as a PWA on mobile.
