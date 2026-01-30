import { adaptiveDifficulty } from './adaptive_difficulty.js';
import { dataLoader } from './data_loader.js';
import { aiService } from './ai_service.js';
import { questionValidator } from './question_validator.js';

export class QuestionGenerator {
    constructor() {
        this.syllabusIndex = null;
        this.questionBank = null;
        this.questionHistory = []; // Track asked questions to prevent repeats
        this.maxHistorySize = 50; // Remember last 50 questions
        this.questionCache = {}; // Cache batches of questions by class_subject_difficulty
    }

    async init() {
        if (!this.syllabusIndex) {
            this.syllabusIndex = await dataLoader.loadIndex();
        }
        if (!this.questionBank) {
            this.questionBank = await dataLoader.loadQuestionBank();
        }
    }

    async generateQuestion(classId, subjectId) {
        await this.init();
        const difficulty = adaptiveDifficulty.getCurrentDifficulty();

        // Check if we have cached questions for this class/subject/difficulty
        const cacheKey = `${classId}_${subjectId}_${difficulty}`;

        if (!this.questionCache[cacheKey] || this.questionCache[cacheKey].length === 0) {
            console.log(`[QuestionGenerator] 📦 No cached questions for ${cacheKey}, generating batch...`);
            await this.generateBatch(classId, subjectId, difficulty, cacheKey);
        }

        // Get next question from cache
        if (this.questionCache[cacheKey] && this.questionCache[cacheKey].length > 0) {
            const question = this.questionCache[cacheKey].shift(); // Take first question
            this.addToHistory(question);
            console.log(`[QuestionGenerator] ✓ Serving cached question (${this.questionCache[cacheKey].length} remaining)`);
            return question;
        }

        // Cache is empty and generation failed, fallback to question bank
        console.log('[QuestionGenerator] ⚠️ Cache empty, using question bank');
        const bankQuestion = this.getFromBank(classId, subjectId, difficulty);

        if (bankQuestion) {
            this.addToHistory(bankQuestion);
            return bankQuestion;
        }

        // Ultimate fallback
        return this.createFallbackQuestion("Unable to generate question. Please try again.");
    }

    async generateBatch(classId, subjectId, difficulty, cacheKey) {
        // Only use models that actually exist in v1beta API
        const models = [
            'gemini-2.5-flash-lite',
            'gemini-2.0-flash-lite',
            'gemini-2.5-flash',
            'gemini-3-flash-preview',
            'gemini-3-pro-preview',
            'gemini-2.5-pro'
            // Removed: gemini-1.5-flash-latest, gemini-2.0-flash-exp, gemini-2.0-pro-exp, gemini-1.5-pro-latest (404 errors)
        ];

        // Try each model until one succeeds
        for (const model of models) {
            try {
                console.log(`[QuestionGenerator] 🔄 Trying batch generation with ${model}...`);

                const questions = await this.generateBatchWithAI(classId, subjectId, difficulty, model);

                if (questions && questions.length > 0) {
                    this.questionCache[cacheKey] = questions;
                    console.log(`[QuestionGenerator] ✅ Generated ${questions.length} questions with ${model}`);
                    return;
                }
            } catch (error) {
                console.warn(`[QuestionGenerator] ✗ Batch generation failed with ${model}:`, error.message);
                continue;
            }
        }

        // All models failed, populate cache from question bank
        console.log('[QuestionGenerator] ⚠️ All AI models failed, loading from question bank');
        const bankQuestions = this.getBatchFromBank(classId, subjectId, difficulty, 5);
        if (bankQuestions.length > 0) {
            this.questionCache[cacheKey] = bankQuestions;
            console.log(`[QuestionGenerator] ✓ Loaded ${bankQuestions.length} questions from bank`);
        }
    }

    async generateBatchWithAI(classId, subjectId, difficulty, modelName) {
        // Load syllabus context
        const classData = this.syllabusIndex.classes[classId];
        if (!classData || !classData.subjects[subjectId]) {
            throw new Error("Invalid Class/Subject");
        }

        const subjectMeta = classData.subjects[subjectId];
        const jsonPath = subjectMeta.json_file.replace(/^syllabus\//, '');
        const subjectData = await dataLoader.loadFile(jsonPath);

        // Build focused topic
        const topic = this.selectTopic(subjectData, subjectId);

        console.log(`[QuestionGenerator] Topic: ${topic}, Difficulty: ${difficulty}`);

        // Build strict prompt for batch generation
        const prompt = this.buildBatchPrompt(classId, subjectId, topic, difficulty);

        // Call AI directly (not through aiService to avoid nested model loops)
        const url = `https://generativelanguage.googleapis.com/v1beta/models/${modelName}:generateContent?key=AIzaSyCeCArTxIyT3ch_QNJDUJYFjaRO0TOq910`;

        const response = await fetch(url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                contents: [{ parts: [{ text: prompt }] }],
                generationConfig: {
                    temperature: 0.7,
                    maxOutputTokens: 3000  // Increased for batch generation
                }
            })
        });

        if (!response.ok) {
            const errorData = await response.json().catch(() => ({}));
            throw new Error(errorData.error?.message || `HTTP ${response.status}`);
        }

        const aiResponse = await response.json();

        // Parse response
        const rawText = aiResponse.candidates[0].content.parts[0].text;
        console.log("[QuestionGenerator] AI Raw Batch Response:", rawText);

        // Remove markdown code blocks if present
        let cleanText = rawText.replace(/```json\s*/g, '').replace(/```\s*/g, '');

        // Extract JSON array - be more careful about finding complete JSON
        // Look for [ ... ] pattern and ensure it's complete
        const arrayStart = cleanText.indexOf('[');
        const arrayEnd = cleanText.lastIndexOf(']');

        if (arrayStart === -1 || arrayEnd === -1 || arrayEnd <= arrayStart) {
            throw new Error("No complete JSON array found in response");
        }

        const jsonText = cleanText.substring(arrayStart, arrayEnd + 1);

        let rawQuestions;
        try {
            rawQuestions = JSON.parse(jsonText);
        } catch (parseError) {
            console.error("[QuestionGenerator] JSON Parse Error:", parseError.message);
            console.error("[QuestionGenerator] Attempted to parse:", jsonText.substring(0, 200));
            throw new Error(`JSON parse failed: ${parseError.message}`);
        }

        if (!Array.isArray(rawQuestions)) {
            throw new Error("Response is not an array");
        }

        const validQuestions = [];
        for (const qData of rawQuestions) {
            try {
                // Clean and validate each question
                const questionData = {
                    text: String(qData.text).trim(),
                    options: qData.options.map(o => String(o).trim()),
                    correctAnswer: String(qData.correctAnswer).trim()
                };

                const validation = questionValidator.validate(questionData, subjectId);

                if (validation.valid && !questionValidator.isDuplicate(questionData, this.questionHistory)) {
                    validQuestions.push({
                        text: questionData.text,
                        options: this.shuffle(questionData.options),
                        correctAnswer: questionData.correctAnswer,
                        difficulty: difficulty,
                        type: 'multiple-choice'
                    });
                } else {
                    console.warn('[QuestionGenerator] Skipped invalid/duplicate question from batch:', validation.errors || 'Duplicate');
                }
            } catch (parseError) {
                console.warn('[QuestionGenerator] Error parsing individual question from batch:', parseError.message);
            }
        }
        return validQuestions;
    }

    async generateWithAI(classId, subjectId, difficulty) {
        // Load syllabus context
        const classData = this.syllabusIndex.classes[classId];
        if (!classData || !classData.subjects[subjectId]) {
            throw new Error("Invalid Class/Subject");
        }

        const subjectMeta = classData.subjects[subjectId];
        const jsonPath = subjectMeta.json_file.replace(/^syllabus\//, '');
        const subjectData = await dataLoader.loadFile(jsonPath);

        // Build focused topic
        const topic = this.selectTopic(subjectData, subjectId);

        console.log(`[QuestionGenerator] Topic: ${topic}, Difficulty: ${difficulty}`);

        // Build strict prompt
        const prompt = this.buildPrompt(classId, subjectId, topic, difficulty);

        // Call AI
        const aiResponse = await aiService.generateContent(prompt);

        // Parse response
        const questionData = this.parseAIResponse(aiResponse);

        // Validate
        const validation = questionValidator.validate(questionData, subjectId);

        if (!validation.valid) {
            console.warn('[QuestionGenerator] Validation failed:', validation.errors);
            throw new Error(`Validation failed: ${validation.errors.join(', ')}`);
        }

        // Check for duplicates
        if (questionValidator.isDuplicate(questionData, this.questionHistory)) {
            console.warn('[QuestionGenerator] Duplicate question detected');
            throw new Error('Duplicate question');
        }

        // Success!
        return {
            text: questionData.text,
            options: this.shuffle(questionData.options),
            correctAnswer: questionData.correctAnswer,
            difficulty: difficulty,
            type: 'multiple-choice'
        };
    }

    buildPrompt(classId, subjectId, topic, difficulty) {
        const className = classId.replace('class_', '');
        const subjectName = subjectId.charAt(0).toUpperCase() + subjectId.slice(1);

        return `You are an expert ${subjectName} teacher for Class ${className}.

TASK: Generate ONE short, concise multiple-choice question.

CONSTRAINTS:
- Subject: ${subjectName} ONLY (DO NOT generate questions from other subjects)
- Topic: ${topic}
- Difficulty: ${difficulty}
- Class Level: ${className}
- Question Length: MAXIMUM 15 words

CRITICAL REQUIREMENTS:
1. **Subject Accuracy**: Question MUST be about ${subjectName}. No Math in English, no English in Math.
2. **Brevity**: Keep question SHORT and SIMPLE (max 15 words).
3. **Correctness**: Verify your answer is correct before generating options.
4. **Real Options**: Options must be actual values (e.g., "Paris", "42"), NOT "Option A".
5. **One Correct Answer**: Exactly one option must be correct.
6. **Distinct Options**: All 4 options must be different.

OUTPUT FORMAT - IMPORTANT:
- Output ONLY the JSON object below
- NO markdown code blocks
- NO explanations or extra text
- JUST the JSON:

{
  "text": "Short clear question?",
  "options": ["Answer1", "Answer2", "Answer3", "Answer4"],
  "correctAnswer": "Answer1"
}`;
    }

    buildBatchPrompt(classId, subjectId, topic, difficulty) {
        const className = classId.replace('class_', '');
        const subjectName = subjectId.charAt(0).toUpperCase() + subjectId.slice(1);

        return `You are an expert ${subjectName} teacher for Class ${className}.

TASK: Generate EXACTLY 5 short, concise multiple-choice questions.

CONSTRAINTS:
- Subject: ${subjectName} ONLY (DO NOT generate questions from other subjects)
- Topic: ${topic}
- Difficulty: ${difficulty}
- Class Level: ${className}
- Question Length: MAXIMUM 15 words each

CRITICAL REQUIREMENTS:
1. **Subject Accuracy**: All questions MUST be about ${subjectName}. No Math in English, no English in Math.
2. **Brevity**: Keep each question SHORT and SIMPLE (max 15 words).
3. **Correctness**: Verify answers are correct before generating options.
4. **Real Options**: Options must be actual values (e.g., "Paris", "42"), NOT "Option A".
5. **One Correct Answer**: Exactly one option must be correct per question.
6. **Distinct Options**: All 4 options must be different per question.
7. **Variety**: Make each question different from the others.

OUTPUT FORMAT - IMPORTANT:
- Output ONLY a JSON array of 5 question objects
- NO markdown code blocks
- NO explanations or extra text
- JUST the JSON array:

[
  {
    "text": "Short clear question 1?",
    "options": ["Answer1", "Answer2", "Answer3", "Answer4"],
    "correctAnswer": "Answer1"
  },
  {
    "text": "Short clear question 2?",
    "options": ["Answer1", "Answer2", "Answer3", "Answer4"],
    "correctAnswer": "Answer2"
  },
  {
    "text": "Short clear question 3?",
    "options": ["Answer1", "Answer2", "Answer3", "Answer4"],
    "correctAnswer": "Answer3"
  },
  {
    "text": "Short clear question 4?",
    "options": ["Answer1", "Answer2", "Answer3", "Answer4"],
    "correctAnswer": "Answer4"
  },
  {
    "text": "Short clear question 5?",
    "options": ["Answer1", "Answer2", "Answer3", "Answer4"],
    "correctAnswer": "Answer1"
  }
]`;
    }


    selectTopic(subjectData, subjectId) {
        const units = this.extractUnits(subjectData || {});

        if (units.length > 0) {
            const randomUnit = units[Math.floor(Math.random() * units.length)];
            return `${randomUnit.name}`;
        }

        // Fallback to subject name
        return subjectId.charAt(0).toUpperCase() + subjectId.slice(1);
    }

    extractUnits(data) {
        let items = [];
        if (data.units && Array.isArray(data.units)) {
            data.units.forEach(block => {
                if (block.rows) {
                    block.rows.forEach(row => {
                        if (row.length >= 2) {
                            items.push({
                                name: (row[1] || row[0]).trim(),
                                topics: row[2] || ""
                            });
                        }
                    });
                }
            });
        }
        return items.filter(i => i.name && i.name.length > 2);
    }

    parseAIResponse(aiResponse) {
        try {
            const rawText = aiResponse.candidates[0].content.parts[0].text;
            console.log("[QuestionGenerator] AI Raw Response:", rawText);

            // Remove markdown code blocks if present
            let cleanText = rawText.replace(/```json\s*/g, '').replace(/```\s*/g, '');

            // Extract JSON - try to find a complete JSON object
            const jsonMatch = cleanText.match(/\{[\s\S]*?\}/);
            if (!jsonMatch) {
                throw new Error("No JSON found in response");
            }

            let jsonText = jsonMatch[0];

            // Check if JSON looks complete (has closing brace for options array and main object)
            if (!jsonText.includes('"options"') || !jsonText.includes('"correctAnswer"')) {
                throw new Error("Incomplete JSON - missing required fields");
            }

            const questionData = JSON.parse(jsonText);

            // Validate required fields exist
            if (!questionData.text || !questionData.options || !questionData.correctAnswer) {
                throw new Error("Missing required fields in parsed JSON");
            }

            // Clean and trim
            questionData.text = String(questionData.text).trim();
            questionData.options = questionData.options.map(o => String(o).trim());
            questionData.correctAnswer = String(questionData.correctAnswer).trim();

            return questionData;
        } catch (error) {
            throw new Error(`Parse error: ${error.message}`);
        }
    }

    getFromBank(classId, subjectId, difficulty) {
        if (!this.questionBank) {
            console.warn('[QuestionGenerator] Question bank not loaded');
            return null;
        }

        const classBank = this.questionBank[classId];
        if (!classBank) {
            console.warn(`[QuestionGenerator] No questions for ${classId}`);
            return null;
        }

        const subjectBank = classBank[subjectId];
        if (!subjectBank) {
            console.warn(`[QuestionGenerator] No questions for ${subjectId}`);
            return null;
        }

        const difficultyBank = subjectBank[difficulty.toLowerCase()];
        if (!difficultyBank || difficultyBank.length === 0) {
            console.warn(`[QuestionGenerator] No ${difficulty} questions`);
            return null;
        }

        // Filter out already asked questions
        const availableQuestions = difficultyBank.filter(q =>
            !questionValidator.isDuplicate(q, this.questionHistory)
        );

        if (availableQuestions.length === 0) {
            console.warn('[QuestionGenerator] All bank questions already used');
            // Reset history and try again
            this.questionHistory = [];
            return difficultyBank[Math.floor(Math.random() * difficultyBank.length)];
        }

        // Pick random question
        const question = availableQuestions[Math.floor(Math.random() * availableQuestions.length)];

        return {
            text: question.text,
            options: this.shuffle([...question.options]),
            correctAnswer: question.correctAnswer,
            difficulty: difficulty,
            type: 'multiple-choice'
        };
    }

    getBatchFromBank(classId, subjectId, difficulty, count = 5) {
        if (!this.questionBank) {
            console.warn('[QuestionGenerator] Question bank not loaded');
            return [];
        }

        const classBank = this.questionBank[classId];
        if (!classBank) return [];

        const subjectBank = classBank[subjectId];
        if (!subjectBank) return [];

        const difficultyBank = subjectBank[difficulty.toLowerCase()];
        if (!difficultyBank || difficultyBank.length === 0) return [];

        // Filter out already asked questions
        const availableQuestions = difficultyBank.filter(q =>
            !questionValidator.isDuplicate(q, this.questionHistory)
        );

        // If not enough unique questions, reset history
        const questionsToUse = availableQuestions.length >= count ?
            availableQuestions : difficultyBank;

        // Shuffle and take up to 'count' questions
        const shuffled = this.shuffle([...questionsToUse]);
        const selected = shuffled.slice(0, Math.min(count, shuffled.length));

        return selected.map(q => ({
            text: q.text,
            options: this.shuffle([...q.options]),
            correctAnswer: q.correctAnswer,
            difficulty: difficulty,
            type: 'multiple-choice'
        }));
    }


    addToHistory(question) {
        this.questionHistory.push({
            text: question.text,
            timestamp: Date.now()
        });

        // Keep history size manageable
        if (this.questionHistory.length > this.maxHistorySize) {
            this.questionHistory.shift();
        }
    }

    shuffle(array) {
        const shuffled = [...array];
        for (let i = shuffled.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
        }
        return shuffled;
    }

    createFallbackQuestion(reason = "Unknown Error") {
        return {
            text: reason,
            options: ["Retry"],
            correctAnswer: "Retry",
            difficulty: "ERROR",
            type: "error"
        };
    }
}

export const questionGenerator = new QuestionGenerator();
