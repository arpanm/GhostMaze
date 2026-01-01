# Ahir's Shark Race - Retrospective Documentation

> [!NOTE]
> This documentation was generated retrospectively based on the codebase as of Jan 2026.

## Game Overview
**Ahir's Shark Race** is a side-scrolling aquatic racing game where you play as a shark competing against AI opponents. The unique twist is that **Speed is tied to Health**. To go fast, you must stay healthy by eating fish and avoiding dangers.

### Objective
- **Race:** Reach the finish line before the AI sharks.
- **Survive:** Keep your health above zero. If health drops to 0, game over.
- **Progress:** Complete 3 Sectors to advance to the next "Tier" (Level).

## Core Mechanics

### 1. The Health-Speed Engine
The most critical mechanic is defined in `shark.js`:
- **High Health (60-100%)**: Maximum Speed (100% of base speed).
- **Medium Health (30-60%)**: Reduced Speed (80% of base speed).
- **Critical Health (<30%)**: Limp Mode (50% of base speed).

This creates a risk/reward loop: *Do you take a detour to eat a fish and heal, or push forward and risk slowing down later?*

### 2. Edibles & Hazards
- **Boosts (Eat):** Small fish (🐠, 🐟), Tortoises (🐢), Crabs (🦀). Restores Health & Score.
- **Dangers (Avoid):** Jellyfish (🪼, Shock damage), Electric Eels (🐍), Whales (🐋, Heavy damage).
- **Humans:** Swimmers (🏊) and Boats (🚣). Some boats may fire bullets!

## Controls
- **Desktop:** `WASD` or `Arrow Keys`.
- **Mobile:** On-screen Joystick.
- **Pause:** `P` key or Pause Button.

## Technical Architecture

### Key Files
- **`main.js`**:
  - Manages the Game Loop (`requestAnimationFrame`).
  - Handles UI transitions (Start Screen -> Game -> Leaderboard).
  - Manages global state (`active`, `paused`, `score`).
  - **Sector Logic:** Tracks progress through Sectors and Tiers.
  
- **`shark.js`**:
  - Defines the `Shark` class (used for both Player and AI).
  - Handles physics, velocity, and the "Health = Speed" logic.
  - Draws the shark using HTML5 Canvas primitives (curves for tail, ellipses for body).

- **`sea.js`**:
  - Manages the scrolling background to create the illusion of forward movement.
  
- **`shared.js`**:
  - Stores configuration constants (`CONFIG`) and shared state.

## Credits
created by **Ahir Mukherjee** (8 years old) with technical assistance from his father.
