export class AIController {
    constructor(game, difficulty) {
        this.game = game;
        this.difficulty = difficulty; // 'easy', 'medium', 'hard'
        this.lastActionTime = 0;
        this.actionInterval = this.getInterval();
    }

    getInterval() {
        switch (this.difficulty) {
            case 'hard': return 1000; // Fast checks
            case 'medium': return 2000;
            default: return 3500; // Slow
        }
    }

    update(timestamp) {
        if (timestamp - this.lastActionTime > this.actionInterval) {
            this.lastActionTime = timestamp;
            this.decideAction();
        }

        this.checkDanger();
    }

    checkDanger() {
        if (this.difficulty === 'easy') return; // Easy AI doesn't dodge well

        // Check if any projectile is coming towards an AI unit
        // "Sensing danger"
        const evasionRadius = this.difficulty === 'hard' ? 150 : 80;

        this.game.units.filter(u => u.team === 'red' && u.type === 'tank').forEach(tank => {
            const danger = this.game.projectiles.some(p => {
                const dist = Math.hypot(p.x - tank.x, p.y - tank.y);
                // Simple prediction: is it within radius and moving towards me?
                // Just distance check for now
                return dist < evasionRadius && p.team !== 'red'; // Assuming projectiles have owners/teams
            });

            if (danger) {
                // Evasion Maneuver: Move randomly
                tank.move(Math.random() > 0.5 ? 1 : -1, this.game.terrain);
            }
        });
    }

    decideAction() {
        // 1. Economy: Buy stuff?
        if (this.shouldBuy()) {
            this.buyUnit();
            return;
        }

        // 2. Attack: Pick a unit and fire
        const myUnits = this.game.units.filter(u => u.team === 'red');
        if (myUnits.length === 0) return;

        const attacker = myUnits[Math.floor(Math.random() * myUnits.length)];
        const target = this.findTarget();

        if (attacker && target) {
            if (attacker.type === 'tank') {
                this.aimAndFireTank(attacker, target);
            } else if (attacker.type === 'plane') {
                this.dropBomb(attacker, target);
            }
        }
    }

    shouldBuy() {
        // Hard AI buys more aggressively
        const money = this.game.enemyCurrency || 0;
        const threshold = this.difficulty === 'hard' ? 600 : 1000;
        return money > threshold && Math.random() > 0.3;
    }

    buyUnit() {
        // Logic to interface with game buy method (to be implemented in main)
        // this.game.enemyBuy('tank');
        console.log("AI deciding to buy...");
    }

    findTarget() {
        const targets = this.game.units.filter(u => u.team === 'blue');
        if (targets.length === 0) return null;
        return targets[Math.floor(Math.random() * targets.length)];
    }

    aimAndFireTank(tank, target) {
        // Calculate physics trajectory specific to wind
        // v^2 = (g * x^2) / (2 * cos^2(theta) * (x * tan(theta) - y))... complex.

        // heuristic aim
        let dx = target.x - tank.x;
        let dy = target.y - tank.y;

        // Wind compensation
        let windFactor = this.game.wind * 100; // Arbitrary scaler

        // Error for difficulty
        let error = 0;
        if (this.difficulty === 'easy') error = (Math.random() - 0.5) * 200;
        if (this.difficulty === 'medium') error = (Math.random() - 0.5) * 100;

        let aimX = dx - windFactor + error;
        // Logic to set turret angle would go here... for now just fire

        // Simulating a fire event
        // Ideally we calculate the distinct angle/power.
        // For prototype, we'll just fire in general direction.

        const angle = Math.atan2(dy - 100, dx); // Aim slightly higher
        const power = Math.min(Math.hypot(dx, dy) * 0.15, 20); // Cap power

        this.game.fireProjectile(tank, angle, power);
    }

    dropBomb(plane, target) {
        // If overhead, drop
        if (Math.abs(plane.x - target.x) < 50) {
            this.game.fireProjectile(plane, Math.PI / 2, 0); // Drop straight down?
        }
    }
}
