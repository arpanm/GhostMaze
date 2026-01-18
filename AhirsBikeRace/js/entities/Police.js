import Entity from './Entity.js';

export default class Police extends Entity {
    constructor(z, offset) {
        super(z, offset, 0);
        this.spriteDef = { imageId: 'police', scale: 7, w: 64, h: 64 };
        this.state = 'IDLE'; // IDLE, CHASING, CAUGHT
        this.chaseTimer = 0;
    }
    update(dt, game) {
        this.z += this.speed * dt;

        switch (this.state) {
            case 'IDLE':
                // Appear behind player randomly
                // Reduced chance slightly as it was too frequent in testing? Or kept same?
                if (Math.random() < 0.002) {
                    this.state = 'CHASING';
                    this.z = game.position - 2000; // Start behind
                    this.speed = game.player.speed + 2000; // Faster
                    game.ui.onMessage("POLICE CHASE!");
                }
                break;
            case 'CHASING':
                // Catch up
                this.speed = game.player.maxSpeed + 1000; // Force faster

                // Match lane
                let targetOffset = game.player.x;
                if (this.offset < targetOffset) this.offset += dt;
                if (this.offset > targetOffset) this.offset -= dt;

                // CAUGHT_ANIMATION handling is done by Game loop freezing logic, 
                // but we need to ensure we don't override speed if game tells us to freeze.
                // Actually the game loop overrides e.speed in the animation block, so this is fine.

                // Check catch
                // We access game methods. game.overlap and game.onPoliceCatch
                // Note: overlap method is on Game class.
                if (game.overlap(game.player.x, 0.8, this.offset, 0.8) &&
                    Math.abs((game.position + game.player.z) - this.z) < 200) {
                    this.state = 'CAUGHT';
                    game.onPoliceCatch();
                }

                // Give up if too far?
                break;

            case 'CAUGHT_ANIMATION':
                // Controlled by game loop
                break;
        }
    }

    render(ctx, game, segment) {
        super.render(ctx, game, segment);

        // Draw Siren Lights if Chasing
        if (this.state === 'CHASING' || this.state === 'CAUGHT_ANIMATION') {
            // Screen position of police is calculated in super.render?
            // Actually super.render does the drawing. We need coordinates.
            // Entity.render calculates sx, sy, scale. 
            // We can't easily hook into the exact screen coordinates unless we duplicate logic or 
            // make Entity save the last screen coords.

            // Alternative: Add 'extraDraw' hook in Entity?
            // Or just recalculate here.

            let scale = segment.p1.screen.scale;
            let sx = segment.p1.screen.x + (scale * this.offset * game.roadWidth * game.width / 2);
            let sy = segment.p1.screen.y;

            // Simple flashing relative to time
            let time = new Date().getTime();
            let flash = Math.floor(time / 200) % 2 === 0;

            let w = this.width * scale * game.width / 2 * (this.spriteDef.scale || 1);
            let h = this.height * scale * game.width / 2 * (this.spriteDef.scale || 1);

            // Adjust position to top of car
            let lx = sx - w * 0.2;
            let rx = sx + w * 0.2;
            let ly = sy - h * 0.8;

            ctx.fillStyle = flash ? 'rgba(255, 0, 0, 0.7)' : 'rgba(0, 0, 255, 0.7)';
            ctx.beginPath();
            ctx.arc(lx, ly, w * 0.15, 0, Math.PI * 2);
            ctx.fill();

            ctx.fillStyle = flash ? 'rgba(0, 0, 255, 0.7)' : 'rgba(255, 0, 0, 0.7)';
            ctx.beginPath();
            ctx.arc(rx, ly, w * 0.15, 0, Math.PI * 2);
            ctx.fill();
        }
    }
}
