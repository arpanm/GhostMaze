# Implementation Plan: Immersion & HUD

**Goal**: Fix HUD Position indicator and add Audio/Visual feedback (Sounds, Lights, Lean, Shake).

## User Review Required
> [!NOTE]
> Since no audio files were provided, I will use `AudioContext` to generate synthesized sound effects (Engine hum, Siren wail, Crash noise, Hit thud).

## Proposed Changes

### [Audio]
#### [NEW] [js/audio.js](file:///Users/arpan1.mukherjee/code/GhostMaze/AhirsBikeRace/js/audio.js)
- Create `SoundManager` class.
- Methods: `playEngine(speed)`, `playSiren()`, `playCrash()`, `playHit()`.
- Use OscillatorNodes for procedural sound generation.

### [Game Logic & HUD]
#### [MODIFY] [js/game.js](file:///Users/arpan1.mukherjee/code/GhostMaze/AhirsBikeRace/js/game.js)
- **Rank**: Implement `getRank()`: count entities with `z > (this.position + this.player.z)`. Pass to `updateHud`.
- **Shake**: Add `this.screenShake` variable. Set it on crash/hit. Apply random x/y offset in `draw()`.
- **Lean**: In `renderPlayer`, rotate context if `this.input.left` or `right` is active.
- **Police Animation**:
    - In `updateGameLogic`, if `state === 'GAME_OVER_ANIMATION'` (Busted), ensure Player and Police ease to a stop side-by-side. 
    - Delay Game Over screen by 2-3 seconds to show them standing together.
- **Scoring**:
    - Verify `this.score += 200` happens on Takedown.

#### [MODIFY] [js/entities/Police.js](file:///Users/arpan1.mukherjee/code/GhostMaze/AhirsBikeRace/js/entities/Police.js)
- **Visuals**: In `render()`, if `state === 'CHASING'`, draw alternating Red/Blue circles (glows) on top of the sprite to simulate siren lights.
- **Audio**: Trigger `playSiren` if chasing.

#### [MODIFY] [js/main.js](file:///Users/arpan1.mukherjee/code/GhostMaze/AhirsBikeRace/js/main.js)
- Update `updateHud` to display `rank`.
- Initialize `SoundManager` (user interaction required to start AudioContext usually, bind to Start button).

#### [MODIFY] [index.html](file:///Users/arpan1.mukherjee/code/GhostMaze/AhirsBikeRace/index.html)
- Add "Hall of Fame" / "Games by Ahir" carousel section at bottom or start screen.
- Links to: `AhirsSnakeInARoom`, `AhirSharkRace`, `AhirsShootingBattle`, `AhirsWarZone`, `AhirsChess`, `AhirsSnakeAndLadder`.

## Verification Plan
1.  **HUD**: Verify "POS" updates in real-time (e.g., 4/5 -> 1/5).
2.  **Audio**: Listen for engine pitch change with speed, siren when chased, and crash sounds.
3.  **Visuals**:
    - Check Police have flashing lights when chasing.
    - Check Player bike slight tilt when steering.
    - Check Screen shake on impact.
    - **Police Catch**: Verify player and police stop together before "Busted" screen.
4.  **Meta**: Check links to other games work.
