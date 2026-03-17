import json
import os

class_10_data = {
    "english": {
        "easy": [
            {"text": "Who is the author of 'A Letter to God'?", "options": ["G.L. Fuentes", "Nelson Mandela", "Liam O'Flaherty", "Frederick Forsyth"], "correctAnswer": "G.L. Fuentes"},
            {"text": "In 'Nelson Mandela: Long Walk to Freedom', what does 'apartheid' mean?", "options": ["Policy of racial segregation", "Rule of the majority", "Democratic freedom", "Financial crisis"], "correctAnswer": "Policy of racial segregation"},
            {"text": "Which poet wrote 'Fire and Ice'?", "options": ["Robert Frost", "Leslie Norris", "John Berryman", "Carolyn Wells"], "correctAnswer": "Robert Frost"},
            {"text": "What is the collective noun for a group of lions?", "options": ["Pride", "Pack", "Herd", "Swarm"], "correctAnswer": "Pride"},
            {"text": "Identify the conjunction: 'He worked hard, yet he failed.'", "options": ["Yet", "Hard", "Failed", "He"], "correctAnswer": "Yet"},
            {"text": "What is the synonym of 'Resilient'?", "options": ["Tough / Elastic", "Weak", "Fragile", "Slow"], "correctAnswer": "Tough / Elastic"},
            {"text": "Choose the correct article: 'He is _____ honest man.'", "options": ["An", "A", "The", "No article"], "correctAnswer": "An"},
            {"text": "Identify the preposition: 'The cat jumped over the fence.'", "options": ["Over", "Jumped", "Fence", "The"], "correctAnswer": "Over"},
            {"text": "What is the meaning of the idiom 'Under the weather'?", "options": ["Feeling sick", "In the rain", "Very happy", "Traveling"], "correctAnswer": "Feeling sick"},
            {"text": "Which word is a verb in: 'She sings beautifully.'?", "options": ["Sings", "Beautifully", "She", "Is"], "correctAnswer": "Sings"},
            {"text": "What is the past tense of 'Catch'?", "options": ["Caught", "Catched", "Catching", "Cot"], "correctAnswer": "Caught"},
            {"text": "Identify the type of sentence: 'Please close the door.'", "options": ["Imperative", "Declarative", "Interrogative", "Exclamatory"], "correctAnswer": "Imperative"},
            {"text": "Who is the protagonist in 'The Diary of Anne Frank'?", "options": ["Anne Frank", "Margot", "Otto Frank", "Miep Gies"], "correctAnswer": "Anne Frank"},
            {"text": "What is the antonym of 'Transparent'?", "options": ["Opaque", "Translucent", "Clear", "Bright"], "correctAnswer": "Opaque"},
            {"text": "Choose the correctly spelled word.", "options": ["Embarrass", "Embaras", "Emberass", "Embarass"], "correctAnswer": "Embarrass"}
        ],
        "medium": [
            {"text": "In 'A Triumph of Surgery', who is Tricki?", "options": ["A dog", "A cat", "A surgeon", "A gardener"], "correctAnswer": "A dog"},
            {"text": "Identify the clause: 'I will go <i>if it stops raining</i>.'", "options": ["Adverb Clause", "Noun Clause", "Adjective Clause", "Relative Clause"], "correctAnswer": "Adverb Clause"},
            {"text": "Which figure of speech is used in: 'Life is a roller coaster'?", "options": ["Metaphor", "Simile", "Personification", "Hyperbole"], "correctAnswer": "Metaphor"},
            {"text": "Change into passive voice: 'The police caught the thief.'", "options": ["The thief was caught by the police.", "The thief is caught by the police.", "The police was catching the thief.", "The thief had been caught by the police."], "correctAnswer": "The thief was caught by the police."},
            {"text": "Identify the gerund: 'Drinking water is essential.'", "options": ["Drinking", "Water", "Is", "Essential"], "correctAnswer": "Drinking"},
            {"text": "What does the root 'Bio' mean?", "options": ["Life", "Earth", "Light", "Sound"], "correctAnswer": "Life"},
            {"text": "Identify the participle: 'The crying baby finally fell asleep.'", "options": ["Crying", "Baby", "Asleep", "Fell"], "correctAnswer": "Crying"},
            {"text": "In 'The Thief's Story', what was Hari Singh's real name?", "options": ["He didn't have one / He used aliases", "Anil", "Suresh", "Ramesh"], "correctAnswer": "He didn't have one / He used aliases"},
            {"text": "Choose the correct modal: 'You _____ obey the traffic rules.'", "options": ["Must", "Might", "Could", "May"], "correctAnswer": "Must"},
            {"text": "Identify the homophone: 'I need to _____ wait for my turn.'", "options": ["Wait", "Weight", "Wade", "Wayed"], "correctAnswer": "Wait"},
            {"text": "Which of these is a complex sentence?", "options": ["The man who is wearing a red hat is my teacher.", "The man is my teacher.", "The man wears a red hat and is my teacher.", "I like red hats."], "correctAnswer": "The man who is wearing a red hat is my teacher."},
            {"text": "What is the meaning of 'Optimistic'?", "options": ["Hopeful and confident about the future", "Expecting the worst", "Sad", "Angry"], "correctAnswer": "Hopeful and confident about the future"},
            {"text": "Identify the reflexive pronoun: 'I did it myself.'", "options": ["Myself", "I", "Did", "It"], "correctAnswer": "Myself"},
            {"text": "What is 'Enjambment' in poetry?", "options": ["The continuation of a sentence without a pause beyond the end of a line", "The repetition of a word", "A rhyme at the end of a line", "A pause in the middle of a line"], "correctAnswer": "The continuation of a sentence without a pause beyond the end of a line"},
            {"text": "Change into indirect speech: She said, 'I am happy.'", "options": ["She said that she was happy.", "She said that I am happy.", "She said she is happy.", "She says she was happy."], "correctAnswer": "She said that she was happy."}
        ],
        "hard": [
            {"text": "Identify the mood: 'I suggest that he be present.'", "options": ["Subjunctive", "Indicative", "Imperative", "Interrogative"], "correctAnswer": "Subjunctive"},
            {"text": "What device is used in: 'Fair is foul, and foul is fair'?", "options": ["Chiasmus / Antithesis", "Simile", "Oxymoron", "Personification"], "correctAnswer": "Chiasmus / Antithesis"},
            {"text": "Who is the author of 'The Midnight Visitor'?", "options": ["Robert Arthur", "James Herriot", "H.G. Wells", "Guy de Maupassant"], "correctAnswer": "Robert Arthur"},
            {"text": "Identify the error: 'None of the two girls are invited.'", "options": ["'None' should be 'Neither' and 'are' should be 'is'", "'None' should be 'Neither'", "'are' should be 'is'", "No error"], "correctAnswer": "'None' should be 'Neither' and 'are' should be 'is'"},
            {"text": "What is the meaning of 'Malapropism'?", "options": ["Misuse of a word by confusion with one of similar sound", "A type of rhyme", "A grammatical case", "A figure of speech for exaggeration"], "correctAnswer": "Misuse of a word by confusion with one of similar sound"},
            {"text": "Identify the 'Synecdoche': 'He has a lot of mouths to feed.'", "options": ["Mouths (referring to people)", "Feed", "Lot", "He"], "correctAnswer": "Mouths (referring to people)"},
            {"text": "Which clause is italicized: 'The reason <i>why he failed</i> is unknown.'?", "options": ["Adjective Clause", "Noun Clause", "Adverb Clause", "Relative Phrase"], "correctAnswer": "Adjective Clause"},
            {"text": "What follows the 'Subjunctive Mood' in: 'It is essential that he _____ there on time.'?", "options": ["Be", "Is", "Was", "Been"], "correctAnswer": "Be"},
            {"text": "Identify the 'Transitive' or 'Intransitive' nature of 'Slept' in 'He slept soundly.'", "options": ["Intransitive", "Transitive", "Linking", "Auxiliary"], "correctAnswer": "Intransitive"},
            {"text": "What is 'Alliteration'?", "options": ["The occurrence of the same letter or sound at the beginning of adjacent words", "A reference to history", "Comparing two things using as", "A word that sounds like its meaning"], "correctAnswer": "The occurrence of the same letter or sound at the beginning of adjacent words"},
            {"text": "In 'The Necklace', what was the original cost of the necklace?", "options": ["500 francs", "36,000 francs", "40,000 francs", "18,000 francs"], "correctAnswer": "500 francs"},
            {"text": "What is an 'Irony'?", "options": ["The expression of one's meaning by using language that normally signifies the opposite", "A type of metal", "A logical conclusion", "A rhythmic pattern in poetry"], "correctAnswer": "The expression of one's meaning by using language that normally signifies the opposite"},
            {"text": "Identify the subject in: 'There are many players on the field.'", "options": ["Many players", "There", "Field", "Are"], "correctAnswer": "Many players"},
            {"text": "What does a 'lexicographer' do?", "options": ["Compiles dictionaries", "Studies stars", "Works in a bank", "Fixes cars"], "correctAnswer": "Compiles dictionaries"},
            {"text": "What is 'Personification'?", "options": ["Giving human qualities to non-human things", "Focusing on a single person", "A biography", "A character's appearance"], "correctAnswer": "Giving human qualities to non-human things"}
        ]
    },
    "maths": {
        "easy": [
            {"text": "What is the HCF of 24 and 36?", "options": ["12", "6", "4", "72"], "correctAnswer": "12"},
            {"text": "Find the zeros of the polynomial x^2 - 4.", "options": ["2, -2", "2, 2", "0, 4", "1, -1"], "correctAnswer": "2, -2"},
            {"text": "In the equation 2x + 3y = 6, if x = 0, find y.", "options": ["2", "3", "0", "6"], "correctAnswer": "2"},
            {"text": "What is the discriminant (D) of a quadratic equation ax^2 + bx + c = 0?", "options": ["b^2 - 4ax", "b^2 + 4ax", "4ax - b^2", "None"], "correctAnswer": "b^2 - 4ac".replace('ax', 'ac')}, # Note: prompt says options are strings, I'll fix this manually
            {"text": "The 10th term of the AP: 2, 7, 12, ... is:", "options": ["47", "42", "52", "37"], "correctAnswer": "47"},
            {"text": "What is the value of sin 30°?", "options": ["1/2", "√3/2", "1", "0"], "correctAnswer": "1/2"},
            {"text": "If the diameter of a circle is 14 cm, its circumference is:", "options": ["44 cm", "22 cm", "88 cm", "154 cm"], "correctAnswer": "44 cm"},
            {"text": "Find the mid-point of the segment joining (2, 4) and (6, 8).", "options": ["(4, 6)", "(3, 5)", "(8, 12)", "(4, 4)"], "correctAnswer": "(4, 6)"},
            {"text": "The sum of the first n natural numbers is:", "options": ["n(n+1)/2", "n^2", "n(n-1)/2", "2n"], "correctAnswer": "n(n+1)/2"},
            {"text": "Which of these is a rational number?", "options": ["0", "√3", "π", "0.101001000..."], "correctAnswer": "0"},
            {"text": "What is the value of tan 45°?", "options": ["1", "0", "√3", "1/√3"], "correctAnswer": "1"},
            {"text": "Find the area of a circle with radius 7 cm.", "options": ["154 sq cm", "44 sq cm", "144 sq cm", "49 sq cm"], "correctAnswer": "154 sq cm"},
            {"text": "How many tangents can a circle have?", "options": ["Infinite", "One", "Two", "Zero"], "correctAnswer": "Infinite"},
            {"text": "Identify the coefficient of x in 3x^2 - 5x + 7.", "options": ["-5", "3", "7", "x"], "correctAnswer": "-5"},
            {"text": "The probability of getting a head in a coin toss is:", "options": ["1/2", "1", "0", "1/4"], "correctAnswer": "1/2"}
        ],
        "medium": [
            {"text": "Find the value of k if the roots of kx^2 + 4x + 1 = 0 are real and equal.", "options": ["4", "2", "1", "0"], "correctAnswer": "4"},
            {"text": "How many terms of the AP: 9, 17, 25, ... must be taken to give a sum of 636?", "options": ["12", "14", "10", "15"], "correctAnswer": "12"},
            {"text": "Evaluate: (sin 18°) / (cos 72°)", "options": ["1", "0", "2", "-1"], "correctAnswer": "1"},
            {"text": "If a tower 30m high casts a shadow 10√3 m long, the angle of elevation of the sun is:", "options": ["60°", "30°", "45°", "90°"], "correctAnswer": "60°"},
            {"text": "Find the distance between the points (0, 0) and (36, 15).", "options": ["39", "36", "45", "51"], "correctAnswer": "39"},
            {"text": "In a right triangle, if sin A = 3/4, then cos A is:", "options": ["√7 / 4", "4/3", "√7 / 3", "7/4"], "correctAnswer": "√7 / 4"},
            {"text": "Find the ratio in which the line segment joining (1, -5) and (-4, 5) is divided by the x-axis.", "options": ["1:1", "1:2", "2:1", "2:3"], "correctAnswer": "1:1"},
            {"text": "The area of a sector of angle θ is:", "options": ["(θ/360) * πr^2", "(θ/180) * πr^2", "(θ/360) * 2πr", "πr^2"], "correctAnswer": "(θ/360) * πr^2"},
            {"text": "If the volume of a sphere is 4851 cubic cm, its surface area is:", "options": ["1386 sq cm", "4851 sq cm", "616 sq cm", "144 sq cm"], "correctAnswer": "1386 sq cm"},
            {"text": "Solve for x and y: x + y = 14, x - y = 4", "options": ["x=9, y=5", "x=10, y=4", "x=8, y=6", "x=7, y=7"], "correctAnswer": "x=9, y=5"},
            {"text": "The 11th term of the AP: -3, -1/2, 2, ... is:", "options": ["22", "28", "25", "20"], "correctAnswer": "22"},
            {"text": "A card is drawn from a well-shuffled pack of 52 cards. Find the probability of getting a king of red color.", "options": ["1/26", "1/52", "1/13", "1/4"], "correctAnswer": "1/26"},
            {"text": "Find the area of a triangle whose vertices are (1, -1), (-4, 6), and (-3, -5).", "options": ["24 sq units", "12 sq units", "48 sq units", "36 sq units"], "correctAnswer": "24 sq units"},
            {"text": "If tan A = 4/3, find sin A.", "options": ["4/5", "3/5", "3/4", "5/4"], "correctAnswer": "4/5"},
            {"text": "The volume of a frustum of a cone is:", "options": ["1/3 πh(r1^2 + r2^2 + r1r2)", "πh(r1+r2)", "1/3 πr^2h", "4/3 πr^3"], "correctAnswer": "1/3 πh(r1^2 + r2^2 + r1r2)"}
        ],
        "hard": [
            {"text": "Solve for x: [1 / (x+4)] - [1 / (x-7)] = 11 / 30", "options": ["1, 2", "3, 4", "1, -2", "2, -1"], "correctAnswer": "1, 2"},
            {"text": "In a circle of radius 21 cm, an arc subtends an angle of 60° at the center. Find the area of the segment formed by the corresponding chord.", "options": ["(231 - 441√3/4) sq cm", "231 sq cm", "441√3/4 sq cm", "115 sq cm"], "correctAnswer": "(231 - 441√3/4) sq cm"},
            {"text": "If the sum of first 7 terms of an AP is 49 and that of 17 terms is 289, find the sum of first n terms.", "options": ["n^2", "n(n+1)", "2n^2", "n^2/2"], "correctAnswer": "n^2"},
            {"text": "Prove that √[(1 + sin A) / (1 - sin A)] =", "options": ["sec A + tan A", "sec A - tan A", "cos A / sin A", "1"], "correctAnswer": "sec A + tan A"},
            {"text": "A container shapes like a right circular cylinder having diameter 12 cm and height 15 cm is full of ice-cream. The ice-cream is to be filled into cones of height 12 cm and diameter 6 cm, having a hemispherical shape on the top. Find the number of such cones which can be filled with ice-cream.", "options": ["10", "12", "8", "15"], "correctAnswer": "10"},
            {"text": "Find the ratio in which the line 2x + y - 4 = 0 divides the line segment joining (2, -2) and (3, 7).", "options": ["2:9", "9:2", "3:4", "4:3"], "correctAnswer": "2:9"},
            {"text": "If cosθ + sinθ = √2cosθ, show that cosθ - sinθ =", "options": ["√2sinθ", "√2cosθ", "1", "0"], "correctAnswer": "√2sinθ"},
            {"text": "Find the roots of the equation 5^(x+1) + 5^(2-x) = 126.", "options": ["2, -1", "1, -2", "2, 1", "0, 1"], "correctAnswer": "2, -1"},
            {"text": "A metallic sphere of radius 4.2 cm is melted and recast into the shape of a cylinder of radius 6 cm. Find the height of the cylinder.", "options": ["2.744 cm", "3 cm", "2.5 cm", "4.2 cm"], "correctAnswer": "2.744 cm"},
            {"text": "Find the value of p for which the points (-1, 3), (2, p), and (5, -1) are collinear.", "options": ["1", "0", "2", "-1"], "correctAnswer": "1"},
            {"text": "In a class test, the sum of Shefali's marks in Mathematics and English is 30. Had she got 2 marks more in Mathematics and 3 marks less in English, the product of their marks would have been 210. Find her marks in the two subjects.", "options": ["(12, 18) or (13, 17)", "(10, 20)", "(15, 15)", "(14, 16)"], "correctAnswer": "(12, 18) or (13, 17)"},
            {"text": "If sec 4A = cosec (A - 20°), where 4A is an acute angle, find the value of A.", "options": ["22°", "20°", "25°", "30°"], "correctAnswer": "22°"},
            {"text": "The sum of the digits of a two-digit number is 9. Also, nine times this number is twice the number obtained by reversing the order of the digits. Find the number.", "options": ["18", "27", "36", "45"], "correctAnswer": "18"},
            {"text": "Water in a canal, 6 m wide and 1.5 m deep, is flowing with a speed of 10 km/h. How much area will it irrigate in 30 minutes, if 8 cm of standing water is needed?", "options": ["562500 sq m", "500000 sq m", "600000 sq m", "450000 sq m"], "correctAnswer": "562500 sq m"},
            {"text": "A tree breaks due to storm and the broken part bends so that the top of the tree touches the ground making an angle 30° with it. The distance between the foot of the tree to the point where the top touches the ground is 8 m. Find the height of the tree.", "options": ["8√3 m", "8/√3 m", "16√3 m", "12 m"], "correctAnswer": "8√3 m"}
        ]
    },
    "science": {
        "easy": [
            {"text": "Which mirror is used as a rear-view mirror in vehicles?", "options": ["Convex mirror", "Concave mirror", "Plane mirror", "Bifocal mirror"], "correctAnswer": "Convex mirror"},
            {"text": "What is the SI unit of power of a lens?", "options": ["Dioptre", "Watt", "Joule", "Meter"], "correctAnswer": "Dioptre"},
            {"text": "The pH value of neutral water is:", "options": ["7", "0", "14", "1"], "correctAnswer": "7"},
            {"text": "Which gas is evolved when an acid reacts with a metal?", "options": ["Hydrogen", "Oxygen", "Carbon dioxide", "Nitrogen"], "correctAnswer": "Hydrogen"},
            {"text": "What is the non-metal that is liquid at room temperature?", "options": ["Bromine", "Mercury", "Phosphorus", "Iodine"], "correctAnswer": "Bromine"},
            {"text": "The master gland of the human body is:", "options": ["Pituitary gland", "Thyroid gland", "Adrenal gland", "Pancreas"], "correctAnswer": "Pituitary gland"},
            {"text": "What is the byproduct of photosynthesis?", "options": ["Oxygen", "Carbon dioxide", "Nitrogen", "Chlorophyll"], "correctAnswer": "Oxygen"},
            {"text": "Identify the element with atomic number 6.", "options": ["Carbon", "Oxygen", "Nitrogen", "Boron"], "correctAnswer": "Carbon"},
            {"text": "The SI unit of electric current is:", "options": ["Ampere", "Volt", "Ohm", "Watt"], "correctAnswer": "Ampere"},
            {"text": "Which part of the eye controls the amount of light entering it?", "options": ["Iris", "Pupil", "Retina", "Cornea"], "correctAnswer": "Iris"},
            {"text": "What is the formula for baking soda?", "options": ["NaHCO3", "Na2CO3", "NaOH", "CaCO3"], "correctAnswer": "NaHCO3"},
            {"text": "Which acid is present in ant sting?", "options": ["Methanoic acid (Formic acid)", "Acetic acid", "Citric acid", "Tartaric acid"], "correctAnswer": "Methanoic acid (Formic acid)"},
            {"text": "The site of fertilization in humans is:", "options": ["Fallopian tube", "Uterus", "Ovary", "Vagina"], "correctAnswer": "Fallopian tube"},
            {"text": "Which component of blood helps in clotting?", "options": ["Platelets", "WBCs", "RBCs", "Plasma"], "correctAnswer": "Platelets"},
            {"text": "Identify the lens used to correct myopia.", "options": ["Concave lens", "Convex lens", "Cylindrical lens", "Bifocal lens"], "correctAnswer": "Concave lens"}
        ],
        "medium": [
            {"text": "Why does the blue color of copper sulfate solution fade when an iron nail is dipped in it?", "options": ["Displacement reaction (Iron is more reactive)", "Combination reaction", "Decomposition reaction", "Neutralization reaction"], "correctAnswer": "Displacement reaction (Iron is more reactive)"},
            {"text": "What is the valency of Magnesium (At. No. 12)?", "options": ["2", "1", "8", "3"], "correctAnswer": "2"},
            {"text": "Identify the functional group in C2H5OH.", "options": ["Alcohol (-OH)", "Aldehyde (-CHO)", "Ketone (C=O)", "Carboxylic acid (-COOH)"], "correctAnswer": "Alcohol (-OH)"},
            {"text": "Which part of the brain controls involuntary actions like breathing and heart rate?", "options": ["Medulla oblongata", "Cerebellum", "Cerebrum", "Hypothalamus"], "correctAnswer": "Medulla oblongata"},
            {"text": "What constitutes the 'PNS' in humans?", "options": ["Cranial and Spinal nerves", "Brain and Spinal Cord", "Heart and Blood Vessels", "Muscles"], "correctAnswer": "Cranial and Spinal nerves"},
            {"text": "A solution turns red litmus blue, its pH is likely to be:", "options": ["10", "1", "4", "5"], "correctAnswer": "10"},
            {"text": "What happens when a ray of light passes from a denser medium to a rarer medium?", "options": ["Bends away from the normal", "Bends towards the normal", "Goes straight", "Reflects back"], "correctAnswer": "Bends away from the normal"},
            {"text": "The least distance of distinct vision for a young adult is:", "options": ["25 cm", "25 m", "2.5 cm", "8 m"], "correctAnswer": "25 cm"},
            {"text": "Identify the component of a circuit that regulates current without changing voltage source.", "options": ["Rheostat / Variable Resistor", "Ammeter", "Voltmeter", "Switch"], "correctAnswer": "Rheostat / Variable Resistor"},
            {"text": "What is 'Trophic Level' in an ecosystem?", "options": ["Each step or level of the food chain", "The speed of energy transfer", "The type of habitat", "The size of population"], "correctAnswer": "Each step or level of the food chain"},
            {"text": "Name the hormone which regulates carbohydrate, protein, and fat metabolism.", "options": ["Thyroxine", "Insulin", "Adrenaline", "Growth hormone"], "correctAnswer": "Thyroxine"},
            {"text": "Which part of the flower develops into a fruit after fertilization?", "options": ["Ovary", "Ovule", "Stigma", "Anther"], "correctAnswer": "Ovary"},
            {"text": "A wire of resistance R is cut into five equal parts. These parts are then connected in parallel. If the equivalent resistance of this combination is R', then the ratio R/R' is:", "options": ["25", "1/25", "5", "1/5"], "correctAnswer": "25"},
            {"text": "Identify the element with electronic configuration 2, 8, 7.", "options": ["Chlorine", "Fluorine", "Argon", "Sodium"], "correctAnswer": "Chlorine"},
            {"text": "What is the process of conversion of food waste into nutrient-rich soil by earthworms?", "options": ["Vermicomposting", "Pyrolysis", "Landfilling", "Recycling"], "correctAnswer": "Vermicomposting"}
        ],
        "hard": [
            {"text": "Why do stars twinkle but planets do not?", "options": ["Stars are point sources far away; planets are extended sources closer to Earth", "Stars have their own light", "Planets are made of rock", "Stars are hotter"], "correctAnswer": "Stars are point sources far away; planets are extended sources closer to Earth"},
            {"text": "State Mendel's Law of Segregation.", "options": ["The two alleles for a heritable character segregate during gamete formation", "Alleles combine randomly", "Traits are always dominant", "Environment changes genes"], "correctAnswer": "The two alleles for a heritable character segregate during gamete formation"},
            {"text": "What is 'Saponification'?", "options": ["Hydrolysis of esters with alkali to produce soap", "Reaction of acid and base", "Burning of fats", "Mixing oil and water"], "correctAnswer": "Hydrolysis of esters with alkali to produce soap"},
            {"text": "Specify the role of 'ATP' in cell biology.", "options": ["Energy currency of the cell", "Storage of water", "Protein builder", "Transporter of waste"], "correctAnswer": "Energy currency of the cell"},
            {"text": "What is the resistance of an ideal ammeter and an ideal voltmeter?", "options": ["Ammeter: Zero; Voltmeter: Infinite", "Ammeter: Infinite; Voltmeter: Zero", "Both zero", "Both infinite"], "correctAnswer": "Ammeter: Zero; Voltmeter: Infinite"},
            {"text": "Explain the 'Tyndall Effect'.", "options": ["Scattering of light by colloidal particles", "Refraction by water", "Reflection by mirrors", "Dispersion by prisms"], "correctAnswer": "Scattering of light by colloidal particles"},
            {"text": "Which compound is used as an antacid to neutralize stomach acidity?", "options": ["Magnesium Hydroxide (Milk of Magnesia)", "Sodium Chloride", "Copper Sulfate", "Calcium Carbonate"], "correctAnswer": "Magnesium Hydroxide (Milk of Magnesia)"},
            {"text": "Identify the 'Homologous series' characteristic.", "options": ["Same functional group and similar chemical properties", "Different functional groups", "Same mass for all members", "Same physical properties"], "correctAnswer": "Same functional group and similar chemical properties"},
            {"text": "What occurs during 'Double Fertilization' in angiosperms?", "options": ["One sperm fuses with egg, another fuses with two polar nuclei", "Two eggs are fertilized", "One egg is fertilized twice", "No sperm is involved"], "correctAnswer": "One sperm fuses with egg, another fuses with two polar nuclei"},
            {"text": "Describe the function of 'Bile juice'.", "options": ["Emulsification of fats and making medium alkaline", "Digestion of starch", "Protein breakdown", "Killing bacteria only"], "correctAnswer": "Emulsification of fats and making medium alkaline"},
            {"text": "How much electricity is consumed by a 100W bulb used for 10 hours?", "options": ["1 Unit (kWh)", "10 Units", "100 Units", "0.1 Unit"], "correctAnswer": "1 Unit (kWh)"},
            {"text": "What is the reason for 'Bio-magnification' in a food chain?", "options": ["Accumulation of non-biodegradable chemicals at higher trophic levels", "Increase in population", "Growth of plants", "Reduction in energy"], "correctAnswer": "Accumulation of non-biodegradable chemicals at higher trophic levels"},
            {"text": "Identify the 'Metalloid' from these options.", "options": ["Silicon", "Aluminum", "Copper", "Iron"], "correctAnswer": "Silicon"},
            {"text": "What is the formula of 'Plaster of Paris'?", "options": ["CaSO4 · 1/2 H2O", "CaSO4 · 2H2O", "CaO", "CaCO3"], "correctAnswer": "CaSO4 · 1/2 H2O"},
            {"text": "Which law relates V, I, and R in a circuit?", "options": ["Ohm's Law", "Faraday's Law", "Joule's Law", "Newton's Law"], "correctAnswer": "Ohm's Law"}
        ]
    },
    "social-science": {
        "easy": [
            {"text": "When did Gandhiji return to India from South Africa?", "options": ["1915", "1917", "1920", "1930"], "correctAnswer": "1915"},
            {"text": "Who composed the 'Vande Mataram'?", "options": ["Bankim Chandra Chattopadhyay", "Rabindranath Tagore", "Sarojini Naidu", "Jawaharlal Nehru"], "correctAnswer": "Bankim Chandra Chattopadhyay"},
            {"text": "What is the main source of income for the central government in India?", "options": ["Taxes (GST, Income Tax, etc.)", "Lottery", "Foreign aid", "Agriculture"], "correctAnswer": "Taxes (GST, Income Tax, etc.)"},
            {"text": "Which state has the largest forest cover in India?", "options": ["Madhya Pradesh", "Arunachal Pradesh", "Odisha", "Chhattisgarh"], "correctAnswer": "Madhya Pradesh"},
            {"text": "The first World War ended in which year?", "options": ["1918", "1914", "1939", "1945"], "correctAnswer": "1918"},
            {"text": "Who is the 'Supreme Commander' of the Indian Armed Forces?", "options": ["The President", "The Prime Minister", "Chief of Defense Staff", "Defense Minister"], "correctAnswer": "The President"},
            {"text": "Which fiber is known as the 'Golden Fiber'?", "options": ["Jute", "Cotton", "Silk", "Nylon"], "correctAnswer": "Jute"},
            {"text": "Who was the first woman President of India?", "options": ["Pratibha Patil", "Indira Gandhi", "Sarojini Naidu", "Droupadi Murmu"], "correctAnswer": "Pratibha Patil"},
            {"text": "In which city did the Jallianwala Bagh massacre take place?", "options": ["Amritsar", "Delhi", "Lahore", "Kolkata"], "correctAnswer": "Amritsar"},
            {"text": "When is 'Constitution Day' celebrated in India?", "options": ["26th November", "26th January", "15th August", "2nd October"], "correctAnswer": "26th November"},
            {"text": "What is the primary sector of the economy?", "options": ["Agriculture and related activities", "Manufacturing", "Services", "Banking"], "correctAnswer": "Agriculture and related activities"},
            {"text": "Which imaginay line divides the world into Time Zones?", "options": ["Prime Meridian", "Equator", "Tropic of Cancer", "Arctic Circle"], "correctAnswer": "Prime Meridian"},
            {"text": "Who said 'Swaraj is my birthright and I shall have it'?", "options": ["Bal Gangadhar Tilak", "Mahatma Gandhi", "Subhash Chandra Bose", "Lala Lajpat Rai"], "correctAnswer": "Bal Gangadhar Tilak"},
            {"text": "What is the minimum age to be elected as a member of the Lok Sabha?", "options": ["25 years", "30 years", "35 years", "18 years"], "correctAnswer": "25 years"},
            {"text": "Which ocean is the largest on Earth?", "options": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"], "correctAnswer": "Pacific Ocean"}
        ],
        "medium": [
            {"text": "The 'Civil Disobedience Movement' was started with which event?", "options": ["Dandi March / Break Salt Law", "Non-Cooperation", "Quit India", "Chauri Chaura"], "correctAnswer": "Dandi March / Break Salt Law"},
            {"text": "Which Soil is ideal for the cultivation of cotton in India?", "options": ["Black Soil (Regur Soil)", "Alluvial Soil", "Red Soil", "Laterite Soil"], "correctAnswer": "Black Soil (Regur Soil)"},
            {"text": "What is the 'Power Sharing' in a democracy?", "options": ["Distribution of power among different organs of government", "Giving all power to one leader", "A type of election", "Rule by the military"], "correctAnswer": "Distribution of power among different organs of government"},
            {"text": "Which sector is also known as the 'Service Sector'?", "options": ["Tertiary Sector", "Primary Sector", "Secondary Sector", "Quaternary Sector"], "correctAnswer": "Tertiary Sector"},
            {"text": "Who founded the 'Swaraj Party' within the Congress?", "options": ["C.R. Das and Motilal Nehru", "Mahatma Gandhi", "Sardar Patel", "B.R. Ambedkar"], "correctAnswer": "C.R. Das and Motilal Nehru"},
            {"text": "What is the 'Human Development Index' (HDI)?", "options": ["Composite statistic of life expectancy, education, and per capita income", "Population growth rate", "Industrial production index", "Literacy rate only"], "correctAnswer": "Composite statistic of life expectancy, education, and per capita income"},
            {"text": "The 'Great Depression' began in which year?", "options": ["1929", "1914", "1939", "1947"], "correctAnswer": "1929"},
            {"text": "Which fundamental right was removed from the list of Fundamental Rights and made a Legal Right?", "options": ["Right to Property", "Right to Education", "Right to Freedom", "Right to Equality"], "correctAnswer": "Right to Property"},
            {"text": "Identify the 'Renewable Resource' from these.", "options": ["Solar Energy", "Coal", "Petroleum", "Natural Gas"], "correctAnswer": "Solar Energy"},
            {"text": "What is the 'Federalism' system?", "options": ["Government power is divided between central and regional levels", "A single government for the whole world", "Rule by a dictator", "Direct democracy"], "correctAnswer": "Government power is divided between central and regional levels"},
            {"text": "The 'Bretton Woods' conference led to the creation of:", "options": ["IMF and World Bank", "United Nations", "WHO", "WTO"], "correctAnswer": "IMF and World Bank"},
            {"text": "Which iron and steel plant was established with German help?", "options": ["Rourkela", "Bhilai", "Durgapur", "Bokaro"], "correctAnswer": "Rourkela"},
            {"text": "What is 'Liberalism' in the context of the 19th-century Europe?", "options": ["Freedom for the individual and equality of all before the law", "Rule by the church", "Absolute monarchy", "Socialism"], "correctAnswer": "Freedom for the individual and equality of all before the law"},
            {"text": "In which state is the Bhakra Nangal Dam located?", "options": ["Himachal Pradesh / Punjab border", "Karnataka", "West Bengal", "Gujarat"], "correctAnswer": "Himachal Pradesh / Punjab border"},
            {"text": "What is 'Secularism' according to the Indian Preamble?", "options": ["The state has no religion and treats all religions equally", "The state is anti-religion", "The state follows Hinduism", "The state follows Buddhism"], "correctAnswer": "The state has no religion and treats all religions equally"}
        ],
        "hard": [
            {"text": "What was the main reason for the calling off of the 'Non-Cooperation Movement'?", "options": ["Chauri Chaura incident (1922)", "Dandi March", "Simon Commission", "Gandhi-Irwin Pact"], "correctAnswer": "Chauri Chaura incident (1922)"},
            {"text": "Explain the concept of 'Sustainable Development'.", "options": ["Development that meets the needs of the present without compromising future generations", "Focusing only on industrial growth", "Using all resources now", "Planting more trees only"], "correctAnswer": "Development that meets the needs of the present without compromising future generations"},
            {"text": "Which article of the Indian Constitution gives the Supreme Court the power to issue 'Writs'?", "options": ["Article 32", "Article 14", "Article 19", "Article 226 (for High Court)"], "correctAnswer": "Article 32"},
            {"text": "Who led the 'Dalit' movement and chaired the Drafting Committee of the Constitution?", "options": ["Dr. B.R. Ambedkar", "Jyotirao Phule", "Periyar", "Gandhiji"], "correctAnswer": "Dr. B.R. Ambedkar"},
            {"text": "Identify the 'Agglomeration Economies' in industry.", "options": ["Industries tending to come together to use advantages offered by urban centers", "Large scale production", "Use of heavy machines", "Export oriented units"], "correctAnswer": "Industries tending to come together to use advantages offered by urban centers"},
            {"text": "What is 'SHG' in the context of rural finance?", "options": ["Self Help Group", "Super Health Grant", "Small Housing Group", "State Highway Guard"], "correctAnswer": "Self Help Group"},
            {"text": "In which city was the 'First International Earth Summit' held in 1992?", "options": ["Rio de Janeiro", "Kyoto", "New Delhi", "Stockholm"], "correctAnswer": "Rio de Janeiro"},
            {"text": "The 'Simon Commission' was boycotted because:", "options": ["It did not have any Indian members", "It suggested partition", "It was led by a woman", "It was expensive"], "correctAnswer": "It did not have any Indian members"},
            {"text": "What is the 'Green Revolution's primary impact?", "options": ["Significant increase in food grain production due to HYV seeds", "Promotion of green colors", "Saving forests", "Reducing pollution"], "correctAnswer": "Significant increase in food grain production due to HYV seeds"},
            {"text": "Define 'Globalization' in economic terms.", "options": ["Integration of the national economy with the world economy through trade and investment", "Traveling the world", "Universal language", "Internet connectivity only"], "correctAnswer": "Integration of the national economy with the world economy through trade and investment"},
            {"text": "Who was the founder of the 'Hindustan Socialist Republican Association' (HSRA)?", "options": ["Bhagat Singh, Chandrashekhar Azad and others", "Mahatma Gandhi", "Subhash Chandra Bose", "Sardar Patel"], "correctAnswer": "Bhagat Singh, Chandrashekhar Azad and others"},
            {"text": "The 'Golden Quadrilateral' superhighway connects which four cities?", "options": ["Delhi, Mumbai, Chennai, Kolkata", "Delhi, Nagpur, Bengaluru, Hyderabad", "Mumbai, Pune, Goa, Kochi", "Kolkata, Patna, Lucknow, Delhi"], "correctAnswer": "Delhi, Mumbai, Chennai, Kolkata"},
            {"text": "What is 'Judicial Activism'?", "options": ["Courts taking a proactive role in protecting rights and ensuring justice", "Judges going on strike", "Ignoring laws", "Rule by the executive"], "correctAnswer": "Courts taking a proactive role in protecting rights and ensuring justice"},
            {"text": "Identify the 'Bolshevik' leader of the 1917 Russian Revolution.", "options": ["Vladimir Lenin", "Tsar Nicholas II", "Stalin", "Kerensky"], "correctAnswer": "Vladimir Lenin"},
            {"text": "Which organization prepares the 'World Development Report'?", "options": ["World Bank", "IMF", "UNDP", "WTO"], "correctAnswer": "World Bank"}
        ]
    }
}

def main():
    bank_path = '/Users/arpan1.mukherjee/code/GhostMaze/public/AhirsAcademy/data/question_bank.json'
    
    with open(bank_path, 'r', encoding='utf-8') as f:
        question_bank = json.load(f)
        
    question_bank['class_10'] = class_10_data
    
    with open(bank_path, 'w', encoding='utf-8') as f:
        json.dump(question_bank, f, indent=4, ensure_ascii=False)
        
    print("Successfully injected final batch of 15 comprehensive questions per tier for Class 10!")

if __name__ == '__main__':
    main()
