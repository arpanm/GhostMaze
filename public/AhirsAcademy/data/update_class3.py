import json
import os

class_3_data = {
    "english": {
        "easy": [
            {"text": "Which word is a noun in the sentence: 'The happy dog barked loudly.'?", "options": ["Dog", "Happy", "Barked", "Loudly"], "correctAnswer": "Dog"},
            {"text": "What is the past tense form of 'eat'?", "options": ["Ate", "Eated", "Eating", "Eats"], "correctAnswer": "Ate"},
            {"text": "Identify the homophone for 'sea'.", "options": ["See", "She", "Say", "Saw"], "correctAnswer": "See"},
            {"text": "Which punctuation mark should end this sentence: 'Wow, that is amazing'", "options": ["Exclamation Mark (!)", "Full Stop (.)", "Question Mark (?)", "Comma (,)"], "correctAnswer": "Exclamation Mark (!)"},
            {"text": "Select the correct plural form of 'leaf'.", "options": ["Leaves", "Leafs", "Leefs", "Leves"], "correctAnswer": "Leaves"},
            {"text": "Which prefix can be added to the word 'happy' to make its opposite?", "options": ["Un-", "Dis-", "Re-", "Mis-"], "correctAnswer": "Un-"},
            {"text": "Identify the adjective in the following phrase: 'The tall building'.", "options": ["Tall", "The", "Building", "None"], "correctAnswer": "Tall"},
            {"text": "What does the abbreviation 'Dr.' stand for?", "options": ["Doctor", "Driver", "Director", "Drummer"], "correctAnswer": "Doctor"},
            {"text": "Choose the word with correct spelling.", "options": ["Surprise", "Suprise", "Surprize", "Supprise"], "correctAnswer": "Surprise"},
            {"text": "Which type of noun is 'London'?", "options": ["Proper Noun", "Common Noun", "Collective Noun", "Abstract Noun"], "correctAnswer": "Proper Noun"}
        ],
        "medium": [
            {"text": "Find the adverb in the sentence: 'The turtle moved slowly across the road.'", "options": ["Slowly", "Moved", "Across", "Road"], "correctAnswer": "Slowly"},
            {"text": "Identify the conjunction in the sentence: 'I like apples and bananas.'", "options": ["And", "I", "Like", "Apples"], "correctAnswer": "And"},
            {"text": "What is a synonym for 'Huge'?", "options": ["Gigantic", "Tiny", "Quick", "Clever"], "correctAnswer": "Gigantic"},
            {"text": "Which is the correct pronoun for the sentence: 'Rahul told _____ mother about the prize.'", "options": ["His", "Her", "Him", "He"], "correctAnswer": "His"},
            {"text": "Fill in the blank with the correct preposition: 'The book is placed _____ the table.'", "options": ["On", "In", "Under", "At"], "correctAnswer": "On"},
            {"text": "Which word is a collective noun?", "options": ["Flock", "Bird", "Sky", "Fly"], "correctAnswer": "Flock"},
            {"text": "What does the idiom 'Piece of cake' mean?", "options": ["Very easy", "A sweet dessert", "Something difficult", "A slice of food"], "correctAnswer": "Very easy"},
            {"text": "Complete the simile: 'As brave as a _____.'", "options": ["Lion", "Mouse", "Fox", "Bear"], "correctAnswer": "Lion"},
            {"text": "What tense is this sentence: 'She is reading a book.'?", "options": ["Present Continuous", "Simple Present", "Past Continuous", "Future Tense"], "correctAnswer": "Present Continuous"},
            {"text": "Which suffix can be added to the word 'Care' to make it an adjective?", "options": ["-ful", "-ness", "-ly", "-ment"], "correctAnswer": "-ful"}
        ],
        "hard": [
            {"text": "Identify the subject in the sentence: 'Under the old oak tree sat a wise owl.'", "options": ["A wise owl", "The old oak tree", "Under", "Sat"], "correctAnswer": "A wise owl"},
            {"text": "Which of the following sentences uses correct subject-verb agreement?", "options": ["The group of boys is playing outside.", "The group of boys are playing outside.", "The boys is playing outside.", "The boy are playing outside."], "correctAnswer": "The group of boys is playing outside."},
            {"text": "Find the abstract noun from the options below.", "options": ["Honesty", "Gold", "Teacher", "Mountain"], "correctAnswer": "Honesty"},
            {"text": "Change 'The cat chased the mouse' into passive voice.", "options": ["The mouse was chased by the cat.", "The mouse chases the cat.", "The mouse is being chased.", "The cat was chasing the mouse."], "correctAnswer": "The mouse was chased by the cat."},
            {"text": "What is the meaning of the prefix 'Re-' in 'Rewrite'?", "options": ["Again", "Not", "Before", "After"], "correctAnswer": "Again"},
            {"text": "Identify the tense: 'I had finished my homework before dinner.'", "options": ["Past Perfect", "Simple Past", "Present Perfect", "Past Continuous"], "correctAnswer": "Past Perfect"},
            {"text": "Choose the correct relative pronoun: 'This is the boy _____ won the race.'", "options": ["Who", "Which", "Whom", "Whose"], "correctAnswer": "Who"},
            {"text": "What does a biography mean?", "options": ["A book written about someone's life by another person.", "A book written by a person about their own life.", "A story about animals.", "A fiction book about space."], "correctAnswer": "A book written about someone's life by another person."},
            {"text": "Which of these is a compound sentence?", "options": ["It rained, so we played indoors.", "Playing indoors is fun.", "Because it rained, we stayed inside.", "The heavy rain stopped us from playing outside."], "correctAnswer": "It rained, so we played indoors."},
            {"text": "Identify the homograph (spelled same, different meaning/pronunciation) in these options.", "options": ["Tear", "Here / Hear", "See / Sea", "Right / Write"], "correctAnswer": "Tear"}
        ]
    },
    "maths": {
        "easy": [
            {"text": "What is 450 + 200?", "options": ["650", "470", "250", "600"], "correctAnswer": "650"},
            {"text": "Which number is formed by 5 thousands, 3 hundreds, and 8 ones?", "options": ["5308", "5038", "5380", "5830"], "correctAnswer": "5308"},
            {"text": "What comes just after 999?", "options": ["1000", "990", "1001", "1099"], "correctAnswer": "1000"},
            {"text": "What is 3 multiplied by 9?", "options": ["27", "24", "18", "30"], "correctAnswer": "27"},
            {"text": "How many minutes are there in 1 hour?", "options": ["60", "30", "120", "24"], "correctAnswer": "60"},
            {"text": "Which fraction represents one-fourth?", "options": ["1/4", "1/2", "3/4", "1/3"], "correctAnswer": "1/4"},
            {"text": "If you divide 20 candies equally among 4 children, how many does each child get?", "options": ["5", "4", "6", "10"], "correctAnswer": "5"},
            {"text": "What is 85 minus 25?", "options": ["60", "50", "70", "65"], "correctAnswer": "60"},
            {"text": "Which shape has 4 equal sides and 4 equal corners?", "options": ["Square", "Rectangle", "Rhombus", "Triangle"], "correctAnswer": "Square"},
            {"text": "How many days are there in a Leap Year?", "options": ["366", "365", "364", "360"], "correctAnswer": "366"}
        ],
        "medium": [
            {"text": "Convert 3 meters into centimeters.", "options": ["300 cm", "30 cm", "3000 cm", "3 cm"], "correctAnswer": "300 cm"},
            {"text": "What is 72 divided by 8?", "options": ["9", "8", "7", "6"], "correctAnswer": "9"},
            {"text": "If a movie starts at 2:15 PM and ends at 4:30 PM, how long did the movie last?", "options": ["2 hours 15 minutes", "2 hours", "1 hour 45 minutes", "2 hours 30 minutes"], "correctAnswer": "2 hours 15 minutes"},
            {"text": "Which fraction is bigger: 1/2 or 1/4?", "options": ["1/2", "1/4", "They are equal", "Cannot be determined"], "correctAnswer": "1/2"},
            {"text": "What is the product of 15 and 4?", "options": ["60", "50", "45", "55"], "correctAnswer": "60"},
            {"text": "Find the difference between 1000 and 456.", "options": ["544", "644", "444", "554"], "correctAnswer": "544"},
            {"text": "A box has 6 rows of chocolates, with 12 chocolates in each row. How many chocolates are there in total?", "options": ["72", "60", "48", "84"], "correctAnswer": "72"},
            {"text": "Identify the polygon with 6 straight sides.", "options": ["Hexagon", "Pentagon", "Octagon", "Heptagon"], "correctAnswer": "Hexagon"},
            {"text": "What is the sum of the place value and face value of '5' in the number 3524?", "options": ["505", "500", "5", "555"], "correctAnswer": "505"},
            {"text": "If 1 kg of apples costs Rs 80, how much will 2.5 kg cost?", "options": ["Rs 200", "Rs 160", "Rs 240", "Rs 180"], "correctAnswer": "Rs 200"}
        ],
        "hard": [
            {"text": "Which of these fractions is equivalent to 2/4?", "options": ["1/2", "2/8", "3/4", "4/8"], "correctAnswer": "1/2"},
            {"text": "If the perimeter of a square is 36 cm, what is the length of one side?", "options": ["9 cm", "6 cm", "12 cm", "18 cm"], "correctAnswer": "9 cm"},
            {"text": "Ravi leaves home at 7:50 AM. It takes him 35 minutes to reach school. At what time does he reach?", "options": ["8:25 AM", "8:15 AM", "8:35 AM", "8:20 AM"], "correctAnswer": "8:25 AM"},
            {"text": "What is the largest 4-digit number you can form using the digits 3, 8, 1, 9 without repeating?", "options": ["9831", "9138", "9813", "8931"], "correctAnswer": "9831"},
            {"text": "A bucket holds 15 liters of water. How many 500 ml mugs of water are needed to fill it entirely?", "options": ["30", "15", "20", "25"], "correctAnswer": "30"},
            {"text": "Divide 1500 by 50.", "options": ["30", "300", "3", "35"], "correctAnswer": "30"},
            {"text": "If a cube has 6 square faces, how many edges does it have?", "options": ["12", "8", "6", "16"], "correctAnswer": "12"},
            {"text": "Subtract Rs 45.50 from Rs 100.00.", "options": ["Rs 54.50", "Rs 64.50", "Rs 55.50", "Rs 44.50"], "correctAnswer": "Rs 54.50"},
            {"text": "Identify the next number in the sequence: 5, 11, 17, 23, ___?", "options": ["29", "28", "30", "27"], "correctAnswer": "29"},
            {"text": "Multiply 45 by 12.", "options": ["540", "480", "500", "560"], "correctAnswer": "540"}
        ]
    },
    "hindi": {
        "easy": [
            {"text": "हिंदी वर्णमाला में कुल कितने व्यंजन होते हैं?", "options": ["33", "11", "52", "25"], "correctAnswer": "33"},
            {"text": "'पवन' शब्द का क्या अर्थ है?", "options": ["हवा", "पानी", "आग", "आसमान"], "correctAnswer": "हवा"},
            {"text": "'किताब' का बहुवचन क्या होगा?", "options": ["किताबें", "किताबों", "किताबी", "किताब"], "correctAnswer": "किताबें"},
            {"text": "इनमें से कौन सा शब्द सर्वनाम है?", "options": ["वह", "राम", "सुंदर", "आना"], "correctAnswer": "वह"},
            {"text": "'दिन' का विलोम शब्द क्या है?", "options": ["रात", "सुबह", "शाम", "दोपहर"], "correctAnswer": "रात"},
            {"text": "गणतंत्र दिवस कब मनाया जाता है?", "options": ["26 जनवरी", "15 अगस्त", "2 अक्टूबर", "14 नवंबर"], "correctAnswer": "26 जनवरी"},
            {"text": "'शेर' शब्द का स्त्रीलिंग क्या होगा?", "options": ["शेरनी", "बाघिन", "मृगी", "मादा शेर"], "correctAnswer": "शेरनी"},
            {"text": "जो कपड़े सीलता है उसे क्या कहते हैं?", "options": ["दर्जी", "धोबी", "मोची", "सुनार"], "correctAnswer": "दर्जी"},
            {"text": "वाक्य पूरा करें: 'मोहन बाज़ार _____।' ", "options": ["गया", "गई", "गए", "जाती"], "correctAnswer": "गया"},
            {"text": "इनमें से कौन सा फल पीले रंग का होता है?", "options": ["केला", "सेब", "अनार", "अंगूर"], "correctAnswer": "केला"}
        ],
        "medium": [
            {"text": "'आसमान से बातें करना' मुहावरे का क्या अर्थ है?", "options": ["बहुत ऊंचा होना", "पागल हो जाना", "हवा में उड़ना", "असंभव काम करना"], "correctAnswer": "बहुत ऊंचा होना"},
            {"text": "संज्ञा के स्थान पर प्रयोग होने वाले शब्द क्या कहलाते हैं?", "options": ["सर्वनाम", "विशेषण", "क्रिया", "कारक"], "correctAnswer": "सर्वनाम"},
            {"text": "'अग्नि' का पर्यायवाची शब्द क्या है?", "options": ["आग", "पानी", "हवा", "धरती"], "correctAnswer": "आग"},
            {"text": "इनमें से कौन सा शब्द विशेषण नहीं है?", "options": ["घोड़ा", "सुंदर", "लाल", "बड़ा"], "correctAnswer": "घोड़ा"},
            {"text": "'कच्चा' शब्द का विलोम क्या होगा?", "options": ["पक्का", "अधूरा", "खराब", "गलत"], "correctAnswer": "पक्का"},
            {"text": "सही वर्तनी (Spelling) वाला शब्द चुनें।", "options": ["आशीर्वाद", "आशिर्वाद", "आशीर्बाद", "अशीर्वाद"], "correctAnswer": "आशीर्वाद"},
            {"text": "जो ईश्वर में विश्वास रखता हो, उसे क्या कहते हैं?", "options": ["आस्तिक", "नास्तिक", "धार्मिक", "संत"], "correctAnswer": "आस्तिक"},
            {"text": "कारक के कितने भेद होते हैं?", "options": ["8", "6", "5", "7"], "correctAnswer": "8"},
            {"text": "'नदी' का पर्यायवाची शब्द नहीं है?", "options": ["सरोवर", "सरिता", "तटिनी", "तरंगिणी"], "correctAnswer": "सरोवर"},
            {"text": "महात्मा गांधी जी का जन्म कहाँ हुआ था?", "options": ["पोरबंदर (गुजरात)", "अहमदाबाद", "दिल्ली", "राजकोट"], "correctAnswer": "पोरबंदर (गुजरात)"}
        ],
        "hard": [
            {"text": "क्रिया के जिस रूप से भूतकाल का बोध हो, उसे क्या कहते हैं?", "options": ["भूतकाल", "वर्तमान काल", "भविष्यत काल", "इनमें से कोई नहीं"], "correctAnswer": "भूतकाल"},
            {"text": "'नौ दो ग्यारह होना' मुहावरे का क्या अर्थ है?", "options": ["भाग जाना", "गणित हल करना", "धोखा देना", "मिलकर काम करना"], "correctAnswer": "भाग जाना"},
            {"text": "इनमें से कौन सा शब्द 'तत्सम' (संस्कृत का मूल शब्द) है?", "options": ["सूर्य", "सूरज", "आग", "काम"], "correctAnswer": "सूर्य"},
            {"text": "जो कभी बूढ़ा न हो, उसके लिए एक शब्द क्या होगा?", "options": ["अजर", "अमर", "अनंत", "देवता"], "correctAnswer": "अजर"},
            {"text": "वाक्य में जो शब्द काम का करना या होना बताते हैं, क्या कहलाते हैं?", "options": ["क्रिया", "कर्म", "कर्ता", "विशेषण"], "correctAnswer": "क्रिया"},
            {"text": "'अंधे की लकड़ी' मुहावरे का अर्थ क्या है?", "options": ["एकमात्र सहारा", "मारने की छड़ी", "अंधेरा होना", "बेकार की वस्तु"], "correctAnswer": "एकमात्र सहारा"},
            {"text": "संधि विच्छेद करें: 'विद्यालय' ", "options": ["विद्या + आलय", "विद्य + आलय", "विद्या + लय", "विद्या + आलयः"], "correctAnswer": "विद्या + आलय"},
            {"text": "इनमें से भाववाचक संज्ञा पहचानें।", "options": ["ईमानदारी", "राम", "नदी", "सोना"], "correctAnswer": "ईमानदारी"},
            {"text": "'कमल' का पर्यायवाची शब्द चुनिए।", "options": ["पंकज", "अंबुद", "पयोद", "गिरी"], "correctAnswer": "पंकज"},
            {"text": "विलोम शब्दों का सही जोड़ा पहचानें।", "options": ["आय - व्यय", "लाभ - नुकसानदायक", "मित्र - साथी", "प्रकाश - रोशनी"], "correctAnswer": "आय - व्यय"}
        ]
    },
    "evs": {
        "easy": [
            {"text": "Which organ helps us to breathe?", "options": ["Lungs", "Heart", "Stomach", "Brain"], "correctAnswer": "Lungs"},
            {"text": "What do plants need to make their food?", "options": ["Sunlight, Water, and Air", "Soil and Sugar", "Milk and Bread", "Animals and Rocks"], "correctAnswer": "Sunlight, Water, and Air"},
            {"text": "Which transport moves on water?", "options": ["Ship", "Train", "Aeroplane", "Bus"], "correctAnswer": "Ship"},
            {"text": "Which of these is a non-living thing?", "options": ["Rock", "Tree", "Dog", "Bird"], "correctAnswer": "Rock"},
            {"text": "What do we call the covering on a bird's body?", "options": ["Feathers", "Fur", "Scales", "Shell"], "correctAnswer": "Feathers"},
            {"text": "Which animal is kept as a pet?", "options": ["Dog", "Lion", "Tiger", "Bear"], "correctAnswer": "Dog"},
            {"text": "Where does a farmer grow crops?", "options": ["Field", "Hospital", "School", "Bank"], "correctAnswer": "Field"},
            {"text": "What does a postman do?", "options": ["Delivers letters", "Treats sick people", "Sews clothes", "Teaches children"], "correctAnswer": "Delivers letters"},
            {"text": "Which sense organ helps us taste our food?", "options": ["Tongue", "Nose", "Eyes", "Skin"], "correctAnswer": "Tongue"},
            {"text": "The Sun rises in which direction?", "options": ["East", "West", "North", "South"], "correctAnswer": "East"}
        ],
        "medium": [
            {"text": "What is the process by which a caterpillar turns into a butterfly called?", "options": ["Metamorphosis", "Photosynthesis", "Digestion", "Evaporation"], "correctAnswer": "Metamorphosis"},
            {"text": "We get wool mainly from which animal?", "options": ["Sheep", "Cow", "Horse", "Pig"], "correctAnswer": "Sheep"},
            {"text": "Which is the national animal of India?", "options": ["Tiger", "Lion", "Elephant", "Peacock"], "correctAnswer": "Tiger"},
            {"text": "What are the three main states of water?", "options": ["Solid, Liquid, Gas", "Hot, Cold, Warm", "Rain, Snow, Ice", "Fresh, Salty, Dirty"], "correctAnswer": "Solid, Liquid, Gas"},
            {"text": "Which part of the plant grows under the soil?", "options": ["Roots", "Stem", "Leaves", "Flowers"], "correctAnswer": "Roots"},
            {"text": "Who orbits around the Earth?", "options": ["The Moon", "The Sun", "Mars", "Jupiter"], "correctAnswer": "The Moon"},
            {"text": "Which of these foods is rich in protein?", "options": ["Eggs", "Rice", "Bread", "Sugar"], "correctAnswer": "Eggs"},
            {"text": "What type of house is made of snow and ice?", "options": ["Igloo", "Tent", "Caravan", "Hut"], "correctAnswer": "Igloo"},
            {"text": "A place where many animals and birds are kept for the public to see is called?", "options": ["Zoo", "Forest", "Desert", "Aquarium"], "correctAnswer": "Zoo"},
            {"text": "Which festival is known as the 'Festival of Lights'?", "options": ["Diwali", "Holi", "Eid", "Christmas"], "correctAnswer": "Diwali"}
        ],
        "hard": [
            {"text": "What is the name of the gas that plants take in during photosynthesis?", "options": ["Carbon Dioxide", "Oxygen", "Nitrogen", "Hydrogen"], "correctAnswer": "Carbon Dioxide"},
            {"text": "Which blood vessels carry blood away from the heart to the body?", "options": ["Arteries", "Veins", "Capillaries", "Nerves"], "correctAnswer": "Arteries"},
            {"text": "Identify the amphibian from the options given.", "options": ["Frog", "Snake", "Fish", "Turtle"], "correctAnswer": "Frog"},
            {"text": "What instrument is used to measure temperature?", "options": ["Thermometer", "Barometer", "Anemometer", "Stethoscope"], "correctAnswer": "Thermometer"},
            {"text": "Which planet is known as the 'Red Planet'?", "options": ["Mars", "Venus", "Jupiter", "Saturn"], "correctAnswer": "Mars"},
            {"text": "What is the hardest natural substance found on Earth?", "options": ["Diamond", "Gold", "Iron", "Coal"], "correctAnswer": "Diamond"},
            {"text": "Which organ in the human body is responsible for filtering blood and forming urine?", "options": ["Kidneys", "Liver", "Lungs", "Heart"], "correctAnswer": "Kidneys"},
            {"text": "What is a habitat?", "options": ["The natural environment where an organism lives", "A type of food", "A disease", "A part of a plant"], "correctAnswer": "The natural environment where an organism lives"},
            {"text": "In which season do trees typically shed their leaves?", "options": ["Autumn", "Spring", "Summer", "Winter"], "correctAnswer": "Autumn"},
            {"text": "What does a seismograph measure?", "options": ["Earthquakes", "Wind speed", "Rainfall", "Air pressure"], "correctAnswer": "Earthquakes"}
        ]
    }
}

def main():
    bank_path = '/Users/arpan1.mukherjee/code/GhostMaze/public/AhirsAcademy/data/question_bank.json'
    
    with open(bank_path, 'r', encoding='utf-8') as f:
        question_bank = json.load(f)
        
    question_bank['class_3'] = class_3_data
    
    with open(bank_path, 'w', encoding='utf-8') as f:
        json.dump(question_bank, f, indent=4, ensure_ascii=False)
        
    print("Successfully injected deep questions for Class 3 (English, Maths, Hindi, EVS)!")

if __name__ == '__main__':
    main()
