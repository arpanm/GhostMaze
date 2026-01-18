# Ahirs Road Rash Walkthrough

I have successfully created **Ahirs Road Rash**, a retro-style pseudo-3D bike racing game.

## Features Implemented
- **Pseudo-3D Engine**: Built from scratch using the classic "Jake Gordon / Lou's Pseudo 3d" algorithm for authentic retro racing feel.
- **Dynamic Terrain**: Selectable environments (Desert Hills, Neon City, Icy Peaks) that change road rendering colors.
- **Combat & Physics**:
    - **Steering**: Arrow keys or Touch D-Pad.
    - **Speed Control**: Accelerate/Brake logic with inertia.
    - **Collision**: Hit trees/rocks to crash (health loss).
- **Responsive UI**:
    - Mobile-first controls (Touch D-Pad + Action Buttons).
    - Premium glassmorphism UI for Start, Pause, and Game Over screens.
- **Generated Assets**:
    - Custom Pixel Art Player Bike, Backgrounds, and Obstacles.

## How to Verify

### 1. Launch the Game
Run the development server:
```bash
npm run dev
```
Navigate to: `http://localhost:5173/AhirsRoadRash/index.html` (port number may vary).

### 2. Gameplay Test
1.  **Start Screen**: Enter your name and select a Terrain (e.g., "Neon City").
2.  **Controls**:
    -   **Desktop**: Use `Arrow Keys` to steer/accelerate. Spacebar to Attack.
    -   **Mobile**: Use the on-screen buttons.
3.  **Race**:
    -   Drive through the track.
    -   Notice the **Parallax Background** and **Road Curves**.
    -   Try hitting a **Tree** or **Rock** to see the crash logic (Speed resets, Health drops).
    -   Finish the lap or crash out to see the **Game Over** screen.
    
### 3. Pause
-   Press `Esc` or `P` to pause.
-   Click "Resume" to continue or "Restart" to reset.

## Screenshots

![](/Users/arpan1.mukherjee/code/GhostMaze/AhirsRoadRash/assets/images/background.png)
*(Generated Parallax Background)*

![](/Users/arpan1.mukherjee/code/GhostMaze/AhirsRoadRash/assets/images/player.png)
*(Player Sprite)*
