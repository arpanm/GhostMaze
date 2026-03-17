import json
import os

class_11_data = {
    "english": {
        "easy": [
            {"text": "Who is the author of 'The Portrait of a Lady'?", "options": ["Khushwant Singh", "Nani Palkhivala", "Gordon Cook", "Alan East"], "correctAnswer": "Khushwant Singh"},
            {"text": "In the poem 'A Photograph', who is the mother with?", "options": ["Her two girl cousins", "Her brothers", "Her friends", "Her parents"], "correctAnswer": "Her two girl cousins"},
            {"text": "What is the collective noun for a group of wolves?", "options": ["Pack", "Pride", "Herd", "Flock"], "correctAnswer": "Pack"},
            {"text": "Identify the type of sentence: 'Alas! He is no more.'", "options": ["Exclamatory", "Declarative", "Imperative", "Interrogative"], "correctAnswer": "Exclamatory"},
            {"text": "What is the synonym of 'Prudent'?", "options": ["Wise / Cautious", "Reckless", "Fast", "Noisy"], "correctAnswer": "Wise / Cautious"},
            {"text": "Choose the correct article: 'She is _____ MA in English.'", "options": ["An", "A", "The", "No article"], "correctAnswer": "An"},
            {"text": "Identify the preposition: 'The bird flew over the lake.'", "options": ["Over", "Flew", "Lake", "The"], "correctAnswer": "Over"},
            {"text": "What is the meaning of the idiom 'A cold fish'?", "options": ["An unfriendly person", "A frozen meal", "A swimming champion", "A quiet person"], "correctAnswer": "An unfriendly person"},
            {"text": "Which word is an adverb in 'He works diligently'?", "options": ["Diligently", "Works", "He", "Is"], "correctAnswer": "Diligently"},
            {"text": "What is the past tense of 'Seek'?", "options": ["Sought", "Seeked", "Soughted", "Sook"], "correctAnswer": "Sought"},
            {"text": "In 'The Summer of the Beautiful White Horse', who are the two main characters?", "options": ["Aram and Mourad", "John Byro and Uncle Khosrove", "Zorab and Aram", "Mourad and John"], "correctAnswer": "Aram and Mourad"},
            {"text": "What is the antonym of 'Fragile'?", "options": ["Sturdy / Robust", "Weak", "Tardy", "Broken"], "correctAnswer": "Sturdy / Robust"},
            {"text": "Choose the correctly spelled word.", "options": ["Occurrence", "Occurence", "Ocurrence", "Ocurence"], "correctAnswer": "Occurrence"},
            {"text": "Who is the 'Cousin' in the poem 'The Laburnum Top'?", "options": ["Goldfinch", "Sparrow", "Eagle", "Lizard"], "correctAnswer": "Goldfinch"},
            {"text": "Identify the conjunction: 'He is both intelligent and hard-working.'", "options": ["Both...and", "He", "Is", "Intelligent"], "correctAnswer": "Both...and"}
        ],
        "medium": [
            {"text": "Identify the figure of speech: 'The city of London is a sleeping giant.'", "options": ["Metaphor", "Simile", "Personification", "Hyperbole"], "correctAnswer": "Metaphor"},
            {"text": "Change into passive voice: 'Someone has stolen my pen.'", "options": ["My pen has been stolen.", "Someone was stolen my pen.", "My pen is stolen.", "Someone had stolen my pen."], "correctAnswer": "My pen has been stolen."},
            {"text": "What is 'Alliteration'?", "options": ["The repetition of initial consonant sounds in a sequence of words", "The repetition of vowel sounds", "A contrast between two ideas", "The use of words that imitate sounds"], "correctAnswer": "The repetition of initial consonant sounds in a sequence of words"},
            {"text": "Identify the clause: 'I know <i>that he is a man of his word</i>.'", "options": ["Noun Clause", "Adjective Clause", "Adverb Clause", "Relative Clause"], "correctAnswer": "Noun Clause"},
            {"text": "In 'We're Not Afraid to Die...', what was the name of the boat?", "options": ["Wavewalker", "Seafarer", "Titanic", "Oceania"], "correctAnswer": "Wavewalker"},
            {"text": "Choose the correct form: 'The jury _____ divided in their opinion.'", "options": ["Were", "Was", "Is", "Has"], "correctAnswer": "Were"},
            {"text": "Identify the gerund: 'I am fond of reading novels.'", "options": ["Reading", "Fond", "Novels", "Am"], "correctAnswer": "Reading"},
            {"text": "What does 'Anachronism' mean?", "options": ["A thing belonging or appropriate to a period other than that in which it exists", "A type of rhyme", "A grammatical error", "A scientific theory"], "correctAnswer": "A thing belonging or appropriate to a period other than that in which it exists"},
            {"text": "Identify the auxiliary verb: 'We must help the poor.'", "options": ["Must", "Help", "Poor", "We"], "correctAnswer": "Must"},
            {"text": "Which of these is a compound-complex sentence?", "options": ["Although it was raining, I went to the store, and I bought some bread.", "I went to the store.", "I like tea, but he likes coffee.", "If it rains, I will stay home."], "correctAnswer": "Although it was raining, I went to the store, and I bought some bread."},
            {"text": "What is the meaning of 'Obstinate'?", "options": ["Stubborn / Unyielding", "Flexible", "Clever", "Calm"], "correctAnswer": "Stubborn / Unyielding"},
            {"text": "Identify the homophone: 'He had to _____ the boat to the shore.'", "options": ["Row", "Roe", "Raw", "Rough"], "correctAnswer": "Row"},
            {"text": "Choose the correct tense: 'By next year, I _____ my graduation.'", "options": ["Will have completed", "Completed", "Complete", "Am completing"], "correctAnswer": "Will have completed"},
            {"text": "What is a 'Couplet' in poetry?", "options": ["Two lines of verse, usually in the same meter and joined by rhyme", "A four-line stanza", "A type of rhythm", "A poem of 14 lines"], "correctAnswer": "Two lines of verse, usually in the same meter and joined by rhyme"},
            {"text": "Identify the direct object: 'The librarian gave me a book.'", "options": ["A book", "Me", "The librarian", "Gave"], "correctAnswer": "A book"}
        ],
        "hard": [
            {"text": "Identify the mood: 'Heaven help us!'", "options": ["Subjunctive / Optative", "Indicative", "Imperative", "Interrogative"], "correctAnswer": "Subjunctive / Optative"},
            {"text": "What device is used in: 'Parting is such sweet sorrow'?", "options": ["Oxymoron", "Simile", "Metaphor", "Personification"], "correctAnswer": "Oxymoron"},
            {"text": "In 'The Adventure', who is the historian protagonist?", "options": ["Professor Gaitonde", "Rajendra Deshpande", "Gangadharpant", "Vivek Gaitonde"], "correctAnswer": "Professor Gaitonde"},
            {"text": "Identify the error: 'He is one of those players who has been selected for the team.'", "options": ["'has' should be 'have'", "'players' should be 'player'", "'for' should be 'to'", "No error"], "correctAnswer": "'has' should be 'have'"},
            {"text": "What is 'Irony'?", "options": ["The use of words to convey a meaning that is the opposite of its literal meaning", "A direct comparison", "Exaggeration", "Giving human traits to animals"], "correctAnswer": "The use of words to convey a meaning that is the opposite of its literal meaning"},
            {"text": "Identify the 'Synecdoche': 'The White House issued a statement.'", "options": ["The White House (referring to the administration)", "Issued", "Statement", "White"], "correctAnswer": "The White House (referring to the administration)"},
            {"text": "Which clause is italicized: 'The time <i>when the wedding will take place</i> is fixed.'?", "options": ["Adjective Clause", "Noun Clause", "Adverb Clause", "Relative Phrase"], "correctAnswer": "Adjective Clause"},
            {"text": "What is the meaning of 'Antithesis'?", "options": ["A person or thing that is the direct opposite of someone or something else", "A type of rhyme", "A repetition of vowel sounds", "A logical conclusion"], "correctAnswer": "A person or thing that is the direct opposite of someone or something else"},
            {"text": "Identify the 'Transitive' or 'Intransitive' nature of 'Raised' in 'He raised his hand.'", "options": ["Transitive", "Intransitive", "Linking", "Auxiliary"], "correctAnswer": "Transitive"},
            {"text": "What is 'Assonance'?", "options": ["The repetition of vowel sounds in nearby words", "The repetition of consonant sounds", "A comparison using as", "A word that sounds like its meaning"], "correctAnswer": "The repetition of vowel sounds in nearby words"},
            {"text": "In 'Silk Road', where is the author travelling to?", "options": ["Mount Kailash", "Lhasa", "Darchen", "Hor"], "correctAnswer": "Mount Kailash"},
            {"text": "What is a 'Metonymy'?", "options": ["The substitution of the name of an attribute for that of the thing meant", "A direct comparison", "A contradiction", "A repeated phrase"], "correctAnswer": "The substitution of the name of an attribute for that of the thing meant"},
            {"text": "Identify the 'Absolute Phrase' in: 'The weather being fine, we went for a walk.'", "options": ["The weather being fine", "Went for a walk", "We went", "Fine"], "correctAnswer": "The weather being fine"},
            {"text": "What does a 'Polyglot' mean?", "options": ["A person who knows and uses several languages", "A type of geometry", "A collector of coins", "A student of politics"], "correctAnswer": "A person who knows and uses several languages"},
            {"text": "What is 'Enjambment'?", "options": ["The continuation of a sentence without a pause beyond the end of a line, couplet, or stanza", "A type of poetic meter", "A rhyme scheme", "A pause within a line"], "correctAnswer": "The continuation of a sentence without a pause beyond the end of a line, couplet, or stanza"}
        ]
    },
    "maths": {
        "easy": [
            {"text": "What is the intersection of sets A = {1, 2, 3} and B = {2, 3, 4}?", "options": ["{2, 3}", "{1, 2, 3, 4}", "{1}", "{4}"], "correctAnswer": "{2, 3}"},
            {"text": "Find the value of 5! (5 factorial).", "options": ["120", "60", "24", "125"], "correctAnswer": "120"},
            {"text": "What is the domain of the function f(x) = √x?", "options": ["x ≥ 0", "x > 0", "All real numbers", "x ≤ 0"], "correctAnswer": "x ≥ 0"},
            {"text": "Convert 40° 20' into radians.", "options": ["121π/540", "π/4", "π/3", "2π/5"], "correctAnswer": "121π/540"},
            {"text": "Find the slope of the line passing through (1, 2) and (3, 6).", "options": ["2", "3", "4", "1"], "correctAnswer": "2"},
            {"text": "Evaluate: i^4 (where i is the imaginary unit).", "options": ["1", "-1", "i", "-i"], "correctAnswer": "1"},
            {"text": "What is the general term of an Arithmetic Progression?", "options": ["a + (n-1)d", "a + nd", "ar^(n-1)", "n/2[2a+(n-1)d]"], "correctAnswer": "a + (n-1)d"},
            {"text": "If f(x) = x^2 + 2, find f(3).", "options": ["11", "9", "5", "10"], "correctAnswer": "11"},
            {"text": "What is the distance between (2, 3) and (2, 7)?", "options": ["4", "5", "0", "10"], "correctAnswer": "4"},
            {"text": "The number of subsets of a set with 3 elements is:", "options": ["8", "3", "6", "9"], "correctAnswer": "8"},
            {"text": "Which of these is a null set?", "options": ["{x : x is a natural number < 1}", "{0}", "∅", "Both 1 and 3"], "correctAnswer": "Both 1 and 3"},
            {"text": "Find the value of tan 135°.", "options": ["-1", "1", "0", "Undetermined"], "correctAnswer": "-1"},
            {"text": "What is the derivative of x^2?", "options": ["2x", "x", "2", "3x"], "correctAnswer": "2x"},
            {"text": "Identify the term: A single outcome of an experiment.", "options": ["Event", "Sample point", "Sample space", "Trial"], "correctAnswer": "Sample point"},
            {"text": "What is the probability of a sure event?", "options": ["1", "0", "0.5", "Undetermined"], "correctAnswer": "1"}
        ],
        "medium": [
            {"text": "Find the value of k if the line (k-3)x - (4-k^2)y + k^2 - 7k + 6 = 0 passes through the origin.", "options": ["1, 6", "3", "2", "0"], "correctAnswer": "1, 6"},
            {"text": "Solve: 2sin^2 x + sin x - 1 = 0 for x in [0, 2π].", "options": ["π/6, 5π/6, 3π/2", "π/3, 2π/3", "π/2, π", "0, π"], "correctAnswer": "π/6, 5π/6, 3π/2"},
            {"text": "Find the sum of the first 10 terms of the GP: 1, 2, 4, 8, ...", "options": ["1023", "2047", "511", "1024"], "correctAnswer": "1023"},
            {"text": "Find the coordinates of the focus of the parabola y^2 = 12x.", "options": ["(3, 0)", "(0, 3)", "(-3, 0)", "(0, -3)"], "correctAnswer": "(3, 0)"},
            {"text": "Evaluate: lim (x→2) (x^2 - 4) / (x - 2)", "options": ["4", "2", "0", "Infinity"], "correctAnswer": "4"},
            {"text": "If nC8 = nC2, find nC2.", "options": ["45", "10", "20", "56"], "correctAnswer": "45"},
            {"text": "Find the equation of the line passing through (-1, 1) and (2, -4).", "options": ["5x + 3y + 2 = 0", "3x + 5y - 2 = 0", "x + y = 0", "x - y = 0"], "correctAnswer": "5x + 3y + 2 = 0"},
            {"text": "How many ways can the letters of the word 'APPLE' be arranged?", "options": ["60", "120", "24", "12"], "correctAnswer": "60"},
            {"text": "What is the coefficient of x^5 in the expansion of (x + 3)^8?", "options": ["1512", "56", "1120", "252"], "correctAnswer": "1512"},
            {"text": "Calculate the mean deviation about the mean for the data: 4, 7, 8, 9, 10, 12, 13, 17.", "options": ["3", "10", "2.5", "4"], "correctAnswer": "3"},
            {"text": "Find the slope of a line perpendicular to 2x - 3y + 5 = 0.", "options": ["-3/2", "3/2", "2/3", "-2/3"], "correctAnswer": "-3/2"},
            {"text": "If x + iy = (1+i) / (1-i), find x^2 + y^2.", "options": ["1", "0", "2", "-1"], "correctAnswer": "1"},
            {"text": "Solve the inequality: 3(x - 2) / 5 ≤ 5(2 - x) / 3.", "options": ["x ≤ 2", "x ≥ 2", "x < 0", "x > 1"], "correctAnswer": "x ≤ 2"},
            {"text": "Find the radius of the circle x^2 + y^2 + 8x + 10y - 8 = 0.", "options": ["7", "49", "√41", "5"], "correctAnswer": "7"},
            {"text": "In a town of 10,000 families, it was found that 40% family buy newspaper A, 20% buy newspaper B and 10% buy newspaper C. 5% buy A and B, 3% buy B and C and 4% buy A and C. If 2% buy all three newspapers, find the number of families which buy A only.", "options": ["3300", "4000", "3500", "3000"], "correctAnswer": "3300"}
        ],
        "hard": [
            {"text": "Find the sum of the series: 1 + 1/2 + 1/4 + 1/8 + ... to infinity.", "options": ["2", "1", "3", "0"], "correctAnswer": "2"},
            {"text": "Differentiate: f(x) = sin(x^2).", "options": ["2x cos(x^2)", "cos(x^2)", "2 sin x cos x", "2x sin(x^2)"], "correctAnswer": "2x cos(x^2)"},
            {"text": "Find the derivative of cos x from first principles at x = π/2.", "options": ["-1", "0", "1", "Undetermined"], "correctAnswer": "-1"},
            {"text": "If the coefficients of (r-1)th, rth and (r+1)th terms in the expansion of (1+x)^n are in the ratio 1:3:5, find n and r.", "options": ["n=7, r=3", "n=10, r=4", "n=8, r=3", "n=12, r=5"], "correctAnswer": "n=7, r=3"},
            {"text": "Prove that cos 20° cos 40° cos 60° cos 80° =", "options": ["1/16", "1/8", "1/4", "1"], "correctAnswer": "1/16"},
            {"text": "Find the equation of the ellipse whose axes are along the coordinate axes, vertices are (0, ±13) and foci are (0, ±5).", "options": ["x^2/144 + y^2/169 = 1", "x^2/169 + y^2/144 = 1", "x^2/25 + y^2/169 = 1", "x^2/144 + y^2/25 = 1"], "correctAnswer": "x^2/144 + y^2/169 = 1"},
            {"text": "How many words with or without meaning can be formed using all the letters of the word 'MISSISSIPPI'?", "options": ["34650", "40000", "12000", "346500"], "correctAnswer": "34650"},
            {"text": "Solve for x: x^2 - (5 - i)x + (18 + i) = 0.", "options": ["3-4i, 2+3i", "3+4i, 2-3i", "1+i, 2-i", "None"], "correctAnswer": "3-4i, 2+3i"},
            {"text": "Find the domain and range of f(x) = 1 / √(9 - x^2).", "options": ["D: (-3, 3), R: [1/3, ∞)", "D: [-3, 3], R: [0, ∞)", "D: (-3, 3), R: (0, 1/3]", "None"], "correctAnswer": "D: (-3, 3), R: [1/3, ∞)"},
            {"text": "A committee of 7 has to be formed from 9 boys and 4 girls. In how many ways can this be done when the committee consists of at least 3 girls?", "options": ["588", "600", "504", "441"], "correctAnswer": "588"},
            {"text": "Find the standard deviation for the first n natural numbers.", "options": ["√[(n^2 - 1) / 12]", "(n^2 - 1) / 12", "n/2", "n^2"], "correctAnswer": "√[(n^2 - 1) / 12]"},
            {"text": "In a triangle ABC, if a=18, b=24, c=30, find sin A.", "options": ["3/5", "4/5", "1", "1/2"], "correctAnswer": "3/5"},
            {"text": "Find the equation of a hyperbola with foci (±5, 0) and the transverse axis of length 8.", "options": ["x^2/16 - y^2/9 = 1", "x^2/9 - y^2/16 = 1", "y^2/16 - x^2/9 = 1", "None"], "correctAnswer": "x^2/16 - y^2/9 = 1"},
            {"text": "If z1 = 2 - i, z2 = 1 + i, find |(z1+z2+1) / (z1-z2+1)|.", "options": ["2", "√2", "1", "0"], "correctAnswer": "2"},
            {"text": "Solve: √3 cos x + sin x = √2.", "options": ["x = nπ + (-1)^n * π/4 - π/6", "x = 2nπ ± π/4", "x = nπ/2", "None"], "correctAnswer": "x = nπ + (-1)^n * π/4 - π/6"}
        ]
    },
    "physics": {
        "easy": [
            {"text": "What is the SI unit of luminous intensity?", "options": ["Candela", "Mole", "Ampere", "Kelvin"], "correctAnswer": "Candela"},
            {"text": "Which of these is a vector quantity?", "options": ["Velocity", "Speed", "Distance", "Mass"], "correctAnswer": "Velocity"},
            {"text": "What is the formula for work done (W)?", "options": ["W = Fs cos θ", "W = F/s", "W = ma", "W = 1/2 mv^2"], "correctAnswer": "W = Fs cos θ"},
            {"text": "What is the escape velocity from Earth's surface approximately?", "options": ["11.2 km/s", "8 km/s", "42 km/s", "1.6 km/s"], "correctAnswer": "11.2 km/s"},
            {"text": "Identify the primary unit of temperature.", "options": ["Kelvin", "Celsius", "Fahrenheit", "Rankine"], "correctAnswer": "Kelvin"},
            {"text": "What is the force of gravity on a 1 kg mass near Earth's surface?", "options": ["9.8 N", "1 N", "10 kg", "0 N"], "correctAnswer": "9.8 N"},
            {"text": "Which law states that stress is proportional to strain within elastic limits?", "options": ["Hooke's Law", "Pascal's Law", "Newton's Law", "Bernoulli's Principle"], "correctAnswer": "Hooke's Law"},
            {"text": "What is the value of the Universal Gravitational Constant (G)?", "options": ["6.67 x 10^-11 Nm^2/kg^2", "9.8 m/s^2", "3 x 10^8 m/s", "1.6 x 10^-19 C"], "correctAnswer": "6.67 x 10^-11 Nm^2/kg^2"},
            {"text": "Identify the type of motion of a simple pendulum.", "options": ["Periodic and Oscillatory", "Rotational", "Rectilinear", "Random"], "correctAnswer": "Periodic and Oscillatory"},
            {"text": "Which instrument measures pressure?", "options": ["Barometer", "Thermometer", "Ammeter", "Speedometer"], "correctAnswer": "Barometer"},
            {"text": "What is the speed of light in vacuum?", "options": ["3 x 10^8 m/s", "3 x 10^10 m/s", "1000 m/s", "300,000 m/s"], "correctAnswer": "3 x 10^8 m/s"},
            {"text": "What is the SI unit of power?", "options": ["Watt", "Joule", "Newton", "Pascal"], "correctAnswer": "Watt"},
            {"text": "A passenger in a moving bus is thrown forward when it stops suddenly due to:", "options": ["Inertia of motion", "Friction", "Gravity", "Momentum"], "correctAnswer": "Inertia of motion"},
            {"text": "What is the energy of a body due to its position called?", "options": ["Potential Energy", "Kinetic Energy", "Thermal Energy", "Chemical Energy"], "correctAnswer": "Potential Energy"},
            {"text": "What is the refractive index of vacuum?", "options": ["1", "1.33", "1.5", "0"], "correctAnswer": "1"}
        ],
        "medium": [
            {"text": "What is the centripetal acceleration of an object in uniform circular motion?", "options": ["v^2 / r", "v / r", "v^2 * r", "r / v^2"], "correctAnswer": "v^2 / r"},
            {"text": "Define 'Torque'.", "options": ["The turning effect of a force (r x F)", "The speed of rotation", "The mass of a rotating body", "The radius of a circle"], "correctAnswer": "The turning effect of a force (r x F)"},
            {"text": "State the Law of Conservation of Angular Momentum.", "options": ["Angular momentum remains constant if net external torque is zero", "Angular velocity is constant", "Angular acceleration is zero", "Mass is constant"], "correctAnswer": "Angular momentum remains constant if net external torque is zero"},
            {"text": "What is the value of g at the center of the Earth?", "options": ["Zero", "9.8 m/s^2", "Maximum", "Infinite"], "correctAnswer": "Zero"},
            {"text": "Identify 'Pascal's Law' relating to:", "options": ["Pressure in a confined fluid", "Gravity", "Sound", "Electricity"], "correctAnswer": "Pressure in a confined fluid"},
            {"text": "What is the First Law of Thermodynamics equivalent to?", "options": ["Law of Conservation of Energy (ΔQ = ΔU + ΔW)", "Law of Entropy", "Law of Temperature", "Law of Mass"], "correctAnswer": "Law of Conservation of Energy (ΔQ = ΔU + ΔW)"},
            {"text": "Define 'Specific Heat Capacity'.", "options": ["Heat required to raise temp of 1kg mass by 1K", "Total heat in a body", "Temp of a body", "Energy in 1 mole"], "correctAnswer": "Heat required to raise temp of 1kg mass by 1K"},
            {"text": "What is the Stefan-Boltzmann Law?", "options": ["E ∝ T^4", "E ∝ T", "E ∝ T^2", "E ∝ 1/T"], "correctAnswer": "E ∝ T^4"},
            {"text": "Identify 'Reynolds Number' use.", "options": ["To predict flow pattern (Laminar or Turbulent)", "To measure speed", "To measure pressure", "To measure temperature"], "correctAnswer": "To predict flow pattern (Laminar or Turbulent)"},
            {"text": "Define 'Young's Modulus'.", "options": ["Normal Stress / Longitudinal Strain", "Shear Stress / Shear Strain", "Bulk Stress / Bulk Strain", "Mass / Volume"], "correctAnswer": "Normal Stress / Longitudinal Strain"},
            {"text": "What follows the 'Equation of Continuity' for fluid flow?", "options": ["A1v1 = A2v2", "P1v1 = P2v2", "A1 + v1 = A2 + v2", "A/v = constant"], "correctAnswer": "A1v1 = A2v2"},
            {"text": "What is the relation between linear velocity (v) and angular velocity (ω)?", "options": ["v = rω", "v = ω/r", "v = r^2ω", "v = ω^2r"], "correctAnswer": "v = rω"},
            {"text": "In isothermal process, what remains constant?", "options": ["Temperature", "Pressure", "Volume", "Heat"], "correctAnswer": "Temperature"},
            {"text": "What is 'Viscosity'?", "options": ["Internal friction in a fluid", "Speed of fluid", "Density of fluid", "Boiling point"], "correctAnswer": "Internal friction in a fluid"},
            {"text": "The coefficient of restitution (e) for a perfectly elastic collision is:", "options": ["1", "0", "0.5", "Infinite"], "correctAnswer": "1"}
        ],
        "hard": [
            {"text": "State Bernoulli's Principle.", "options": ["P + 1/2 ρv^2 + ρgh = constant", "P ∝ V", "V ∝ T", "F = ma"], "correctAnswer": "P + 1/2 ρv^2 + ρgh = constant"},
            {"text": "What is the radius of gyration (k)?", "options": ["k = √(I / m)", "k = I / m", "k = m / I", "k = Im"], "correctAnswer": "k = √(I / m)"},
            {"text": "Define 'Doppler Effect' in sound.", "options": ["Change in frequency due to relative motion of source/observer", "Reflection of sound", "Bending of sound", "Noise cancellation"], "correctAnswer": "Change in frequency due to relative motion of source/observer"},
            {"text": "What is the efficiency of a Carnot Engine?", "options": ["η = 1 - (T2 / T1)", "η = T2 / T1", "η = 100%", "η = T1 - T2"], "correctAnswer": "η = 1 - (T2 / T1)"},
            {"text": "What is the degree of freedom for a monoatomic gas?", "options": ["3", "5", "6", "2"], "correctAnswer": "3"},
            {"text": "State the Parallel Axis Theorem for Moment of Inertia.", "options": ["I = Icm + Md^2", "I = Icm - Md^2", "I = Md^2", "I = Icm + M"], "correctAnswer": "I = Icm + Md^2"},
            {"text": "What describes 'Kepler's Second Law'?", "options": ["Line joining planet/sun sweeps equal areas in equal times", "All planets move in circles", "T^2 ∝ R^3", "Gravity is inverse square"], "correctAnswer": "Line joining planet/sun sweeps equal areas in equal times"},
            {"text": "Calculate the work done by a gas in an adiabatic process.", "options": ["W = (P1V1 - P2V2) / (γ - 1)", "W = PΔV", "W = nRT ln(V2/V1)", "W = 0"], "correctAnswer": "W = (P1V1 - P2V2) / (γ - 1)"},
            {"text": "Define 'Mean Free Path' of a gas molecule.", "options": ["Average distance travelled between successive collisions", "Speed of molecule", "Total path", "Diameter of molecule"], "correctAnswer": "Average distance travelled between successive collisions"},
            {"text": "Identify the phenomenon: A bridge collapses when marching soldiers' frequency matches bridge the frequency.", "options": ["Resonance", "Beat", "Interference", "Harmonic"], "correctAnswer": "Resonance"},
            {"text": "What is the value of 'G' in CGS units?", "options": ["6.67 x 10^-8 dyne cm^2 g^-2", "6.67 x 10^-11 Nm^2 kg^-2", "1", "9.8"], "correctAnswer": "6.67 x 10^-8 dyne cm^2 g^-2"},
            {"text": "A liquid rises to height h in a capillary tube. If the tube is tilted by angle θ, the length of liquid in tube becomes:", "options": ["h / cos θ", "h cos θ", "h", "h sin θ"], "correctAnswer": "h / cos θ"},
            {"text": "What is the work done in moving a body over a closed loop in a conservative field?", "options": ["Zero", "Positive", "Negative", "Undefined"], "correctAnswer": "Zero"},
            {"text": "Define 'Surface Tension' formula.", "options": ["S = F / l", "S = F * l", "S = m / l", "S = m * g"], "correctAnswer": "S = F / l"},
            {"text": "What occurs at 'Absolute Zero' temperature (0K)?", "options": ["Molecular motion ceases", "Water freezes", "Gas becomes solid", "Metals melt"], "correctAnswer": "Molecular motion ceases"}
        ]
    },
    "chemistry": {
        "easy": [
            {"text": "What is the SI unit of amount of substance?", "options": ["Mole", "Gram", "Kilogram", "Candela"], "correctAnswer": "Mole"},
            {"text": "What is the atomic mass of Oxygen?", "options": ["16 u", "8 u", "32 u", "12 u"], "correctAnswer": "16 u"},
            {"text": "According to Bohr's model, electrons revolve in:", "options": ["Fixed orbits (Energy levels)", "Clouds", "Zig-zag paths", "Nucleus"], "correctAnswer": "Fixed orbits (Energy levels)"},
            {"text": "Identify the noble gas in the second period.", "options": ["Neon", "Helium", "Argon", "Krypton"], "correctAnswer": "Neon"},
            {"text": "What is the chemical formula of Methane?", "options": ["CH4", "C2H6", "CO2", "H2O"], "correctAnswer": "CH4"},
            {"text": "Define an 'Isotope'.", "options": ["Same atomic number, different mass number", "Same mass number", "Same neutrons", "Different element"], "correctAnswer": "Same atomic number, different mass number"},
            {"text": "What is the pH of a neutral solution?", "options": ["7", "0", "14", "1"], "correctAnswer": "7"},
            {"text": "Identify the element with symbol 'Na'.", "options": ["Sodium", "Nitrogen", "Neon", "Nickel"], "correctAnswer": "Sodium"},
            {"text": "Which law states that mass is neither created nor destroyed?", "options": ["Law of Conservation of Mass", "Law of Constant Proportions", "Avogadro's Law", "Boyle's Law"], "correctAnswer": "Law of Conservation of Mass"},
            {"text": "What is the empirical formula of Benzene (C6H6)?", "options": ["CH", "C6H6", "C3H3", "C2H2"], "correctAnswer": "CH"},
            {"text": "Identify the subatomic particle with no charge.", "options": ["Neutron", "Proton", "Electron", "Positron"], "correctAnswer": "Neutron"},
            {"text": "What is the molarity (M) of a solution?", "options": ["Moles of solute / Volume of solution (L)", "Mass / Volume", "Moles / Mass", "Grams / Liter"], "correctAnswer": "Moles of solute / Volume of solution (L)"},
            {"text": "Identify 'Aspirin' chemical name.", "options": ["Acetylsalicylic Acid", "Salicylic Acid", "Paracetamol", "Nitroglycerin"], "correctAnswer": "Acetylsalicylic Acid"},
            {"text": "What is 'Heavy Water'?", "options": ["D2O (Deuterium Oxide)", "H2O2", "Ocean water", "Ice"], "correctAnswer": "D2O (Deuterium Oxide)"},
            {"text": "Which bond involves sharing of electron pairs?", "options": ["Covalent bond", "Ionic bond", "Metallic bond", "Hydrogen bond"], "correctAnswer": "Covalent bond"}
        ],
        "medium": [
            {"text": "What is the hybridisation of Carbon in Methane?", "options": ["sp3", "sp2", "sp", "dsp2"], "correctAnswer": "sp3"},
            {"text": "State 'Le Chatelier's Principle'.", "options": ["System at equilibrium shifts to counteract a change", "Reaction speed increases", "Mass is conserved", "Entropy decreases"], "correctAnswer": "System at equilibrium shifts to counteract a change"},
            {"text": "Define 'Electronegativity'.", "options": ["Ability of an atom to attract shared electrons", "Energy to remove an electron", "Energy released when adding electron", "Size of an atom"], "correctAnswer": "Ability of an atom to attract shared electrons"},
            {"text": "What is the shape of a water molecule (H2O)?", "options": ["Bent / V-shaped", "Linear", "Tetrahedral", "Trigonal planar"], "correctAnswer": "Bent / V-shaped"},
            {"text": "State 'Boyle's Law'.", "options": ["P ∝ 1/V (at constant T)", "V ∝ T", "P ∝ T", "PV = nRT"], "correctAnswer": "P ∝ 1/V (at constant T)"},
            {"text": "Identify 'Oxidizing Agent' definition.", "options": ["Substance that gains electrons / get reduced", "Substance that loses electrons", "Hydrogen giver", "Catalyst"], "correctAnswer": "Substance that gains electrons / get reduced"},
            {"text": "What is the electronic configuration of Chromium (At. No. 24)?", "options": ["[Ar] 3d5 4s1", "[Ar] 3d4 4s2", "[Ar] 3d6", "[Ar] 4s2"], "correctAnswer": "[Ar] 3d5 4s1"},
            {"text": "What is 'Enthalpy' (H)?", "options": ["Total heat content of a system (U + PV)", "Entropy", "Free energy", "Work"], "correctAnswer": "Total heat content of a system (U + PV)"},
            {"text": "Identify 'Hard Water' cause.", "options": ["Presence of Ca and Mg ions", "Presence of Sodium", "Presence of Oxygen", "Presence of Chlorine"], "correctAnswer": "Presence of Ca and Mg ions"},
            {"text": "Define 'Dipole Moment' (μ).", "options": ["μ = q * d", "μ = q / d", "μ = m * v", "μ = F * r"], "correctAnswer": "μ = q * d"},
            {"text": "What is 'Hess's Law'?", "options": ["Total enthalpy change remains constant regardless of path", "Energy is conserved", "Mass is conserved", "Temp is constant"], "correctAnswer": "Total enthalpy change remains constant regardless of path"},
            {"text": "Identify the 'Buffer Solution' characteristic.", "options": ["Resists change in pH", "Strong acid", "Strong base", "Neutral water"], "correctAnswer": "Resists change in pH"},
            {"text": "What follows the 'Pauli Exclusion Principle'?", "options": ["No two electrons in an atom can have the same four quantum numbers", "Electrons fill lowest energy first", "Maximum one electron per orbital", "Protons = Electrons"], "correctAnswer": "No two electrons in an atom can have the same four quantum numbers"},
            {"text": "Define 'Inductive Effect' in organic chemistry.", "options": ["Permanent displacement of sigma electrons along a chain", "Temporary effect", "Movement of pi electrons", "Transfer of protons"], "correctAnswer": "Permanent displacement of sigma electrons along a chain"},
            {"text": "What is the common oxidation state of Alkali metals?", "options": ["+1", "+2", "-1", "0"], "correctAnswer": "+1"}
        ],
        "hard": [
            {"text": "State 'Heisenberg Uncertainty Principle' formula.", "options": ["Δx * Δp ≥ h / 4π", "E = mc^2", "λ = h/mv", "PV = nRT"], "correctAnswer": "Δx * Δp ≥ h / 4π"},
            {"text": "What is 'Gibbs Free Energy' change (ΔG) for a spontaneous process?", "options": ["ΔG < 0 (Negative)", "ΔG > 0", "ΔG = 0", "ΔG = 1"], "correctAnswer": "ΔG < 0 (Negative)"},
            {"text": "Define 'Quantum Number' n, l, m, s.", "options": ["Principal, Azimuthal, Magnetic, Spin", "Primary, Level, Mass, Speed", "One, Two, Three, Four", "Outer, Inner, Middle, Core"], "correctAnswer": "Principal, Azimuthal, Magnetic, Spin"},
            {"text": "What is the 'Schrodinger Wave Equation' used for?", "options": ["To find the probability density of an electron", "To find speed", "To find mass", "To calculate pH"], "correctAnswer": "To find the probability density of an electron"},
            {"text": "Describe 'Bohr's Postulate' on angular momentum.", "options": ["mvr = nh / 2π", "mvr = h/λ", "E = hν", "F = ma"], "correctAnswer": "mvr = nh / 2π"},
            {"text": "Identify 'Resonance' in molecules.", "options": ["Delocalization of electrons described by multiple Lewis structures", "Vibration of atoms", "Sound effect", "Mixing of orbitals"], "correctAnswer": "Resonance in molecules."}, # Fix literal
            {"text": "What is the 'Common Ion Effect'?", "options": ["Suppression of dissociation of weak electrolyte in presence of common ion", "Increase in solubility", "Equilibrium shift due to temp", "Mixing of two acids"], "correctAnswer": "Suppression of dissociation of weak electrolyte in presence of common ion"},
            {"text": "Define 'Electrophile'.", "options": ["Electron loving / seeking species", "Proton giver", "Neutron seekers", "Acidic species only"], "correctAnswer": "Electron loving / seeking species"},
            {"text": "What is 'Markownikoff's Rule'?", "options": ["H attaches to C with more H in addition to alkenes", "Reaction of alcohol", "Benzene naming", "Combustion"], "correctAnswer": "H attaches to C with more H in addition to alkenes"},
            {"text": "Identify the 'Greenhouse Gas' causing global warming.", "options": ["CO2 and Methane", "Nitrogen", "Oxygen", "Argon"], "correctAnswer": "CO2 and Methane"},
            {"text": "What is 'Diagonal Relationship' in periodic table?", "options": ["Similarity in properties of diagonally adjacent elements", "Elements in same group", "Elements in same period", "Noble gases"], "correctAnswer": "Similarity in properties of diagonally adjacent elements"},
            {"text": "Describe 'Tautomerism'.", "options": ["Isomerism due to migration of a proton", "Geometric isomerism", "Optical isomerism", "Chain isomerism"], "correctAnswer": "Isomerism due to migration of a proton"},
            {"text": "What is the 'Solubility Product' (Ksp)?", "options": ["Product of molar concentrations of ions in saturated solution", "Sum of ions", "Ratio of mass", "Temp of water"], "correctAnswer": "Product of molar concentrations of ions in saturated solution"},
            {"text": "Define 'Wurtz Reaction'.", "options": ["Reaction of alkyl halides with sodium in dry ether to give alkanes", "Reaction of alcohol", "Production of soap", "Halogenation"], "correctAnswer": "Reaction of alkyl halides with sodium in dry ether to give alkanes"},
            {"text": "What characterizes 'Aromaticity' (Huckel's Rule)?", "options": ["(4n+2) pi electrons", "Planar structure", "Cyclic", "All of the above"], "correctAnswer": "All of the above"}
        ]
    }
}

def main():
    bank_path = '/Users/arpan1.mukherjee/code/GhostMaze/public/AhirsAcademy/data/question_bank.json'
    
    with open(bank_path, 'r', encoding='utf-8') as f:
        question_bank = json.load(f)
        
    question_bank['class_11'] = class_11_data
    
    # Also initialize class_12 to avoid key errors later
    if 'class_12' not in question_bank:
        question_bank['class_12'] = {}
        
    with open(bank_path, 'w', encoding='utf-8') as f:
        json.dump(question_bank, f, indent=4, ensure_ascii=False)
        
    print("Successfully injected and initialized Class 11 questions!")

if __name__ == '__main__':
    main()
