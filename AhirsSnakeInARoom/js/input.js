export class InputHandler {
    constructor() {
        this.keys = {};
        this.direction = { x: 0, y: 0 }; // Current desired direction
        this.lastDirection = { x: 1, y: 0 }; // Last non-zero direction

        // Joystick state
        this.joystickActive = false;
        this.joystickBase = { x: 0, y: 0 };
        this.joystickTouchId = null;
        this.joyStickMaxRadius = 40;

        this.joystickZone = document.getElementById('joystick-zone');
        this.joystickKnob = document.getElementById('joystick-knob');

        this.init();
    }

    init() {
        // Key listeners
        window.addEventListener('keydown', (e) => {
            this.keys[e.key] = true;
            this.updateDirectionFromKeys();
        });

        window.addEventListener('keyup', (e) => {
            this.keys[e.key] = false;
            // We don't stop the snake on keyup, it keeps moving
        });

        // Touch listeners
        if (this.joystickZone) {
            this.joystickZone.addEventListener('touchstart', (e) => this.handleTouchStart(e), { passive: false });
            this.joystickZone.addEventListener('touchmove', (e) => this.handleTouchMove(e), { passive: false });
            this.joystickZone.addEventListener('touchend', (e) => this.handleTouchEnd(e), { passive: false });
        }
    }

    updateDirectionFromKeys() {
        // Priority: Arrow keys/WASD override each other based on press
        // Snake moves constantly, so we just update the target vector
        let dx = 0;
        let dy = 0;

        if (this.keys['ArrowUp'] || this.keys['w'] || this.keys['W']) dy = -1;
        if (this.keys['ArrowDown'] || this.keys['s'] || this.keys['S']) dy = 1;
        if (this.keys['ArrowLeft'] || this.keys['a'] || this.keys['A']) dx = -1;
        if (this.keys['ArrowRight'] || this.keys['d'] || this.keys['D']) dx = 1;

        // If diagonal, normalize later. If keys pressed, update direction
        if (dx !== 0 || dy !== 0) {
            this.direction = { x: dx, y: dy };
            this.lastDirection = { x: dx, y: dy };
        }
    }

    handleTouchStart(e) {
        e.preventDefault();
        const touch = e.changedTouches[0];
        this.joystickTouchId = touch.identifier;
        this.joystickActive = true;

        // Get center of joystick zone
        const rect = this.joystickZone.getBoundingClientRect();
        this.joystickBase = {
            x: rect.left + rect.width / 2,
            y: rect.top + rect.height / 2
        };

        this.updateJoystick(touch.clientX, touch.clientY);
    }

    handleTouchMove(e) {
        e.preventDefault();
        if (!this.joystickActive) return;

        for (let i = 0; i < e.changedTouches.length; i++) {
            if (e.changedTouches[i].identifier === this.joystickTouchId) {
                this.updateJoystick(e.changedTouches[i].clientX, e.changedTouches[i].clientY);
                break;
            }
        }
    }

    handleTouchEnd(e) {
        e.preventDefault();
        for (let i = 0; i < e.changedTouches.length; i++) {
            if (e.changedTouches[i].identifier === this.joystickTouchId) {
                this.joystickActive = false;
                this.resetJoystickUI();
                break;
            }
        }
    }

    updateJoystick(touchX, touchY) {
        const dx = touchX - this.joystickBase.x;
        const dy = touchY - this.joystickBase.y;

        const distance = Math.sqrt(dx * dx + dy * dy);
        const angle = Math.atan2(dy, dx);

        // Cap distance
        const cappedDist = Math.min(distance, this.joyStickMaxRadius);

        // Update UI
        const knobX = Math.cos(angle) * cappedDist;
        const knobY = Math.sin(angle) * cappedDist;

        this.joystickKnob.style.transform = `translate(calc(-50% + ${knobX}px), calc(-50% + ${knobY}px))`;

        // Update direction vector
        // Allow full analog control or snap to grid? 
        // Snake usually prefers specific directions, but "Snake in a Room" implies slither style
        // Let's do normalized vector for smooth movement
        this.direction = { x: Math.cos(angle), y: Math.sin(angle) };
        this.lastDirection = this.direction;
    }

    resetJoystickUI() {
        this.joystickKnob.style.transform = `translate(-50%, -50%)`;
    }

    getInputDirection() {
        // Normalize direction if needed
        if (this.direction.x === 0 && this.direction.y === 0) {
            return this.lastDirection; // Keep moving in last known direction
        }

        // If keys are not pressed and no joystick, return last Direction
        // If keys are pressed, they set this.direction.

        // Check normalization
        const len = Math.sqrt(this.direction.x ** 2 + this.direction.y ** 2);
        if (len > 0) {
            return { x: this.direction.x / len, y: this.direction.y / len };
        }
        return this.lastDirection;
    }
}
