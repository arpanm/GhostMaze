# Task: Enhancing Immersion and HUD

- [ ] **HUD Position Fix** <!-- id: 0 -->
    - [ ] Implement `calculateRank()` in `Game` class. <!-- id: 1 -->
    - [ ] Pass `rank` to `updateHud` logic. <!-- id: 2 -->
- [ ] **Audio System** <!-- id: 3 -->
    - [ ] Create `js/audio.js` with `SoundManager` (using `AudioContext` for procedural sounds: Engine, Siren, Crash, Hit). <!-- id: 4 -->
    - [ ] Integrate `SoundManager` into `Game` class. <!-- id: 5 -->
    - [ ] Trigger sounds in `game.js`, `Police.js`. <!-- id: 6 -->
- [ ] **Visual Enhancements** <!-- id: 7 -->
    - [ ] **Police Lights**: Update `Police.js` `render` to draw flashing red/blue lights when chasing. <!-- id: 8 -->
    - [ ] **Bike Lean**: Update `game.js` `renderPlayer` to tilt sprite based on input. <!-- id: 9 -->
    - [ ] **Screen Shake**: Add `shake` offset to `draw()` camera logic when crashing/hitting. <!-- id: 10 -->
    - [ ] **Police Animation**: Implement `CAUGHT_ANIMATION` state where Police and Player stop side-by-side before Game Over. <!-- id: 11 -->
- [ ] **Meta-Game Features** <!-- id: 12 -->
    - [ ] **Hall of Fame**: Add cross-game links carousel to `index.html`. <!-- id: 13 -->
