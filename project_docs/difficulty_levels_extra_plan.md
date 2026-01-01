# Difficulty Level Implementation Plan

## Overview
Implement three difficulty levels (Easy, Medium, Hard) with varying ghost behaviors and score multipliers.

## Difficulty Settings

| Level  | Spawn Distance | Chase Duration | Spawn Interval | Score Multiplier |
|--------|---------------|----------------|----------------|------------------|
| Easy   | Far (8-12 cells) | 3 seconds | 5 seconds | 10x |
| Medium | Medium (4-7 cells) | 4 seconds | 4 seconds | 100x |
| Hard   | Near (1-3 cells) | 5 seconds | 3 seconds | 1000x |

## Implementation Steps

### 1. UI Changes
- Add difficulty selector to start screen (radio buttons or dropdown)
- Store selected difficulty in global state
- Display difficulty badge in HUD during gameplay
- Show difficulty in leaderboard entries

### 2. Ghost Class Updates
**File**: `js/ghost.js`
- Add `spawnDistance` parameter to constructor
- Modify spawn logic to respect distance constraint
- Keep existing chase/flee state machine

### 3. Main Game Logic Updates
**File**: `js/main.js`
- Add global `difficulty` variable with config object
- Update ghost spawn logic:
  - Use difficulty-specific spawn interval
  - Pass spawn distance to Ghost constructor
- Update ghost chase duration in `update()` loop
- Modify score calculation with difficulty multiplier

### 4. Score System Updates
- Change ghost escape bonus formula: `multiplier * distance`
- Store difficulty level with leaderboard entries
- Display difficulty icon/badge in leaderboard

## Proposed Changes

### [NEW] Difficulty Configuration
```javascript
const DIFFICULTY_SETTINGS = {
    easy: {
        name: 'Easy',
        icon: '🟢',
        spawnDistance: { min: 8, max: 12 },
        chaseDuration: 3000,
        spawnInterval: 5000,
        scoreMultiplier: 10
    },
    medium: {
        name: 'Medium',
        icon: '🟡',
        spawnDistance: { min: 4, max: 7 },
        chaseDuration: 4000,
        spawnInterval: 4000,
        scoreMultiplier: 100
    },
    hard: {
        name: 'Hard',
        icon: '🔴',
        spawnDistance: { min: 1, max: 3 },
        chaseDuration: 5000,
        spawnInterval: 3000,
        scoreMultiplier: 1000
    }
};
```

### [MODIFY] index.html
Add difficulty selector to start screen after avatar selection.

### [MODIFY] js/ghost.js
Update constructor to accept and use spawn distance constraints.

### [MODIFY] js/main.js
- Add difficulty state variable
- Update ghost spawning logic
- Update score calculation
- Save difficulty with leaderboard entries

## Verification Plan
- Test each difficulty level
- Verify ghost spawn distances are correct
- Confirm chase durations match specifications
- Validate score multipliers work correctly
- Check leaderboard displays difficulty
