export const CONFIG = {
    canvasWidth: window.innerWidth,
    canvasHeight: window.innerHeight,
    baseSpeed: 5,
    maxHealth: 100,
    raceDistance: 10000, // Distance to finial
    diffs: {
        easy: { id: 'easy', enemySpeedMult: 0.8, spawnRate: 1.2, scoreMult: 1 },
        medium: { id: 'medium', enemySpeedMult: 1.0, spawnRate: 1.0, scoreMult: 10 },
        hard: { id: 'hard', enemySpeedMult: 1.2, spawnRate: 0.8, scoreMult: 100 }
    }
};

export const state = {
    active: false,
    paused: false,
    player: null,
    enemies: [],
    entities: [], // Fish, obstacles, humans
    sea: null,
    canvas: null,
    ctx: null,
    level: 1,
    score: 0,
    difficulty: CONFIG.diffs.easy,
    lastTime: 0,
    distanceTravelled: 0,
    gameTime: 0
};

export const input = {
    up: false, down: false, left: false, right: false,
    joystick: { x: 0, y: 0, active: false }
};
