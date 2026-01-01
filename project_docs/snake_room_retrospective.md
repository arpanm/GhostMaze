# Ahir's Snake Room - Retrospective Documentation

> [!NOTE]
> This documentation covers the Battle Royale mechanics of Snake Room.

## Game Overview
**Ahir's Snake Room** is not a traditional snake game where you eat to grow indefinitely. It is a **Battle Royale** arena where you compete against AI snakes to be the last survivor.

### Objective
- **Clear the Room:** Kill all 5-10 AI snakes.
- **Survival:** Don't get killed by others.
- **Grow:** Eating insects and remains of enemies increases your size, giving you an advantage in combat.

## Core Mechanics

### 1. Combat System
Unlike classic snake, you don't die by touching walls (you bounce). You die by combat:
- **Head-to-Head:** If two heads collide, the **Larger Snake Wins**. The loser is destroyed and turns into food particles.
- **Severing:** If you bite another snake's body, you **Cut** them at that point. The severed tail turns into food, and the victim shrinks. If they shrink too much, they die.
- **Encirclement:** If you form a closed loop around an enemy, they are instantly killed (a valid polygon check logic).

### 2. Growth & Economy
- **Insects:** 🐞, 🪰, 🦗 spawn randomly. Eating them grows your length.
- **Remains:** Dead snakes drop "Body Orbs" (🏐) which grant massive growth.
- **Length = Power:** Length determines who wins head-on collisions.

### 3. Controls & Physics
- **360° Movement:** The snake moves in any direction (radians), not just 4 grid axes.
- **Input:** Mouse/Touch to steer, or simple Joystick logic.
- **Bouncing:** Hitting a wall reflects the snake back into the arena.

## Technical Architecture

### Key Files
- **`main.js`**: UI Controller. Handles menus, leaderboards, and DOM interaction.
- **`game.js`**: The Physics Engine. Manages the entity list (`snakes`, `insects`) and collision detection loops. Implements the "Battle Royale" win condition.
- **`snake.js`**: The Entity class. Handles steering (smooth turning), history trail (for body rendering), and self-loop detection logic for encirclement.
- **`utils.js`**: Helper math for collisions (Circle-Circle, Point-in-Polygon).

## Credits
A combat-focused twist on the classic Snake genre.
