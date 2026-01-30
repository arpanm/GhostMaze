export class AdaptiveDifficulty {
    constructor() {
        this.storageKey = 'ahir_academy_stats';
        this.levels = ['EASY', 'MEDIUM', 'HARD'];
        this.stats = this.loadStats();
    }

    loadStats() {
        const stored = localStorage.getItem(this.storageKey);
        if (!stored) {
            return {
                currentDifficultyIndex: 0, // 0=EASY
                currentStreak: 0,
                totalQuestions: 0,
                correctAnswers: 0,
                history: []
            };
        }
        return JSON.parse(stored);
    }

    saveStats() {
        localStorage.setItem(this.storageKey, JSON.stringify(this.stats));
    }

    getCurrentDifficulty() {
        return this.levels[this.stats.currentDifficultyIndex];
    }

    recordResult(isCorrect) {
        this.stats.totalQuestions++;
        if (isCorrect) {
            this.stats.correctAnswers++;
            this.stats.currentStreak++;
            this.checkUpgrade();
        } else {
            this.stats.currentStreak = 0;
            this.checkDowngrade();
        }
        this.saveStats();
    }

    checkUpgrade() {
        // Upgrade if streak > 3 and not already at max
        if (this.stats.currentStreak >= 3 && this.stats.currentDifficultyIndex < this.levels.length - 1) {
            this.stats.currentDifficultyIndex++;
            this.stats.currentStreak = 0; // Reset streak on level change
            console.log("Upgraded to", this.getCurrentDifficulty());
        }
    }

    checkDowngrade() {
        // Downgrade if wrong answer and not at min
        // Optional: Could require 2 wrong in a row to strictly downgrade, 
        // but for now immediate downgrade helps reducing frustration.
        if (this.stats.currentDifficultyIndex > 0) {
            this.stats.currentDifficultyIndex--;
            console.log("Downgraded to", this.getCurrentDifficulty());
        }
    }

    getStats() {
        return {
            difficulty: this.getCurrentDifficulty(),
            accuracy: this.stats.totalQuestions === 0 ? 0 : Math.round((this.stats.correctAnswers / this.stats.totalQuestions) * 100),
            streak: this.stats.currentStreak
        };
    }
}

export const adaptiveDifficulty = new AdaptiveDifficulty();
