/**
 * Question Validator
 * Validates generated questions for structure, logic, and quality
 */

class QuestionValidator {
    /**
     * Validate a question object
     * @param {Object} questionData - The question to validate
     * @param {string} subject - The subject (for subject-specific validation)
     * @returns {Object} { valid: boolean, errors: string[] }
     */
    validate(questionData, subject = '') {
        const errors = [];

        // Structure validation
        const structureErrors = this.validateStructure(questionData);
        errors.push(...structureErrors);

        if (structureErrors.length > 0) {
            return { valid: false, errors };
        }

        // Logic validation
        const logicErrors = this.validateLogic(questionData, subject);
        errors.push(...logicErrors);

        // Quality validation
        const qualityErrors = this.validateQuality(questionData);
        errors.push(...qualityErrors);

        return {
            valid: errors.length === 0,
            errors
        };
    }

    /**
     * Validate JSON structure
     */
    validateStructure(q) {
        const errors = [];

        if (!q || typeof q !== 'object') {
            errors.push('Question must be an object');
            return errors;
        }

        if (!q.text || typeof q.text !== 'string' || q.text.trim().length === 0) {
            errors.push('Question text is missing or empty');
        }

        if (!Array.isArray(q.options)) {
            errors.push('Options must be an array');
        } else if (q.options.length !== 4) {
            errors.push(`Expected 4 options, got ${q.options.length}`);
        }

        if (!q.correctAnswer || typeof q.correctAnswer !== 'string') {
            errors.push('correctAnswer is missing or not a string');
        }

        return errors;
    }

    /**
     * Validate logic and correctness
     */
    validateLogic(q, subject) {
        const errors = [];

        // Ensure correctAnswer is in options
        const trimmedOptions = q.options.map(o => String(o).trim());
        const trimmedCorrect = String(q.correctAnswer).trim();

        if (!trimmedOptions.includes(trimmedCorrect)) {
            errors.push(`correctAnswer "${trimmedCorrect}" not found in options: [${trimmedOptions.join(', ')}]`);
        }

        // Subject-specific validation
        if (subject) {
            const subjectLower = subject.toLowerCase();
            const questionLower = q.text.toLowerCase();

            // Prevent math questions in non-math subjects
            if (subjectLower === 'english' || subjectLower === 'hindi') {
                const mathKeywords = ['area', 'perimeter', 'radius', 'diameter', 'calculate', 'equation', 'solve', 'cm²', 'meters'];
                const hasMathKeyword = mathKeywords.some(kw => questionLower.includes(kw));

                if (hasMathKeyword) {
                    errors.push(`Math-related question detected in ${subject} subject`);
                }
            }

            // Prevent language questions in math/science
            if (subjectLower === 'maths' || subjectLower === 'science') {
                const langKeywords = ['poem', 'story', 'character', 'author', 'rhyme', 'grammar'];
                const hasLangKeyword = langKeywords.some(kw => questionLower.includes(kw));

                if (hasLangKeyword) {
                    errors.push(`Language-related question detected in ${subject} subject`);
                }
            }
        }

        return errors;
    }

    /**
     * Validate quality standards
     */
    validateQuality(q) {
        const errors = [];

        // Question should end with "?"
        if (!q.text.trim().endsWith('?')) {
            errors.push('Question should end with a question mark');
        }

        // Check for placeholder options
        const placeholderPattern = /^option\s*[a-d]$/i;
        const hasPlaceholders = q.options.some(opt =>
            placeholderPattern.test(String(opt).trim())
        );

        if (hasPlaceholders) {
            errors.push('Options contain placeholder text like "Option A"');
        }

        // Options should be distinct
        const uniqueOptions = new Set(q.options.map(o => String(o).trim().toLowerCase()));
        if (uniqueOptions.size !== q.options.length) {
            errors.push('Options must be distinct (found duplicates)');
        }

        // Options should not be empty
        const hasEmptyOption = q.options.some(opt => !String(opt).trim());
        if (hasEmptyOption) {
            errors.push('One or more options are empty');
        }

        // Question should not be too short
        if (q.text.trim().length < 10) {
            errors.push('Question text is too short');
        }

        return errors;
    }

    /**
     * Check if a question is a duplicate
     * @param {Object} question - The question to check
     * @param {Array} history - Array of previously asked questions
     * @returns {boolean} - True if duplicate
     */
    isDuplicate(question, history) {
        if (!history || history.length === 0) return false;

        const normalizedText = question.text.trim().toLowerCase();

        return history.some(prevQ =>
            prevQ.text.trim().toLowerCase() === normalizedText
        );
    }
}

export const questionValidator = new QuestionValidator();
