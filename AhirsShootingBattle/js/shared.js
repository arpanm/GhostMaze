// js/shared.js

export const CONFIG = {
    FPS: 60,
    INITIAL_HEALTH: 100,
    HEAL_COST: 2000,
    STRIKE_BONUS: 1000,
    WIN_BONUS: 100000,
    SURVIVAL_MULTIPLIER: 100
};

export const DIFFICULTY_SETTINGS = {
    easy: {
        accuracy: 0.3,
        speed: 1.5,
        vaultCount: 8,
        multiplier: 2
    },
    medium: {
        accuracy: 0.6,
        speed: 2.0,
        vaultCount: 5,
        multiplier: 1.5
    },
    hard: {
        accuracy: 0.9,
        speed: 2.5,
        vaultCount: 3,
        multiplier: 1
    }
};

export const state = {
    canvas: null,
    ctx: null,
    active: false,
    paused: false,
    difficulty: 'medium',
    lastTime: 0,
    player: null,
    enemy: null,
    map: null,
    projectiles: [],
    vaults: [],
    decoys: [],
    startTime: 0,
    timerInterval: null
};

export const input = {
    up: false,
    down: false,
    left: false,
    right: false,
    fire: false,
    tapPos: null,
    joystick: { x: 0, y: 0, active: false }
};
