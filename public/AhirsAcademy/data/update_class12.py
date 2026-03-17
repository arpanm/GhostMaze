import json
import os

class_12_data = {
    "english": {
        "easy": [
            {"text": "Who is the author of 'The Last Lesson'?", "options": ["Alphonse Daudet", "Anees Jung", "Louis Fischer", "Selma Lagerlöf"], "correctAnswer": "Alphonse Daudet"},
            {"text": "In 'Lost Spring', what is Mukesh's ambition?", "options": ["To be a motor mechanic", "To be a pilot", "To make bangles", "To go to school"], "correctAnswer": "To be a motor mechanic"},
            {"text": "Which poet wrote 'My Mother at Sixty-six'?", "options": ["Kamala Das", "Stephen Spender", "Pablo Neruda", "John Keats"], "correctAnswer": "Kamala Das"},
            {"text": "Identify the type of sentence: 'Were I a king, I would help everyone.'", "options": ["Subjunctive / Conditional", "Declarative", "Imperative", "Interrogative"], "correctAnswer": "Subjunctive / Conditional"},
            {"text": "What is the synonym of 'Evanescent'?", "options": ["Short-lived / Fading", "Permanent", "Beautiful", "Noisy"], "correctAnswer": "Short-lived / Fading"},
            {"text": "Choose the correct article: 'It was _____ unique opportunity.'", "options": ["A", "An", "The", "No article"], "correctAnswer": "A"},
            {"text": "Identify the preposition: 'The solution depends on your effort.'", "options": ["On", "Depends", "Solution", "Effort"], "correctAnswer": "On"},
            {"text": "What is the meaning of the idiom 'To burn the midnight oil'?", "options": ["To work late into the night", "To waste energy", "To cook food", "To save money"], "correctAnswer": "To work late into the night"},
            {"text": "Which word is an adjective in 'The majestic mountains'?", "options": ["Majestic", "Mountains", "The", "Is"], "correctAnswer": "Majestic"},
            {"text": "What is the past participle of 'Slay'?", "options": ["Slain", "Slew", "Slayed", "Slaying"], "correctAnswer": "Slain"},
            {"text": "In 'The Rattrap', who is the ironmaster's daughter?", "options": ["Edla Willmansson", "Maria", "Sophie", "Jansie"], "correctAnswer": "Edla Willmansson"},
            {"text": "What is the antonym of 'Ambiguous'?", "options": ["Clear / Precise", "Vague", "Dark", "Loud"], "correctAnswer": "Clear / Precise"},
            {"text": "Choose the correctly spelled word.", "options": ["Maintenance", "Maintainance", "Maintenence", "Maintennance"], "correctAnswer": "Maintenance"},
            {"text": "In the poem 'Keeping Quiet', what does the poet ask us to do?", "options": ["To stay still and introspect", "To run fast", "To shout loudly", "To fight for rights"], "correctAnswer": "To stay still and introspect"},
            {"text": "Identify the conjunction: 'Neither the teacher nor the students were ready.'", "options": ["Neither...nor", "Teacher", "Students", "Ready"], "correctAnswer": "Neither...nor"}
        ],
        "medium": [
            {"text": "Identify the figure of speech: 'The camel is the ship of the desert.'", "options": ["Metaphor", "Simile", "Personification", "Hyperbole"], "correctAnswer": "Metaphor"},
            {"text": "Change into passive voice: 'One should keep one's promises.'", "options": ["Promises should be kept.", "Promises should be kept by one.", "Promises are to be kept.", "One had been kept promises."], "correctAnswer": "Promises should be kept."},
            {"text": "What is 'Alliteration'?", "options": ["The repetition of initial consonant sounds in a sentence", "A comparison using like", "An exaggeration", "A contradiction"], "correctAnswer": "The repetition of initial consonant sounds in a sentence"},
            {"text": "Identify the clause: 'He works hard <i>so that he can pass</i>.'", "options": ["Adverb Clause", "Noun Clause", "Adjective Clause", "Relative Clause"], "correctAnswer": "Adverb Clause"},
            {"text": "In 'Indigo', who accompanied Gandhi to Champaran?", "options": ["Rajkumar Shukla", "Jawaharlal Nehru", "Sardar Patel", "Rajendra Prasad"], "correctAnswer": "Rajkumar Shukla"},
            {"text": "Choose the correct form: 'The number of people _____ increasing.'", "options": ["Is", "Are", "Were", "Has"], "correctAnswer": "Is"},
            {"text": "Identify the gerund: 'Singing is my passion.'", "options": ["Singing", "Passion", "My", "Is"], "correctAnswer": "Singing"},
            {"text": "What does 'Euphemism' mean?", "options": ["A mild or indirect word substituted for one considered to be too harsh", "A direct insult", "A type of rhyme", "A grammatical error"], "correctAnswer": "A mild or indirect word substituted for one considered to be too harsh"},
            {"text": "Identify the auxiliary verb: 'I should have gone there.'", "options": ["Should", "Have", "Gone", "There"], "correctAnswer": "Should"},
            {"text": "Which of these is a complex sentence?", "options": ["The man who stole the bag was caught.", "The man stole the bag and was caught.", "The man was caught.", "I like bags."], "correctAnswer": "The man who stole the bag was caught."},
            {"text": "What is the meaning of 'Loquacious'?", "options": ["Talkative", "Quiet", "Smart", "Lazy"], "correctAnswer": "Talkative"},
            {"text": "Identify the homophone: 'The horse has a beautiful _____.'", "options": ["Mane", "Main", "Mean", "Meen"], "correctAnswer": "Mane"},
            {"text": "Choose the correct tense: 'By this time tomorrow, I _____ reaches Mumbai.'", "options": ["Will have reached", "Reached", "Reaches", "Will reach"], "correctAnswer": "Will have reached"},
            {"text": "What is an 'Ode' in poetry?", "options": ["A lyric poem addressed to a particular subject", "A 14-line poem", "A humorous story", "A long narrative"], "correctAnswer": "A lyric poem addressed to a particular subject"},
            {"text": "Identify the direct object: 'He told me a secret.'", "options": ["A secret", "Me", "He", "Told"], "correctAnswer": "A secret"}
        ],
        "hard": [
            {"text": "Identify the mood: 'Would that I were young again!'", "options": ["Optative / Subjunctive", "Indicative", "Imperative", "Interrogative"], "correctAnswer": "Optative / Subjunctive"},
            {"text": "What device is used in: 'Death lays his icy hands on kings'?", "options": ["Personification", "Simile", "Metaphor", "Oxymoron"], "correctAnswer": "Personification"},
            {"text": "In 'The Third Level', what is the name of the protagonist?", "options": ["Charley", "Louisa", "Sam", "Arthur"], "correctAnswer": "Charley"},
            {"text": "Identify the error: 'None of the three boys have completed the task.'", "options": ["'have' should be 'has'", "'None' should be 'Neither'", "'boys' should be 'boy'", "No error"], "correctAnswer": "'have' should be 'has'"},
            {"text": "What is 'Paradox'?", "options": ["A seemingly absurd or self-contradictory statement that when investigated may prove to be true", "A comparison using as", "A repetition of sounds", "A rhyme scheme"], "correctAnswer": "A seemingly absurd or self-contradictory statement that when investigated may prove to be true"},
            {"text": "Identify the 'Metonymy': 'The pen is mightier than the sword.'", "options": ["Pen/Sword (referring to writing/force)", "Mightier", "The", "Is"], "correctAnswer": "Pen/Sword (referring to writing/force)"},
            {"text": "Which clause is italicized: 'I don't know the reason <i>why she is upset</i>.'?", "options": ["Adjective Clause", "Noun Clause", "Adverb Clause", "Relative Phrase"], "correctAnswer": "Adjective Clause"},
            {"text": "What is the meaning of 'Hyperbole'?", "options": ["Exaggerated statements not meant to be taken literally", "Understatement", "Direct comparison", "Logic"], "correctAnswer": "Exaggerated statements not meant to be taken literally"},
            {"text": "Identify the 'Transitive' or 'Intransitive' nature of 'Raised' in 'Prices have raised.'", "options": ["Incorrect usage (should be 'risen', intransitive)", "Transitive", "Intransitive", "Linking"], "correctAnswer": "Incorrect usage (should be 'risen', intransitive)"},
            {"text": "What is 'Onomatopoeia'?", "options": ["The formation of a word from a sound associated with what is named", "A comparison", "A reference to history", "A riddle"], "correctAnswer": "The formation of a word from a sound associated with what is named"},
            {"text": "In 'The Enemy', who is Dr. Sadao's wife?", "options": ["Hana", "Yumi", "Sadaia", "Maki"], "correctAnswer": "Hana"},
            {"text": "What is a 'Soliloquy'?", "options": ["An act of speaking one's thoughts aloud when by oneself", "A dialogue", "A song", "A funny story"], "correctAnswer": "An act of speaking one's thoughts aloud when by oneself"},
            {"text": "Identify the 'Participle Phrase' in: 'Having finished the work, he went home.'", "options": ["Having finished the work", "He went home", "Finished the work", "Home"], "correctAnswer": "Having finished the work"},
            {"text": "What does 'Omniscient' mean?", "options": ["Knowing everything", "Very powerful", "Present everywhere", "Very kind"], "correctAnswer": "Knowing everything"},
            {"text": "What is 'Enjambment'?", "options": ["Continuing a sentence across poetic lines without punctuation", "Ending a line with a rhyme", "A pause in the middle", "A type of rhythm"], "correctAnswer": "Continuing a sentence across poetic lines without punctuation"}
        ]
    },
    "maths": {
        "easy": [
            {"text": "What are the elements of a set defined as {x : x is a prime number < 10}?", "options": ["{2, 3, 5, 7}", "{1, 2, 3, 5, 7}", "{2, 3, 5, 7, 9}", "{3, 5, 7}"], "correctAnswer": "{2, 3, 5, 7}"},
            {"text": "Calculate the value of log10(1000).", "options": ["3", "10", "100", "1"], "correctAnswer": "3"},
            {"text": "What is the domain of f(x) = 1/x?", "options": ["All real numbers except 0", "All real numbers", "x > 0", "x < 0"], "correctAnswer": "All real numbers except 0"},
            {"text": "Find the slope of a line parallel to 3x - 4y + 5 = 0.", "options": ["3/4", "4/3", "-3/4", "1"], "correctAnswer": "3/4"},
            {"text": "Evaluate: C(n, n).", "options": ["1", "n", "0", "n!"], "correctAnswer": "1"},
            {"text": "What is the distance of the point (3, 4) from the origin?", "options": ["5", "7", "25", "√7"], "correctAnswer": "5"},
            {"text": "If A = {1, 2} and B = {3, 4}, how many elements are in A x B?", "options": ["4", "2", "3", "0"], "correctAnswer": "4"},
            {"text": "What is the derivative of e^x?", "options": ["e^x", "xe^(x-1)", "1", "ln x"], "correctAnswer": "e^x"},
            {"text": "Find the value of sin^-1(1).", "options": ["π/2", "0", "π", "2π"], "correctAnswer": "π/2"},
            {"text": "The number of non-empty subsets of a set with n elements is:", "options": ["2^n - 1", "2^n", "n^2", "n"], "correctAnswer": "2^n - 1"},
            {"text": "Evaluate: lim (x→0) (sin x / x).", "options": ["1", "0", "Infinity", "Undetermined"], "correctAnswer": "1"},
            {"text": "What is the integral of 1/x dx?", "options": ["ln |x| + C", "x^0", "-1/x^2", "e^x"], "correctAnswer": "ln |x| + C"},
            {"text": "Identify the identity matrix of order 2.", "options": ["[[1,0],[0,1]]", "[[0,1],[1,0]]", "[[1,1],[1,1]]", "[[0,0],[0,0]]"], "correctAnswer": "[[1,0],[0,1]]"},
            {"text": "If f(x) = sin x, then f'(x) is:", "options": ["cos x", "-cos x", "tan x", "sec x"], "correctAnswer": "cos x"},
            {"text": "What is the probability of an impossible event?", "options": ["0", "1", "0.5", "Undetermined"], "correctAnswer": "0"}
        ],
        "medium": [
            {"text": "Find the value of k if f(x) = {kx+1 if x≤5, 3x-5 if x>5} is continuous at x=5.", "options": ["9/5", "2", "3", "1"], "correctAnswer": "9/5"},
            {"text": "Find the derivative of x^x with respect to x.", "options": ["x^x (1 + ln x)", "x * x^(x-1)", "ln x", "e^x"], "correctAnswer": "x^x (1 + ln x)"},
            {"text": "Evaluate the integral: ∫ sin^2 x dx.", "options": ["x/2 - (sin 2x)/4 + C", "cos^2 x", "-cos x", "x + C"], "correctAnswer": "x/2 - (sin 2x)/4 + C"},
            {"text": "Find the area bounded by y = x^2, x-axis and lines x=1, x=2.", "options": ["7/3", "1", "3", "8/3"], "correctAnswer": "7/3"},
            {"text": "Find the order and degree of the differential equation: (dy/dx)^2 + y = 0.", "options": ["Order 1, Degree 2", "Order 2, Degree 1", "Order 1, Degree 1", "Order 2, Degree 2"], "correctAnswer": "Order 1, Degree 2"},
            {"text": "If A is a square matrix of order 3 and |A| = 5, find |adj A|.", "options": ["25", "125", "5", "15"], "correctAnswer": "25"},
            {"text": "Find the vector equation of the line passing through (1, 2, 3) and parallel to vector 3i + 2j - 2k.", "options": ["r = (i+2j+3k) + λ(3i+2j-2k)", "r = (3i+2j-2k) + λ(i+2j+3k)", "r = λ(i+2j+3k)", "None"], "correctAnswer": "r = (i+2j+3k) + λ(3i+2j-2k)"},
            {"text": "Solve the LPP: Maximize Z = 3x + 4y subject to x + y ≤ 4, x, y ≥ 0.", "options": ["16", "12", "0", "7"], "correctAnswer": "16"},
            {"text": "Find the probability of getting 5 exactly twice in 7 throws of a die.", "options": ["21 * (1/6)^2 * (5/6)^5", "(1/6)^2", "1/2", "None"], "correctAnswer": "21 * (1/6)^2 * (5/6)^5"},
            {"text": "If P(A) = 0.8, P(B) = 0.5 and P(B|A) = 0.4, find P(A ∩ B).", "options": ["0.32", "0.4", "0.2", "0.1"], "correctAnswer": "0.32"},
            {"text": "Find the angle between vectors a = i + j - k and b = i - j + k.", "options": ["cos^-1(-1/3)", "π/2", "0", "π/4"], "correctAnswer": "cos^-1(-1/3)"},
            {"text": "Find the projection of vector i + 3j + 7k on 7i - j + 8k.", "options": ["60 / √114", "10", "√114", "5"], "correctAnswer": "60 / √114"},
            {"text": "Evaluate: ∫ e^x (sin x + cos x) dx.", "options": ["e^x sin x + C", "e^x cos x + C", "e^x + C", "sin x + cos x"], "correctAnswer": "e^x sin x + C"},
            {"text": "Find the direction cosines of a line which makes equal angles with the coordinate axes.", "options": ["±1/√3, ±1/√3, ±1/√3", "1, 1, 1", "0, 0, 0", "1/2, 1/2, 1/2"], "correctAnswer": "±1/√3, ±1/√3, ±1/√3"},
            {"text": "If [[x, 2],[3, y]] = [[1, 2],[3, 4]], find x and y.", "options": ["x=1, y=4", "x=4, y=1", "x=2, y=3", "None"], "correctAnswer": "x=1, y=4"}
        ],
        "hard": [
            {"text": "Find the value of ∫ (0 to π/2) log(sin x) dx.", "options": ["-π/2 log 2", "π/2 log 2", "0", "1"], "correctAnswer": "-π/2 log 2"},
            {"text": "Solve the differential equation: dy/dx + y/x = x^2.", "options": ["y = x^3/4 + C/x", "y = x^2 + C", "y = x^3 + C", "None"], "correctAnswer": "y = x^3/4 + C/x"},
            {"text": "Find the shortest distance between lines r = a1 + λb1 and r = a2 + μb2.", "options": ["|(a2 - a1) . (b1 x b2)| / |b1 x b2|", "|a2 - a1|", "|b1 x b2|", "0"], "correctAnswer": "|(a2 - a1) . (b1 x b2)| / |b1 x b2|"},
            {"text": "Find the area of the region bounded by the ellipse x^2/a^2 + y^2/b^2 = 1.", "options": ["πab", "2πab", "πr^2", "ab"], "correctAnswer": "πab"},
            {"text": "Solve the following system of equations using matrix method: 2x+3y+3z=5, x-2y+z=-4, 3x-y-2z=3.", "options": ["x=1, y=2, z=-1", "x=1, y=1, z=1", "x=0, y=0, z=0", "None"], "correctAnswer": "x=1, y=2, z=-1"},
            {"text": "Find the absolute maximum and minimum values of f(x) = x^3 - 3x in [-2, 2].", "options": ["Max: 2, Min: -2", "Max: 3, Min: -3", "Max: 0, Min: -2", "None"], "correctAnswer": "Max: 2, Min: -2"},
            {"text": "If a card is drawn from a well-shuffled pack of 52 cards, find the probability that it is a king given that it is a red card.", "options": ["1/13", "1/26", "2/13", "1/4"], "correctAnswer": "1/13"},
            {"text": "Find the equation of the plane passing through (1, 1, -1) and perpendicular to the planes x+2y+3z=7 and 2x-3y+4z=0.", "options": ["17x + 2y - 7z = 26", "x + y + z = 1", "x - y + z = 0", "None"], "correctAnswer": "17x + 2y - 7z = 26"},
            {"text": "Integrate: ∫ dx / (x^2 + 2x + 5).", "options": ["1/2 tan^-1((x+1)/2) + C", "tan^-1(x+1)", "ln(x^2+2x+5)", "None"], "correctAnswer": "1/2 tan^-1((x+1)/2) + C"},
            {"text": "Find the distance between parallel planes 2x - 2y + z + 3 = 0 and 4x - 4y + 2z + 5 = 0.", "options": ["1/6", "1/3", "1", "0"], "correctAnswer": "1/6"},
            {"text": "If f(x) = |x - 1|, find the derivative at x=1.", "options": ["Does not exist", "1", "-1", "0"], "correctAnswer": "Does not exist"},
            {"text": "Find the sum of the series: 1/1! + 1/2! + 1/3! + ... to infinity.", "options": ["e - 1", "e", "1", "Infinity"], "correctAnswer": "e - 1"},
            {"text": "Solve: tan^-1(2x) + tan^-1(3x) = π/4.", "options": ["1/6", "1/2", "1/3", "1"], "correctAnswer": "1/6"},
            {"text": "Calculate the volume of the parallelopiped whose edges are represented by vectors a=2i-3j+4k, b=i+2j-k, c=3i-j+2k.", "options": ["-7 (Take absolute: 7)", "10", "15", "0"], "correctAnswer": "-7 (Take absolute: 7)"},
            {"text": "Find the probability of a success in a binomial distribution with n=6 if 9P(X=4) = P(X=2).", "options": ["1/4", "1/2", "1/3", "2/3"], "correctAnswer": "1/4"}
        ]
    },
    "physics": {
        "easy": [
            {"text": "What is the SI unit of electric charge?", "options": ["Coulomb", "Ampere", "Volt", "Ohm"], "correctAnswer": "Coulomb"},
            {"text": "Define 'Ohm's Law'.", "options": ["V = IR", "P = VI", "F = ma", "E = mc^2"], "correctAnswer": "V = IR"},
            {"text": "Which particle is responsible for electricity in metals?", "options": ["Electrons", "Protons", "Neutrons", "Positrons"], "correctAnswer": "Electrons"},
            {"text": "What is the unit of magnetic flux?", "options": ["Weber", "Tesla", "Gauss", "Henry"], "correctAnswer": "Weber"},
            {"text": "Identify the mirror formula.", "options": ["1/f = 1/v + 1/u", "1/f = 1/v - 1/u", "P = 1/f", "v = u + at"], "correctAnswer": "1/f = 1/v + 1/u"},
            {"text": "What is the speed of light in water approximately?", "options": ["2.25 x 10^8 m/s", "3 x 10^8 m/s", "1.5 x 10^8 m/s", "1000 m/s"], "correctAnswer": "2.25 x 10^8 m/s"},
            {"text": "Which phenomenon causes rainbows?", "options": ["Dispersion and Internal Reflection", "Reflection only", "Refraction only", "Diffraction"], "correctAnswer": "Dispersion and Internal Reflection"},
            {"text": "What is the SI unit of radioactivity?", "options": ["Becquerel", "Curie", "Roentgen", "Mole"], "correctAnswer": "Becquerel"},
            {"text": "What is 'Light Year' a unit of?", "options": ["Distance", "Time", "Speed", "Intensity"], "correctAnswer": "Distance"},
            {"text": "Identify 'Einstein's mass-energy relation'.", "options": ["E = mc^2", "F = ma", "P = mv", "W = Fs"], "correctAnswer": "E = mc^2"},
            {"text": "Which lens is used in a simple magnifying glass?", "options": ["Convex lens", "Concave lens", "Cylindrical lens", "Bifocal lens"], "correctAnswer": "Convex lens"},
            {"text": "The power of a lens is -2D. Its focal length is:", "options": ["-0.5 m", "0.5 m", "2 m", "-2 m"], "correctAnswer": "-0.5 m"},
            {"text": "Which particle has zero rest mass?", "options": ["Photon", "Electron", "Proton", "Neutron"], "correctAnswer": "Photon"},
            {"text": "What is the primary color of light?", "options": ["Red, Green, Blue", "Red, Yellow, Blue", "Cyan, Magenta, Yellow", "White"], "correctAnswer": "Red, Green, Blue"},
            {"text": "Who discovered X-rays?", "options": ["Röntgen", "Newton", "Einstein", "Curie"], "correctAnswer": "Röntgen"}
        ],
        "medium": [
            {"text": "State 'Coulomb's Law' force formula.", "options": ["F = k q1q2 / r^2", "F = ma", "F = qE", "F = BIl"], "correctAnswer": "F = k q1q2 / r^2"},
            {"text": "What is the capacitance of a parallel plate capacitor?", "options": ["C = ε0A / d", "C = Q / V", "C = 1/2 CV^2", "C = IR"], "correctAnswer": "C = ε0A / d"},
            {"text": "Define 'Drift Velocity'.", "options": ["Average velocity of electrons in a conductor under electric field", "Speed of light", "Velocity of sound", "Total distance / time"], "correctAnswer": "Average velocity of electrons in a conductor under electric field"},
            {"text": "What is 'Kirchhoff's First Law' (Junction Rule) based on?", "options": ["Conservation of Charge", "Conservation of Energy", "Conservation of Momentum", "Conservation of Mass"], "correctAnswer": "Conservation of Charge"},
            {"text": "Identify 'Lorentz Force' formula.", "options": ["F = q(E + v x B)", "F = ma", "F = qE", "F = Gmm/r^2"], "correctAnswer": "F = q(E + v x B)"},
            {"text": "What is 'Lenz's Law' used for?", "options": ["To find the direction of induced current", "To calculate resistance", "To find magnetic field", "To measure mass"], "correctAnswer": "To find the direction of induced current"},
            {"text": "Define 'Self Inductance'.", "options": ["Phenomenon of inducing emf in same coil due to change in current", "Current in a resistor", "Gravity effect", "Radioactivity"], "correctAnswer": "Phenomenon of inducing emf in same coil due to change in current"},
            {"text": "What is the impedance (Z) of an LCR circuit?", "options": ["Z = √[R^2 + (XL - XC)^2]", "Z = R + L + C", "Z = V / I", "Z = R"], "correctAnswer": "Z = √[R^2 + (XL - XC)^2]"},
            {"text": "Identify 'Snell's Law' of refraction.", "options": ["sin i / sin r = n2 / n1", "v = u + at", "F = ma", "P = VI"], "correctAnswer": "sin i / sin r = n2 / n1"},
            {"text": "What is the 'Brewster's Law' relating to polarization?", "options": ["n = tan ip", "n = sin i", "n = cos i", "n = 1/sin c"], "correctAnswer": "n = tan ip"},
            {"text": "State 'Huygens' Principle'.", "options": ["Every point on a wavefront is a source of secondary wavelets", "Light is a particle", "Gravity is curved", "Entropy increases"], "correctAnswer": "Every point on a wavefront is a source of secondary wavelets"},
            {"text": "What is 'Work Function' in photoelectric effect?", "options": ["Minimum energy required to eject an electron from metal surface", "Energy of a photon", "Heat generated", "Kinetic energy"], "correctAnswer": "Minimum energy required to eject an electron from metal surface"},
            {"text": "Identify 'De Broglie Wavelength' formula.", "options": ["λ = h / p", "E = mc^2", "F = ma", "v = fλ"], "correctAnswer": "λ = h / p"},
            {"text": "What is 'Half-life' of a radioactive substance?", "options": ["Time in which half the nuclei decay", "Whole life / 2", "1 / decay constant", "Decay constant * 0.693"], "correctAnswer": "Time in which half the nuclei decay"},
            {"text": "Identify the logic gate that gives 1 only if both inputs are 1.", "options": ["AND gate", "OR gate", "NOT gate", "NAND gate"], "correctAnswer": "AND gate"}
        ],
        "hard": [
            {"text": "What is 'Gauss's Law' in electrostatics?", "options": ["Φ = q_enclosed / ε0", "E = kQ/r^2", "V = kQ/r", "F = qE"], "correctAnswer": "Φ = q_enclosed / ε0"},
            {"text": "State 'Biot-Savart Law' for magnetic field.", "options": ["dB = (μ0/4π) * (I dl sinθ / r^2)", "B = μ0nI", "Φ = BA", "F = qvB"], "correctAnswer": "dB = (μ0/4π) * (I dl sinθ / r^2)"},
            {"text": "What occurs during 'Total Internal Reflection'?", "options": ["Light goes from denser to rarer medium with i > critical angle", "Light is absorbed", "Light scatters", "Light diffracts"], "correctAnswer": "Light goes from denser to rarer medium with i > critical angle"},
            {"text": "Describe 'Young's Double Slit Experiment' outcome.", "options": ["Demonstrates interference of light (Wave nature)", "Particle nature of light", "Gravity waves", "Speed of light"], "correctAnswer": "Demonstrates interference of light (Wave nature)"},
            {"text": "What is the 'Photoelectric Equation' of Einstein?", "options": ["Kmax = hν - Φ", "E = mc^2", "p = h/λ", "F = qE"], "correctAnswer": "Kmax = hν - Φ"},
            {"text": "What describes 'Bohr's Orbit Quantization'?", "options": ["L = n * (h / 2π)", "mvr = h", "E = hν", "p = mv"], "correctAnswer": "L = n * (h / 2π)"},
            {"text": "Define 'Binding Energy' of a nucleus.", "options": ["Energy required to separate nucleons completely", "Energy of electrons", "Energy of a photon", "Chemical energy"], "correctAnswer": "Energy required to separate nucleons completely"},
            {"text": "Identify 'Zener Diode' primary use.", "options": ["Voltage regulator", "Rectifier", "Amplifier", "Oscillator"], "correctAnswer": "Voltage regulator"},
            {"text": "What is 'Modulation' in communication systems?", "options": ["Process of superimposing low freq signal on high freq carrier wave", "Noise removal", "Signal amplification", "Digital to Analog conversion"], "correctAnswer": "Process of superimposing low freq signal on high freq carrier wave"},
            {"text": "Identify 'Ampere's Circuital Law'.", "options": ["∮ B.dl = μ0 I_enclosed", "Φ = LI", "V = IR", "F = ma"], "correctAnswer": "∮ B.dl = μ0 I_enclosed"},
            {"text": "What is 'Displacement Current'?", "options": ["Current due to changing electric flux", "Current in a wire", "Flow of protons", "Battery current"], "correctAnswer": "Current due to changing electric flux"},
            {"text": "What constitutes a 'Full Wave Rectifier'?", "options": ["Two diodes that rectify both halves of AC cycle", "One diode", "A capacitor", "A transformer only"], "correctAnswer": "Two diodes that rectify both halves of AC cycle"},
            {"text": "What is the 'Threshold Frequency' in photoelectric effect?", "options": ["Minimum frequency of incident light below which no emission occurs", "Highest frequency", "Frequency of sound", "Visible light range"], "correctAnswer": "Minimum frequency of incident light below which no emission occurs"},
            {"text": "Identify the 'p-n junction diode' at forward bias behavior.", "options": ["Low resistance / conducts current", "High resistance / no current", "Becomes an insulator", "Explodes"], "correctAnswer": "Low resistance / conducts current"},
            {"text": "Define 'Capacitive Reactance' (XC).", "options": ["XC = 1 / (2πfC)", "XC = 2πfL", "XC = R", "XC = V/I"], "correctAnswer": "XC = 1 / (2πfC)"}
        ]
    },
    "chemistry": {
        "easy": [
            {"text": "What is the SI unit of molar mass?", "options": ["g/mol", "kg/mol", "mol/g", "amu"], "correctAnswer": "g/mol"},
            {"text": "Identify the element with atomic number 1.", "options": ["Hydrogen", "Helium", "Lithium", "Oxygen"], "correctAnswer": "Hydrogen"},
            {"text": "What is the chemical formula of Sulfuric Acid?", "options": ["H2SO4", "HCl", "HNO3", "H2O"], "correctAnswer": "H2SO4"},
            {"text": "Define 'Mole Fraction'.", "options": ["Moles of component / Total moles", "Mass / Volume", "Gram equivalent / Liter", "Density / Molar mass"], "correctAnswer": "Moles of component / Total moles"},
            {"text": "Identify the strongest oxidizing agent.", "options": ["Fluorine (F2)", "Oxygen (O2)", "Chlorine (Cl2)", "Hydrogen (H2)"], "correctAnswer": "Fluorine (F2)"},
            {"text": "What is the pH of a solution with [H+] = 10^-3 M?", "options": ["3", "10", "7", "1"], "correctAnswer": "3"},
            {"text": "What is 'Dry Ice'?", "options": ["Solid Carbon Dioxide", "Frozen Nitrogen", "Ice with salt", "Cloud"], "correctAnswer": "Solid Carbon Dioxide"},
            {"text": "Identify the functional group in CH3COOH.", "options": ["Carboxylic acid (-COOH)", "Alcohol (-OH)", "Aldehyde (-CHO)", "Ketone"], "correctAnswer": "Carboxylic acid (-COOH)"},
            {"text": "What is the coordination number of an atom in a Simple Cubic unit cell?", "options": ["6", "8", "12", "4"], "correctAnswer": "6"},
            {"text": "What is the rate of reaction unit for first order?", "options": ["s^-1", "mol L^-1 s^-1", "L mol^-1 s^-1", "No unit"], "correctAnswer": "s^-1"},
            {"text": "Identify 'Aspirin' Structure.", "options": ["2-Acetoxybenzoic acid", "Salicylic acid", "Paracetamol", "Nitroglycerin"], "correctAnswer": "2-Acetoxybenzoic acid"},
            {"text": "What is 'Bakelite'?", "options": ["A thermosetting polymer", "A thermoplastic", "A natural fiber", "A metal"], "correctAnswer": "A thermosetting polymer"},
            {"text": "The common oxidation state of transition metals is usually:", "options": ["Variable", "+1", "+2", "-1"], "correctAnswer": "Variable"},
            {"text": "Which gas is used in a lead-acid battery?", "options": ["None (it uses H2SO4 liquid)", "Hydrogen", "Oxygen", "Nitrogen"], "correctAnswer": "None (it uses H2SO4 liquid)"},
            {"text": "What is 'Galvanization'?", "options": ["Coating iron with Zinc to prevent rusting", "Mixing gold and silver", "Heating coal", "Electrolysis of water"], "correctAnswer": "Coating iron with Zinc to prevent rusting"}
        ],
        "medium": [
            {"text": "State 'Raoult's Law' for volatile liquids.", "options": ["PA = PA° * xA", "P ∝ T", "V ∝ 1/P", "PV = nRT"], "correctAnswer": "PA = PA° * xA"},
            {"text": "What is 'Molarity' of pure water?", "options": ["55.5 M", "18 M", "1 M", "10 M"], "correctAnswer": "55.5 M"},
            {"text": "Define 'Specific Conductance' (κ).", "options": ["κ = (1/R) * (l/A)", "κ = R/T", "κ = V/I", "κ = m/V"], "correctAnswer": "κ = (1/R) * (l/A)"},
            {"text": "What describes 'Order of Reaction'?", "options": ["Sum of powers of concentration terms in rate law", "Number of molecules reacting", "Speed of reaction", "Temp dependence"], "correctAnswer": "Sum of powers of concentration terms in rate law"},
            {"text": "Identify 'Adsorption' vs 'Absorption'.", "options": ["Adsorption is a surface phenomenon", "Absorption is surface only", "Both are same", "Adsorption is bulk"], "correctAnswer": "Adsorption is a surface phenomenon"},
            {"text": "What is 'Lanthanoid Contraction'?", "options": ["Steady decrease in atomic radius from La to Lu", "Increase in size", "Color of ions", "Radioactivity"], "correctAnswer": "Steady decrease in atomic radius from La to Lu"},
            {"text": "State 'Werner's Theory' primary valency.", "options": ["Oxidation state of the metal", "Coordination number", "Shape of molecule", "Color"], "correctAnswer": "Oxidation state of the metal"},
            {"text": "What is 'Cannizzaro Reaction'?", "options": ["Disproportionation of aldehydes without alpha-H", "Reaction of ketones", "Acid-base reaction", "Halogenation"], "correctAnswer": "Disproportionation of aldehydes without alpha-H"},
            {"text": "Define 'Isotonic Solutions'.", "options": ["Solutions with same osmotic pressure", "Solutions with same volume", "Solutions with same mass", "Buffer solutions"], "correctAnswer": "Solutions with same osmotic pressure"},
            {"text": "What is 'Kohlrausch's Law' used for?", "options": ["To find limiting molar conductivity of an electrolyte", "To measure pressure", "To measure volume of gas", "To count atoms"], "correctAnswer": "To find limiting molar conductivity of an electrolyte"},
            {"text": "Identify 'Azeotrope'.", "options": ["Constant boiling mixture that distills without change in composition", "Pure liquid", "Mixture of sand and water", "Suspension"], "correctAnswer": "Constant boiling mixture that distills without change in composition"},
            {"text": "What is 'Half-life' of a zero order reaction?", "options": ["t1/2 = [A]0 / 2k", "t1/2 = 0.693 / k", "t1/2 = 1 / k", "t1/2 = k"], "correctAnswer": "t1/2 = [A]0 / 2k"},
            {"text": "Define 'Peptization'.", "options": ["Process of converting a precipitate into a colloid", "Formation of solid", "Melting", "Boiling"], "correctAnswer": "Process of converting a precipitate into a colloid"},
            {"text": "Identify the 'Schottky Defect'.", "options": ["Equal number of cations and anions are missing from lattice", "Cation in interstitial site", "Extra metal", "Impurity"], "correctAnswer": "Equal number of cations and anions are missing from lattice"},
            {"text": "What is 'SN2 Reaction' characteristic?", "options": ["Single step with inversion of configuration", "Two steps", "Formation of carbocation", "No reaction"], "correctAnswer": "Single step with inversion of configuration"}
        ],
        "hard": [
            {"text": "State 'Nernst Equation' for electrode potential.", "options": ["E = E° - (RT/nF)lnQ", "ΔG = nFE", "PV = nRT", "λ = h/p"], "correctAnswer": "E = E° - (RT/nF)lnQ"},
            {"text": "What is the 'Arrhenius Equation' for rate constant?", "options": ["k = A * e^(-Ea/RT)", "k = Ae", "k = ln A", "k = Ea / RT"], "correctAnswer": "k = A * e^(-Ea/RT)"},
            {"text": "Define 'Optical Isomerism' condition.", "options": ["Presence of chiral center and non-superimposable mirror image", "Presence of double bond", "Presence of same atom", "Symmetry"], "correctAnswer": "Presence of chiral center and non-superimposable mirror image"},
            {"text": "What is 'Crystal Field Splitting' (Δ)?", "options": ["Splitting of d-orbitals in presence of ligands", "Mixing of orbitals", "Excitation of electrons", "Bonding"], "correctAnswer": "Splitting of d-orbitals in presence of ligands"},
            {"text": "Describe 'Reimer-Tiemann Reaction'.", "options": ["Reaction of phenol with CHCl3/NaOH to give salicylaldehyde", "Production of soap", "Formation of ester", "Combustion"], "correctAnswer": "Reaction of phenol with CHCl3/NaOH to give salicylaldehyde"},
            {"text": "What is 'Gabriel Phthalimide Synthesis' used for?", "options": ["Preparation of primary amines", "Preparation of alcohols", "Preparation of acids", "Preparation of esters"], "correctAnswer": "Preparation of primary amines"},
            {"text": "Identify 'Zwitterion' nature in amino acids.", "options": ["Dipolar ion containing both positive and negative charge", "Anion only", "Cation only", "Neutral molecule"], "correctAnswer": "Dipolar ion containing both positive and negative charge"},
            {"text": "What characterizes 'Thermosetting Polymers'?", "options": ["Cross-linked or heavily branched molecules that don't soften on heating", "They melt easily", "Linear chains", "Soluble in water"], "correctAnswer": "Cross-linked or heavily branched molecules that don't soften on heating"},
            {"text": "Define 'Peptide Bond'.", "options": ["-CO-NH- bond connecting amino acids", "C-C bond", "O-H bond", "H-H bond"], "correctAnswer": "-CO-NH- bond connecting amino acids"},
            {"text": "Identify 'Molality' formula (m).", "options": ["Moles of solute / Mass of solvent (kg)", "Moles / Volume", "Mass / Volume", "Density"], "correctAnswer": "Moles of solute / Mass of solvent (kg)"},
            {"text": "What is 'Faraday's First Law' of electrolysis?", "options": ["w = ZIt", "V = IR", "F = ma", "PV = nRT"], "correctAnswer": "w = ZIt"},
            {"text": "State 'Henry's Law' for solubility of gases.", "options": ["p = KH * x", "p ∝ V", "V ∝ T", "pA = xA * pA°"], "correctAnswer": "p = KH * x"},
            {"text": "What is 'Enantiomer'?", "options": ["Non-superimposable mirror images", "Same molecule", "Diastereomer", "Isotopes"], "correctAnswer": "Non-superimposable mirror images"},
            {"text": "Describe 'Hinsberg Test'.", "options": ["Used to distinguish primary, secondary, and tertiary amines", "Test for starch", "Test for glucose", "Test for alcohols"], "correctAnswer": "Used to distinguish primary, secondary, and tertiary amines"},
            {"text": "Identify 'Standard Hydrogen Electrode' (SHE) potential.", "options": ["0.00 V", "1.10 V", "0.76 V", "1.00 V"], "correctAnswer": "0.00 V"}
        ]
    }
}

def main():
    bank_path = '/Users/arpan1.mukherjee/code/GhostMaze/public/AhirsAcademy/data/question_bank.json'
    
    with open(bank_path, 'r', encoding='utf-8') as f:
        question_bank = json.load(f)
        
    question_bank['class_12'] = class_12_data
    
    with open(bank_path, 'w', encoding='utf-8') as f:
        json.dump(question_bank, f, indent=4, ensure_ascii=False)
        
    print("Successfully injected final batch of 15 comprehensive questions per tier for Class 12!")

if __name__ == '__main__':
    main()
