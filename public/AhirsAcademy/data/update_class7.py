import json
import os

class_7_data = {
    "english": {
        "easy": [
            {"text": "Which of these is a collective noun?", "options": ["Fleet", "Ship", "Sailor", "Ocean"], "correctAnswer": "Fleet"},
            {"text": "Identify the conjunction: 'He failed because he did not study.'", "options": ["Because", "Failed", "Not", "Study"], "correctAnswer": "Because"},
            {"text": "What is the past participle of 'fly'?", "options": ["Flown", "Flew", "Flying", "Flies"], "correctAnswer": "Flown"},
            {"text": "Choose the correct article: 'She is _____ European citizen.'", "options": ["A", "An", "The", "No article needed"], "correctAnswer": "A"},
            {"text": "Identify the type of noun: 'Wisdom'.", "options": ["Abstract Noun", "Proper Noun", "Common Noun", "Collective Noun"], "correctAnswer": "Abstract Noun"},
            {"text": "Which word is a synonym for 'Trivial'?", "options": ["Unimportant", "Crucial", "Massive", "Difficult"], "correctAnswer": "Unimportant"},
            {"text": "What is the antonym of 'Transparent'?", "options": ["Opaque", "Clear", "Bright", "Thin"], "correctAnswer": "Opaque"},
            {"text": "Identify the preposition: 'The cat is hiding under the bed.'", "options": ["Under", "Hiding", "Cat", "Bed"], "correctAnswer": "Under"},
            {"text": "Which degree of comparison is 'Best'?", "options": ["Superlative", "Positive", "Comparative", "Absolute"], "correctAnswer": "Superlative"},
            {"text": "Correct the spelling: 'Acomodation'", "options": ["Accommodation", "Accomodation", "Acommodation", "Acommodasion"], "correctAnswer": "Accommodation"},
            {"text": "What does the root 'Aqua' mean?", "options": ["Water", "Fire", "Air", "Earth"], "correctAnswer": "Water"},
            {"text": "Match the idiom: 'Once in a blue moon' means?", "options": ["Very rarely", "Every night", "Occasionally", "During a full moon"], "correctAnswer": "Very rarely"},
            {"text": "Identify the subject: 'My little brother's friend won the race.'", "options": ["My little brother's friend", "Won", "The race", "Friend"], "correctAnswer": "My little brother's friend"},
            {"text": "Which word is an adverb?", "options": ["Quietly", "Quiet", "Silence", "Still"], "correctAnswer": "Quietly"},
            {"text": "What is a autobiography?", "options": ["An account of a person's life written by that person.", "An account of a person's life written by someone else.", "A fictional story.", "A poem."], "correctAnswer": "An account of a person's life written by that person."}
        ],
        "medium": [
            {"text": "Change into passive voice: 'The grandmother tells stories to the children.'", "options": ["Stories are told to the children by the grandmother.", "The grandmother told stories to the children.", "Children are told stories.", "Stories have been told to the children by the grandmother."], "correctAnswer": "Stories are told to the children by the grandmother."},
            {"text": "Identify the mood: 'If I were a king, I would make everyone happy.'", "options": ["Subjunctive", "Indicative", "Imperative", "Interrogative"], "correctAnswer": "Subjunctive"},
            {"text": "Which clause is italicized: 'The boy <i>who won the prize</i> is my cousin.'?", "options": ["Adjective Clause", "Noun Clause", "Adverb Clause", "Relative Phrase"], "correctAnswer": "Adjective Clause"},
            {"text": "Find the correct homophone: 'He had to _____ through the crowded market.'", "options": ["Wade", "Weighed", "Wait", "Wayed"], "correctAnswer": "Wade"},
            {"text": "What does the idiom 'Burning the midnight oil' mean?", "options": ["Working late into the night", "Wasting fuel", "Sleeping early", "Cooking dinner"], "correctAnswer": "Working late into the night"},
            {"text": "Identify the part of speech of the underlined word: 'He is <u>very</u> smart.'", "options": ["Adverb", "Adjective", "Noun", "Verb"], "correctAnswer": "Adverb"},
            {"text": "Which is a complex sentence?", "options": ["I will go to the park when the rain stops.", "I went to the park and it rained.", "The rain stopped.", "I like rain."], "correctAnswer": "I will go to the park when the rain stops."},
            {"text": "What suffix makes 'Friend' into an abstract noun?", "options": ["-ship", "-ly", "-ness", "-able"], "correctAnswer": "-ship"},
            {"text": "Identify the figure of speech: 'The city was a beehive of activity.'", "options": ["Metaphor", "Simile", "Personification", "Hyperbole"], "correctAnswer": "Metaphor"},
            {"text": "Choose the correctly spelled word.", "options": ["Entrepreneur", "Enterprenure", "Entreprener", "Enterprenure"], "correctAnswer": "Entrepreneur"},
            {"text": "What is the meaning of the prefix 'Omni-' as in 'Omnipotent'?", "options": ["All", "Few", "None", "Below"], "correctAnswer": "All"},
            {"text": "Which pair of words are antonyms?", "options": ["Abundant - Scarce", "Rich - Wealthy", "Sorrow - Sadness", "Quick - Speedy"], "correctAnswer": "Abundant - Scarce"},
            {"text": "Identify the direct object: 'Ravi gave Meena a book.'", "options": ["A book", "Meena", "Ravi", "Gave"], "correctAnswer": "A book"},
            {"text": "Which tense is used here: 'I have been living here for five years.'?", "options": ["Present Perfect Continuous", "Present Perfect", "Present Continuous", "Past Perfect Continuous"], "correctAnswer": "Present Perfect Continuous"},
            {"text": "Find the correctly punctuated sentence.", "options": ["\"Where are you going?\" asked Rahul.", "\"Where are you going\" asked Rahul.", "Where are you going asked Rahul.", "\"Where are you going? asked Rahul.\""], "correctAnswer": "\"Where are you going?\" asked Rahul."}
        ],
        "hard": [
            {"text": "Identify the error: 'None of the two options are acceptable to me.'", "options": ["'None' should be 'Neither' and 'are' should be 'is'", "'None' should be 'Neither'", "'are' should be 'is'", "No error"], "correctAnswer": "'None' should be 'Neither' and 'are' should be 'is'"},
            {"text": "What is the meaning of the phrase 'En route'?", "options": ["On the way", "At the end", "From the start", "By any means"], "correctAnswer": "On the way"},
            {"text": "Identify the portmanteau word.", "options": ["Brunch (Breakfast + Lunch)", "Computer", "Telephone", "Notebook"], "correctAnswer": "Brunch (Breakfast + Lunch)"},
            {"text": "What device is used here: 'Better late than never.'?", "options": ["Antithesis / Epigram", "Oxymoron", "Onomatopoeia", "Personification"], "correctAnswer": "Antithesis / Epigram"},
            {"text": "Change into indirect speech: The teacher said to us, 'Honesty is the best policy.'", "options": ["The teacher told us that honesty is the best policy.", "The teacher said us that honesty was the best policy.", "The teacher told us that honesty was the best policy.", "The teacher said that honesty is the best policy to us."], "correctAnswer": "The teacher told us that honesty is the best policy."},
            {"text": "Which clause is 'if it rains' in 'I will stay home if it rains'?", "options": ["Adverb Clause", "Adjective Clause", "Noun Clause", "Prepositional Clause"], "correctAnswer": "Adverb Clause"},
            {"text": "Identify the transitive verb in these options.", "options": ["The boy kicked the ball.", "He slept.", "She laughed.", "The sun shines."], "correctAnswer": "The boy kicked the ball."},
            {"text": "What is a 'misanthrope'?", "options": ["A person who hates mankind", "A person who loves books", "A person who travels a lot", "A person who studies rocks"], "correctAnswer": "A person who hates mankind"},
            {"text": "Identify the mood: 'Shut the door immediately.'", "options": ["Imperative", "Subjunctive", "Indicative", "Declarative"], "correctAnswer": "Imperative"},
            {"text": "Which of these is a malapropism (misuse of a word with a similar sounding one)?", "options": ["He is a man of great statue (instead of stature).", "He is very tall.", "He is short.", "He is strong."], "correctAnswer": "He is a man of great statue (instead of stature)."},
            {"text": "What is the origin of the word 'Paparazzi'?", "options": ["Italian (character in a Fellini film)", "French", "Spanish", "English"], "correctAnswer": "Italian (character in a Fellini film)"},
            {"text": "Identify the grammatical case of 'John' in 'John's book'.", "options": ["Possessive (Genitive)", "Nominative", "Accusative", "Dative"], "correctAnswer": "Possessive (Genitive)"},
            {"text": "What does a 'lexicographer' do?", "options": ["Writes dictionaries", "Studies stars", "Collects stamps", "Fixes shoes"], "correctAnswer": "Writes dictionaries"},
            {"text": "Identify the rhetorical question.", "options": ["Who doesn't want to be happy?", "Where is the post office?", "What is your name?", "How are you?"], "correctAnswer": "Who doesn't want to be happy?"},
            {"text": "Find the sequence of tenses: 'He told me that he _____ the work.'", "options": ["Had finished", "Finishes", "Will finish", "Has finished"], "correctAnswer": "Had finished"}
        ]
    },
    "maths": {
        "easy": [
            {"text": "Evaluate: (-15) + (-20)", "options": ["-35", "35", "5", "-5"], "correctAnswer": "-35"},
            {"text": "What is the reciprocal of 3/4?", "options": ["4/3", "-3/4", "1/4", "3"], "correctAnswer": "4/3"},
            {"text": "Solve for x: x + 5 = -2", "options": ["-7", "3", "7", "-3"], "correctAnswer": "-7"},
            {"text": "What is the area of a square with perimeter 40 cm?", "options": ["100 sq cm", "40 sq cm", "1600 sq cm", "20 sq cm"], "correctAnswer": "100 sq cm"},
            {"text": "A triangle with all sides unequal is called a:", "options": ["Scalene triangle", "Isosceles triangle", "Equilateral triangle", "Right triangle"], "correctAnswer": "Scalene triangle"},
            {"text": "What is 15% of 200?", "options": ["30", "15", "20", "45"], "correctAnswer": "30"},
            {"text": "Find the median of the data: 2, 4, 6, 8, 10.", "options": ["6", "4", "8", "5"], "correctAnswer": "6"},
            {"text": "What is the value of 5^0 (five to the power zero)?", "options": ["1", "0", "5", "Not defined"], "correctAnswer": "1"},
            {"text": "An angle measuring 180 degrees is called a:", "options": ["Straight angle", "Right angle", "Acute angle", "Reflex angle"], "correctAnswer": "Straight angle"},
            {"text": "Convert 3/5 into a decimal.", "options": ["0.6", "0.3", "0.5", "0.8"], "correctAnswer": "0.6"},
            {"text": "If a dozen eggs cost Rs 60, how much will 5 eggs cost?", "options": ["Rs 25", "Rs 30", "Rs 20", "Rs 15"], "correctAnswer": "Rs 25"},
            {"text": "What is the perimeter of a rectangle with length 10 cm and breadth 5 cm?", "options": ["30 cm", "15 cm", "50 cm", "25 cm"], "correctAnswer": "30 cm"},
            {"text": "Which is the smallest prime number?", "options": ["2", "1", "3", "0"], "correctAnswer": "2"},
            {"text": "Identify the coefficient of x in the expression 5x - 3y.", "options": ["5", "-3", "x", "3"], "correctAnswer": "5"},
            {"text": "What is the unit digit of 23^2?", "options": ["9", "3", "6", "1"], "correctAnswer": "9"}
        ],
        "medium": [
            {"text": "The sum of three consecutive integers is 51. What is the middle integer?", "options": ["17", "16", "18", "15"], "correctAnswer": "17"},
            {"text": "Simplify: 1/2 + 1/3 - 1/4", "options": ["7/12", "5/12", "1", "1/6"], "correctAnswer": "7/12"},
            {"text": "If the radius of a circle is doubled, what happens to its area?", "options": ["Becomes four times", "Doubles", "Stays the same", "Becomes eight times"], "correctAnswer": "Becomes four times"},
            {"text": "Solve for y: 2(y - 3) = 10", "options": ["8", "5", "13", "11"], "correctAnswer": "8"},
            {"text": "What is the probability of getting an even number in a single throw of a die?", "options": ["1/2", "1/3", "1/6", "2/3"], "correctAnswer": "1/2"},
            {"text": "Find the mode of the following data: 3, 5, 2, 3, 5, 3, 7.", "options": ["3", "5", "2", "7"], "correctAnswer": "3"},
            {"text": "If cost price is Rs 400 and selling price is Rs 450, what is the profit percentage?", "options": ["12.5%", "10%", "15%", "25%"], "correctAnswer": "12.5%"},
            {"text": "Convert 36 km/h into m/s.", "options": ["10 m/s", "15 m/s", "5 m/s", "20 m/s"], "correctAnswer": "10 m/s"},
            {"text": "In a triangle, if two angles are 45 and 75 degrees, what is the third angle?", "options": ["60", "70", "80", "90"], "correctAnswer": "60"},
            {"text": "Find the simple interest on Rs 1000 at 5% per annum for 2 years.", "options": ["Rs 100", "Rs 50", "Rs 200", "Rs 150"], "correctAnswer": "Rs 100"},
            {"text": "A number exceeded by its 20% is 120. Find the number.", "options": ["100", "80", "110", "90"], "correctAnswer": "100"},
            {"text": "The length of a rectangular plot is twice its breadth. If the perimeter is 60m, find the length.", "options": ["20m", "10m", "30m", "15m"], "correctAnswer": "20m"},
            {"text": "Simplify: (4^3) / (4^2)", "options": ["4", "16", "1", "64"], "correctAnswer": "4"},
            {"text": "If 3 men can do a piece of work in 6 days, how many men can do it in 2 days?", "options": ["9", "6", "12", "4"], "correctAnswer": "9"},
            {"text": "Which of these is equivalent to 0.125?", "options": ["1/8", "1/4", "1/5", "1/10"], "correctAnswer": "1/8"}
        ],
        "hard": [
            {"text": "A wire in the shape of a square encloses an area of 121 sq cm. If the same wire is bent into a circle, what is the area of the circle? (Take π = 22/7)", "options": ["154 sq cm", "144 sq cm", "121 sq cm", "176 sq cm"], "correctAnswer": "154 sq cm"},
            {"text": "Divide 50 into two parts such that the sum of their reciprocals is 1/12.", "options": ["20 and 30", "10 and 40", "25 and 25", "15 and 35"], "correctAnswer": "20 and 30"},
            {"text": "Find the value of x: 3^(x+2) = 81", "options": ["2", "4", "3", "1"], "correctAnswer": "2"},
            {"text": "The ratio of the ages of A and B is 3:4. After 5 years, the ratio becomes 4:5. Find their present ages.", "options": ["15 and 20", "12 and 16", "9 and 12", "18 and 24"], "correctAnswer": "15 and 20"},
            {"text": "If a^2 + b^2 = 25 and ab = 12, what is the value of (a + b)^2?", "options": ["49", "37", "13", "25"], "correctAnswer": "49"},
            {"text": "The perimeter of a semi-circle is 36 cm. Find its diameter. (π = 22/7)", "options": ["14 cm", "7 cm", "21 cm", "28 cm"], "correctAnswer": "14 cm"},
            {"text": "What is the smallest number by which 675 must be multiplied so that the product is a perfect cube?", "options": ["5", "3", "2", "7"], "correctAnswer": "5"},
            {"text": "Find the sum of all interior angles of a pentagon.", "options": ["540 degrees", "360 degrees", "720 degrees", "180 degrees"], "correctAnswer": "540 degrees"},
            {"text": "At what rate of simple interest will a sum of money double itself in 8 years?", "options": ["12.5%", "10%", "15%", "8%"], "correctAnswer": "12.5%"},
            {"text": "Solve for x: (x - 1)/3 + (x - 2)/4 = 1", "options": ["22/7", "3", "2", "4"], "correctAnswer": "22/7"},
            {"text": "The difference between the squares of two consecutive odd integers is always divisible by:", "options": ["8", "3", "6", "10"], "correctAnswer": "8"},
            {"text": "If the price of sugar increases by 25%, by what percentage must a household reduce consumption to keep the expenditure same?", "options": ["20%", "25%", "15%", "10%"], "correctAnswer": "20%"},
            {"text": "Find the area of a rhombus whose diagonals are 16 cm and 12 cm.", "options": ["96 sq cm", "192 sq cm", "48 sq cm", "144 sq cm"], "correctAnswer": "96 sq cm"},
            {"text": "If x + 1/x = 3, find x^2 + 1/x^2.", "options": ["7", "9", "11", "5"], "correctAnswer": "7"},
            {"text": "How many tiles of size 10cm x 10cm are needed to cover a floor of 4m x 3m?", "options": ["1200", "120", "600", "2400"], "correctAnswer": "1200"}
        ]
    },
    "hindi": {
        "easy": [
            {"text": "हिंदी वर्णमाला में कितने स्वर होते हैं?", "options": ["11", "13", "33", "25"], "correctAnswer": "11"},
            {"text": "'सत्य' का विलोम शब्द क्या है?", "options": ["असत्य", "झूठ", "पाप", "क्रोध"], "correctAnswer": "असत्य"},
            {"text": "'आकाश' का पर्यायवाची शब्द है:", "options": ["गगन", "धरा", "नीर", "अनल"], "correctAnswer": "गगन"},
            {"text": "संज्ञा के कितने भेद होते हैं?", "options": ["पाँच", "तीन", "चार", "दो"], "correctAnswer": "पाँच"},
            {"text": "कर्म के आधार पर क्रिया के कितने भेद होते हैं?", "options": ["दो (सकर्मक और अकर्मक)", "तीन", "चार", "पाँच"], "correctAnswer": "दो (सकर्मक और अकर्मक)"},
            {"text": "'कमल' का पर्यायवाची शब्द नहीं है:", "options": ["पावक", "पंकज", "नीरज", "सरोज"], "correctAnswer": "पावक"},
            {"text": "कारक के कितने भेद होते हैं?", "options": ["आठ", "छह", "सात", "नौ"], "correctAnswer": "आठ"},
            {"text": "सर्वनाम के कितने भेद होते हैं?", "options": ["छह", "पाँच", "चार", "आठ"], "correctAnswer": "छह"},
            {"text": "शुद्ध शब्द चुनें:", "options": ["आशीर्वाद", "आशिर्वाद", "आशीर्बाद", "अशीर्वाद"], "correctAnswer": "आशीर्वाद"},
            {"text": "'नदी' का बहुवचन है:", "options": ["नदियाँ", "नदीयों", "नदिएँ", "नदिया"], "correctAnswer": "नदियाँ"},
            {"text": "विलोम शब्दों का सही जोड़ा पहचानें:", "options": ["दिन - रात", "मित्र - दोस्त", "पानी - जल", "फूल - पुष्प"], "correctAnswer": "दिन - रात"},
            {"text": "जो चित्र बनाता है उसे क्या कहते हैं?", "options": ["चित्रकार", "लेखक", "गायिका", "नर्तक"], "correctAnswer": "चित्रकार"},
            {"text": "सप्ताह में कितने दिन होते हैं?", "options": ["सात", "छह", "आठ", "पाँच"], "correctAnswer": "सात"},
            {"text": "हमारे देश का राष्ट्रीय फूल क्या है?", "options": ["कमल", "गुलाब", "सूरजमुखी", "गेंदा"], "correctAnswer": "कमल"},
            {"text": "'मामा' का स्त्रीलिंग क्या होगा?", "options": ["मामी", "मौसी", "बुआ", "ताई"], "correctAnswer": "मामी"}
        ],
        "medium": [
            {"text": "संधि के कितने मुख्य भेद होते हैं?", "options": ["तीन (स्वर, व्यंजन, विसर्ग)", "दो", "चार", "पाँच"], "correctAnswer": "तीन (स्वर, व्यंजन, विसर्ग)"},
            {"text": "'यथाशक्ति' में कौन सा समास है?", "options": ["अव्ययीभाव", "तत्पुरुष", "द्वंद्व", "बहुव्रीहि"], "correctAnswer": "अव्ययीभाव"},
            {"text": "'नौ दो ग्यारह होना' मुहावरे का अर्थ है:", "options": ["भाग जाना", "गणित हल करना", "धोखा देना", "मिल जाना"], "correctAnswer": "भाग जाना"},
            {"text": "विशेषण के कितने भेद होते हैं?", "options": ["चार", "पाँच", "छह", "तीन"], "correctAnswer": "चार"},
            {"text": "संधि विच्छेद कीजिए: 'नरेश'", "options": ["नर + ईश", "न + रेश", "नरे + श", "नर + ऐश"], "correctAnswer": "नर + ईश"},
            {"text": "अलंकार पहचानें: 'कनक कनक ते सौ गुनी मादकता अधिकाय।'", "options": ["यमक अलंकार", "अनुप्रास अलंकार", "उपमा अलंकार", "रूपक अलंकार"], "correctAnswer": "यमक अलंकार"},
            {"text": "इनमें से कौन सा शब्द भाववाचक संज्ञा है?", "options": ["बचपन", "बच्चा", "खेलना", "मैदान"], "correctAnswer": "बचपन"},
            {"text": "जिस शब्द से किसी काम के करने या होने का पता चले, उसे कहते हैं:", "options": ["क्रिया", "संज्ञा", "सर्वनाम", "विशेषण"], "correctAnswer": "क्रिया"},
            {"text": "'अतिथि' का विलोम शब्द है:", "options": ["आतिथेय", "मेहमान", "शत्रु", "मित्र"], "correctAnswer": "आतिथेय"},
            {"text": "उपसर्ग पहचानें: 'अत्यधिक'", "options": ["अति", "अ", "अत्य", "अत्यध"], "correctAnswer": "अति"},
            {"text": "जो ईश्वर में विश्वास रखता हो, उसे कहते हैं:", "options": ["आस्तिक", "नास्तिक", "धार्मिक", "भगत"], "correctAnswer": "आस्तिक"},
            {"text": "वाक्य में 'करण कारक' की विभक्ति है:", "options": ["से (के द्वारा)", "ने", "को", "में"], "correctAnswer": "से (के द्वारा)"},
            {"text": "शुद्ध वाक्य पहचानें:", "options": ["राम ने खाना खाया।", "राम खाना खाया।", "राम ने खाना खाया है।", "राम ने खाना खा लिया।"], "correctAnswer": "राम ने खाना खाया।"},
            {"text": "'आँखों का तारा' मुहावरे का अर्थ है:", "options": ["बहुत प्यारा", "आँखों में दर्द", "आँख की पुतली", "बहुत दूर"], "correctAnswer": "बहुत प्यारा"},
            {"text": "सर्वनाम का प्रकार पहचानें: 'मैं'", "options": ["उत्तम पुरुष", "मध्यम पुरुष", "अन्य पुरुष", "निश्चयवाचक"], "correctAnswer": "उत्तम पुरुष"}
        ],
        "hard": [
            {"text": "'गजानन' में कौन सा समास है? (गज के समान आनन है जिसका - गणेश)", "options": ["बहुव्रीहि", "कर्मधारय", "अव्ययीभाव", "तत्पुरुष"], "correctAnswer": "बहुव्रीहि"},
            {"text": "नीचे दिए गए वाक्यों में से अशुद्ध वाक्य चुनें:", "options": ["मेरे को यह काम नहीं करना।", "मुझे यह काम नहीं करना।", "राम स्कूल जा रहा है।", "सीता खेल रही है।"], "correctAnswer": "मेरे को यह काम नहीं करना।"},
            {"text": "इनमें से कौन सा शब्द 'तत्सम' है?", "options": ["अग्नि", "आग", "सूरज", "काम"], "correctAnswer": "अग्नि"},
            {"text": "रस के कितने अंग होते हैं?", "options": ["चार (स्थायी भाव, विभाव, अनुभाव, संचारी भाव)", "नौ", "दस", "ग्यारह"], "correctAnswer": "चार (स्थायी भाव, विभाव, अनुभाव, संचारी भाव)"},
            {"text": "'सरोज' का संधि विच्छेद है:", "options": ["सरः + ज", "सर + ओज", "सरो + ज", "सर् + ओज"], "correctAnswer": "सरः + ज"},
            {"text": "अलंकार पहचानें: 'तरनि तनूजा तट तमाल तरुवर बहु छाए।'", "options": ["अनुप्रास अलंकार", "श्लेष अलंकार", "यमक अलंकार", "उपमा अलंकार"], "correctAnswer": "अनुप्रास अलंकार"},
            {"text": "वाच्य के कितने भेद होते हैं?", "options": ["तीन (कर्तृवाच्य, कर्मवाच्य, भाववाच्य)", "दो", "चार", "पाँच"], "correctAnswer": "तीन (कर्तृवाच्य, कर्मवाच्य, भाववाच्य)"},
            {"text": "'अंधे के हाथ बटेर लगना' लोकोक्ति का अर्थ है:", "options": ["बिना प्रयास के बड़ी वस्तु मिल जाना", "अंधे व्यक्ति का अमीर होना", "धोखा घड़ी करना", "भाग्य का साथ देना"], "correctAnswer": "बिना प्रयास के बड़ी वस्तु मिल जाना"},
            {"text": "प्रत्यय पहचानें: 'मिठास'", "options": ["आस", "स", "मीठा", "मिठ"], "correctAnswer": "आस"},
            {"text": "'कमल' शब्द का पर्यायवाची नहीं है:", "options": ["अंबुद", "पंकज", "राजीव", "नीरज"], "correctAnswer": "अंबुद"},
            {"text": "शांत रस का स्थायी भाव क्या है?", "options": ["निर्वेद", "उत्साह", "भय", "क्रोध"], "correctAnswer": "निर्वेद"},
            {"text": "जिस समास में दोनों पद प्रधान होते हैं, उसे कहते हैं:", "options": ["द्वंद्व समास", "तत्पुरुष समास", "कर्मधारय समास", "द्विगु समास"], "correctAnswer": "द्वंद्व समास"},
            {"text": "इनमें से कौन सा शब्द विशेषण है?", "options": ["सुंदर", "राम", "नदी", "खेलना"], "correctAnswer": "सुंदर"},
            {"text": "वाक्यों के अंग पहचानें:", "options": ["उद्देश्य और विधेय", "संज्ञा और सर्वनाम", "कर्ता और कर्म", "क्रिया और विशेषण"], "correctAnswer": "उद्देश्य और विधेय"},
            {"text": "'पवन' में कौन सी संधि है?", "options": ["अयादि संधि", "यण संधि", "गुण संधि", "दीर्घ संधि"], "correctAnswer": "अयादि संधि"}
        ]
    },
    "science": {
        "easy": [
            {"text": "What is the basic unit of living organisms?", "options": ["Cell", "Tissue", "Organ", "System"], "correctAnswer": "Cell"},
            {"text": "Which gas is necessary for breathing?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Methane"], "correctAnswer": "Oxygen"},
            {"text": "What is the process of changing liquid to gas called?", "options": ["Evaporation", "Condensation", "Melting", "Freezing"], "correctAnswer": "Evaporation"},
            {"text": "Which part of the plant prepares food?", "options": ["Leaf", "Stem", "Root", "Flower"], "correctAnswer": "Leaf"},
            {"text": "Light travels in which type of path?", "options": ["Straight line", "Curved line", "Zig-zag line", "Circular line"], "correctAnswer": "Straight line"},
            {"text": "Which vitamin deficiency causes Scurvy?", "options": ["Vitamin C", "Vitamin A", "Vitamin D", "Vitamin B"], "correctAnswer": "Vitamin C"},
            {"text": "Water boils at how many degrees Celsius?", "options": ["100°C", "0°C", "50°C", "110°C"], "correctAnswer": "100°C"},
            {"text": "Identify the primary source of light for Earth.", "options": ["The Sun", "The Moon", "Flashlight", "Fire"], "correctAnswer": "The Sun"},
            {"text": "Which of these is a non-living thing?", "options": ["Computer", "Dog", "Tree", "Bird"], "correctAnswer": "Computer"},
            {"text": "What do we call the green pigment in plants?", "options": ["Chlorophyll", "Hemoglobin", "Melanin", "Xanthophyll"], "correctAnswer": "Chlorophyll"},
            {"text": "Which instrument is used to measure temperature?", "options": ["Thermometer", "Barometer", "Anemometer", "Seismograph"], "correctAnswer": "Thermometer"},
            {"text": "How many states of matter are common on Earth?", "options": ["Three (Solid, Liquid, Gas)", "Two", "Four", "Five"], "correctAnswer": "Three (Solid, Liquid, Gas)"},
            {"text": "Which part of the respiratory system filters air?", "options": ["Nose/Nasal Cavity", "Lungs", "Stomach", "Heart"], "correctAnswer": "Nose/Nasal Cavity"},
            {"text": "A magnet attracts which material?", "options": ["Iron", "Wood", "Plastic", "Rubber"], "correctAnswer": "Iron"},
            {"text": "What is the force that pulls things down to Earth?", "options": ["Gravity", "Friction", "Magnetism", "Pressure"], "correctAnswer": "Gravity"}
        ],
        "medium": [
            {"text": "Which part of the flower attracts insects for pollination?", "options": ["Petals", "Sepals", "Stamen", "Pistil"], "correctAnswer": "Petals"},
            {"text": "Deficiency of Vitamin D causes which disease in children?", "options": ["Rickets", "Anemia", "Beriberi", "Scurvy"], "correctAnswer": "Rickets"},
            {"text": "What is the SI unit of electric current?", "options": ["Ampere", "Volt", "Ohm", "Watt"], "correctAnswer": "Ampere"},
            {"text": "Which component of blood helps in clotting?", "options": ["Platelets", "RBCs", "WBCs", "Plasma"], "correctAnswer": "Platelets"},
            {"text": "What type of reflection occurs from a mirror?", "options": ["Regular reflection", "Diffused reflection", "Total internal reflection", "Refraction"], "correctAnswer": "Regular reflection"},
            {"text": "Which part of our body handles the maximum chemical digestion?", "options": ["Small Intestine", "Stomach", "Mouth", "Large Intestine"], "correctAnswer": "Small Intestine"},
            {"text": "Sound travels fastest in which medium?", "options": ["Solids", "Liquids", "Gases", "Vacuum"], "correctAnswer": "Solids"},
            {"text": "Which animal has a four-chambered heart?", "options": ["Human", "Frog", "Snake", "Fish"], "correctAnswer": "Human"},
            {"text": "A solution that turns red litmus paper blue is:", "options": ["Basic", "Acidic", "Neutral", "Salty"], "correctAnswer": "Basic"},
            {"text": "What constitutes the 'master gland' of the endocrine system?", "options": ["Pituitary gland", "Thyroid gland", "Adrenal gland", "Pancreas"], "correctAnswer": "Pituitary gland"},
            {"text": "The process of loss of water vapor from the leaves of plants is called:", "options": ["Transpiration", "Respiration", "Photosynthesis", "Pollination"], "correctAnswer": "Transpiration"},
            {"text": "Which mirror is used as a rear-view mirror in vehicles?", "options": ["Convex mirror", "Concave mirror", "Plane mirror", "Parabolic mirror"], "correctAnswer": "Convex mirror"},
            {"text": "What is the chemical name of common salt?", "options": ["Sodium Chloride", "Sodium Bicarbonate", "Calcium Carbonate", "Magnesium Sulfate"], "correctAnswer": "Sodium Chloride"},
            {"text": "An earthquake's intensity is measured on which scale?", "options": ["Richter Scale", "Beaufort Scale", "Celsius Scale", "Meters"], "correctAnswer": "Richter Scale"},
            {"text": "What is the primary function of white blood cells (WBCs)?", "options": ["To fight infection", "To carry oxygen", "To digest food", "To give color to blood"], "correctAnswer": "To fight infection"}
        ],
        "hard": [
            {"text": "Identify the phenomenon where light bends when moving from one medium to another.", "options": ["Refraction", "Reflection", "Dispersion", "Diffraction"], "correctAnswer": "Refraction"},
            {"text": "Which organ filters metabolic wastes like urea from the blood?", "options": ["Kidneys", "Liver", "Lungs", "Lien (Spleen)"], "correctAnswer": "Kidneys"},
            {"text": "What is the name of the process by which glucose is broken down in the absence of oxygen?", "options": ["Anaerobic Respiration", "Aerobic Respiration", "Photosynthesis", "Fermentation"], "correctAnswer": "Anaerobic Respiration"},
            {"text": "In the human eye, where is the image formed?", "options": ["Retina", "Cornea", "Lens", "Iris"], "correctAnswer": "Retina"},
            {"text": "Who proposed the theory of evolution by natural selection?", "options": ["Charles Darwin", "Gregor Mendel", "Louis Pasteur", "Isaac Newton"], "correctAnswer": "Charles Darwin"},
            {"text": "What is the pH level of pure water?", "options": ["7", "0", "14", "1"], "correctAnswer": "7"},
            {"text": "Which metal is liquid at room temperature?", "options": ["Mercury", "Gallium", "Sodium", "Aluminum"], "correctAnswer": "Mercury"},
            {"text": "Ozone layer depletion is primarily caused by which chemical?", "options": ["Chlorofluorocarbons (CFCs)", "Carbon Dioxide", "Methane", "Sewage"], "correctAnswer": "Chlorofluorocarbons (CFCs)"},
            {"text": "What is the speed of light in vacuum?", "options": ["3 x 10^8 m/s", "3 x 10^10 m/s", "1000 m/s", "300,000 m/s"], "correctAnswer": "3 x 10^8 m/s"},
            {"text": "Which bond is formed by the sharing of electrons between atoms?", "options": ["Covalent bond", "Ionic bond", "Metallic bond", "Hydrogen bond"], "correctAnswer": "Covalent bond"},
            {"text": "What constitutes the 'PNS' (Peripheral Nervous System)?", "options": ["Nerves branching from brain and spinal cord", "Brain and Spinal Cord", "Heart and Blood Vessels", "Muscles and Bones"], "correctAnswer": "Nerves branching from brain and spinal cord"},
            {"text": "The hereditary material in most organisms is:", "options": ["DNA", "RNA", "Protein", "Lipid"], "correctAnswer": "DNA"},
            {"text": "What is the acceleration due to gravity on Earth's surface?", "options": ["9.8 m/s^2", "1.6 m/s^2", "10 cm/s^2", "0 m/s^2"], "correctAnswer": "9.8 m/s^2"},
            {"text": "Which enzyme in the saliva starts the digestion of starch?", "options": ["Amylase (Ptyalin)", "Pepsin", "Lipase", "Trypsin"], "correctAnswer": "Amylase (Ptyalin)"},
            {"text": "Identify the noble gas from these options.", "options": ["Argon", "Oxygen", "Nitrogen", "Hydrogen"], "correctAnswer": "Argon"}
        ]
    },
    "social-science": {
        "easy": [
            {"text": "Which is the largest planet in our solar system?", "options": ["Jupiter", "Saturn", "Jupiter", "Neptune"], "correctAnswer": "Jupiter"},
            {"text": "Which continent is known as the 'Dark Continent'?", "options": ["Africa", "Asia", "Europe", "Australia"], "correctAnswer": "Africa"},
            {"text": "Who was the first woman Prime Minister of India?", "options": ["Indira Gandhi", "Sarojini Naidu", "Sushma Swaraj", "Pratibha Patil"], "correctAnswer": "Indira Gandhi"},
            {"text": "A book of maps is called an:", "options": ["Atlas", "Alphabet", "Encyclopedia", "Dictionary"], "correctAnswer": "Atlas"},
            {"text": "Which imaginay line divides India into almost two equal halves?", "options": ["Tropic of Cancer", "Equator", "Prime Meridian", "Tropic of Capricorn"], "correctAnswer": "Tropic of Cancer"},
            {"text": "How many states are there in India currently?", "options": ["28", "29", "27", "25"], "correctAnswer": "28"},
            {"text": "Who is known as the 'Father of the Nation' in India?", "options": ["Mahatma Gandhi", "Jawaharlal Nehru", "Subhash Chandra Bose", "B.R. Ambedkar"], "correctAnswer": "Mahatma Gandhi"},
            {"text": "In which direction does the Sun rise?", "options": ["East", "West", "North", "South"], "correctAnswer": "East"},
            {"text": "Which is the longest river in India?", "options": ["Gunga", "Indus", "Brahmaputra", "Yamuna"], "correctAnswer": "Gunga"},
            {"text": "The Ashoka Chakra in the Indian Flag has how many spokes?", "options": ["24", "22", "26", "20"], "correctAnswer": "24"},
            {"text": "Which ocean is named after a country?", "options": ["Indian Ocean", "Pacific Ocean", "Atlantic Ocean", "Arctic Ocean"], "correctAnswer": "Indian Ocean"},
            {"text": "Who wrote the Indian Constitution?", "options": ["B.R. Ambedkar", "Rajendra Prasad", "Jawaharlal Nehru", "Sardar Patel"], "correctAnswer": "B.R. Ambedkar"},
            {"text": "Which city is known as the 'Pink City' of India?", "options": ["Jaipur", "Jodhpur", "Udaipur", "Bikaner"], "correctAnswer": "Jaipur"},
            {"text": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Rome"], "correctAnswer": "Paris"},
            {"text": "Which instrument is used to show directions?", "options": ["Compass", "Thermometer", "Scale", "Protractor"], "correctAnswer": "Compass"}
        ],
        "medium": [
            {"text": "The industrial revolution began in which country?", "options": ["Great Britain", "France", "Germany", "USA"], "correctAnswer": "Great Britain"},
            {"text": "Which mountain range separates Europe from Asia?", "options": ["Ural Mountains", "Himalayas", "Alps", "Andes"], "correctAnswer": "Ural Mountains"},
            {"text": "Who was the founder of the Mughal Empire in India?", "options": ["Babur", "Akbar", "Humayun", "Sher Shah Suri"], "correctAnswer": "Babur"},
            {"text": "Which layer of the atmosphere contains the ozone layer?", "options": ["Stratosphere", "Troposphere", "Mesosphere", "Thermosphere"], "correctAnswer": "Stratosphere"},
            {"text": "The 'Quit India Movement' was started in which year?", "options": ["1942", "1930", "1947", "1920"], "correctAnswer": "1942"},
            {"text": "Which planet is known as the 'Red Planet'?", "options": ["Mars", "Venus", "Mercury", "Saturn"], "correctAnswer": "Mars"},
            {"text": "What constitutes the 'Supreme Court' of India?", "options": ["Highest judicial court", "Parliament", "Cabinet", "Local court"], "correctAnswer": "Highest judicial court"},
            {"text": "Who was the chief architect of the Taj Mahal?", "options": ["Ustad Ahmad Lahauri", "Shah Jahan", "Mirza Ghiyas Beg", "Isar Khan"], "correctAnswer": "Ustad Ahmad Lahauri"},
            {"text": "Which is the smallest continent in the world?", "options": ["Australia", "Europe", "Antarctica", "South America"], "correctAnswer": "Australia"},
            {"text": "The 'Green Revolution' in India was primarily related to which crop?", "options": ["Wheat and Rice", "Cotton", "Tea", "Sugarcane"], "correctAnswer": "Wheat and Rice"},
            {"text": "Which imaginay line represents 0° longitude?", "options": ["Prime Meridian", "Equator", "International Date Line", "Tropic of Cancer"], "correctAnswer": "Prime Meridian"},
            {"text": "Who said 'Swaraj is my birthright and I shall have it'?", "options": ["Bal Gangadhar Tilak", "Lala Lajpat Rai", "Subhash Chandra Bose", "Gopal Krishna Gokhale"], "correctAnswer": "Bal Gangadhar Tilak"},
            {"text": "Which state in India has the highest literacy rate?", "options": ["Kerala", "Tamil Nadu", "Maharashtra", "Gujarat"], "correctAnswer": "Kerala"},
            {"text": "What is the tenure of the President of India?", "options": ["5 years", "6 years", "4 years", "Lifetime"], "correctAnswer": "5 years"},
            {"text": "The period of human history before writing was invented is called:", "options": ["Prehistory", "Ancient History", "Proto-history", "Medieval History"], "correctAnswer": "Prehistory"}
        ],
        "hard": [
            {"text": "In which session did the Indian National Congress pass the 'Purna Swaraj' resolution?", "options": ["Lahore Session (1929)", "Belgaum Session", "Calcutta Session", "Nagpur Session"], "correctAnswer": "Lahore Session (1929)"},
            {"text": "What constitutes the 'Third Estate' in pre-revolutionary France?", "options": ["Commoners (98% of population)", "Clergy", "Nobility", "Government officials"], "correctAnswer": "Commoners (98% of population)"},
            {"text": "The Deepest point on Earth, the Mariana Trench, is located in which ocean?", "options": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"], "correctAnswer": "Pacific Ocean"},
            {"text": "Who was the last Mughal Emperor of India?", "options": ["Bahadur Shah Zafar", "Aurangzeb", "Shah Alam II", "Muhammad Shah"], "correctAnswer": "Bahadur Shah Zafar"},
            {"text": "Which article of the Indian Constitution deals with the 'Abolition of Untouchability'?", "options": ["Article 17", "Article 14", "Article 19", "Article 21"], "correctAnswer": "Article 17"},
            {"text": "The concept of 'Separation of Powers' was proposed by which philosopher?", "options": ["Montesquieu", "Rousseau", "John Locke", "Voltaire"], "correctAnswer": "Montesquieu"},
            {"text": "Identify the type of rainfall caused when moisture-laden air is forced to rise over a mountain range.", "options": ["Orographic rainfall", "Convectional rainfall", "Cyclonic rainfall", "Frontal rainfall"], "correctAnswer": "Orographic rainfall"},
            {"text": "Who was the Viceroy of India during the partition of Bengal in 1905?", "options": ["Lord Curzon", "Lord Mountbatten", "Lord Dalhousie", "Lord Canning"], "correctAnswer": "Lord Curzon"},
            {"text": "What is the 'International Date Line'?", "options": ["An imaginary line at 180° longitude", "The Equator", "0° longitude", "Arctic Circle"], "correctAnswer": "An imaginary line at 180° longitude"},
            {"text": "Which fundamental right was called the 'Heart and Soul of the Constitution' by Dr. B.R. Ambedkar?", "options": ["Right to Constitutional Remedies", "Right to Equality", "Right to Freedom", "Right against Exploitation"], "correctAnswer": "Right to Constitutional Remedies"},
            {"text": "The Harappan civilization was first discovered in which year?", "options": ["1921", "1910", "1947", "1899"], "correctAnswer": "1921"},
            {"text": "What is 'Secularism' in the context of the Indian Constitution?", "options": ["State has no official religion and treats all equally", "State supports one religion", "State is against all religions", "State is ruled by religious leaders"], "correctAnswer": "State has no official religion and treats all equally"},
            {"text": "Which is the highest plateau in the world?", "options": ["Tibetan Plateau", "Deccan Plateau", "Colorado Plateau", "Bolivian Plateau"], "correctAnswer": "Tibetan Plateau"},
            {"text": "Who established the 'Servants of India Society'?", "options": ["Gopal Krishna Gokhale", "Mahatma Gandhi", "Annie Besant", "Jyotirao Phule"], "correctAnswer": "Gopal Krishna Gokhale"},
            {"text": "What causes 'Ocean Currents'?", "options": ["Wind, Earth's rotation, and Temperature/Salinity differences", "Tides only", "Moon's gravity only", "Ship movements"], "correctAnswer": "Wind, Earth's rotation, and Temperature/Salinity differences"}
        ]
    }
}

def main():
    bank_path = '/Users/arpan1.mukherjee/code/GhostMaze/public/AhirsAcademy/data/question_bank.json'
    
    with open(bank_path, 'r', encoding='utf-8') as f:
        question_bank = json.load(f)
        
    question_bank['class_7'] = class_7_data
    
    with open(bank_path, 'w', encoding='utf-8') as f:
        json.dump(question_bank, f, indent=4, ensure_ascii=False)
        
    print("Successfully injected 15 comprehensive questions per tier for Class 7!")

if __name__ == '__main__':
    main()
