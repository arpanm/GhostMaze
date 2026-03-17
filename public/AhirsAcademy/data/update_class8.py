import json
import os

class_8_data = {
    "english": {
        "easy": [
            {"text": "Which of these is a relative pronoun?", "options": ["Who", "He", "Him", "His"], "correctAnswer": "Who"},
            {"text": "Identify the conjunction: 'Wait here until I come back.'", "options": ["Until", "Wait", "Come", "Back"], "correctAnswer": "Until"},
            {"text": "What is the past tense of 'Drink'?", "options": ["Drank", "Drunk", "Drinks", "Drinking"], "correctAnswer": "Drank"},
            {"text": "Choose the correct article: 'He is _____ university professor.'", "options": ["A", "An", "The", "None"], "correctAnswer": "A"},
            {"text": "Which word is a synonym for 'Vanish'?", "options": ["Disappear", "Appear", "Stay", "Wait"], "correctAnswer": "Disappear"},
            {"text": "What is the antonym of 'Amateur'?", "options": ["Professional", "Beginner", "Skilled", "Learner"], "correctAnswer": "Professional"},
            {"text": "Identify the preposition: 'The sun is above the clouds.'", "options": ["Above", "Sun", "Clouds", "The"], "correctAnswer": "Above"},
            {"text": "Which degree of comparison is 'Worst'?", "options": ["Superlative", "Positive", "Comparative", "Absolute"], "correctAnswer": "Superlative"},
            {"text": "Correct the spelling: 'Maintenence'", "options": ["Maintenance", "Maintenence", "Maintainance", "Mantenance"], "correctAnswer": "Maintenance"},
            {"text": "What does a 'biography' mean?", "options": ["A story of a person's life written by someone else.", "A story written by oneself.", "A book of maps.", "A study of plants."], "correctAnswer": "A story of a person's life written by someone else."},
            {"text": "Which word is an adverb in 'He runs extremely fast'?", "options": ["Extremely", "Runs", "Fast", "He"], "correctAnswer": "Extremely"},
            {"text": "What does the idiom 'Under the weather' mean?", "options": ["Feeling sick", "Wetting in rain", "In a storm", "Under a tree"], "correctAnswer": "Feeling sick"},
            {"text": "Identify the type of noun for 'Family'.", "options": ["Collective Noun", "Proper Noun", "Material Noun", "Abstract Noun"], "correctAnswer": "Collective Noun"},
            {"text": "Which punctuation shows a short pause?", "options": ["Comma", "Full stop", "Colon", "Semicolon"], "correctAnswer": "Comma"},
            {"text": "Complete the simile: 'As light as a _____.'", "options": ["Feather", "Stone", "Cloud", "Bird"], "correctAnswer": "Feather"}
        ],
        "medium": [
            {"text": "Change into passive voice: 'The boy is flying a kite.'", "options": ["A kite is being flown by the boy.", "A kite was being flown by the boy.", "The boy flew a kite.", "A kite is flying by the boy."], "correctAnswer": "A kite is being flown by the boy."},
            {"text": "Identify the figure of speech: 'The moon smiled at the stars.'", "options": ["Personification", "Simile", "Metaphor", "Oxymoron"], "correctAnswer": "Personification"},
            {"text": "Which clause is italicized: 'I know <i>that he is honest</i>.'?", "options": ["Noun Clause", "Adjective Clause", "Adverb Clause", "Relative Clause"], "correctAnswer": "Noun Clause"},
            {"text": "What is the meaning of the prefix 'Pseudo-' as in 'Pseudonym'?", "options": ["False", "True", "Small", "Large"], "correctAnswer": "False"},
            {"text": "Choose the correctly spelled word.", "options": ["Millennium", "Millenium", "Milenium", "Milennium"], "correctAnswer": "Millennium"},
            {"text": "Identify the gerund: 'I love singing in the shower.'", "options": ["Singing", "Love", "Shower", "In"], "correctAnswer": "Singing"},
            {"text": "What does the idiom 'The elephant in the room' mean?", "options": ["An obvious problem no one wants to discuss", "A literal elephant", "A large person", "Something expensive"], "correctAnswer": "An obvious problem no one wants to discuss"},
            {"text": "Which tense is used here: 'He will have completed the task by tomorrow.'?", "options": ["Future Perfect", "Future Continuous", "Simple Future", "Present Perfect"], "correctAnswer": "Future Perfect"},
            {"text": "Identify the homophone: 'I need to _____ some flour for the cake.'", "options": ["Buy", "By", "Bye", "Bough"], "correctAnswer": "Buy"},
            {"text": "Select the correct plural form of 'Medium'.", "options": ["Media", "Mediums", "Medias", "Mediumes"], "correctAnswer": "Media"},
            {"text": "What does 'Posthumous' mean?", "options": ["Occurring after death", "Before the war", "Very fast", "Secretly"], "correctAnswer": "Occurring after death"},
            {"text": "Identify the conditional sentence.", "options": ["If it rains, we will stay home.", "It is raining outside.", "Stay home when it rains.", "Will you stay home?"], "correctAnswer": "If it rains, we will stay home."},
            {"text": "What is the meaning of the suffix '-logy' as in 'Biology'?", "options": ["Study of", "Without", "Maker of", "State of"], "correctAnswer": "Study of"},
            {"text": "Identify the direct object: 'He gave the teacher a rose.'", "options": ["A rose", "The teacher", "He", "Gave"], "correctAnswer": "A rose"},
            {"text": "Which part of speech is 'Alas!'?", "options": ["Interjection", "Preposition", "Conjunction", "Adverb"], "correctAnswer": "Interjection"}
        ],
        "hard": [
            {"text": "Identify the mood: 'I suggest that he be invited to the conference.'", "options": ["Subjunctive", "Indicative", "Imperative", "Interrogative"], "correctAnswer": "Subjunctive"},
            {"text": "What is a 'Spoonerism'?", "options": ["An error in speech where sounds or letters within a phrase are swapped.", "A type of spoon.", "A grammatical error in case usage.", "A figure of speech using irony."], "correctAnswer": "An error in speech where sounds or letters within a phrase are swapped."},
            {"text": "Identify the correct indirect speech: He said, 'I have been working hard.'", "options": ["He said that he had been working hard.", "He said that he has been working hard.", "He said he had been working hard.", "He says that he had been working hard."], "correctAnswer": "He said that he had been working hard."},
            {"text": "What is the meaning of the Latin phrase 'In situ'?", "options": ["In its original place", "In a bad situation", "In a hurry", "From the start"], "correctAnswer": "In its original place"},
            {"text": "Identify the rhetorical device: 'War is peace. Freedom is slavery. Ignorance is strength.'", "options": ["Paradox / Oxymoron", "Simile", "Alliteration", "Onomatopoeia"], "correctAnswer": "Paradox / Oxymoron"},
            {"text": "Which sentence contains a dangling modifier?", "options": ["Having finished the assignment, the TV was turned on.", "Having finished the assignment, I turned on the TV.", "After I finished the assignment, the TV was turned on.", "The TV was turned on after I finished the assignment."], "correctAnswer": "Having finished the assignment, the TV was turned on."},
            {"text": "What does 'Ephemeral' mean?", "options": ["Lasting for a very short time", "Lasting forever", "Changing colors", "Very heavy"], "correctAnswer": "Lasting for a very short time"},
            {"text": "Identify the intransitive verb from the options below.", "options": ["The baby sleeps.", "He kicked the ball.", "She wrote a letter.", "They ate dinner."], "correctAnswer": "The baby sleeps."},
            {"text": "What is 'Anaphora' in literature?", "options": ["The repetition of a word or phrase at the beginning of successive clauses.", "A comparison using 'like' or 'as'.", "The use of contrasting ideas.", "A play on words."], "correctAnswer": "The repetition of a word or phrase at the beginning of successive clauses."},
            {"text": "Which of these is a malapropism?", "options": ["He is the pineapple of politeness (instead of pinnacle).", "He is very polite.", "He is not polite.", "He is polite."], "correctAnswer": "He is the pineapple of politeness (instead of pinnacle)."},
            {"text": "What is the difference between 'It's' and 'Its'?", "options": ["'It's' is a contraction of 'it is', 'Its' is possessive.", "They mean the same thing.", "'Its' is a contraction, 'It's' is possessive.", "Both are used for plural nouns."], "correctAnswer": "'It's' is a contraction of 'it is', 'Its' is possessive."},
            {"text": "Identify the case of the underlined word: 'This is <u>Rahul's</u> car.'", "options": ["Genitive (Possessive)", "Nominative", "Accusative", "Dative"], "correctAnswer": "Genitive (Possessive)"},
            {"text": "Which sentence uses the correct subjunctive mood?", "options": ["I wish I were rich.", "I wish I was rich.", "I wish I am rich.", "I wish I will be rich."], "correctAnswer": "I wish I were rich."},
            {"text": "What is the meaning of 'Philanthropist'?", "options": ["A person who seeks to promote the welfare of others", "A person who collects stamps", "A person who studies languages", "A person who hates society"], "correctAnswer": "A person who seeks to promote the welfare of others"},
            {"text": "Identify the type of sentence: 'Give me the book.'", "options": ["Imperative", "Declarative", "Interrogative", "Exclamatory"], "correctAnswer": "Imperative"}
        ]
    },
    "maths": {
        "easy": [
            {"text": "What is the multiplicative inverse of -5/8?", "options": ["-8/5", "8/5", "5/8", "1"], "correctAnswer": "-8/5"},
            {"text": "Solve for x: 3x - 4 = 11", "options": ["5", "3", "4", "7"], "correctAnswer": "5"},
            {"text": "How many rational numbers are there between any two rational numbers?", "options": ["Infinitely many", "One", "Two", "None"], "correctAnswer": "Infinitely many"},
            {"text": "What is the square of 16?", "options": ["256", "196", "225", "160"], "correctAnswer": "256"},
            {"text": "What is the cube of 5?", "options": ["125", "75", "15", "25"], "correctAnswer": "125"},
            {"text": "A quadrilateral with all sides equal and no angle equal to 90 degrees is a:", "options": ["Rhombus", "Square", "Rectangle", "Parallelogram"], "correctAnswer": "Rhombus"},
            {"text": "Find 20% of Rs 400.", "options": ["Rs 80", "Rs 40", "Rs 20", "Rs 100"], "correctAnswer": "Rs 80"},
            {"text": "Simplify: 2^3 x 2^4", "options": ["2^7", "2^12", "4^7", "4^12"], "correctAnswer": "2^7"},
            {"text": "The sum of all interior angles of a quadrilateral is:", "options": ["360 degrees", "180 degrees", "540 degrees", "720 degrees"], "correctAnswer": "360 degrees"},
            {"text": "What is the value of 10^-2?", "options": ["0.01", "0.1", "100", "0.001"], "correctAnswer": "0.01"},
            {"text": "Which of these is a perfect square?", "options": ["121", "120", "111", "99"], "correctAnswer": "121"},
            {"text": "Find the range of the data: 2, 8, 5, 12, 7.", "options": ["10", "12", "2", "5"], "correctAnswer": "10"},
            {"text": "If x = 2 and y = 3, find the value of x^2 + y^2.", "options": ["13", "5", "10", "12"], "correctAnswer": "13"},
            {"text": "The probability of an impossible event is:", "options": ["0", "1", "0.5", "Undetermined"], "correctAnswer": "0"},
            {"text": "What is the coefficient of x^2 in the expression 3x^2 - 5x + 2?", "options": ["3", "-5", "2", "0"], "correctAnswer": "3"}
        ],
        "medium": [
            {"text": "Find the square root of 625 using prime factorization.", "options": ["25", "15", "35", "20"], "correctAnswer": "25"},
            {"text": "If 15 workers can build a wall in 48 hours, how many workers will be required to do the same work in 30 hours?", "options": ["24", "20", "25", "30"], "correctAnswer": "24"},
            {"text": "Solve: (2x + 3) / 5 = (x - 2) / 3", "options": ["-19", "19", "-11", "11"], "correctAnswer": "-19"},
            {"text": "What is the compound interest on Rs 10,000 for 1 year at 10% per annum compounded half-yearly?", "options": ["Rs 1,025", "Rs 1,000", "Rs 1,100", "Rs 500"], "correctAnswer": "Rs 1,025"},
            {"text": "Factorize: x^2 - 16", "options": ["(x-4)(x+4)", "(x-8)(x+8)", "(x-4)^2", "(x+4)^2"], "correctAnswer": "(x-4)(x+4)"},
            {"text": "A shopkeeper gives a 10% discount on a marked price of Rs 500. What is the selling price?", "options": ["Rs 450", "Rs 490", "Rs 400", "Rs 550"], "correctAnswer": "Rs 450"},
            {"text": "Find the value of x if 2^(3x-1) = 32.", "options": ["2", "3", "1", "4"], "correctAnswer": "2"},
            {"text": "A polyhedra has 6 faces and 8 vertices. How many edges does it have? (Euler's Formula)", "options": ["12", "14", "10", "6"], "correctAnswer": "12"},
            {"text": "The price of a car increases from Rs 5,00,000 to Rs 5,50,000. Find the percentage increase.", "options": ["10%", "5%", "15%", "12.5%"], "correctAnswer": "10%"},
            {"text": "Divide: 12x^2y by 3xy.", "options": ["4x", "4xy", "4y", "4x^2"], "correctAnswer": "4x"},
            {"text": "The area of a trapezium is 34 sq cm and the length of one of the parallel sides is 10 cm and its height is 4 cm. Find the length of the other parallel side.", "options": ["7 cm", "8 cm", "6 cm", "9 cm"], "correctAnswer": "7 cm"},
            {"text": "If x + y = 10 and x - y = 4, find x and y.", "options": ["x=7, y=3", "x=6, y=4", "x=8, y=2", "x=5, y=5"], "correctAnswer": "x=7, y=3"},
            {"text": "Simplify: (3^-5 x 10^-5 x 125) / (5^-7 x 6^-5)", "options": ["5^5", "5^2", "1", "5^3"], "correctAnswer": "5^5"},
            {"text": "Find the smallest number by which 256 must be divided to obtain a perfect cube.", "options": ["4", "2", "8", "16"], "correctAnswer": "4"},
            {"text": "The diagonals of a rhombus are 24 cm and 10 cm. Find its perimeter.", "options": ["52 cm", "48 cm", "60 cm", "26 cm"], "correctAnswer": "52 cm"}
        ],
        "hard": [
            {"text": "Find the value of x: √[1 + (x / 144)] = 13/12", "options": ["25", "24", "13", "12"], "correctAnswer": "25"},
            {"text": "Factorize completely: a^4 - b^4", "options": ["(a-b)(a+b)(a^2+b^2)", "(a^2-b^2)(a^2+b^2)", "(a-b)^2(a+b)^2", "(a-b)^4"], "correctAnswer": "(a-b)(a+b)(a^2+b^2)"},
            {"text": "A cylindrical tank has a capacity of 6160 cubic cm. If its radius is 14 cm, find its height. (Take π = 22/7)", "options": ["10 cm", "8 cm", "12 cm", "7 cm"], "correctAnswer": "10 cm"},
            {"text": "Three numbers are in the ratio 2:3:4. The sum of their cubes is 33957. Find the numbers.", "options": ["14, 21, 28", "12, 18, 24", "10, 15, 20", "16, 24, 32"], "correctAnswer": "14, 21, 28"},
            {"text": "Solve for x: (0.25(4x - 3)) = (0.05(10x - 9))", "options": ["0.6", "0.5", "0.4", "0.8"], "correctAnswer": "0.6"},
            {"text": "What is the probability of a Leap Year having 53 Sundays?", "options": ["2/7", "1/7", "53/366", "1/53"], "correctAnswer": "2/7"},
            {"text": "If a + b + c = 0, find the value of (a^3 + b^3 + c^3) / (abc).", "options": ["3", "1", "0", "-3"], "correctAnswer": "3"},
            {"text": "Find the compound interest on Rs 16000 for 9 months at 20% per annum compounded quarterly.", "options": ["Rs 2522", "Rs 2400", "Rs 2600", "Rs 3000"], "correctAnswer": "Rs 2522"},
            {"text": "The difference between two whole numbers is 66. The ratio of the two numbers is 2:5. What are the two numbers?", "options": ["44 and 110", "22 and 88", "33 and 99", "66 and 132"], "correctAnswer": "44 and 110"},
            {"text": "Simplify: [ (x^a) / (x^b) ]^(a+b) * [ (x^b) / (x^c) ]^(b+c) * [ (x^c) / (x^a) ]^(c+a)", "options": ["1", "x", "0", "x^(a+b+c)"], "correctAnswer": "1"},
            {"text": "Find the area of a square whose diagonal is 10√2 cm.", "options": ["100 sq cm", "200 sq cm", "50 sq cm", "400 sq cm"], "correctAnswer": "100 sq cm"},
            {"text": "A vendor bought oranges at 6 for Rs 10 and sold them at 4 for Rs 6. Find his gain or loss percent.", "options": ["Loss 10%", "Gain 10%", "Loss 20%", "Gain 20%"], "correctAnswer": "Loss 10%"},
            {"text": "Divide 232.14 by 14.4.", "options": ["16.12", "15.5", "17.2", "16.1208..."], "correctAnswer": "16.1208..."},
            {"text": "Find the value of (x - a)^3 + (x - b)^3 + (x - c)^3 - 3(x - a)(x - b)(x - c) if 3x = a + b + c.", "options": ["0", "1", "3", "x"], "correctAnswer": "0"},
            {"text": "In a range of numbers 1 to 100, how many times does the digit 2 occur?", "options": ["20", "19", "10", "21"], "correctAnswer": "20"}
        ]
    },
    "hindi": {
        "easy": [
            {"text": "हिंदी वर्णमाला में कितने व्यंजन होते हैं?", "options": ["33", "11", "52", "25"], "correctAnswer": "33"},
            {"text": "'स्वाधीन' का विलोम शब्द क्या है?", "options": ["पराधीन", "स्वतंत्र", "आजाद", "गुलाम"], "correctAnswer": "पराधीन"},
            {"text": "'अग्नि' का पर्यायवाची शब्द है:", "options": ["पावक", "नीर", "गगन", "धरा"], "correctAnswer": "पावक"},
            {"text": "संज्ञा के स्थान पर आने वाले शब्द को क्या कहते हैं?", "options": ["सर्वनाम", "विशेषण", "क्रिया", "कारक"], "correctAnswer": "सर्वनाम"},
            {"text": "कारक के कितने भेद होते हैं?", "options": ["आठ", "छह", "सात", "नौ"], "correctAnswer": "आठ"},
            {"text": "शुद्ध शब्द पहचानिए:", "options": ["उज्ज्वल", "उज्वल", "उजवल", "ऊज्वल"], "correctAnswer": "उज्ज्वल"},
            {"text": "'हाथ मलना' मुहावरे का अर्थ है:", "options": ["पछताना", "तैयारी करना", "क्रोध करना", "हाथ धोना"], "correctAnswer": "पछताना"},
            {"text": "भाषा के कितने रूप होते हैं?", "options": ["दो (मौखिक और लिखित)", "तीन", "चार", "एक"], "correctAnswer": "दो (मौखिक और लिखित)"},
            {"text": "संज्ञा के कितने मुख्य भेद होते हैं?", "options": ["तीन", "पाँच", "चार", "दो"], "correctAnswer": "तीन"},
            {"text": "'पुष्प' का पर्यायवाची शब्द नहीं है:", "options": ["तरु", "फूल", "सुमन", "कुसुम"], "correctAnswer": "तरु"},
            {"text": "'ऊँचा' का विलोम क्या होगा?", "options": ["नीचा", "गहरा", "छोटा", "समतल"], "correctAnswer": "नीचा"},
            {"text": "सप्ताह का आखिरी दिन कौन सा माना जाता है?", "options": ["रविवार", "शनिवार", "सोमवार", "शुक्रवार"], "correctAnswer": "रविवार"},
            {"text": "गणतंत्र दिवस कब मनाया जाता है?", "options": ["26 जनवरी", "15 अगस्त", "2 अक्टूबर", "14 नवंबर"], "correctAnswer": "26 जनवरी"},
            {"text": "जो कपड़े सीता है उसे क्या कहते हैं?", "options": ["दर्जी", "धोबी", "मोची", "नाई"], "correctAnswer": "दर्जी"},
            {"text": "'बैल' का स्त्रीलिंग क्या है?", "options": ["गाय", "भैंस", "बकरी", "शेरनी"], "correctAnswer": "गाय"}
        ],
        "medium": [
            {"text": "संधि विच्छेद कीजिए: 'परोपकार'", "options": ["पर + उपकार", "परो + पकार", "पर + ओपकार", "परोप + कार"], "correctAnswer": "पर + उपकार"},
            {"text": "'दशानन' में कौन सा समास है?", "options": ["बहुव्रीहि", "अव्ययीभाव", "तत्पुरुष", "द्वंद्व"], "correctAnswer": "बहुव्रीहि"},
            {"text": "विशेषण के मुख्य कितने भेद होते हैं?", "options": ["चार", "पाँच", "छह", "आठ"], "correctAnswer": "चार"},
            {"text": "'आँखें फेर लेना' मुहावरे का अर्थ है:", "options": ["प्रतिकूल होना / बदल जाना", "अंधा होना", "गुस्सा करना", "नींद आना"], "correctAnswer": "प्रतिकूल होना / बदल जाना"},
            {"text": "अलंकार पहचानें: 'पीपर पात सरिस मन डोला।'", "options": ["उपमा अलंकार", "रूपक अलंकार", "उत्प्रेक्षा अलंकार", "अनुप्रास अलंकार"], "correctAnswer": "उपमा अलंकार"},
            {"text": "क्रिया के जिस रूप से आने वाले समय का बोध हो उसे कहते हैं:", "options": ["भविष्यत काल", "भूतकाल", "वर्तमान काल", "इनमें से कोई नहीं"], "correctAnswer": "भविष्यत काल"},
            {"text": "इनमें से कौन सा शब्द भाववाचक संज्ञा है?", "options": ["ईमानदारी", "राम", "नदी", "सोना"], "correctAnswer": "ईमानदारी"},
            {"text": "'अग्रज' का विलोम शब्द है:", "options": ["अनुज", "छोटा", "पीछे", "अंतिम"], "correctAnswer": "अनुज"},
            {"text": "संधि विच्छेद कीजिए: 'स्वागत'", "options": ["सु + आगत", "स्व + आगत", "स्वा + गत", "स + वागत"], "correctAnswer": "सु + आगत"},
            {"text": "जो सब कुछ जानता हो, उसे कहते हैं:", "options": ["सर्वज्ञ", "अल्पज्ञ", "बहुज्ञ", "विद्वान"], "correctAnswer": "सर्वज्ञ"},
            {"text": "वाक्य में 'अपादान कारक' की विभक्ति क्या है?", "options": ["से (अलग होने के अर्थ में)", "ने", "को", "के लिए"], "correctAnswer": "से (अलग होने के अर्थ में)"},
            {"text": "शुद्ध वाक्य पहचानिए:", "options": ["वह स्कूल जा रहा है।", "वह स्कूल जा रहे है।", "वे स्कूल जा रहा है।", "वह स्कूल जाती रहा है।"], "correctAnswer": "वह स्कूल जा रहा है।"},
            {"text": "'दाँतों तले उँगली दबाना' मुहावरे का अर्थ है:", "options": ["हैरान होना", "पछताना", "दर्द होना", "भूख लगना"], "correctAnswer": "हैरान होना"},
            {"text": "रचना के आधार पर वाक्य के कितने भेद होते हैं?", "options": ["तीन (सरल, संयुक्त, मिश्र)", "दो", "चार", "पाँच"], "correctAnswer": "तीन (सरल, संयुक्त, मिश्र)"},
            {"text": "'यथाशक्ति' में कौन सा समास है?", "options": ["अव्ययीभाव", "तत्पुरुष", "द्विगु", "द्वंद्व"], "correctAnswer": "अव्ययीभाव"}
        ],
        "hard": [
            {"text": "अलंकार पहचानें: 'चरण कमल बंदौ हरिराई।'", "options": ["रूपक अलंकार", "उपमा अलंकार", "श्लेष अलंकार", "यमक अलंकार"], "correctAnswer": "रूपक अलंकार"},
            {"text": "'कामायनी' महाकाव्य के रचयिता कौन हैं?", "options": ["जयशंकर प्रसाद", "सूर्यकांत त्रिपाठी निराला", "सुमित्रानंदन पंत", "महादेवी वर्मा"], "correctAnswer": "जयशंकर प्रसाद"},
            {"text": "इनमें से किस रस का स्थायी भाव 'निर्वेद' है?", "options": ["शांत रस", "शृंगार रस", "करुण रस", "वीर रस"], "correctAnswer": "शांत रस"},
            {"text": "वाच्य के भेद पहचानें: 'मुझसे चला नहीं जाता।'", "options": ["भाववाच्य", "कर्तृवाच्य", "कर्मवाच्य", "इनमें से कोई नहीं"], "correctAnswer": "भाववाच्य"},
            {"text": "'अन्धायुग' किसकी रचना है?", "options": ["धर्मवीर भारती", "मुक्तिबोध", "अज्ञेय", "निराला"], "correctAnswer": "धर्मवीर भारती"},
            {"text": "संधि विच्छेद कीजिए: 'अत्यधिक'", "options": ["अति + अधिक", "अत्य + अधिक", "अत + अधिक", "अत्यध + इक"], "correctAnswer": "अति + अधिक"},
            {"text": "जिस समास में उत्तर पद प्रधान हो, उसे कहते हैं:", "options": ["तत्पुरुष समास", "अव्ययीभाव समास", "द्वंद्व समास", "बहुव्रीहि समास"], "correctAnswer": "तत्पुरुष समास"},
            {"text": "'उल्टे बाँस बरेली को' लोकोक्ति का अर्थ है:", "options": ["विपरीत कार्य करना", "बेकार का काम करना", "मुश्किल काम करना", "गलती सुधारना"], "correctAnswer": "विपरीत कार्य करना"},
            {"text": "तत्सम शब्द पहचानें:", "options": ["कर्क", "केकड़ा", "काम", "रात"], "correctAnswer": "कर्क"},
            {"text": "छंद के कितने मुख्य अंग होते हैं?", "options": ["सात", "चार", "छह", "आठ"], "correctAnswer": "सात"},
            {"text": "'कमल' का पर्यायवाची नहीं है:", "options": ["वारिद", "जलज", "नीरज", "पंकज"], "correctAnswer": "वारिद"},
            {"text": "भाववाचक संज्ञा का उदाहरण नहीं है:", "options": ["मिठाई (यह जातिवाचक है, मिठास भाववाचक है)", "खटास", "मिठास", "सुंदरता"], "correctAnswer": "मिठाई (यह जातिवाचक है, मिठास भाववाचक है)"},
            {"text": "'आविष्कार' का संधि विच्छेद है:", "options": ["आविः + कार", "आवि + कार", "आविश + कार", "आवी + कार"], "correctAnswer": "आविः + कार"},
            {"text": "'अधजल गगरी छलकत जाए' का अर्थ है:", "options": ["कम ज्ञान वाले का अधिक दिखावा करना", "गगरी का फूटना", "पानी का गिरना", "गर्व करना"], "correctAnswer": "कम ज्ञान वाले का अधिक दिखावा करना"},
            {"text": "'पवन' शब्द में कौन सी संधि है?", "options": ["अयादि संधि", "यण संधि", "गुण संधि", "दीर्घ संधि"], "correctAnswer": "अयादि संधि"}
        ]
    },
    "science": {
        "easy": [
            {"text": "Which of these is a microorganism involved in curd formation?", "options": ["Lactobacillus", "Amoeba", "Paramecium", "Yeast"], "correctAnswer": "Lactobacillus"},
            {"text": "What is the process of loosening and turning the soil called?", "options": ["Tilling / Ploughing", "Sowing", "Irrigation", "Harvesting"], "correctAnswer": "Tilling / Ploughing"},
            {"text": "Which synthetic fiber is known as artificial silk?", "options": ["Rayon", "Nylon", "Polyester", "Acrylic"], "correctAnswer": "Rayon"},
            {"text": "What is the hardest natural substance known?", "options": ["Diamond", "Gold", "Iron", "Coal"], "correctAnswer": "Diamond"},
            {"text": "Which non-metal is stored in water to prevent it from catching fire?", "options": ["Phosphorus", "Sulfur", "Carbon", "Iodine"], "correctAnswer": "Phosphorus"},
            {"text": "The resource which can be renewed or replenished is called:", "options": ["Renewable resource", "Non-renewable resource", "Exhaustible resource", "Limited resource"], "correctAnswer": "Renewable resource"},
            {"text": "Which gas is used by plants during photosynthesis?", "options": ["Carbon dioxide", "Oxygen", "Nitrogen", "Hydrogen"], "correctAnswer": "Carbon dioxide"},
            {"text": "What is the male reproductive part of a flower called?", "options": ["Stamen", "Pistil", "Petal", "Sepal"], "correctAnswer": "Stamen"},
            {"text": "Which force helps us walk on the ground without slipping?", "options": ["Friction", "Gravity", "Magnetism", "Electrostatic"], "correctAnswer": "Friction"},
            {"text": "Sound is produced by ________.", "options": ["Vibrations", "Light", "Heat", "Pressure"], "correctAnswer": "Vibrations"},
            {"text": "Which instrument is used to measure earthquakes?", "options": ["Seismograph", "Barometer", "Thermometer", "Ammeter"], "correctAnswer": "Seismograph"},
            {"text": "What is the unit of frequency?", "options": ["Hertz (Hz)", "Decibel (dB)", "Meter (m)", "Second (s)"], "correctAnswer": "Hertz (Hz)"},
            {"text": "Which planet is known as the 'Morning or Evening Star'?", "options": ["Venus", "Mars", "Mercury", "Jupiter"], "correctAnswer": "Venus"},
            {"text": "What is the full form of LED?", "options": ["Light Emitting Diode", "Long Electronic Device", "Light Energy Disk", "Low Electric Dose"], "correctAnswer": "Light Emitting Diode"},
            {"text": "Which part of the cell is known as the power house?", "options": ["Mitochondria", "Nucleus", "Ribosome", "Chloroplast"], "correctAnswer": "Mitochondria"}
        ],
        "medium": [
            {"text": "Which of these diseases is caused by a protozoan?", "options": ["Malaria", "Tuberculosis", "Measles", "Typhoid"], "correctAnswer": "Malaria"},
            {"text": "What is the process of conversion of sugar into alcohol called?", "options": ["Fermentation", "Nitrogen Fixation", "Pasteurization", "Molding"], "correctAnswer": "Fermentation"},
            {"text": "Why are copper wires coated with PVC?", "options": ["PVC is an expert insulator", "To make wires look good", "PVC is a great conductor", "To increase weight"], "correctAnswer": "PVC is an expert insulator"},
            {"text": "Which fuel has the highest calorific value?", "options": ["Hydrogen", "Petrol", "LPG", "Coal"], "correctAnswer": "Hydrogen"},
            {"text": "What is the process of depositing a layer of zinc on iron to prevent rusting called?", "options": ["Galvanization", "Anodizing", "Electroplating", "Tinning"], "correctAnswer": "Galvanization"},
            {"text": "Which endocrine gland is known as the master gland?", "options": ["Pituitary gland", "Thyroid gland", "Adrenal gland", "Pancreas"], "correctAnswer": "Pituitary gland"},
            {"text": "If the angle of incidence is 30 degrees, what is the angle of reflection?", "options": ["30 degrees", "60 degrees", "90 degrees", "0 degrees"], "correctAnswer": "30 degrees"},
            {"text": "The pressure exerted by a liquid increases with ________.", "options": ["Depth", "Temperature", "Volume", "Color"], "correctAnswer": "Depth"},
            {"text": "Which mirror is used in street lights to diverge light over a large area?", "options": ["Convex mirror", "Concave mirror", "Plane mirror", "Parabolic mirror"], "correctAnswer": "Convex mirror"},
            {"text": "Identify the non-metal that is a good conductor of electricity.", "options": ["Graphite", "Diamond", "Sulfur", "Phosphorus"], "correctAnswer": "Graphite"},
            {"text": "What causes land breeze?", "options": ["Differential heating of land and sea", "Rotation of Earth", "Moon's gravity", "Magnetic fields"], "correctAnswer": "Differential heating of land and sea"},
            {"text": "Which fertilizer provides only Potassium?", "options": ["Potash (Muriate of Potash)", "Urea", "DAP", "Super Phosphate"], "correctAnswer": "Potash (Muriate of Potash)"},
            {"text": "What is the audible range of frequencies for humans?", "options": ["20 Hz to 20,000 Hz", "0 Hz to 100 Hz", "50,000 Hz and above", "Under 20 Hz only"], "correctAnswer": "20 Hz to 20,000 Hz"},
            {"text": "Define the phenomenon of splitting of white light into seven colors.", "options": ["Dispersion", "Reflection", "Refraction", "Diffraction"], "correctAnswer": "Dispersion"},
            {"text": "Which plant hormone promotes cell division?", "options": ["Cytokinin", "Auxin", "Gibberellin", "Abscisic acid"], "correctAnswer": "Cytokinin"}
        ],
        "hard": [
            {"text": "What is the sequence of the Nitrogen Cycle processes?", "options": ["Nitrogen Fixation -> Nitrification -> Assimilation -> Ammonification -> Denitrification", "Assimilation -> Fixation -> Denitrification", "Denitrification -> Fixation -> Nitrification", "Nitrification -> Ammonification -> Fixation"], "correctAnswer": "Nitrogen Fixation -> Nitrification -> Assimilation -> Ammonification -> Denitrification"},
            {"text": "Who discovered the process of vaccination for Smallpox?", "options": ["Edward Jenner", "Louis Pasteur", "Alexander Fleming", "Robert Koch"], "correctAnswer": "Edward Jenner"},
            {"text": "Identify the true property of thermoplastics.", "options": ["They soften on heating and can be reshaped repeatedly.", "They become permanently hard once molded.", "They are heat resistant and don't change shape.", "They are made of highly cross-linked polymers."], "correctAnswer": "They soften on heating and can be reshaped repeatedly."},
            {"text": "Which metal is refined by its reaction with carbon monoxide in the Mond's Process?", "options": ["Nickel", "Iron", "Copper", "Aluminum"], "correctAnswer": "Nickel"},
            {"text": "What occurs during the process of 'In vitro Fertilization' (IVF)?", "options": ["Fertilization occurs outside the female body in a lab dish.", "Fertilization occurs inside the womb naturally.", "No fertilization is required.", "Fertilization occurs in a test tube inside the body."], "correctAnswer": "Fertilization occurs outside the female body in a lab dish."},
            {"text": "What happens to the focal length of a concave mirror when it is immersed in water?", "options": ["Remains unchanged", "Increases", "Decreases", "Becomes zero"], "correctAnswer": "Remains unchanged"},
            {"text": "Which gas is evolved when a metal reacts with dilute hydrochloric acid?", "options": ["Hydrogen", "Oxygen", "Carbon dioxide", "Chlorine"], "correctAnswer": "Hydrogen"},
            {"text": "The constellation 'Ursa Major' is also known as:", "options": ["Saptarishi / Big Dipper", "Orion", "Cassiopeia", "Leo"], "correctAnswer": "Saptarishi / Big Dipper"},
            {"text": "Define 'Interference' of light waves.", "options": ["The superposition of two or more waves to form a resultant wave.", "Bending of light around corners.", "Splitting of light into colors.", "Total reflection inside a medium."], "correctAnswer": "The superposition of two or more waves to form a resultant wave."},
            {"text": "Which part of the brain controls voluntary actions and thinking?", "options": ["Cerebrum", "Cerebellum", "Medulla", "Hypothalamus"], "correctAnswer": "Cerebrum"},
            {"text": "What is the escape velocity of Earth?", "options": ["11.2 km/s", "9.8 km/s", "7.9 km/s", "25 km/s"], "correctAnswer": "11.2 km/s"},
            {"text": "Identify the isotope used in the treatment of goiter.", "options": ["Iodine-131", "Carbon-14", "Cobalt-60", "Uranium-235"], "correctAnswer": "Iodine-131"},
            {"text": "Which phenomenon makes the sky appear blue?", "options": ["Scattering of light", "Reflection of light", "Refraction of light", "Dispersion of light"], "correctAnswer": "Scattering of light"},
            {"text": "What is 'Cation' in chemistry?", "options": ["A positively charged ion", "A negatively charged ion", "A neutral atom", "A nucleus"], "correctAnswer": "A positively charged ion"},
            {"text": "Function of the hormone 'Thyroxine' is:", "options": ["Regulate carbohydrate, protein, and fat metabolism", "Regulate blood sugar", "Control growth", "Prepare body for emergency"], "correctAnswer": "Regulate carbohydrate, protein, and fat metabolism"}
        ]
    },
    "social-science": {
        "easy": [
            {"text": "Who was the first President of Independent India?", "options": ["Dr. Rajendra Prasad", "Jawaharlal Nehru", "Sardar Patel", "Dr. S. Radhakrishnan"], "correctAnswer": "Dr. Rajendra Prasad"},
            {"text": "When did the Constitution of India come into effect?", "options": ["26th January 1950", "15th August 1947", "26th November 1949", "2nd October 1950"], "correctAnswer": "26th January 1950"},
            {"text": "Which is the most populous country in the world currently?", "options": ["India", "China", "USA", "Russia"], "correctAnswer": "India"},
            {"text": "Who is known as the 'Iron Man of India'?", "options": ["Sardar Vallabhbhai Patel", "Subhash Chandra Bose", "Mahatma Gandhi", "Lala Lajpat Rai"], "correctAnswer": "Sardar Vallabhbhai Patel"},
            {"text": "Which fundamental right allows citizens to move court if their rights are violated?", "options": ["Right to Constitutional Remedies", "Right to Equality", "Right to Freedom", "Right against Exploitation"], "correctAnswer": "Right to Constitutional Remedies"},
            {"text": "Silicon Valley of the East is located in:", "options": ["Bengaluru", "Hyderabad", "Seoul", "Tokyo"], "correctAnswer": "Bengaluru"},
            {"text": "The British rule in India ended in which year?", "options": ["1947", "1942", "1950", "1930"], "correctAnswer": "1947"},
            {"text": "Which resource is considered the most important for the development of any country?", "options": ["Human Resources", "Land", "Water", "Minerals"], "correctAnswer": "Human Resources"},
            {"text": "What is the minimum voting age in India?", "options": ["18 years", "21 years", "25 years", "16 years"], "correctAnswer": "18 years"},
            {"text": "Which imaginay line divides Earth into Eastern and Western Hemispheres?", "options": ["Prime Meridian", "Equator", "International Date Line", "Tropic of Cancer"], "correctAnswer": "Prime Meridian"},
            {"text": "A place where the record of history is kept is called:", "options": ["Archives", "Library", "Museum", "Fort"], "correctAnswer": "Archives"},
            {"text": "Who established the first English factory in Hugli?", "options": ["English East India Company", "French EIC", "Dutch EIC", "Portuguese"], "correctAnswer": "English East India Company"},
            {"text": "Which is the largest coffee-producing country in the world?", "options": ["Brazil", "India", "Vietnam", "Colombia"], "correctAnswer": "Brazil"},
            {"text": "The Upper House of the Indian Parliament is:", "options": ["Rajya Sabha", "Lok Sabha", "Vidhan Sabha", "Parliament House"], "correctAnswer": "Rajya Sabha"},
            {"text": "Who led the revolt of 1857 in Kanpur?", "options": ["Nana Saheb", "Rani Lakshmibai", "Kunwar Singh", "Tantia Tope"], "correctAnswer": "Nana Saheb"}
        ],
        "medium": [
            {"text": "Which Battle established British supremacy in Bengal?", "options": ["Battle of Buxar (1764)", "Battle of Plassey (1757)", "Battle of Panipat", "Battle of Haldighati"], "correctAnswer": "Battle of Buxar (1764)"},
            {"text": "The 'Doctrine of Lapse' was introduced by:", "options": ["Lord Dalhousie", "Lord Curzon", "Lord Canning", "Lord Wellesley"], "correctAnswer": "Lord Dalhousie"},
            {"text": "What constitutes the 'Parliament' of India?", "options": ["President, Lok Sabha, and Rajya Sabha", "Lok Sabha and Rajya Sabha only", "Prime Minister and Cabinet", "Supreme Court and High Courts"], "correctAnswer": "President, Lok Sabha, and Rajya Sabha"},
            {"text": "In shifting cultivation, what is another name given to it in North-east India?", "options": ["Jhuming", "Milpa", "Roca", "Ladang"], "correctAnswer": "Jhuming"},
            {"text": "Which land revenue system was introduced by Lord Cornwallis in Bengal and Bihar?", "options": ["Permanent Settlement", "Ryotwari System", "Mahalwari System", "Zabti System"], "correctAnswer": "Permanent Settlement"},
            {"text": "The major causes of soil erosion are:", "options": ["Deforestation and overgrazing", "Afforestation", "Terrace farming", "Crop rotation"], "correctAnswer": "Deforestation and overgrazing"},
            {"text": "Who was the architect of the 'New Delhi' planned during British rule?", "options": ["Edwin Lutyens and Herbert Baker", "Le Corbusier", "Charles Correa", "B.V. Doshi"], "correctAnswer": "Edwin Lutyens and Herbert Baker"},
            {"text": "The 'Right to Information' (RTI) Act was passed in India in:", "options": ["2005", "2000", "2010", "1995"], "correctAnswer": "2005"},
            {"text": "Which planet is unique for having life and being called the 'Watery Planet'?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "correctAnswer": "Earth"},
            {"text": "What is 'Judicial Review'?", "options": ["Power of the courts to examine the legality of laws and government actions", "Rewriting history", "Reviewing a book", "Police investigation"], "correctAnswer": "Judicial Review"},
            {"text": "A person who describes an event of history is called a/an:", "options": ["Historian", "Archaeologist", "Anthropologist", "Biographer"], "correctAnswer": "Historian"},
            {"text": "Who was the last Governor-General of India before independence?", "options": ["Lord Mountbatten", "Lord Wavell", "Lord Linlithgow", "Lord Curzon"], "correctAnswer": "Lord Mountbatten"},
            {"text": "Which industry is often called the 'Backbone of Modern Industry'?", "options": ["Steel Industry", "Information Technology", "Textile Industry", "Tourism"], "correctAnswer": "Steel Industry"},
            {"text": "The term of a member of the Rajya Sabha is:", "options": ["6 years", "5 years", "2 years", "Lifetime"], "correctAnswer": "6 years"},
            {"text": "Which fiber is known as 'Golden Fiber'?", "options": ["Jute", "Cotton", "Silk", "Nylon"], "correctAnswer": "Jute"}
        ],
        "hard": [
            {"text": "The 'Subsidiary Alliance' was a system devised by:", "options": ["Lord Wellesley", "Lord Dalhousie", "Lord Hastings", "Lord Cornwallis"], "correctAnswer": "Lord Wellesley"},
            {"text": "Who founded the 'Brahmo Samaj'?", "options": ["Raja Ram Mohan Roy", "Swami Dayananda Saraswati", "Swami Vivekananda", "Ishwar Chandra Vidyasagar"], "correctAnswer": "Raja Ram Mohan Roy"},
            {"text": "What is the primary objective of the 'Directive Principles of State Policy' (DPSP)?", "options": ["To establish a social and economic democracy (Welfare State)", "To give power to the police", "To protect fundamental rights", "To regulate trade"], "correctAnswer": "To establish a social and economic democracy (Welfare State)"},
            {"text": "Which session of the Indian National Congress was presided over by Mahatma Gandhi?", "options": ["Belgaum Session (1924)", "Lahore Session", "Haripura Session", "tripuri Session"], "correctAnswer": "Belgaum Session (1924)"},
            {"text": "What is the formula for 'Resource Conservation'?", "options": ["Reduce, Reuse, Recycle", "Use and throw", "Ignore the future", "Only export"], "correctAnswer": "Reduce, Reuse, Recycle"},
            {"text": "Identify the main feature of the 'Mahalwari System' of land revenue.", "options": ["Revenue was determined for each village (Mahal) collectively.", "Revenue was fixed with the individual farmer.", "Revenue was fixed permanently with Zamindars.", "No revenue was collected."], "correctAnswer": "Revenue was determined for each village (Mahal) collectively."},
            {"text": "Who wrote output text the 'Gulamgiri'?", "options": ["Jyotirao Phule", "Dr. B.R. Ambedkar", "Periyar", "Mahatma Gandhi"], "correctAnswer": "Jyotirao Phule"},
            {"text": "The 'Public Interest Litigation' (PIL) concept helps in:", "options": ["Filing a case in court based on a matter of public interest by anyone.", "Increasing the salary of judges.", "Closing down companies.", "Promoting celebrities."], "correctAnswer": "Filing a case in court based on a matter of public interest by anyone."},
            {"text": "Which is the highest law-making body in India?", "options": ["The Parliament", "Supreme Court", "The President", "The Cabinet"], "correctAnswer": "The Parliament"},
            {"text": "Who was the first woman to become the President of the Indian National Congress?", "options": ["Annie Besant", "Sarojini Naidu", "Indira Gandhi", "Nellie Sengupta"], "correctAnswer": "Annie Besant"},
            {"text": "Which layer of the Earth is in a liquid state?", "options": ["Outer Core", "Inner Core", "Mantle", "Crust"], "correctAnswer": "Outer Core"},
            {"text": "Identify the 'Prinicipal of Secularism' followed in India.", "options": ["State respects all religions equally and maintains principled distance.", "State has an official religion.", "State prohibits any religious activity.", "State is ruled by priests."], "correctAnswer": "State respects all religions equally and maintains principled distance."},
            {"text": "Who led the Champaran Satyagraha in 1917?", "options": ["Mahatma Gandhi", "Rajendra Prasad", "Jawaharlal Nehru", "Sardar Patel"], "correctAnswer": "Mahatma Gandhi"},
            {"text": "The 'Human Development Index' (HDI) is published by:", "options": ["UNDP (United Nations Development Programme)", "World Bank", "WHO", "UNICEF"], "correctAnswer": "UNDP (United Nations Development Programme)"},
            {"text": "What is the term for a situation where population growth exceeds the food supply?", "options": ["Malthusian Trap", "Demographic Transition", "Overpopulation", "Sustenance Crisis"], "correctAnswer": "Malthusian Trap"}
        ]
    }
}

def main():
    bank_path = '/Users/arpan1.mukherjee/code/GhostMaze/public/AhirsAcademy/data/question_bank.json'
    
    with open(bank_path, 'r', encoding='utf-8') as f:
        question_bank = json.load(f)
        
    question_bank['class_8'] = class_8_data
    
    with open(bank_path, 'w', encoding='utf-8') as f:
        json.dump(question_bank, f, indent=4, ensure_ascii=False)
        
    print("Successfully injected final batch of 15 comprehensive questions per tier for Class 8!")

if __name__ == '__main__':
    main()
