// AI controllers for friendly teammates and enemies

export class FriendlyAI {
    update(dt, teammate, player, enemies, projectiles, map, now) {
        if (!teammate.alive) return;
        teammate.stateTimer -= dt;

        // Shield logic
        if (teammate.health < 40 && teammate.shield > 0) {
            teammate.shieldActive = true;
        } else {
            teammate.shieldActive = false;
        }

        // Find nearest enemy
        let nearestEnemy = null;
        let nearestDist = Infinity;
        for (const e of enemies) {
            if (!e.alive) continue;
            const d = Math.hypot(e.x - teammate.x, e.y - teammate.y);
            if (d < nearestDist) { nearestDist = d; nearestEnemy = e; }
        }

        // State machine
        if (teammate.health < 25 && teammate.aiState !== 'retreat') {
            teammate.aiState = 'retreat';
            teammate.stateTimer = 3000;
        }

        switch (teammate.aiState) {
            case 'follow': {
                // Follow player with offset
                const tx = player.x + teammate.followOffset.x;
                const ty = player.y + teammate.followOffset.y;
                const dx = tx - teammate.x;
                const dy = ty - teammate.y;
                const dist = Math.hypot(dx, dy);
                if (dist > 20) {
                    teammate.move(dx / dist, dy / dist, map);
                }
                // Switch to engage if enemy nearby
                if (nearestEnemy && nearestDist < 250) {
                    teammate.aiState = 'engage';
                    teammate.targetEnemy = nearestEnemy;
                }
                break;
            }
            case 'engage': {
                if (!nearestEnemy || !nearestEnemy.alive) {
                    teammate.aiState = 'follow';
                    break;
                }
                // Move towards enemy but stop at weapon range
                const dx = nearestEnemy.x - teammate.x;
                const dy = nearestEnemy.y - teammate.y;
                if (nearestDist > teammate.weapon.range * 0.7) {
                    teammate.move(dx / nearestDist, dy / nearestDist, map);
                }
                // Fire
                if (nearestDist < teammate.weapon.range) {
                    teammate.fire(now, nearestEnemy.x, nearestEnemy.y, projectiles);
                }
                // Back to follow if no enemies close
                if (nearestDist > 350) {
                    teammate.aiState = 'follow';
                }
                break;
            }
            case 'retreat': {
                // Move towards player
                const dx = player.x - teammate.x;
                const dy = player.y - teammate.y;
                const dist = Math.hypot(dx, dy);
                if (dist > 30) {
                    teammate.move(dx / dist, dy / dist, map);
                }
                if (teammate.stateTimer <= 0 || teammate.health > 50) {
                    teammate.aiState = 'follow';
                }
                break;
            }
        }
    }
}

export class EnemyAI {
    update(dt, enemy, greenTeam, projectiles, map, now) {
        if (!enemy.alive) return;
        enemy.stateTimer -= dt;

        // Shield logic
        if (enemy.health < enemy.maxHealth * 0.3 && enemy.shield > 0) {
            enemy.shieldActive = true;
        } else {
            enemy.shieldActive = false;
        }

        // Find nearest green unit
        let nearestGreen = null;
        let nearestDist = Infinity;
        for (const g of greenTeam) {
            if (!g.alive) continue;
            // If player is in sub mode, enemies can't see them
            if (g.vehicleMode === 'sub') continue;
            const d = Math.hypot(g.x - enemy.x, g.y - enemy.y);
            if (d < nearestDist) { nearestDist = d; nearestGreen = g; }
        }

        switch (enemy.aiState) {
            case 'patrol': {
                // Random patrol
                if (!enemy.patrolTarget || enemy.stateTimer <= 0) {
                    const cols = map.cols, rows = map.rows, ts = map.tileSize;
                    let attempts = 0;
                    do {
                        enemy.patrolTarget = {
                            x: (3 + Math.floor(Math.random() * (cols - 6))) * ts,
                            y: (3 + Math.floor(Math.random() * (rows - 6))) * ts
                        };
                        attempts++;
                    } while (map.isWall(enemy.patrolTarget.x, enemy.patrolTarget.y, enemy.radius) && attempts < 10);
                    enemy.stateTimer = 4000;
                }
                const dx = enemy.patrolTarget.x - enemy.x;
                const dy = enemy.patrolTarget.y - enemy.y;
                const dist = Math.hypot(dx, dy);
                if (dist > 10) {
                    enemy.move(dx / dist, dy / dist, map);
                }
                // Detect player
                if (nearestGreen && nearestDist < 200 + enemy.accuracy * 100) {
                    enemy.aiState = 'chase';
                    enemy.targetEntity = nearestGreen;
                }
                break;
            }
            case 'chase': {
                if (!nearestGreen || !nearestGreen.alive) {
                    enemy.aiState = 'patrol';
                    break;
                }
                const dx = nearestGreen.x - enemy.x;
                const dy = nearestGreen.y - enemy.y;
                if (nearestDist > enemy.weapon.range * 0.6) {
                    enemy.move(dx / nearestDist, dy / nearestDist, map);
                }
                if (nearestDist < enemy.weapon.range) {
                    enemy.aiState = 'attack';
                    enemy.targetEntity = nearestGreen;
                }
                if (nearestDist > 400) {
                    enemy.aiState = 'patrol';
                }
                break;
            }
            case 'attack': {
                if (!nearestGreen || !nearestGreen.alive) {
                    enemy.aiState = 'patrol';
                    break;
                }
                // Fire with accuracy jitter
                if (nearestDist < enemy.weapon.range) {
                    const jitter = (1 - enemy.accuracy) * 40;
                    const tx = nearestGreen.x + (Math.random() - 0.5) * jitter;
                    const ty = nearestGreen.y + (Math.random() - 0.5) * jitter;
                    enemy.fire(now, tx, ty, projectiles);
                }
                // Strafe a bit
                const perpX = -(nearestGreen.y - enemy.y);
                const perpY = nearestGreen.x - enemy.x;
                const perpDist = Math.hypot(perpX, perpY);
                if (perpDist > 0) {
                    const dir = Math.sin(now / 800) > 0 ? 1 : -1;
                    enemy.move(dir * perpX / perpDist * 0.5, dir * perpY / perpDist * 0.5, map);
                }
                // Flee if low health
                if (enemy.health < enemy.maxHealth * 0.2) {
                    enemy.aiState = 'flee';
                    enemy.stateTimer = 3000;
                }
                if (nearestDist > enemy.weapon.range * 1.2) {
                    enemy.aiState = 'chase';
                }
                break;
            }
            case 'flee': {
                if (nearestGreen) {
                    const dx = enemy.x - nearestGreen.x;
                    const dy = enemy.y - nearestGreen.y;
                    const dist = Math.hypot(dx, dy);
                    if (dist > 0) {
                        enemy.move(dx / dist, dy / dist, map);
                    }
                }
                if (enemy.stateTimer <= 0) {
                    enemy.aiState = 'patrol';
                }
                break;
            }
        }
    }
}
