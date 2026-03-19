/**
 * Shared Local LLM Service - Runs a small LLM in the browser using Transformers.js
 */

import { pipeline } from 'https://cdn.jsdelivr.net/npm/@xenova/transformers@2.17.1';

class LocalLLMService {
    constructor() {
        this.generator = null;
        this.isLoaded = false;
        this.isLoading = false;
        this.status = '';
        this.modelName = 'Xenova/Qwen2-0.5B-Instruct';
    }

    async init() {
        if (this.isLoaded) return;
        
        if (this.isLoading) {
            // Already loading, wait if there's a promise
            if (this.initPromise) return this.initPromise;
            // Otherwise just wait a bit (fallback)
            return new Promise(resolve => {
                const check = () => {
                    if (this.isLoaded) resolve();
                    else setTimeout(check, 100);
                };
                check();
            });
        }
        
        this.isLoading = true;
        this.initPromise = (async () => {
            this.status = 'Initializing local AI model...';
            console.log(`[LocalLLMService] 🔄 ${this.status}`);
            
            try {
                this.generator = await pipeline('text-generation', this.modelName, {
                    progress_callback: (p) => {
                        this.status = `Downloading Local AI: ${Math.round(p.progress || 0)}%`;
                        if (window.app && window.app.updateLoadingStatus) {
                            window.app.updateLoadingStatus(this.status);
                        }
                    }
                });
                this.isLoaded = true;
                this.status = 'Local AI Ready';
                console.log('[LocalLLMService] ✅ Model loaded');
            } catch (error) {
                console.error('[LocalLLMService] ✗ Failed to load model:', error);
                this.isLoading = false; // Allow retry on failure
                throw error;
            } finally {
                this.initPromise = null;
            }
        })();

        return this.initPromise;
    }

    /**
     * Generate a question for AhirsAcademy
     */
    async generateQuestion(classId, subjectId, difficulty) {
        await this.init();
        const className = classId.replace('class_', '');
        const subjectName = subjectId.charAt(0).toUpperCase() + subjectId.slice(1);

        const prompt = `You are a teacher for Class ${className}. Generate ONE multiple-choice question for ${subjectName}. Difficulty: ${difficulty}. Format: JSON object with "text", "options" (array of 4), "correctAnswer".`;
        return this.generateFromPrompt(prompt);
    }

    /**
     * Generate a hint for AhirsSpy
     */
    async generateSpyHint(killerTraits) {
        await this.init();
        const prompt = `You are a secret agent's handler. Based on these clues: ${killerTraits.join(', ')}. Generate a very short, cryptic hint for the agent to find the killer. Max 10 words.`;
        const response = await this.generateFromPrompt(prompt, false);
        return typeof response === 'string' ? response : (response.text || response.hint || "Check suspicious movements.");
    }

    async generateFromPrompt(prompt, jsonMode = true) {
        const formattedPrompt = `<|im_start|>system\nYou are a helpful assistant.<|im_end|>\n<|im_start|>user\n${prompt}<|im_end|>\n<|im_start|>assistant\n`;

        const output = await this.generator(formattedPrompt, {
            max_new_tokens: 256,
            temperature: 0.7,
            do_sample: true,
            top_k: 50,
            return_full_text: false
        });

        const text = output[0].generated_text.trim();
        if (!jsonMode) return text;

        try {
            const jsonMatch = text.match(/\{[\s\S]*?\}/);
            return jsonMatch ? JSON.parse(jsonMatch[0]) : { text };
        } catch (e) {
            return { text };
        }
    }
}

export const localLLMService = new LocalLLMService();
