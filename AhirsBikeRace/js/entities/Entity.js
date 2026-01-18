export default class Entity {
    constructor(z, offset, speed) {
        this.z = z;
        this.offset = offset;
        this.speed = speed;
        this.width = 64; // Logical
        this.height = 64;
    }
    update(dt, game) {
        this.z += this.speed * dt;
        // Simple wrap for endless traffic, but we want a race.
        // If z > trackLength, loop? Or just disappear.
        if (this.z > game.trackLength) this.z -= game.trackLength;
        if (this.z < 0) this.z += game.trackLength;
    }
}
