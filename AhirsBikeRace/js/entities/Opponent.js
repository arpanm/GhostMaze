import Entity from './Entity.js';

export default class Opponent extends Entity {
    constructor(z, offset, speed) {
        super(z, offset, speed);
        // Randomly pick a competitor sprite
        this.spriteName = Math.random() > 0.5 ? 'COMPETITOR1' : 'COMPETITOR2';
        this.baseSpeed = speed;
        this.changeLaneTimer = 0;
    }
    update(dt, game) {
        // AI Logic
        // Accelerate if behind, slow if ahead? Or just race.
        // Let's make them rubberband slightly or just constant fast speed.
        this.z += this.speed * dt;
        if (this.z > game.trackLength) {
            // Lap or finish? assume 1 lap race for now
            this.finished = true;
        }

        // Avoid player
        // Simple: change lane if close to player
        this.changeLaneTimer -= dt;
        if (this.changeLaneTimer < 0 && Math.abs(this.z - game.position) < 2000) {
            this.offset += (Math.random() > 0.5 ? 0.5 : -0.5);
            // clamp
            if (this.offset < -1) this.offset = -1;
            if (this.offset > 1) this.offset = 1;
            this.changeLaneTimer = 2 + Math.random() * 3;
        }
    }
}
