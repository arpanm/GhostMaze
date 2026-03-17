import json
import os

class_9_data = {
    "english": {
        "easy": [
            {"text": "Which of these is a reflexive pronoun?", "options": ["Themselves", "They", "Them", "Their"], "correctAnswer": "Themselves"},
            {"text": "Identify the type of sentence: 'What a beautiful sunset!'", "options": ["Exclamatory", "Declarative", "Imperative", "Interrogative"], "correctAnswer": "Exclamatory"},
            {"text": "What is the synonym of 'Diligent'?", "options": ["Hard-working", "Lazy", "Smart", "Quiet"], "correctAnswer": "Hard-working"},
            {"text": "Choose the correct preposition: 'He is proficient _____ English.'", "options": ["In", "At", "With", "By"], "correctAnswer": "In"},
            {"text": "Identify the conjunction: 'Although it was raining, we went out.'", "options": ["Although", "It", "Was", "We"], "correctAnswer": "Although"},
            {"text": "What is the antonym of 'Optimistic'?", "options": ["Pessimistic", "Hopeful", "Cheerful", "Negative"], "correctAnswer": "Pessimistic"},
            {"text": "Identify the subject in: 'Under the tree sat an old man.'", "options": ["An old man", "The tree", "Sat", "Under"], "correctAnswer": "An old man"},
            {"text": "Which word is a verb in the sentence: 'The alarm rang loudly.'?", "options": ["Rang", "Alarm", "Loudly", "The"], "correctAnswer": "Rang"},
            {"text": "What is the past participle of 'Rise'?", "options": ["Risen", "Rose", "Rising", "Rises"], "correctAnswer": "Risen"},
            {"text": "Choose the correctly spelled word.", "options": ["Knowledge", "Knowlege", "Knowludge", "Knowladge"], "correctAnswer": "Knowledge"},
            {"text": "Identify the article: 'She has _____ unique style.'", "options": ["A", "An", "The", "No article"], "correctAnswer": "A"},
            {"text": "What does the idiom 'Piece of cake' mean?", "options": ["Something very easy", "A slice of dessert", "A difficult task", "A small portion"], "correctAnswer": "Something very easy"},
            {"text": "Which word is an adjective in 'The blue ocean'?", "options": ["Blue", "Ocean", "The", "Is"], "correctAnswer": "Blue"},
            {"text": "What is the meaning of the prefix 'Dis-'?", "options": ["Not / Opposite", "Before", "Again", "Together"], "correctAnswer": "Not / Opposite"},
            {"text": "Identify the plural of 'Criteria'.", "options": ["Criteria (singular is Criterion)", "Criterias", "Criterions", "Criterium"], "correctAnswer": "Criteria (singular is Criterion)"}
        ],
        "medium": [
            {"text": "Change to passive voice: 'The chef prepared a delicious meal.'", "options": ["A delicious meal was prepared by the chef.", "The chef was preparing a delicious meal.", "A delicious meal is prepared by the chef.", "The chef had prepared a delicious meal."], "correctAnswer": "A delicious meal was prepared by the chef."},
            {"text": "Identify the figure of speech: 'The leaves danced in the wind.'", "options": ["Personification", "Simile", "Metaphor", "Hyperbole"], "correctAnswer": "Personification"},
            {"text": "Which clause is italicized: 'I don't know <i>where he lives</i>.'?", "options": ["Noun Clause", "Adjective Clause", "Adverb Clause", "Relative Clause"], "correctAnswer": "Noun Clause"},
            {"text": "Identify the type of noun: 'The <u>class</u> is quiet.'", "options": ["Collective Noun", "Proper Noun", "Abstract Noun", "Material Noun"], "correctAnswer": "Collective Noun"},
            {"text": "What is the meaning of the idiom 'To hit the nail on the head'?", "options": ["To describe exactly what is causing a situation", "To be violent", "To build something", "To make a mistake"], "correctAnswer": "To describe exactly what is causing a situation"},
            {"text": "Choose the correct form: 'Neither of the boys _____ present.'", "options": ["Was", "Were", "Are", "Will"], "correctAnswer": "Was"},
            {"text": "Identify the gerund: 'Swimming is good for health.'", "options": ["Swimming", "Is", "Good", "Health"], "correctAnswer": "Swimming"},
            {"text": "What does the suffix '-able' mean?", "options": ["Capable of", "Without", "Study of", "Person who"], "correctAnswer": "Capable of"},
            {"text": "Identify the auxiliary verb: 'He has finished his work.'", "options": ["Has", "Finished", "His", "Work"], "correctAnswer": "Has"},
            {"text": "Which of these is a compound sentence?", "options": ["I like tea, but he likes coffee.", "I like tea and coffee.", "Because it was raining, I stayed home.", "He is a good boy."], "correctAnswer": "I like tea, but he likes coffee."},
            {"text": "What is the meaning of 'Incredible'?", "options": ["Unbelievable", "Very common", "Not clever", "Slow"], "correctAnswer": "Unbelievable"},
            {"text": "Identify the homophone: 'The wind _____ the candle out.'", "options": ["Blew", "Blue", "Blewed", "Blow"], "correctAnswer": "Blew"},
            {"text": "Choose the correct tense: 'I _____ my homework by 8 PM.'", "options": ["Will have finished", "Finished", "Finish", "Am finishing"], "correctAnswer": "Will have finished"},
            {"text": "What is a 'Stanza'?", "options": ["A group of lines in a poem", "A type of dance", "A musical instrument", "A character in a play"], "correctAnswer": "A group of lines in a poem"},
            {"text": "Identify the direct object: 'The teacher gave the students a test.'", "options": ["A test", "The students", "The teacher", "Gave"], "correctAnswer": "A test"}
        ],
        "hard": [
            {"text": "Identify the mood: 'If I were you, I would take the offer.'", "options": ["Subjunctive", "Indicative", "Imperative", "Interrogative"], "correctAnswer": "Subjunctive"},
            {"text": "What is 'Alliteration'?", "options": ["The repetition of initial consonant sounds", "A comparison using like or as", "Exaggeration for effect", "Words that sound like what they mean"], "correctAnswer": "The repetition of initial consonant sounds"},
            {"text": "Identify the error: 'One of the student have not submitted the assignment.'", "options": ["'student' should be 'students' and 'have' should be 'has'", "'student' should be 'students'", "'have' should be 'has'", "No error"], "correctAnswer": "'student' should be 'students' and 'have' should be 'has'"},
            {"text": "What is the meaning of 'Euphemism'?", "options": ["An indirect, less offensive way of saying something that is considered unpleasant", "A harsh way of speaking", "A repetition of sounds", "A logical fallacy"], "correctAnswer": "An indirect, less offensive way of saying something that is considered unpleasant"},
            {"text": "Identify the rhetorical device: 'To err is human; to forgive, divine.'", "options": ["Antithesis", "Oxymoron", "Personification", "Metonymy"], "correctAnswer": "Antithesis"},
            {"text": "Which sentence contains a transitive verb?", "options": ["She wrote a letter.", "She slept deeply.", "They laughed loudly.", "The sun shines."], "correctAnswer": "She wrote a letter."},
            {"text": "What is 'Onomatopoeia'?", "options": ["Words that imitate the sound they describe", "A comparison of two unlike things", "A reference to a famous person or event", "A play on words"], "correctAnswer": "Words that imitate the sound they describe"},
            {"text": "Identify the type of phrase: 'The man with the red hat is my uncle.'", "options": ["Adjective Phrase", "Adverb Phrase", "Noun Phrase", "Verb Phrase"], "correctAnswer": "Adjective Phrase"},
            {"text": "What follows the 'sequence of tenses' in indirect speech?", "options": ["If the reporting verb is in the past, the verb in the reported speech changes to a past form.", "The tense never changes.", "Only the pronouns change.", "Only the adverbs of time change."], "correctAnswer": "If the reporting verb is in the past, the verb in the reported speech changes to a past form."},
            {"text": "Identify the 'Oxymoron' in these options.", "options": ["Clearly confused", "Running fast", "Deep blue sea", "Bright sunshine"], "correctAnswer": "Clearly confused"},
            {"text": "What is a 'Sonnet'?", "options": ["A 14-line poem with a fixed rhyme scheme", "A short story", "A long narrative poem", "A play with a tragic hero"], "correctAnswer": "A 14-line poem with a fixed rhyme scheme"},
            {"text": "Identify the 'Transitive' or 'Intransitive' nature of 'Arrival' in 'The arrival of the train was delayed.'", "options": ["Neither (it's a noun)", "Transitive", "Intransitive", "Both"], "correctAnswer": "Neither (it's a noun)"},
            {"text": "What is the meaning of the root 'Phil'?", "options": ["Love", "Fear", "Sound", "Earth"], "correctAnswer": "Love"},
            {"text": "Identify the voice: 'Let the door be shut.'", "options": ["Passive", "Active", "Imperative", "Middle"], "correctAnswer": "Passive"},
            {"text": "What is a 'Soliloquy'?", "options": ["A speech by a character alone on stage expressing their thoughts", "A conversation between two characters", "A short humorous story", "A type of epic poem"], "correctAnswer": "A speech by a character alone on stage expressing their thoughts"}
        ]
    },
    "maths": {
        "easy": [
            {"text": "If a = 2 and b = -3, what is a^2 - b^2?", "options": ["-5", "5", "13", "-13"], "correctAnswer": "-5"},
            {"text": "What is the degree of the polynomial 5x^3 - 2x + 7?", "options": ["3", "1", "0", "2"], "correctAnswer": "3"},
            {"text": "In a right-angled triangle, if base = 3 and height = 4, the hypotenuse is:", "options": ["5", "7", "12", "25"], "correctAnswer": "5"},
            {"text": "Which of these is NOT a rational number?", "options": ["√2", "0", "1/2", "-5"], "correctAnswer": "√2"},
            {"text": "Find the value of (2^3)^2.", "options": ["64", "12", "32", "16"], "correctAnswer": "64"},
            {"text": "The sum of the angles of a triangle is:", "options": ["180°", "90°", "360°", "270°"], "correctAnswer": "180°"},
            {"text": "Evaluate: 15% of 120", "options": ["18", "15", "12", "20"], "correctAnswer": "18"},
            {"text": "What is the formula for the area of a circle?", "options": ["πr^2", "2πr", "πd", "1/2πr"], "correctAnswer": "πr^2"},
            {"text": "Solve for x: 2x + 5 = 13", "options": ["4", "9", "8", "6"], "correctAnswer": "4"},
            {"text": "Find the coordinates of the origin.", "options": ["(0,0)", "(1,1)", "(0,1)", "(1,0)"], "correctAnswer": "(0,0)"},
            {"text": "Which of these is a linear equation in one variable?", "options": ["3x + 2 = 8", "x^2 + 1 = 0", "x + y = 5", "2x + 3y = 4"], "correctAnswer": "3x + 2 = 8"},
            {"text": "The value of 0.333... in p/q form is:", "options": ["1/3", "3/10", "33/100", "1/4"], "correctAnswer": "1/3"},
            {"text": "Find the perimeter of a square whose side is 7 cm.", "options": ["28 cm", "49 cm", "14 cm", "21 cm"], "correctAnswer": "28 cm"},
            {"text": "Identify the coefficient of x in 7 - 2x.", "options": ["-2", "7", "2", "x"], "correctAnswer": "-2"},
            {"text": "What is the probability of an event that is certain to happen?", "options": ["1", "0", "0.5", "Undetermined"], "correctAnswer": "1"}
        ],
        "medium": [
            {"text": "Simplify: (x + 2)(x - 2)", "options": ["x^2 - 4", "x^2 + 4", "x^2 - 4x + 4", "x^2 + 4x + 4"], "correctAnswer": "x^2 - 4"},
            {"text": "If the radius of a sphere is doubled, what is the ratio of their surface areas?", "options": ["1:4", "1:2", "1:8", "1:1"], "correctAnswer": "1:4"},
            {"text": "Find the value of k if (x - 1) is a factor of 4x^3 + 3x^2 - 4x + k.", "options": ["-3", "3", "0", "1"], "correctAnswer": "-3"},
            {"text": "In a cyclic quadrilateral, if one angle is 70°, the opposite angle is:", "options": ["110°", "70°", "180°", "90°"], "correctAnswer": "110°"},
            {"text": "Find the mean of the first five prime numbers.", "options": ["5.6", "5", "6", "4"], "correctAnswer": "5.6"},
            {"text": "The volume of a cone with radius r and height h is:", "options": ["1/3 πr^2h", "πr^2h", "4/3 πr^3", "2πrh"], "correctAnswer": "1/3 πr^2h"},
            {"text": "If the perimeter of a semi-circle is 36 cm, its radius is: (Take π = 22/7)", "options": ["7 cm", "14 cm", "21 cm", "3.5 cm"], "correctAnswer": "7 cm"},
            {"text": "Solve for x: (x/2) + (x/3) = 10", "options": ["12", "6", "10", "15"], "correctAnswer": "12"},
            {"text": "Which of these is a solution to x + y = 4?", "options": ["(2,2)", "(1,2)", "(4,1)", "(0,0)"], "correctAnswer": "(2,2)"},
            {"text": "Find the median of the data: 10, 15, 12, 18, 14.", "options": ["14", "12", "15", "13"], "correctAnswer": "14"},
            {"text": "What is the area of an equilateral triangle with side 4 cm?", "options": ["4√3 sq cm", "16√3 sq cm", "8√3 sq cm", "2√3 sq cm"], "correctAnswer": "4√3 sq cm"},
            {"text": "If cost price is Rs 200 and profit is 10%, selling price is:", "options": ["Rs 220", "Rs 210", "Rs 180", "Rs 190"], "correctAnswer": "Rs 220"},
            {"text": "Factorize: x^2 + 5x + 6", "options": ["(x+2)(x+3)", "(x+1)(x+6)", "(x-2)(x-3)", "(x+5)(x+1)"], "correctAnswer": "(x+2)(x+3)"},
            {"text": "An angle greater than 180° but less than 360° is called:", "options": ["Reflex angle", "Obtuse angle", "Acute angle", "Straight angle"], "correctAnswer": "Reflex angle"},
            {"text": "Find the square root of 0.09.", "options": ["0.3", "0.03", "3", "0.9"], "correctAnswer": "0.3"}
        ],
        "hard": [
            {"text": "Rationalize the denominator of 1 / (√7 - 2).", "options": ["(√7 + 2) / 3", "√7 + 2", "1 / 3", "(√7 - 2) / 3"], "correctAnswer": "(√7 + 2) / 3"},
            {"text": "If x + 1/x = 4, find the value of x^2 + 1/x^2.", "options": ["14", "16", "18", "12"], "correctAnswer": "14"},
            {"text": "Find the remainder when x^4 + x^3 - 2x^2 + x + 1 is divided by x - 1.", "options": ["2", "1", "0", "3"], "correctAnswer": "2"},
            {"text": "In a triangle ABC, if ∠A - ∠B = 33° and ∠B - ∠C = 18°, find ∠B.", "options": ["55°", "88°", "37°", "60°"], "correctAnswer": "55°"},
            {"text": "The area of a triangle with sides 13 cm, 14 cm, and 15 cm is:", "options": ["84 sq cm", "100 sq cm", "90 sq cm", "72 sq cm"], "correctAnswer": "84 sq cm"},
            {"text": "If 3^x - 3^(x-1) = 18, find the value of x^x.", "options": ["27", "4", "9", "1"], "correctAnswer": "27"},
            {"text": "The total surface area of a cube is 216 sq cm. Its volume is:", "options": ["216 cubic cm", "36 cubic cm", "144 cubic cm", "72 cubic cm"], "correctAnswer": "216 cubic cm"},
            {"text": "Solve: √10 * √15", "options": ["5√6", "√25", "25", "10√5"], "correctAnswer": "5√6"},
            {"text": "In Heron's formula, 's' represents:", "options": ["Semi-perimeter", "Side", "Sum", "Surface Area"], "correctAnswer": "Semi-perimeter"},
            {"text": "If the mean of x, x+2, x+4, x+6, x+8 is 11, find x.", "options": ["7", "5", "9", "11"], "correctAnswer": "7"},
            {"text": "What is the relation between volume (V) and radius (r) of a sphere?", "options": ["V ∝ r^3", "V ∝ r^2", "V ∝ r", "V ∝ 1/r"], "correctAnswer": "V ∝ r^3"},
            {"text": "Find the distance between points (0,0) and (3,4).", "options": ["5", "7", "25", "√7"], "correctAnswer": "5"},
            {"text": "Factorize completely: x^3 - 2x^2 - x + 2", "options": ["(x-1)(x+1)(x-2)", "(x-1)^2(x+2)", "(x+1)^2(x-2)", "(x-1)(x+2)(x+3)"], "correctAnswer": "(x-1)(x+1)(x-2)"},
            {"text": "If the edge of a cube is increased by 50%, what is the percentage increase in its surface area?", "options": ["125%", "50%", "100%", "225%"], "correctAnswer": "125%"},
            {"text": "Find the value of (√5 + √2)^2.", "options": ["7 + 2√10", "10", "7", "7 + √10"], "correctAnswer": "7 + 2√10"}
        ]
    },
    "science": {
        "easy": [
            {"text": "What is the SI unit of force?", "options": ["Newton", "Joule", "Watt", "Pascal"], "correctAnswer": "Newton"},
            {"text": "Which organelle is known as the powerhouse of the cell?", "options": ["Mitochondria", "Nucleus", "Ribosome", "Golgi Body"], "correctAnswer": "Mitochondria"},
            {"text": "What is the process of changing a solid directly into a gas called?", "options": ["Sublimation", "Evaporation", "Melting", "Condensation"], "correctAnswer": "Sublimation"},
            {"text": "Which law says 'For every action there is an equal and opposite reaction'?", "options": ["Newton's Third Law", "Newton's First Law", "Law of Gravity", "Ohm's Law"], "correctAnswer": "Newton's Third Law"},
            {"text": "What is the chemical symbol for Gold?", "options": ["Au", "Ag", "Fe", "Cu"], "correctAnswer": "Au"},
            {"text": "Which gas is used during photosynthesis by plants?", "options": ["Carbon dioxide", "Oxygen", "Nitrogen", "Hydrogen"], "correctAnswer": "Carbon dioxide"},
            {"text": "What is the speed of sound in air approximately?", "options": ["340 m/s", "1500 m/s", "3 x 10^8 m/s", "100 m/s"], "correctAnswer": "340 m/s"},
            {"text": "Which acid is present in lemon?", "options": ["Citric acid", "Acetic acid", "Hydrochloric acid", "Malic acid"], "correctAnswer": "Citric acid"},
            {"text": "What is the basic unit of life?", "options": ["Cell", "Atom", "Tissue", "Organ"], "correctAnswer": "Cell"},
            {"text": "Identify the non-metal that is liquid at room temperature.", "options": ["Bromine", "Mercury", "Iodine", "Chlorine"], "correctAnswer": "Bromine"},
            {"text": "What is the approximate percentage of Nitrogen in the atmosphere?", "options": ["78%", "21%", "0.03%", "1%"], "correctAnswer": "78%"},
            {"text": "Who discovered the cell in 1665?", "options": ["Robert Hooke", "Leeuwenhoek", "Darwin", "Mendel"], "correctAnswer": "Robert Hooke"},
            {"text": "Which tissue conducts water in plants?", "options": ["Xylem", "Phloem", "Parenchyma", "Collenchyma"], "correctAnswer": "Xylem"},
            {"text": "What is the valence of Carbon?", "options": ["4", "2", "6", "1"], "correctAnswer": "4"},
            {"text": "Weight of an object on the Moon is _____ of its weight on Earth.", "options": ["1/6", "1/2", "1/10", "Equal"], "correctAnswer": "1/6"}
        ],
        "medium": [
            {"text": "What is the value of 'g' (acceleration due to gravity) on Earth's surface?", "options": ["9.8 m/s^2", "1.6 m/s^2", "10 cm/s^2", "0 m/s^2"], "correctAnswer": "9.8 m/s^2"},
            {"text": "Which subatomic particle has a negative charge?", "options": ["Electron", "Proton", "Neutron", "Positron"], "correctAnswer": "Electron"},
            {"text": "What is the molar mass of water (H2O)?", "options": ["18 g/mol", "16 g/mol", "2 g/mol", "10 g/mol"], "correctAnswer": "18 g/mol"},
            {"text": "Identify the process by which amoeba takes in food.", "options": ["Endocytosis / Phagocytosis", "Exocytosis", "Diffusion", "Osmosis"], "correctAnswer": "Endocytosis / Phagocytosis"},
            {"text": "What type of mixture is salt in water?", "options": ["Homogeneous", "Heterogeneous", "Colloid", "Suspension"], "correctAnswer": "Homogeneous"},
            {"text": "Which plant tissue has dead cells?", "options": ["Sclerenchyma", "Parenchyma", "Collenchyma", "Aerenchyma"], "correctAnswer": "Sclerenchyma"},
            {"text": "What is the boiling point of water in Kelvin?", "options": ["373.15 K", "100 K", "273.15 K", "0 K"], "correctAnswer": "373.15 K"},
            {"text": "Define work done when a force F moves an object by distance d in the same direction.", "options": ["W = F * d", "W = F / d", "W = F + d", "W = F^2 * d"], "correctAnswer": "W = F * d"},
            {"text": "Which cell organelle contains its own DNA?", "options": ["Mitochondria", "Ribosome", "Lysosome", "Vacuole"], "correctAnswer": "Mitochondria"},
            {"text": "What is an isotope?", "options": ["Atoms with same atomic number but different mass number", "Atoms with same mass number", "Atoms with no neutrons", "Atoms of different elements"], "correctAnswer": "Atoms with same atomic number but different mass number"},
            {"text": "Identify the connective tissue that connects bone to bone.", "options": ["Ligament", "Tendon", "Cartilage", "Areolar"], "correctAnswer": "Ligament"},
            {"text": "What is the tendency of an object to resist changes in its state of motion called?", "options": ["Inertia", "Momentum", "Friction", "Velocity"], "correctAnswer": "Inertia"},
            {"text": "Which isotope is used in carbon dating?", "options": ["Carbon-14", "Carbon-12", "Carbon-13", "Nitrogen-14"], "correctAnswer": "Carbon-14"},
            {"text": "What is the function of stomata in leaves?", "options": ["Gas exchange and transpiration", "Photosynthesis only", "Absorb water", "Stores food"], "correctAnswer": "Gas exchange and transpiration"},
            {"text": "Identify the element with atomic number 11.", "options": ["Sodium", "Magnesium", "Aluminum", "Neon"], "correctAnswer": "Sodium"}
        ],
        "hard": [
            {"text": "State the Law of Conservation of Mass.", "options": ["Mass can neither be created nor destroyed in a chemical reaction", "Energy is always conserved", "Total mass of reactants equals total mass of products", "Both 1 and 3"], "correctAnswer": "Both 1 and 3"},
            {"text": "What is the relative density of a substance?", "options": ["Density of substance / Density of water", "Mass / Volume", "Density * Volume", "Density of water / Density of substance"], "correctAnswer": "Density of substance / Density of water"},
            {"text": "Identify the functional unit of the kidney.", "options": ["Nephron", "Neuron", "Alveoli", "Villi"], "correctAnswer": "Nephron"},
            {"text": "What happens to the kinetic energy of an object if its velocity is doubled?", "options": ["Becomes 4 times", "Is doubled", "Remains same", "Becomes 8 times"], "correctAnswer": "Becomes 4 times"},
            {"text": "Who proposed the 'Plum Pudding Model' of the atom?", "options": ["J.J. Thomson", "Rutherford", "Bohr", "Dalton"], "correctAnswer": "J.J. Thomson"},
            {"text": "What is the latent heat of vaporization of water?", "options": ["Heat required to change 1kg of liquid to gas at boiling point", "Heat required to raise temp by 1 degree", "Energy in water", "Temperature of steam"], "correctAnswer": "Heat required to change 1kg of liquid to gas at boiling point"},
            {"text": "Which part of the brain controls balance and posture?", "options": ["Cerebellum", "Cerebrum", "Medulla", "Thalamus"], "correctAnswer": "Cerebellum"},
            {"text": "What is Avogadro's number?", "options": ["6.022 x 10^23", "3 x 10^8", "1.6 x 10^-19", "9.8"], "correctAnswer": "6.022 x 10^23"},
            {"text": "Define 'Echo'.", "options": ["Repetition of sound due to reflection", "Absorption of sound", "Bending of sound", "Diffraction of sound"], "correctAnswer": "Repetition of sound due to reflection"},
            {"text": "Which endocrine gland is often called the 'Master Gland'?", "options": ["Pituitary", "Thyroid", "Adrenal", "Pancreas"], "correctAnswer": "Pituitary"},
            {"text": "Identify the process of conversion of food waste into nutrient-rich soil by earthworms.", "options": ["Vermicomposting", "Composting", "Recycling", "Pasteurization"], "correctAnswer": "Vermicomposting"},
            {"text": "What is the electronic configuration of Calcium (At. No. 20)?", "options": ["2, 8, 8, 2", "2, 8, 10", "2, 18", "2, 8, 9, 1"], "correctAnswer": "2, 8, 8, 2"},
            {"text": "Specify the role of 'Lysosomes' in a cell.", "options": ["Waste disposal (Suicide bags)", "Protein synthesis", "Energy production", "Storage of water"], "correctAnswer": "Waste disposal (Suicide bags)"},
            {"text": "Define 'Free Fall'.", "options": ["Motion of an object under the influence of gravity only", "Falling with constant velocity", "Falling in air", "Parachute jump"], "correctAnswer": "Motion of an object under the influence of gravity only"},
            {"text": "What is the valency of Oxygen?", "options": ["2", "6", "8", "4"], "correctAnswer": "2"}
        ]
    },
    "social-science": {
        "easy": [
            {"text": "When did the French Revolution begin?", "options": ["1789", "1776", "1804", "1799"], "correctAnswer": "1789"},
            {"text": "Who was the leader of the Jacobin club in France?", "options": ["Maximilien Robespierre", "Napoleon Bonaparte", "Louis XVI", "Mirabeau"], "correctAnswer": "Maximilien Robespierre"},
            {"text": "Which is the largest country in terms of area?", "options": ["Russia", "Canada", "China", "India"], "correctAnswer": "Russia"},
            {"text": "India's Standard Meridian passes through which city?", "options": ["Mirzapur", "Delhi", "Mumbai", "Kolkata"], "correctAnswer": "Mirzapur"},
            {"text": "Who is the head of the government in India?", "options": ["Prime Minister", "President", "Chief Justice", "Speaker"], "correctAnswer": "Prime Minister"},
            {"text": "In which continent is the Amazon rainforest located?", "options": ["South America", "Africa", "Asis", "Australia"], "correctAnswer": "South America"},
            {"text": "What is the main occupation in Indian villages according to economics textbooks?", "options": ["Farming", "Manufacturing", "Tourism", "Banking"], "correctAnswer": "Farming"},
            {"text": "Who wrote 'The Social Contract'?", "options": ["Rousseau", "Montesquieu", "Locke", "Voltaire"], "correctAnswer": "Rousseau"},
            {"text": "Which imaginay line divides India into Northern and Southern halves?", "options": ["Tropic of Cancer", "Equator", "Prime Meridian", "Arctic Circle"], "correctAnswer": "Tropic of Cancer"},
            {"text": "Democratic elections must be _____.", "options": ["Free and Fair", "Controlled", "Only for the rich", "Once in 20 years"], "correctAnswer": "Free and Fair"},
            {"text": "What constitutes 'Fixed Capital'?", "options": ["Tools, machines, buildings", "Raw materials and money", "Labor", "Soil"], "correctAnswer": "Tools, machines, buildings"},
            {"text": "Who was the first President of the USA?", "options": ["George Washington", "Abraham Lincoln", "Thomas Jefferson", "John Adams"], "correctAnswer": "George Washington"},
            {"text": "Which island neighbors of India are located in the Arabian Sea?", "options": ["Lakshadweep", "Andaman and Nicobar", "Sri Lanka", "Maldives"], "correctAnswer": "Lakshadweep"},
            {"text": "When is World Environment Day celebrated?", "options": ["June 5", "April 22", "May 1", "March 21"], "correctAnswer": "June 5"},
            {"text": "The Preamble to the Indian Constitution starts with:", "options": ["We, the people of India", "Bharat is a nation", "Justice for all", "In the name of God"], "correctAnswer": "We, the people of India"}
        ],
        "medium": [
            {"text": "Which book was written by Montesquieu?", "options": ["The Spirit of the Laws", "Two Treatises of Government", "Mein Kampf", "The Wealth of Nations"], "correctAnswer": "The Spirit of the Laws"},
            {"text": "A landmass bounded by sea on three sides is referred to as:", "options": ["Peninsula", "Island", "Coast", "Isthmus"], "correctAnswer": "Peninsula"},
            {"text": "What is the meaning of 'Working Capital'?", "options": ["Raw materials and money in hand", "Machines", "Buildings", "Land"], "correctAnswer": "Raw materials and money in hand"},
            {"text": "Who appointed the members of the Drafting Committee of the Indian Constitution?", "options": ["Constituent Assembly", "Mahatma Gandhi", "British Parliament", "Viceroy"], "correctAnswer": "Constituent Assembly"},
            {"text": "Which is the highest peak in the Himalayas in India?", "options": ["Kanchenjunga", "Mt. Everest", "Nanda Devi", "K2"], "correctAnswer": "Kanchenjunga"},
            {"text": "The 'Apartheid' system was followed in which country?", "options": ["South Africa", "USA", "India", "Germany"], "correctAnswer": "South Africa"},
            {"text": "Which sector includes agriculture, forestry, and fishing?", "options": ["Primary Sector", "Secondary Sector", "Tertiary Sector", "Quaternary Sector"], "correctAnswer": "Primary Sector"},
            {"text": "When did the Russian Revolution take place?", "options": ["1917", "1905", "1921", "1945"], "correctAnswer": "1917"},
            {"text": "Identify the active volcano in India.", "options": ["Barren Island", "Narcondam Island", "Mount Abu", "Vesuvius"], "correctAnswer": "Barren Island"},
            {"text": "What is 'Sovereignty'?", "options": ["Supreme power of the state over its territory", "Rule by a king", "Equality for all", "A type of election"], "correctAnswer": "Sovereignty"},
            {"text": "Green Revolution in India was started in the late _____.", "options": ["1960s", "1950s", "1970s", "1980s"], "correctAnswer": "1960s"},
            {"text": "Who was the Tsar of Russia during the 1917 revolution?", "options": ["Nicholas II", "Peter the Great", "Alexander II", "Stalin"], "correctAnswer": "Nicholas II"},
            {"text": "Which drainage pattern is formed when rivers flow in different directions from a central peak?", "options": ["Radial", "Dendritic", "Trellis", "Rectangular"], "correctAnswer": "Radial"},
            {"text": "What is 'Universal Adult Franchise'?", "options": ["Right to vote for all adults", "Right to property", "Right to education", "Right to travel"], "correctAnswer": "Right to vote for all adults"},
            {"text": "Identify the primary source of irrigation in India after wells.", "options": ["Canals", "Rainwater", "Oceans", "Glaciers"], "correctAnswer": "Canals"}
        ],
        "hard": [
            {"text": "What was the 'Reign of Terror' in France?", "options": ["Period of rule by Robespierre (1793-1794)", "The onset of the revolution", "Napoleon's rule", "The storming of Bastille"], "correctAnswer": "Period of rule by Robespierre (1793-1794)"},
            {"text": "In which ocean is the 'Challenger Deep' (Mariana Trench) located?", "options": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Southern Ocean"], "correctAnswer": "Pacific Ocean"},
            {"text": "Define 'Human Capital'.", "options": ["The stock of skill, knowledge, and enterprise in people", "Population size", "The number of workers", "Wealth of a person"], "correctAnswer": "The stock of skill, knowledge, and enterprise in people"},
            {"text": "Which article of the Indian Constitution guarantees the 'Right to Life'?", "options": ["Article 21", "Article 14", "Article 19", "Article 32"], "correctAnswer": "Article 21"},
            {"text": "Who was the main leader of the Bolshevik party during the 1917 revolution?", "options": ["Vladimir Lenin", "Leon Trotsky", "Joseph Stalin", "Karl Marx"], "correctAnswer": "Vladimir Lenin"},
            {"text": "Identify the 'Great India Desert' name.", "options": ["Thar Desert", "Gobi Desert", "Sahara Desert", "Atacama Desert"], "correctAnswer": "Thar Desert"},
            {"text": "What is 'Secularism' according to the Indian Constitution?", "options": ["Separation of religion from state and respect for all", "Anti-religion stance", "Promotion of one religion", "Rule by religious leaders"], "correctAnswer": "Separation of religion from state and respect for all"},
            {"text": "The 'Enclosure Movement' in England was related to _____.", "options": ["Agriculture", "Industry", "Mining", "Shipping"], "correctAnswer": "Agriculture"},
            {"text": "Which river is known as the 'Dakshin Ganga'?", "options": ["Godavari", "Krishna", "Cauvery", "Mahanadi"], "correctAnswer": "Godavari"},
            {"text": "What constitutes the 'Supreme Court' in India?", "options": ["The highest court of appeal", "Parliament", "Police Headquarters", "Cabinet"], "correctAnswer": "The highest court of appeal"},
            {"text": "Identify the 'BPL' full form in economic surveys.", "options": ["Below Poverty Line", "British Petroleum Ltd", "Better Public Life", "Basic Price List"], "correctAnswer": "Below Poverty Line"},
            {"text": "Who was the author of the 'Communist Manifesto'?", "options": ["Karl Marx and Friedrich Engels", "Lenin", "Mao", "Stalin"], "correctAnswer": "Karl Marx and Friedrich Engels"},
            {"text": "Which wind system is responsible for the winter rains in North-west India?", "options": ["Western Disturbances", "Monsoon", "Loo", "Trade Winds"], "correctAnswer": "Western Disturbances"},
            {"text": "Define 'Subsidies' in economic terms.", "options": ["Financial assistance by government to lower the price of a good", "Tax paid to government", "Profit of a company", "Interest on loan"], "correctAnswer": "Financial assistance by government to lower the price of a good"},
            {"text": "What is the 'Cold War'?", "options": ["A state of political tension between USSR and USA without direct fighting", "A war in the Arctic", "A war with ice weapons", "The French Revolution"], "correctAnswer": "A state of political tension between USSR and USA without direct fighting"}
        ]
    }
}

def main():
    bank_path = '/Users/arpan1.mukherjee/code/GhostMaze/public/AhirsAcademy/data/question_bank.json'
    
    with open(bank_path, 'r', encoding='utf-8') as f:
        question_bank = json.load(f)
        
    question_bank['class_9'] = class_9_data
    
    with open(bank_path, 'w', encoding='utf-8') as f:
        json.dump(question_bank, f, indent=4, ensure_ascii=False)
        
    print("Successfully injected tough, researched questions for Class 9!")

if __name__ == '__main__':
    main()
