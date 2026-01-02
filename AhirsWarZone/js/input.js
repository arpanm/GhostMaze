export class InputHandler {
    constructor(canvas, game) {
        this.canvas = canvas;
        this.game = game;

        // State
        this.activePointer = null; // { x, y, id }
        this.isDragging = false;
        this.dragStart = { x: 0, y: 0 };
        this.dragCurrent = { x: 0, y: 0 };

        // Keys
        this.keys = {}; // { ArrowLeft: true, ... }

        this.setupListeners();
    }

    setupListeners() {
        // Mouse
        this.canvas.addEventListener('mousedown', (e) => this.handlePointerDown(e.offsetX, e.offsetY));
        this.canvas.addEventListener('mousemove', (e) => this.handlePointerMove(e.offsetX, e.offsetY));
        this.canvas.addEventListener('mouseup', () => this.handlePointerUp());

        // Touch
        this.canvas.addEventListener('touchstart', (e) => {
            e.preventDefault();
            const rect = this.canvas.getBoundingClientRect();
            const touch = e.touches[0];
            this.handlePointerDown(touch.clientX - rect.left, touch.clientY - rect.top);
        }, { passive: false });

        this.canvas.addEventListener('touchmove', (e) => {
            e.preventDefault();
            const rect = this.canvas.getBoundingClientRect();
            const touch = e.touches[0];
            this.handlePointerMove(touch.clientX - rect.left, touch.clientY - rect.top);
        }, { passive: false });

        this.canvas.addEventListener('touchend', (e) => {
            e.preventDefault();
            this.handlePointerUp();
        });

        // Keyboard
        window.addEventListener('keydown', (e) => {
            this.keys[e.code] = true;
        });

        window.addEventListener('keyup', (e) => {
            this.keys[e.code] = false;
        });

        // UI Control Buttons (Virtual Joystick/Buttons)
        const moveLeft = document.getElementById('move-left');
        const moveRight = document.getElementById('move-right');

        const setKey = (code, val) => { this.keys[code] = val; };

        if (moveLeft) {
            moveLeft.addEventListener('mousedown', () => setKey('ArrowLeft', true));
            moveLeft.addEventListener('mouseup', () => setKey('ArrowLeft', false));
            moveLeft.addEventListener('touchstart', (e) => { e.preventDefault(); setKey('ArrowLeft', true); });
            moveLeft.addEventListener('touchend', (e) => { e.preventDefault(); setKey('ArrowLeft', false); });
        }

        if (moveRight) {
            moveRight.addEventListener('mousedown', () => setKey('ArrowRight', true));
            moveRight.addEventListener('mouseup', () => setKey('ArrowRight', false));
            moveRight.addEventListener('touchstart', (e) => { e.preventDefault(); setKey('ArrowRight', true); });
            moveRight.addEventListener('touchend', (e) => { e.preventDefault(); setKey('ArrowRight', false); });
        }
    }

    handlePointerDown(x, y) {
        this.isDragging = true;
        this.dragStart = { x, y };
        this.dragCurrent = { x, y };

        // Check if we tapped a unit (handled by game logic)
        this.game.handleTap(x, y);
    }

    handlePointerMove(x, y) {
        if (!this.isDragging) return;
        this.dragCurrent = { x, y };
    }

    handlePointerUp() {
        if (!this.isDragging) return;
        this.isDragging = false;

        // If dragging was for aiming (and sufficient distance), fire logic
        const dx = this.dragCurrent.x - this.dragStart.x;
        const dy = this.dragCurrent.y - this.dragStart.y;

        if (Math.hypot(dx, dy) > 20) {
            // Drag release - FIRE/AIM
            this.game.handleDragRelease(this.dragStart, this.dragCurrent);
        } else {
            // Click / Tap
            if (this.game.handleClick) this.game.handleClick(this.dragStart.x, this.dragStart.y);
        }
    }
}
