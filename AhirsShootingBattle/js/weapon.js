export const WEAPONS = {
    pistol: {
        id: 'pistol',
        name: 'Pistol',
        symbol: '🔫',
        price: 0,
        dmg: 10,
        speed: 1, // Cooldown multiplier (1 = normal)
        range: 1000,
        projectileSpeed: 10,
        fireRate: 500 // ms
    },
    rifle: {
        id: 'rifle',
        name: 'Assault Rifle',
        symbol: '🔫',
        price: 5000,
        dmg: 15,
        speed: 0.5,
        range: 1000,
        projectileSpeed: 15,
        fireRate: 200
    },
    sniper: {
        id: 'sniper',
        name: 'Sniper Rifle',
        symbol: '🎯',
        price: 15000,
        dmg: 40,
        speed: 2,
        range: 1000,
        projectileSpeed: 25,
        fireRate: 1500
    },
    smg: {
        id: 'smg',
        name: 'SMG',
        symbol: '💨',
        price: 8000,
        dmg: 8,
        speed: 0.3,
        range: 800,
        projectileSpeed: 12,
        fireRate: 100
    },
    knife: {
        id: 'knife',
        name: 'Combat Knife',
        symbol: '🔪',
        price: 2000,
        dmg: 25,
        speed: 1,
        range: 100,
        projectileSpeed: 0, // Instant/Melee
        fireRate: 600
    }
};

export class WeaponSystem {
    static get(id) {
        return WEAPONS[id] || WEAPONS.pistol;
    }

    static handlePurchase(playerId, itemId, playerMoney) {
        if (itemId === 'heal') {
            if (playerMoney >= 2000) {
                return { success: true, cost: 2000, type: 'heal' };
            }
        } else if (itemId === 'decoy') {
            if (playerMoney >= 10000) {
                return { success: true, cost: 10000, type: 'decoy', charges: 3 };
            }
        } else {
            const weapon = WEAPONS[itemId];
            if (weapon && playerMoney >= weapon.price) {
                return { success: true, cost: weapon.price, type: 'weapon', item: weapon };
            }
        }
        return { success: false, reason: 'Insufficient funds' };
    }
}
