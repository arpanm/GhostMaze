# Fix Mobile Scrolling Issues

The game UI screens (Home, Credits, Leaderboard) are not scrollable on mobile due to restrictive CSS global rules and fixed-height containers.

## Proposed Changes

### [CSS Layer]
#### [MODIFY] [style.css](file:///Users/arpan1.mukherjee/code/GhostMaze/style.css)
- Change global `touch-action: none` to `touch-action: auto` for general UI elements.
- Specifically apply `touch-action: none` only to the game canvas and virtual joystick area to prevent interference with gameplay.
- Update `.screen` to support vertical scrolling:
    - Add `overflow-y: auto`.
    - Change `justify-content: center` to `justify-content: flex-start` with top/bottom padding to ensure content isn't clipped and remains accessible.
    - Set `-webkit-overflow-scrolling: touch` for smooth momentum scrolling on iOS.
- Adjust `credits-content` and `leaderboard-list` to ensure they interact well with the parent scroll.

## Verification Plan

### Manual Verification
- Test on mobile browser emulator (or actual device if possible).
- Verify that the Home screen (with instructions) can be scrolled vertically.
- Verify that the Credits story can be scrolled.
- Verify that the Leaderboard list can be scrolled.
- Ensure that the virtual joystick and game canvas still respond correctly to touch without triggering page scroll.
