/**
 * Economy class - Tracks coin balance in localStorage
 */

export class Economy {
    constructor() {
        this.storageKey = 'ahir_coin_balance';
    }

    getBalance() {
        const coins = localStorage.getItem(this.storageKey);
        return coins ? parseInt(coins) : 100; // Default to 100 if new user
    }

    addCoins(amount, reason = 'Mission Reward') {
        const current = this.getBalance();
        localStorage.setItem(this.storageKey, current + amount);
        console.log(`Economy: +${amount} coins (${reason}). New balance: ${this.getBalance()}`);
    }

    spendCoins(amount, reason = 'Mission Entry') {
        const current = this.getBalance();
        if (current >= amount) {
            localStorage.setItem(this.storageKey, current - amount);
            console.log(`Economy: -${amount} coins (${reason}). New balance: ${this.getBalance()}`);
            return true;
        }
        return false;
    }
}
