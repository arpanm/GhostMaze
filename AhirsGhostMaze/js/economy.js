export class AhirEconomy {
    constructor() {
        this.storageKey = 'ahir_coin_balance';
        this.historyKey = 'ahir_coin_history';
        this.initialBalance = 100;
        // Logic duplicated for standalone safety, ensuring same localStorage keys
    }

    getBalance() {
        return parseInt(localStorage.getItem(this.storageKey) || (this.initialBalance).toString(), 10);
    }

    spendCoins(amount, reason) {
        if (amount <= 0) return false;
        const current = this.getBalance();
        if (current < amount) return false;

        const newBalance = current - amount;
        localStorage.setItem(this.storageKey, newBalance.toString());
        this.logTransaction(amount, reason, 'debit');
        return true;
    }

    hasEnoughBalance(amount) {
        return this.getBalance() >= amount;
    }

    addCoins(amount, reason) {
        if (amount <= 0) return false;
        const current = this.getBalance();
        const newBalance = current + amount;
        localStorage.setItem(this.storageKey, newBalance.toString());
        this.logTransaction(amount, reason, 'credit');
        return true;
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

export const economy = new AhirEconomy();
