import Entity from './Entity.js';

export default class Police extends Entity {
    constructor(z, offset) {
        super(z, offset, 0); // content with player speed initially?
        this.spriteName = 'POLICE';
        this.state = 'IDLE'; // IDLE, CHASING, CAUGHT
        this.chaseTimer = 0;
    }
    update(dt, game) {
        this.z += this.speed * dt;

        switch (this.state) {
            case 'IDLE':
                // Appear behind player randomly
                // Reduced chance slightly as it was too frequent in testing? Or kept same?
                if (Math.random() < 0.0001) {
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
}
