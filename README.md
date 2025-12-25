# Ahir's Ghost Maze

A spooky, responsive, and procedurally generated maze game built with modern AI-assisted development tools.

## 👥 Credits & Roles

This game was developed in a **combined 2-hour effort** between Ahir, a 8 year old boy and his father.

*   **Ahir**: The Architect of Ideas. He was responsible for the core game concept, testing, improvisation, feature improvements, and creative prompting.
*   **Father**: The Technical Enabler. He managed the tooling (Google Antigravity), guided prompting techniques, handled issues during testing and performed debugging and bug fixing and deployment part (GitHub and Vercel).

---

## 🎮 Game Overview

### Functionalities
- **Procedural Maze**: Every game generates a unique maze structure.
- **Dynamic Entities**: Collect gems and avoid ghosts that chase you.
- **Responsive Controls**: Works on PC (Arrow keys) and Mobile (Virtual Joystick).
- **Survival Mechanics**: Health decays overtime; escape via the green door 🚪 to win.

### Difficulty Levels
The game features three distinct difficulty modes that adjust ghost behavior and rewards:

| Level | Ghost Spawn | Chase Duration | Spawn Interval | Score Multiplier |
| :--- | :--- | :--- | :--- | :--- |
| **Easy** 🟢 | Far (8-12 cells) | 3 seconds | 5 seconds | 10x |
| **Medium** 🟡 | Mid (4-7 cells) | 4 seconds | 4 seconds | 100x |
| **Hard** 🔴 | Near (1-3 cells) | 5 seconds | 3 seconds | 1000x |

*Note: Gem spawn rates also vary, being more generous on Easy mode.*

### Scoring Logic
- **Stones**: Fixed points per gem collected.
- **Ghost Escape Bonus**: `Multiplier * Distance` from ghost when it vanishes.
- **Health Bonus**: `Remaining Health * 1000` awarded only on successful escape.
- **Total Score**: Sum of all bonuses and collected stones.

### Leaderboard
High scores are stored locally on your device. You can view the Hall of Fame from the start menu or after a game. There is a "Clear All" option to reset the local history.

---

## 🛠 Technical Architecture

### Tech Stack
- **Core**: Vanilla JavaScript (ES6 Modules).
- **Rendering**: HTML5 Canvas API.
- **Styling**: Vanilla CSS3 with modern effects (Gradients, Animations).
- **Storage**: Browser `localStorage` for the leaderboard.

### Code Structure
- `index.html`: Entry point and UI screens.
- `style.css`: Visual design system and responsive layouts.
- `js/main.js`: Game loop, state management, and UI orchestration.
- `js/maze.js`: Procedural maze generation using a recursive backtracker.
- `js/player.js`: Player movement logic and collision detection.
- `js/ghost.js`: Ghost state machine (Appearing, Chasing, Dead).
- `js/stone.js`: Gemstone entity logic.

### Deployment & CI/CD
- **Source Control**: GitHub repository.
- **Hosting**: [Vercel](https://vercel.com) via the GitHub connector for automated deployments on every push.

---

## 🤖 AI-Driven Development: Google Antigravity

This project was built using **Google Antigravity**, a powerful agentic AI coding environment. 

### Why this matters:
- **Rapid Prototyping**: Ideas are converted to working code in minutes.
- **Complex Debugging**: The AI can trace logical errors across multiple files (like ghost spawn overlaps or scoring edge cases).
- **Instructions for Further Changes**: 
  - To add a new gem type, modify `js/stone.js` and update `stonesDetails` in `main.js`.
  - To tweak difficulty, update the `DIFFICULTY_SETTINGS` object in `main.js`.
  
The combined effort of a creative human mind (Ahir) and AI-augmented technical support (Father + Antigravity) demonstrates how the barrier to creating high-quality applications is being lowered, allowing children and parents to build together effectively.
