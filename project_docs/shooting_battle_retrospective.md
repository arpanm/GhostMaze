# Ahir's Shooting Battle - Retrospective Documentation

> [!NOTE]
> This documentation was generated retrospectively based on the codebase as of Jan 2026.

## Game Overview
**Ahir's Shooting Battle** is a top-down tactical shooter where you face off against an AI Commander. It features an economy system, destructible elements, and a strategic "Decoy" mechanic.

### Objective
- **Eliminate the Enemy Commander:** Reduce their Health to 0.
- **Survive:** Don't let your Health reach 0.

## Core Mechanics

### 1. Economy & Store
Money is crucial. You earn it by collecting **Vaults** generated on the map.
- **Store:** Press `STORE` or pause to buy items.
- **Inventory:** You can carry multiple weapons but equip one at a time.
- **Items:**
    - `Pistol` (Free, Low Dmg)
    - `Assault Rifle` (Fast, Med Dmg)
    - `Sniper` (High Dmg, Slow rate)
    - `Heal` (+10 HP)
    - `Decoy` (Distracts AI)

### 2. Decoy System
A signature feature designed by Ahir.
- **Usage:** Press `E` or the Decoy Button.
- **Effect:** Spawns a "False Soldier" that moves in a straight line.
- **Strategy:** The AI will target the nearest entity, allowing you to flank them while they shoot the decoy.

### 3. AI Behavior
- The Enemy Commander (AI) also collects money, buys weapons, and hunts the player.
- They will chase you or your decoys based on proximity.

## Controls
- **Move:** `WASD` / Arrows / Joystick.
- **Aim & Shoot:** Click / Tap / Spacebar.
- **Decoy:** `E` / Button.
- **Store:** On-screen button.

## Technical Architecture

### Key Files
- **`main.js`**: 
  - Central hub. Initializes `Player`, `Enemy`, and `Map`.
  - Handles the Store UI and purchase logic.
  - Manages Leaderboard (LocalStorage).

- **`player.js` / `enemy.js`**:
  - Character logic. Both share similar attributes (Health, Money, Weapon).
  
- **`decoy.js`**:
  - Defines the `Decoy` class.
  - Features: Temporary lifespan (5s), low health, simple movement logic.

- **`weapon.js`**:
  - Defines weapon statistics (Fire rate, Damage, Cost, Speed).

- **`map.js`**:
  - Generates the battlefield including Walls and Money Vaults.

## Credits
Created by **Ahir Mukherjee** (8 years old). Concept inspired by a desire to make a "Battle Game" after the success of Ghost Maze.
