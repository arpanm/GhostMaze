import Entity from './Entity.js';

export default class Car extends Entity {
    constructor(z, offset, speed) {
        super(z, offset, speed);
        this.spriteName = 'CAR';
    }
}
