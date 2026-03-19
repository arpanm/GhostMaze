/**
 * Economy class - Tracks coin balance in localStorage
 */

export class Economy {
    constructor() {
        this.storageKey = 'ahir_coin_balance';
        this.historyKey = 'ahir_coin_history';
    }

    getBalance() {
        const coins = localStorage.getItem(this.storageKey);
        return coins ? parseInt(coins) : 100; // Default 100 on first load
    }

    spendCoins(amount, reason = 'Chinese Checkers Entry') {
        const balance = this.getBalance();
        if (balance >= amount) {
            const newBalance = balance - amount;
            localStorage.setItem(this.storageKey, newBalance.toString());
            this.logTransaction(amount, reason, 'debit');
            return true;
        }
        return false;
    }

    logTransaction(amount, reason, type = 'credit') {
        const history = JSON.parse(localStorage.getItem(this.historyKey) || '[]');
        history.unshift({
            timestamp: new Date().toISOString(),
            amount: amount,
            type: type,
            reason: reason,
            balanceAfter: this.getBalance()
        });
        if (history.length > 50) history.pop();
        localStorage.setItem(this.historyKey, JSON.stringify(history));
    }
}
