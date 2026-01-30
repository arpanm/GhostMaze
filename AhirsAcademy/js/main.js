import { dataLoader } from './data_loader.js';
import { economy } from './economy.js';
import { questionGenerator } from './question_generator.js';
import { adaptiveDifficulty } from './adaptive_difficulty.js';

class AcademyApp {
    constructor() {
        this.currentClass = null;
        this.currentSubject = null;
        this.currentQuestion = null;

        // Exam Session Tracking
        this.examSession = {
            questionsAnswered: 0,
            correctAnswers: 0,
            wrongAnswers: 0,
            totalCoinsEarned: 0,
            results: [] // {question, userAnswer, correctAnswer, isCorrect, coinsEarned}
        };

        // UI Elements
        this.balanceEl = document.getElementById('coin-balance');
        this.breadcrumbEl = document.getElementById('breadcrumb');

        this.classSection = document.getElementById('class-selection');
        this.classGrid = document.getElementById('class-grid');

        this.subjectSection = document.getElementById('subject-selection');
        this.subjectGrid = document.getElementById('subject-grid');

        this.quizSection = document.getElementById('quiz-interface');
        this.questionText = document.getElementById('question-text');
        this.optionsContainer = document.getElementById('options-container');
        this.feedbackArea = document.getElementById('feedback-area');
        this.nextBtn = document.getElementById('next-btn');

        this.resultsSection = document.getElementById('results-section');
        this.resultsContent = document.getElementById('results-content');

        this.difficultyBadge = document.getElementById('current-difficulty');
        this.streakDisplay = document.getElementById('streak-display');

        this.init();
    }

    async init() {
        this.updateHeader();
        await this.loadClasses();
        this.setupEventListeners();
    }

    setupEventListeners() {
        this.nextBtn.addEventListener('click', () => {
            this.loadQuestion();
        });
    }

    updateHeader() {
        this.balanceEl.textContent = economy.getBalance();
        const stats = adaptiveDifficulty.getStats();
        this.difficultyBadge.textContent = stats.difficulty;
        this.difficultyBadge.className = `difficulty-badge diff-${stats.difficulty}`;
        this.streakDisplay.textContent = `Streak: ${stats.streak} 🔥`;
    }

    async loadClasses() {
        const indexData = await dataLoader.loadIndex();
        if (!indexData) {
            this.classGrid.innerHTML = '<p>Error loading syllabus data. Please try again.</p>';
            return;
        }

        this.classGrid.innerHTML = '';
        Object.values(indexData.classes).forEach(cls => {
            const card = document.createElement('div');
            card.className = 'selection-card';
            card.innerHTML = `<h3>Class ${cls.class}</h3>`;
            card.onclick = () => this.selectClass(cls.class, cls);
            this.classGrid.appendChild(card);
        });
    }

    selectClass(classId, classData) {
        this.currentClass = { id: `class_${classId}`, data: classData };
        this.showSection('subject-selection');
        this.updateBreadcrumb();

        this.subjectGrid.innerHTML = '';
        Object.entries(classData.subjects).forEach(([subjectKey, subjectData]) => {
            const card = document.createElement('div');
            card.className = 'selection-card';
            // Capitalize subject key
            const title = subjectKey.charAt(0).toUpperCase() + subjectKey.slice(1);
            card.innerHTML = `<h3>${title}</h3>`;
            card.onclick = () => this.selectSubject(subjectKey, subjectData);
            this.subjectGrid.appendChild(card);
        });
    }

    selectSubject(subjectKey, subjectData) {
        this.currentSubject = { id: subjectKey, data: subjectData };

        // Reset exam session
        this.examSession = {
            questionsAnswered: 0,
            correctAnswers: 0,
            wrongAnswers: 0,
            totalCoinsEarned: 0,
            results: []
        };

        this.showSection('quiz-interface');
        this.updateBreadcrumb();
        this.loadQuestion();
    }

    async loadQuestion() {
        // UI Reset
        this.nextBtn.style.display = 'none';
        this.feedbackArea.textContent = '';
        this.feedbackArea.className = '';
        this.questionText.textContent = 'Generating Question...';
        this.optionsContainer.innerHTML = '';

        try {
            this.currentQuestion = await questionGenerator.generateQuestion(
                this.currentClass.id,
                this.currentSubject.id
            );

            this.renderQuestion();
            this.updateHeader(); // Update difficulty badge if it changed
        } catch (error) {
            console.error(error);
            this.questionText.textContent = "Error generating question. Please try another subject.";
        }
    }

    renderQuestion() {
        this.questionText.textContent = this.currentQuestion.text;
        this.optionsContainer.innerHTML = '';

        this.currentQuestion.options.forEach(option => {
            const btn = document.createElement('button');
            btn.className = 'option-btn';
            btn.textContent = option;
            btn.onclick = () => this.handleAnswer(option, btn);
            this.optionsContainer.appendChild(btn);
        });
    }

    handleAnswer(selectedOption, btnElement) {
        if (this.nextBtn.style.display === 'block') return; // Already answered

        if (this.currentQuestion.type === 'error') {
            this.loadQuestion();
            return;
        }

        const isCorrect = selectedOption === this.currentQuestion.correctAnswer;

        // Visual Feedback
        const buttons = this.optionsContainer.querySelectorAll('.option-btn');
        buttons.forEach(b => {
            if (b.textContent === this.currentQuestion.correctAnswer) {
                b.classList.add('correct');
            } else if (b === btnElement && !isCorrect) {
                b.classList.add('wrong');
            }
            b.disabled = true; // Disable all
        });

        // Logic
        adaptiveDifficulty.recordResult(isCorrect);

        const reward = isCorrect ? 10 : 0;
        if (isCorrect) {
            economy.addCoins(reward, `Solved ${this.currentQuestion.difficulty} Question`);
            this.feedbackArea.textContent = `Correct! You earned ${reward} Coins! 🎉`;
            this.feedbackArea.style.color = '#238636';
            this.examSession.correctAnswers++;
        } else {
            this.feedbackArea.textContent = `Wrong! The correct answer was: ${this.currentQuestion.correctAnswer}`;
            this.feedbackArea.style.color = '#da3633';
            this.examSession.wrongAnswers++;
        }

        // Track exam session
        this.examSession.questionsAnswered++;
        this.examSession.totalCoinsEarned += reward;
        this.examSession.results.push({
            question: this.currentQuestion.text,
            userAnswer: selectedOption,
            correctAnswer: this.currentQuestion.correctAnswer,
            isCorrect: isCorrect,
            coinsEarned: reward
        });

        this.updateHeader();

        // Check if exam should end (3 correct OR 5 total)
        if (this.examSession.correctAnswers >= 3 || this.examSession.questionsAnswered >= 5) {
            this.nextBtn.textContent = 'View Results';
            this.nextBtn.onclick = () => this.showResults();
        } else {
            this.nextBtn.textContent = 'Next Question';
            this.nextBtn.onclick = () => this.loadQuestion();
        }

        this.nextBtn.style.display = 'inline-block';
    }

    showResults() {
        const { questionsAnswered, correctAnswers, wrongAnswers, totalCoinsEarned, results } = this.examSession;

        const percentage = Math.round((correctAnswers / questionsAnswered) * 100);
        const passed = correctAnswers >= 3;

        let html = `
            <div class="results-header">
                <h2>${passed ? '🎉 Exam Complete!' : '📝 Exam Complete'}</h2>
                <div class="score-display">
                    <div class="score-circle ${passed ? 'passed' : 'failed'}">
                        <span class="score-number">${percentage}%</span>
                        <span class="score-label">${correctAnswers}/${questionsAnswered} Correct</span>
                    </div>
                </div>
            </div>

            <div class="results-stats">
                <div class="stat-card">
                    <div class="stat-value">${correctAnswers}</div>
                    <div class="stat-label">✅ Correct</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value">${wrongAnswers}</div>
                    <div class="stat-label">❌ Wrong</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value">${totalCoinsEarned}</div>
                    <div class="stat-label">🪙 Coins Earned</div>
                </div>
            </div>

            <div class="results-breakdown">
                <h3>Question Breakdown</h3>
                ${results.map((r, i) => `
                    <div class="result-item ${r.isCorrect ? 'correct' : 'wrong'}">
                        <div class="result-number">${i + 1}</div>
                        <div class="result-details">
                            <div class="result-question">${r.question}</div>
                            <div class="result-answers">
                                <span class="your-answer ${r.isCorrect ? 'correct' : 'wrong'}">
                                    Your answer: ${r.userAnswer}
                                </span>
                                ${!r.isCorrect ? `<span class="correct-answer">Correct: ${r.correctAnswer}</span>` : ''}
                            </div>
                        </div>
                        <div class="result-coins">${r.isCorrect ? '+' + r.coinsEarned : '0'} 🪙</div>
                    </div>
                `).join('')}
            </div>

            <!-- Cross-Game Carousel -->
            <div class="game-carousel-container">
                <h4>More Missions</h4>
                <div class="game-carousel">
                    <a href="../AhirsGhostMaze/index.html" class="game-card">
                        <span class="card-icon">👻</span>
                        <h5>Ghost Maze</h5>
                    </a>
                    <a href="../AhirsSnakeInARoom/index.html" class="game-card">
                        <span class="card-icon">🐍</span>
                        <h5>Snake Room</h5>
                    </a>
                    <a href="../AhirSharkRace/index.html" class="game-card">
                        <span class="card-icon">🦈</span>
                        <h5>Shark Race</h5>
                    </a>
                    <a href="../AhirsShootingBattle/index.html" class="game-card">
                        <span class="card-icon">🔫</span>
                        <h5>Shooting Battle</h5>
                    </a>
                    <a href="../AhirsWarZone/index.html" class="game-card">
                        <span class="card-icon">⚔️</span>
                        <h5>War Zone</h5>
                    </a>
                    <a href="../AhirsChess/index.html" class="game-card">
                        <span class="card-icon">♟</span>
                        <h5>Chess</h5>
                    </a>
                    <a href="../AhirsSnakeAndLadder/index.html" class="game-card">
                        <span class="card-icon">🎲</span>
                        <h5>Snake & Ladder</h5>
                    </a>
                    <a href="../AhirsBikeRace/index.html" class="game-card">
                        <span class="card-icon">🚲</span>
                        <h5>Bike Race</h5>
                    </a>
                </div>
            </div>

            <div class="results-actions">
                <button class="btn-primary" onclick="app.retryExam()">🔄 Try Again</button>
                <button class="btn-secondary" onclick="app.reset()">🏠 Back to Home</button>
            </div>
        `;

        this.resultsContent.innerHTML = html;
        this.showSection('results-section');
    }

    retryExam() {
        // Reset session and restart
        this.examSession = {
            questionsAnswered: 0,
            correctAnswers: 0,
            wrongAnswers: 0,
            totalCoinsEarned: 0,
            results: []
        };
        this.showSection('quiz-interface');
        this.loadQuestion();
    }

    showSection(sectionId) {
        // Hide all
        [this.classSection, this.subjectSection, this.quizSection, this.resultsSection].forEach(el => el.classList.remove('active'));
        // Show target
        document.getElementById(sectionId).classList.add('active');
    }

    updateBreadcrumb() {
        let html = '<span onclick="app.reset()">Home</span>';
        if (this.currentClass) {
            html += ` > <span onclick="app.selectClass('${this.currentClass.id.replace('class_', '')}', app.currentClass.data)">Class ${this.currentClass.id.replace('class_', '')}</span>`;
        }
        if (this.currentSubject) {
            html += ` > <span>${this.currentSubject.id}</span>`;
        }
        this.breadcrumbEl.innerHTML = html;
    }

    reset() {
        this.currentClass = null;
        this.currentSubject = null;
        this.showSection('class-selection');
        this.updateBreadcrumb();
    }
}

// Attach to window for breadcrumb onclicks
window.app = new AcademyApp();
