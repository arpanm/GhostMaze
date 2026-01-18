import Entity from './Entity.js';

export default class Car extends Entity {
    constructor(z, offset, speed) {
        super(z, offset, speed);
        this.spriteDef = { imageId: 'car', scale: 8, w: 64, h: 64 };
    }
}
