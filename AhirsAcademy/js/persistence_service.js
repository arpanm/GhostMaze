/**
 * Persistence Service - Tracks answered questions in localStorage
 */

class PersistenceService {
    constructor() {
        this.STORAGE_KEY = 'ahirs_academy_progress';
        this.progress = this.loadProgress();
    }

    loadProgress() {
        try {
            const data = localStorage.getItem(this.STORAGE_KEY);
            return data ? JSON.parse(data) : { answeredIds: {} };
        } catch (e) {
            console.error('[PersistenceService] Error loading progress:', e);
            return { answeredIds: {} };
        }
    }

    saveProgress() {
        try {
            localStorage.setItem(this.STORAGE_KEY, JSON.stringify(this.progress));
        } catch (e) {
            console.error('[PersistenceService] Error saving progress:', e);
        }
    }

    /**
     * Generate a simple hash for the question text
     * @param {string} text 
     * @returns {string}
     */
    generateHash(text) {
        let hash = 0;
        const cleanText = text.trim().toLowerCase();
        for (let i = 0; i < cleanText.length; i++) {
            const char = cleanText.charCodeAt(i);
            hash = ((hash << 5) - hash) + char;
            hash = hash & hash; // Convert to 32bit integer
        }
        return hash.toString(16);
    }

    /**
     * Mark a question as answered
     * @param {string} classId 
     * @param {string} subjectId 
     * @param {string} questionText 
     */
    markAsAnswered(classId, subjectId, questionText) {
        const key = `${classId}_${subjectId}`;
        if (!this.progress.answeredIds[key]) {
            this.progress.answeredIds[key] = [];
        }

        const hash = this.generateHash(questionText);
        if (!this.progress.answeredIds[key].includes(hash)) {
            this.progress.answeredIds[key].push(hash);
            this.saveProgress();
            console.log(`[PersistenceService] Question marked as answered: ${hash}`);
        }
    }

    /**
     * Check if a question has been answered
     * @param {string} classId 
     * @param {string} subjectId 
     * @param {string} questionText 
     * @returns {boolean}
     */
    isAnswered(classId, subjectId, questionText) {
        const key = `${classId}_${subjectId}`;
        const questions = this.progress.answeredIds[key];
        if (!questions) return false;

        const hash = this.generateHash(questionText);
        return questions.includes(hash);
    }

    /**
     * Get count of answered questions for a class/subject
     * @param {string} classId 
     * @param {string} subjectId 
     * @returns {number}
     */
    getAnsweredCount(classId, subjectId) {
        const key = `${classId}_${subjectId}`;
        return this.progress.answeredIds[key]?.length || 0;
    }

    /**
     * Get all answered hashes for a class/subject
     * @param {string} classId 
     * @param {string} subjectId 
     * @returns {string[]}
     */
    getAnsweredHashes(classId, subjectId) {
        const key = `${classId}_${subjectId}`;
        return this.progress.answeredIds[key] || [];
    }
}

export const persistenceService = new PersistenceService();
