/**
 * AI Service - Simplified with hard-coded model priority
 * Tries models in order, no caching, strict error handling
 */

const API_CONFIG = {
    apiKey: 'AIzaSyCeCArTxIyT3ch_QNJDUJYFjaRO0TOq910',
    // Priority order: All available models from fastest/cheapest to most capable
    modelPriority: [
        'models/gemini-2.5-flash-lite',
        'models/gemini-2.0-flash-lite',
        'models/gemini-2.5-flash',
        'models/gemini-3-flash-preview',
        'models/gemini-3-pro-preview',
        'models/gemini-2.5-pro',
        'models/gemini-1.5-flash-latest',
        'models/gemini-2.0-flash-exp',
        'models/gemini-2.0-pro-exp',
        'models/gemini-1.5-pro-latest'
    ]
};

class AIService {
    constructor() {
        this.failedModels = new Set(); // Track failed models for this session
    }

    /**
     * Generate content using AI with automatic model fallback
     * @param {string} prompt - The prompt to send
     * @returns {Promise<Object>} - The AI response
     */
    async generateContent(prompt) {
        const availableModels = API_CONFIG.modelPriority.filter(
            model => !this.failedModels.has(model)
        );

        if (availableModels.length === 0) {
            throw new Error('All AI models have failed. Please try again later.');
        }

        let lastError = null;

        for (const model of availableModels) {
            try {
                console.log(`[AIService] Trying model: ${model}`);

                const response = await this.callModel(model, prompt);

                // Success! Return the response
                console.log(`[AIService] ✓ Success with ${model}`);
                return response;

            } catch (error) {
                console.warn(`[AIService] ✗ Failed with ${model}:`, error.message);
                lastError = error;

                // Mark this model as failed for the session
                this.failedModels.add(model);

                // Continue to next model
                continue;
            }
        }

        // All models failed
        throw lastError || new Error('All AI models failed');
    }

    /**
     * Call a specific model
     * @param {string} model - Model name
     * @param {string} prompt - The prompt
     * @returns {Promise<Object>} - The response
     */
    async callModel(model, prompt) {
        const url = `https://generativelanguage.googleapis.com/v1beta/${model}:generateContent?key=${API_CONFIG.apiKey}`;

        let response;

        try {
            response = await fetch(url, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    contents: [{ parts: [{ text: prompt }] }],
                    generationConfig: {
                        temperature: 0.7,
                        maxOutputTokens: 2000  // Increased to prevent truncation
                    }
                })
            });
        } catch (fetchError) {
            throw new Error(`Network error: ${fetchError.message}`);
        }

        // Handle HTTP errors
        if (!response.ok) {
            if (response.status === 429) {
                throw new Error('Rate limit exceeded');
            }
            if (response.status === 503) {
                throw new Error('Service unavailable');
            }

            const errorData = await response.json().catch(() => ({}));
            const errorMsg = errorData.error?.message || `HTTP ${response.status}`;
            throw new Error(errorMsg);
        }

        // Parse and return
        return await response.json();
    }

    /**
     * Reset failed models (call this if you want to retry all models)
     */
    resetFailedModels() {
        this.failedModels.clear();
        console.log('[AIService] Reset failed models list');
    }
}

export const aiService = new AIService();
