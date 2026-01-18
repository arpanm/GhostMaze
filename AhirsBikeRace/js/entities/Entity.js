import { images } from '../assets.js'; // Ensure we have access or use game.images if passed
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
    render(ctx, game, segment) {
        // Calculate screen position
        let scale = segment.p1.screen.scale;
        let sx = segment.p1.screen.x + (scale * this.offset * game.roadWidth * game.width / 2);
        let sy = segment.p1.screen.y;

        // Draw
        if (this.spriteDef) {
            // We need to resolve image from game.images potentially? 
            // Better to pass images logic or have usage of a global/imported 'images' if possible.
            // Plan said "Import images from ../assets.js".
            // Ensure this.spriteDef has what we need. 
            // Subclasses will define this.spriteDef.

            // We need to merge width/height if not in spriteDef? 
            // Entity has this.width/this.height.
            let def = { w: this.width, h: this.height, ...this.spriteDef };

            // Resolve image
            // Assuming we import { images } from '../assets.js' at top
            // But wait, images might not be loaded when module evaluates? 
            // It's an exported object, should be fine reference.

            // We need to handle the image look up.
            // We need to handle the image look up.
            let img = this.image || (this.spriteDef.imageId ? images[this.spriteDef.imageId] : null);
            // game.images is not standard. game.js imports images!
            // We should probably import images in Entity.js too.

            if (img) {
                this.drawSprite(ctx, game, img, def, scale, sx, sy, -0.5, -1);
            }
        }
    }

    drawSprite(ctx, game, image, spriteDef, scale, destX, destY, offsetX, offsetY) {
        if (!image) return;

        let logicalW = spriteDef.w || 64;
        let logicalH = spriteDef.h || 64;
        let spriteScale = spriteDef.scale || 1;

        let destW = (logicalW * scale * game.width / 2) * spriteScale;
        let destH = (logicalH * scale * game.width / 2) * spriteScale;

        let sw = spriteDef.sourceW || image.width;
        let sh = spriteDef.sourceH || image.height;

        let aspectRatio = sw / sh;
        destH = destW / aspectRatio;

        let sx = spriteDef.sourceX || spriteDef.x || 0;
        let sy = spriteDef.sourceY || spriteDef.y || 0;

        destX += (destW * offsetX);
        destY += (destH * offsetY);

        ctx.drawImage(image, sx, sy, sw, sh, destX, destY, destW, destH);
    }
}
