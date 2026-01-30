export class AhirEconomy {
    constructor() {
        this.storageKey = 'ahir_coin_balance';
        this.historyKey = 'ahir_coin_history';
        this.initialBalance = 100;
        this.initialize();
    }

    initialize() {
        if (localStorage.getItem(this.storageKey) === null) {
            localStorage.setItem(this.storageKey, this.initialBalance.toString());
            this.logTransaction(this.initialBalance, 'Welcome Bonus');
        }
    }

    getBalance() {
        return parseInt(localStorage.getItem(this.storageKey) || '0', 10);
    }

    /**
     * @param {number} amount
     * @param {string} reason
     * @returns {boolean}
     */
    addCoins(amount, reason) {
        if (amount <= 0) return false;
        const current = this.getBalance();
        const newBalance = current + amount;
        localStorage.setItem(this.storageKey, newBalance.toString());
        this.logTransaction(amount, reason, 'credit');
        return true;
    }

    /**
     * @param {number} amount
     * @param {string} reason
     * @returns {boolean} true if successful, false if insufficient funds
     */
    spendCoins(amount, reason) {
        if (amount <= 0) return false;
        const current = this.getBalance();
        if (current < amount) return false;

        const newBalance = current - amount;
        localStorage.setItem(this.storageKey, newBalance.toString());
        this.logTransaction(amount, reason, 'debit');
        return true;
    }

    /**
     * @param {number} amount
     * @returns {boolean}
     */
    hasEnoughBalance(amount) {
        return this.getBalance() >= amount;
    }

    logTransaction(amount, reason, type = 'credit') {
        const history = JSON.parse(localStorage.getItem(this.historyKey) || '[]');
        history.unshift({
            timestamp: new Date().toISOString(),
            amount: amount,
            type: type, // 'credit' or 'debit'
            reason: reason,
            balanceAfter: this.getBalance()
        });
        // Keep last 50 transactions
        if (history.length > 50) history.pop();
        localStorage.setItem(this.historyKey, JSON.stringify(history));
    }

    getHistory() {
        return JSON.parse(localStorage.getItem(this.historyKey) || '[]');
    }
}

// Singleton instance for easy usage if imported directly
export const economy = new AhirEconomy();
