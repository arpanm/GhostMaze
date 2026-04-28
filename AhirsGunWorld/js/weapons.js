// Weapon definitions and modification system
export const WEAPONS = {
    pistol:   { id: 'pistol',   name: 'Pistol',          symbol: '🔫', type: 'gun',       damage: 10, fireRate: 400,  range: 250, speed: 8, cost: 0,    ammo: Infinity },
    rifle:    { id: 'rifle',    name: 'Assault Rifle',   symbol: '🔫', type: 'gun',       damage: 15, fireRate: 200,  range: 350, speed: 10, cost: 500,  ammo: Infinity },
    sniper:   { id: 'sniper',   name: 'Sniper Rifle',    symbol: '🎯', type: 'gun',       damage: 40, fireRate: 1200, range: 600, speed: 15, cost: 1500, ammo: Infinity },
    smg:      { id: 'smg',      name: 'SMG',             symbol: '💨', type: 'gun',       damage: 8,  fireRate: 100,  range: 200, speed: 9, cost: 800,  ammo: Infinity },
    knife:    { id: 'knife',    name: 'Combat Knife',    symbol: '🔪', type: 'melee',     damage: 25, fireRate: 300,  range: 40,  speed: 0, cost: 200,  ammo: Infinity },
    laser:    { id: 'laser',    name: 'Laser Glasses',   symbol: '😎', type: 'beam',      damage: 5,  fireRate: 50,   range: 300, speed: 20, cost: 2000, ammo: Infinity },
    rocket:   { id: 'rocket',   name: 'Rocket Launcher', symbol: '🚀', type: 'explosive', damage: 60, fireRate: 2000, range: 400, speed: 6, cost: 3000, ammo: Infinity }
};

export const MODS = {
    silencer:  { id: 'silencer',  name: 'Silencer',      symbol: '🤫', cost: 300,  effect: { stealth: true } },
    extmag:    { id: 'extmag',    name: 'Extended Mag',  symbol: '📦', cost: 400,  effect: { fireRateMult: 0.85 } },
    scope:     { id: 'scope',     name: 'Scope',         symbol: '🔭', cost: 500,  effect: { rangeMult: 1.3 } },
    rapidfire: { id: 'rapidfire', name: 'Rapid Fire',    symbol: '⚡', cost: 600,  effect: { fireRateMult: 0.6 } }
};

export const STORE_ITEMS = [
    { id: 'heal', name: 'Med Kit', symbol: '❤️', desc: 'Restore +30 HP', cost: 200, type: 'consumable' },
    { id: 'shield_boost', name: 'Shield Charge', symbol: '🛡️', desc: 'Restore shield to full', cost: 500, type: 'consumable' },
    { id: 'pet_heal', name: 'Pet Treat', symbol: '🦴', desc: 'Heal your pet +50 HP', cost: 150, type: 'consumable' },
    ...Object.values(WEAPONS).filter(w => w.cost > 0).map(w => ({ id: w.id, name: w.name, symbol: w.symbol, desc: `${w.damage} DMG • ${w.type}`, cost: w.cost, type: 'weapon' })),
    ...Object.values(MODS).map(m => ({ id: m.id, name: m.name, symbol: m.symbol, desc: 'Weapon mod', cost: m.cost, type: 'mod' }))
];

export function getWeapon(id) {
    const base = WEAPONS[id];
    if (!base) return null;
    return { ...base };
}

export function applyMod(weapon, modId) {
    const mod = MODS[modId];
    if (!mod) return weapon;
    const w = { ...weapon };
    if (!w.mods) w.mods = [];
    if (w.mods.includes(modId)) return w;
    w.mods.push(modId);
    if (mod.effect.fireRateMult) w.fireRate = Math.floor(w.fireRate * mod.effect.fireRateMult);
    if (mod.effect.rangeMult) w.range = Math.floor(w.range * mod.effect.rangeMult);
    if (mod.effect.stealth) w.stealth = true;
    return w;
}
