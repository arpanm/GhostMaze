import json
import os

BANK_PATH = '/Users/arpan1.mukherjee/code/GhostMaze/AhirsAcademy/data/question_bank.json'

def add_class_data(class_key, data):
    if not os.path.exists(BANK_PATH):
        bank = {}
    else:
        with open(BANK_PATH, 'r') as f:
            bank = json.load(f)
    
    bank[class_key] = data
    
    with open(BANK_PATH, 'w', encoding='utf-8') as f:
        json.dump(bank, f, indent=4, ensure_ascii=False)
    print(f"Added data for {class_key}")

# Class 1 Data
class_1_data = {
    "english": {
        "easy": [
            {"text": "A for ___?", "options": ["Apple", "Ball", "Cat", "Dog"], "correctAnswer": "Apple"},
            {"text": "B for ___?", "options": ["Ball", "Ant", "Egg", "Fish"], "correctAnswer": "Ball"},
            {"text": "C for ___?", "options": ["Cat", "Boy", "Fan", "Girl"], "correctAnswer": "Cat"},
            {"text": "D for ___?", "options": ["Dog", "Apple", "Ice", "Jar"], "correctAnswer": "Dog"},
            {"text": "E for ___?", "options": ["Egg", "Kite", "Lion", "Moon"], "correctAnswer": "Egg"},
            {"text": "Which is a fruit?", "options": ["Mango", "Table", "Pen", "Car"], "correctAnswer": "Mango"},
            {"text": "Which is a color?", "options": ["Red", "Book", "Chair", "Spoon"], "correctAnswer": "Red"},
            {"text": "Sun is in the ___.", "options": ["Sky", "Water", "Ground", "House"], "correctAnswer": "Sky"},
            {"text": "We see with our ___.", "options": ["Eyes", "Ears", "Nose", "Hands"], "correctAnswer": "Eyes"},
            {"text": "A cat says ___.", "options": ["Meow", "Woof", "Moo", "Quack"], "correctAnswer": "Meow"}
        ],
        "medium": [
            {"text": "Opposite of 'Big'?", "options": ["Small", "Hot", "Fast", "Up"], "correctAnswer": "Small"},
            {"text": "Plural of 'Boy'?", "options": ["Boys", "Boyes", "Boies", "Boyz"], "correctAnswer": "Boys"},
            {"text": "Which is an animal?", "options": ["Tiger", "Rose", "Pencil", "Cup"], "correctAnswer": "Tiger"},
            {"text": "A cow gives ___.", "options": ["Milk", "Eggs", "Honey", "Wool"], "correctAnswer": "Milk"},
            {"text": "Rainbow has ___ colors.", "options": ["7", "5", "10", "3"], "correctAnswer": "7"},
            {"text": "Opposite of 'Day'?", "options": ["Night", "Morning", "Evening", "Noon"], "correctAnswer": "Night"},
            {"text": "Which starts with 'S'?", "options": ["Sun", "Moon", "Star", "Both Sun & Star"], "correctAnswer": "Both Sun & Star"},
            {"text": "Elephant is a ___ animal.", "options": ["Big", "Small", "Tiny", "Short"], "correctAnswer": "Big"},
            {"text": "We eat with our ___.", "options": ["Mouth", "Eyes", "Ears", "Nose"], "correctAnswer": "Mouth"},
            {"text": "Birds ___ in the sky.", "options": ["Fly", "Swim", "Run", "Walk"], "correctAnswer": "Fly"}
        ],
        "hard": [
            {"text": "Which is a vowel?", "options": ["A", "B", "C", "D"], "correctAnswer": "A"},
            {"text": "Plural of 'Apple'?", "options": ["Apples", "Appless", "Applies", "Apple"], "correctAnswer": "Apples"},
            {"text": "Identify the bird.", "options": ["Parrot", "Lion", "Fish", "Snake"], "correctAnswer": "Parrot"},
            {"text": "Which is a transport?", "options": ["Car", "Chair", "Tree", "Flower"], "correctAnswer": "Car"},
            {"text": "Our national fruit is ___.", "options": ["Mango", "Apple", "Banana", "Orange"], "correctAnswer": "Mango"},
            {"text": "Opposite of 'Happy'?", "options": ["Sad", "Angry", "Fast", "Cold"], "correctAnswer": "Sad"},
            {"text": "Which month has 28 days?", "options": ["February", "January", "March", "April"], "correctAnswer": "February"},
            {"text": "Spider has ___ legs.", "options": ["8", "6", "4", "2"], "correctAnswer": "8"},
            {"text": "Sun rises in the ___.", "options": ["East", "West", "North", "South"], "correctAnswer": "East"},
            {"text": "A baby dog is a ___.", "options": ["Puppy", "Kitten", "Calf", "Kid"], "correctAnswer": "Puppy"}
        ]
    },
    "maths": {
        "easy": [
            {"text": "1 + 1 = ?", "options": ["2", "1", "3", "4"], "correctAnswer": "2"},
            {"text": "2 + 2 = ?", "options": ["4", "3", "5", "6"], "correctAnswer": "4"},
            {"text": "What comes after 5?", "options": ["6", "4", "7", "8"], "correctAnswer": "6"},
            {"text": "Which is bigger: 10 or 2?", "options": ["10", "2", "Equal", "None"], "correctAnswer": "10"},
            {"text": "3 - 1 = ?", "options": ["2", "1", "3", "0"], "correctAnswer": "2"},
            {"text": "How many fingers in one hand?", "options": ["5", "4", "6", "10"], "correctAnswer": "5"},
            {"text": "0 + 5 = ?", "options": ["5", "0", "50", "1"], "correctAnswer": "5"},
            {"text": "What is 10 + 0?", "options": ["10", "0", "1", "100"], "correctAnswer": "10"},
            {"text": "A triangle has ___ sides.", "options": ["3", "4", "2", "5"], "correctAnswer": "3"},
            {"text": "A square has ___ corners.", "options": ["4", "3", "5", "6"], "correctAnswer": "4"}
        ],
        "medium": [
            {"text": "5 + 5 = ?", "options": ["10", "5", "15", "20"], "correctAnswer": "10"},
            {"text": "10 - 2 = ?", "options": ["8", "7", "9", "6"], "correctAnswer": "8"},
            {"text": "Which is smaller: 15 or 50?", "options": ["15", "50", "Equal", "None"], "correctAnswer": "15"},
            {"text": "What is 2 \u00d7 2?", "options": ["4", "2", "6", "8"], "correctAnswer": "4"},
            {"text": "A week has ___ days.", "options": ["7", "5", "6", "10"], "correctAnswer": "7"},
            {"text": "What comes before 20?", "options": ["19", "21", "18", "22"], "correctAnswer": "19"},
            {"text": "6 + 4 = ?", "options": ["10", "9", "11", "12"], "correctAnswer": "10"},
            {"text": "What is 3 + 3 + 3?", "options": ["9", "6", "12", "3"], "correctAnswer": "9"},
            {"text": "A circle is ___.", "options": ["Round", "Square", "Flat", "Long"], "correctAnswer": "Round"},
            {"text": "Which number is even?", "options": ["2", "3", "5", "7"], "correctAnswer": "2"}
        ],
        "hard": [
            {"text": "10 + 10 = ?", "options": ["20", "15", "25", "30"], "correctAnswer": "20"},
            {"text": "20 - 10 = ?", "options": ["10", "5", "15", "0"], "correctAnswer": "10"},
            {"text": "What is 5 \u00d7 2?", "options": ["10", "7", "5", "15"], "correctAnswer": "10"},
            {"text": "How many months in a year?", "options": ["12", "10", "11", "13"], "correctAnswer": "12"},
            {"text": "Next number in 2, 4, 6, ___?", "options": ["8", "7", "10", "9"], "correctAnswer": "8"},
            {"text": "15 + 5 = ?", "options": ["20", "15", "25", "10"], "correctAnswer": "20"},
            {"text": "A year has ___ days usually.", "options": ["365", "366", "300", "400"], "correctAnswer": "365"},
            {"text": "Half of 10 is ___.", "options": ["5", "2", "4", "3"], "correctAnswer": "5"},
            {"text": "What is 10 \u00f7 2?", "options": ["5", "2", "10", "4"], "correctAnswer": "5"},
            {"text": "Which is is the smallest: 10, 5, 20?", "options": ["5", "10", "20", "None"], "correctAnswer": "5"}
        ]
    },
    "hindi": {
        "easy": [
            {"text": "'आम' क्या है?", "options": ["फल", "सब्जी", "पक्षी", "पानी"], "correctAnswer": "फल"},
            {"text": "भारत की राजधानी?", "options": ["दिल्ली", "मुंबई", "आगरा", "पटना"], "correctAnswer": "दिल्ली"},
            {"text": "सूरज किधर से निकलता है?", "options": ["पूर्व", "पश्चिम", "उत्तर", "दक्षिण"], "correctAnswer": "पूर्व"},
            {"text": "'कल' का विलोम?", "options": ["आज", "परसों", "अतीत", "बाद"], "correctAnswer": "आज"},
            {"text": "हमारा राष्ट्रीय पक्षी?", "options": ["मोर", "तोता", "कौआ", "चिड़िया"], "correctAnswer": "मोर"},
            {"text": "'पानी' का पर्यायवाची?", "options": ["जल", "आग", "हवा", "मिट्टी"], "correctAnswer": "जल"},
            {"text": "अनार किस रंग का होता है?", "options": ["लाल", "पीला", "नीला", "हरा"], "correctAnswer": "लाल"},
            {"text": "आसमान का रंग?", "options": ["नीला", "पीला", "सफ़ेद", "काला"], "correctAnswer": "नीला"},
            {"text": "मछली कहाँ रहती है?", "options": ["पानी में", "जमीन पर", "आसमान में", "घर में"], "correctAnswer": "पानी में"},
            {"text": "गाय हमें क्या देती है?", "options": ["दूध", "अंडा", "फल", "सब्जी"], "correctAnswer": "दूध"}
        ],
        "medium": [
            {"text": "'बड़ा' का विलोम?", "options": ["छोटा", "आज", "लंबा", "मोटा"], "correctAnswer": "छोटा"},
            {"text": "'माता' का पर्यायवाची?", "options": ["माँ", "पिता", "भाई", "बहन"], "correctAnswer": "माँ"},
            {"text": "सप्ताह में कितने दिन?", "options": ["7", "5", "6", "10"], "correctAnswer": "7"},
            {"text": "'हवा' का पर्यायवाची?", "options": ["वायु", "जल", "आग", "धरती"], "correctAnswer": "वायु"},
            {"text": "'दिन' का विलोम?", "options": ["रात", "सुबह", "शाम", "दोपहर"], "correctAnswer": "रात"},
            {"text": "'पेड़' हमें क्या देते हैं?", "options": ["फल/ऑक्सीजन", "पानी", "आग", "मिट्टी"], "correctAnswer": "फल/ऑक्सीजन"},
            {"text": "'साहस' का अर्थ?", "options": ["हिम्मत", "डर", "गुस्सा", "दुःख"], "correctAnswer": "हिम्मत"},
            {"text": "'दोस्त' का विलोम?", "options": ["दुश्मन", "भाई", "साथी", "गुरु"], "correctAnswer": "दुश्मन"},
            {"text": "मोर नाचता है, कोयल ___ है।", "options": ["कूकती", "भौंकती", "चिल्लाती", "रोती"], "correctAnswer": "कूकती"},
            {"text": "'घर' का पर्यायवाची?", "options": ["आलय", "भोजन", "पानी", "आग"], "correctAnswer": "आलय"}
        ],
        "hard": [
            {"text": "सं संज्ञा के कितने मुख्य भेद?", "options": ["3", "5", "4", "2"], "correctAnswer": "3"},
            {"text": "'सच' का विलोम?", "options": ["झूठ", "गलत", "पाप", "आज"], "correctAnswer": "झूठ"},
            {"text": "'चाँद' का पर्यायवाची?", "options": ["शशि", "सूर्य", "नभ", "धरा"], "correctAnswer": "शशि"},
            {"text": "'९-२-११ होना'?", "options": ["भाग जाना", "पकड़ना", "खेलना", "पढ़ना"], "correctAnswer": "भाग जाना"},
            {"text": "विशेषण किसकी विशेषता बताता है?", "options": ["संज्ञा/सर्वनाम", "क्रिया", "नाम", "काम"], "correctAnswer": "संज्ञा/सर्वनाम"},
            {"text": "'आँख का तारा' अर्थ?", "options": ["बहुत प्यारा", "दुश्मन", "अंधा", "कम दिखना"], "correctAnswer": "बहुत प्यारा"},
            {"text": "'फूल' का पर्यायवाची नहीं है:", "options": ["जल", "पुष्प", "सुमन", "कुसुम"], "correctAnswer": "जल"},
            {"text": "'ईमानदार' का विलोम?", "options": ["बेईमान", "झूठा", "चोर", "बुरा"], "correctAnswer": "बेईमान"},
            {"text": "'वीर' का स्त्रीलिंग?", "options": ["वीरांगना", "माता", "बहन", "स्त्री"], "correctAnswer": "वीरांगना"},
            {"text": "सर्वनाम के कितने भेद?", "options": ["6", "4", "5", "7"], "correctAnswer": "6"}
        ]
    },
    "science": {
        "easy": [
            {"text": "We see with our ___.", "options": ["Eyes", "Ears", "Nose", "Hands"], "correctAnswer": "Eyes"},
            {"text": "We hear with our ___.", "options": ["Ears", "Eyes", "Nose", "Hands"], "correctAnswer": "Ears"},
            {"text": "We smell with our ___.", "options": ["Nose", "Eyes", "Ears", "Hands"], "correctAnswer": "Nose"},
            {"text": "Which is a living thing?", "options": ["Plant", "Rock", "Toy", "Pen"], "correctAnswer": "Plant"},
            {"text": "Which is non-living?", "options": ["Rock", "Cat", "Dog", "Tree"], "correctAnswer": "Rock"},
            {"text": "Part of a flower?", "options": ["Petal", "Stem", "Leaf", "Root"], "correctAnswer": "Petal"},
            {"text": "Grows on a tree?", "options": ["Fruit", "Stone", "Cloud", "Sun"], "correctAnswer": "Fruit"},
            {"text": "Lives in water?", "options": ["Fish", "Bird", "Cat", "Cow"], "correctAnswer": "Fish"},
            {"text": "A flying animal?", "options": ["Bird", "Fish", "Dog", "Ant"], "correctAnswer": "Bird"},
            {"text": "Smallest part of life?", "options": ["Cell", "Bone", "Hair", "Nail"], "correctAnswer": "Cell"}
        ],
        "medium": [
            {"text": "Baby of a cow?", "options": ["Calf", "Puppy", "Kitten", "Chick"], "correctAnswer": "Calf"},
            {"text": "Food gives us ___.", "options": ["Energy", "Sleep", "Water", "Air"], "correctAnswer": "Energy"},
            {"text": "Rain comes from ___.", "options": ["Clouds", "Sun", "Moon", "Stars"], "correctAnswer": "Clouds"},
            {"text": "Part of a tree trunk?", "options": ["Bark", "Leaf", "Fruit", "Root"], "correctAnswer": "Bark"},
            {"text": "Animal with a trunk?", "options": ["Elephant", "Lion", "Tiger", "Bear"], "correctAnswer": "Elephant"},
            {"text": "We wear wool in ___.", "options": ["Winter", "Summer", "Rain", "Autumn"], "correctAnswer": "Winter"},
            {"text": "Seeds grow into ___.", "options": ["Plants", "Stones", "Clouds", "Rivers"], "correctAnswer": "Plants"},
            {"text": "Sun gives us ___.", "options": ["Light", "Water", "Food", "Air"], "correctAnswer": "Light"},
            {"text": "Moon appears at ___.", "options": ["Night", "Day", "Noon", "Morning"], "correctAnswer": "Night"},
            {"text": "Fish breathe with ___.", "options": ["Gills", "Lungs", "Nose", "Skin"], "correctAnswer": "Gills"}
        ],
        "hard": [
            {"text": "Roots grow ___.", "options": ["Underground", "Above ground", "On leaves", "In fruits"], "correctAnswer": "Underground"},
            {"text": "Green pigment in plants?", "options": ["Chlorophyll", "Water", "Air", "Light"], "correctAnswer": "Chlorophyll"},
            {"text": "Insect with 6 legs?", "options": ["Ant", "Spider", "Dog", "Bird"], "correctAnswer": "Ant"},
            {"text": "Animal with a long neck?", "options": ["Giraffe", "Lion", "Zebra", "Hippo"], "correctAnswer": "Giraffe"},
            {"text": "Spiders have ___ legs.", "options": ["8", "6", "4", "2"], "correctAnswer": "8"},
            {"text": "We get honey from ___.", "options": ["Bees", "Ants", "Flies", "Worms"], "correctAnswer": "Bees"},
            {"text": "King of Fruits in India?", "options": ["Mango", "Apple", "Banana", "Orange"], "correctAnswer": "Mango"},
            {"text": "Fastest land animal?", "options": ["Cheetah", "Lion", "Horse", "Deer"], "correctAnswer": "Cheetah"},
            {"text": "Water is a ___.", "options": ["Liquid", "Solid", "Gas", "None"], "correctAnswer": "Liquid"},
            {"text": "Air is ___.", "options": ["Everywhere", "Nowhere", "Only in sky", "Only in sea"], "correctAnswer": "Everywhere"}
        ]
    },
    "social-science": {
        "easy": [
            {"text": "My country is ___.", "options": ["India", "USA", "China", "Japan"], "correctAnswer": "India"},
            {"text": "Red Planet is ___.", "options": ["Mars", "Venus", "Earth", "Saturn"], "correctAnswer": "Mars"},
            {"text": "National Bird of India?", "options": ["Peacock", "Parrot", "Eagle", "Hen"], "correctAnswer": "Peacock"},
            {"text": "National Animal of India?", "options": ["Tiger", "Lion", "Elephant", "Horse"], "correctAnswer": "Tiger"},
            {"text": "National Flower of India?", "options": ["Lotus", "Rose", "Lily", "Sunflower"], "correctAnswer": "Lotus"},
            {"text": "Capital of India?", "options": ["New Delhi", "Mumbai", "Chennai", "Kolkata"], "correctAnswer": "New Delhi"},
            {"text": "Colors in Indian Flag?", "options": ["3", "4", "2", "5"], "correctAnswer": "3"},
            {"text": "We live on Planet ___.", "options": ["Earth", "Mars", "Moon", "Sun"], "correctAnswer": "Earth"},
            {"text": "Father of the Nation?", "options": ["Mahatma Gandhi", "Nehru", "Patel", "Bose"], "correctAnswer": "Mahatma Gandhi"},
            {"text": "Largest country by population?", "options": ["India", "China", "USA", "Russia"], "correctAnswer": "India"}
        ],
        "medium": [
            {"text": "National Anthem of India?", "options": ["Jana Gana Mana", "Vande Mataram", "Sare Jahan Se", "National Day"], "correctAnswer": "Jana Gana Mana"},
            {"text": "National Song of India?", "options": ["Vande Mataram", "Jana Gana Mana", "Hymn", "Prayer"], "correctAnswer": "Vande Mataram"},
            {"text": "Festival of Colors?", "options": ["Holi", "Diwali", "Eid", "Christmas"], "correctAnswer": "Holi"},
            {"text": "Festival of Lights?", "options": ["Diwali", "Holi", "Lohri", "Onam"], "correctAnswer": "Diwali"},
            {"text": "Gandhi Jayanti date?", "options": ["Oct 2", "Aug 15", "Jan 26", "Nov 14"], "correctAnswer": "Oct 2"},
            {"text": "Children's Day date?", "options": ["Nov 14", "Oct 2", "Jan 26", "Aug 15"], "correctAnswer": "Nov 14"},
            {"text": "Republic Day of India?", "options": ["Jan 26", "Aug 15", "Oct 2", "Nov 14"], "correctAnswer": "Jan 26"},
            {"text": "Independence Day of India?", "options": ["Aug 15", "Jan 26", "Oct 2", "Nov 14"], "correctAnswer": "Aug 15"},
            {"text": "First PM of India?", "options": ["Jawaharlal Nehru", "Indira Gandhi", "Modi", "Rajiv Gandhi"], "correctAnswer": "Jawaharlal Nehru"},
            {"text": "First President of India?", "options": ["Dr. Rajendra Prasad", "Dr. Kalam", "Radhakrishnan", "None"], "correctAnswer": "Dr. Rajendra Prasad"}
        ],
        "hard": [
            {"text": "National Fruit of India?", "options": ["Mango", "Apple", "Grapes", "Orange"], "correctAnswer": "Mango"},
            {"text": "National Tree of India?", "options": ["Banyan", "Peepal", "Neem", "Mango"], "correctAnswer": "Banyan"},
            {"text": "National River of India?", "options": ["Ganga", "Yamuna", "Godavari", "Narmada"], "correctAnswer": "Ganga"},
            {"text": "Blue color circle in flag?", "options": ["Ashoka Chakra", "Moon", "Sun", "Wheel"], "correctAnswer": "Ashoka Chakra"},
            {"text": "Spokes in Ashoka Chakra?", "options": ["24", "20", "22", "26"], "correctAnswer": "24"},
            {"text": "Highest Peak in the world?", "options": ["Mt. Everest", "K2", "Kanchanjunga", "Lhotse"], "correctAnswer": "Mt. Everest"},
            {"text": "Indian Flag name?", "options": ["Tiranga", "Flag", "Banner", "Standard"], "correctAnswer": "Tiranga"},
            {"text": "Who wrote national anthem?", "options": ["Rabindranath Tagore", "Bankim Chandra", "Sarojini Naidu", "Nehru"], "correctAnswer": "Rabindranath Tagore"},
            {"text": "Who wrote national song?", "options": ["Bankim Chandra", "Tagore", "Premchand", "Laxmi"], "correctAnswer": "Bankim Chandra"},
            {"text": "Currency of India?", "options": ["Rupee", "Dollar", "Pound", "Euro"], "correctAnswer": "Rupee"}
        ]
    }
}

# Class 2 Data
class_2_data = {
    "english": {
        "easy": [
            {"text": "Identify the noun: 'The dog barked'.", "options": ["dog", "barked", "The", "is"], "correctAnswer": "dog"},
            {"text": "Opposite of 'Cold'?", "options": ["Hot", "Fast", "Up", "Sad"], "correctAnswer": "Hot"},
            {"text": "Plural of 'Cat'?", "options": ["Cats", "Cates", "Catis", "Cat"], "correctAnswer": "Cats"},
            {"text": "Identify the pronoun: 'He is my friend'.", "options": ["He", "is", "my", "friend"], "correctAnswer": "He"},
            {"text": "Which word is a verb?", "options": ["Run", "Red", "Boy", "Fast"], "correctAnswer": "Run"},
            {"text": "A rose is a ___.", "options": ["Flower", "Fruit", "Animal", "Bird"], "correctAnswer": "Flower"},
            {"text": "Which is a body part?", "options": ["Hand", "Pen", "Cup", "Ball"], "correctAnswer": "Hand"},
            {"text": "The moon shines at ___.", "options": ["Night", "Day", "Morning", "Evening"], "correctAnswer": "Night"},
            {"text": "A lion lives in a ___.", "options": ["Den", "Nest", "Shed", "Pond"], "correctAnswer": "Den"},
            {"text": "Identify the color.", "options": ["Blue", "Book", "Run", "Eat"], "correctAnswer": "Blue"}
        ],
        "medium": [
            {"text": "Use 'a' or 'an': ___ apple.", "options": ["An", "A", "The", "Some"], "correctAnswer": "An"},
            {"text": "Opposite of 'Fast'?", "options": ["Slow", "Hot", "Up", "Big"], "correctAnswer": "Slow"},
            {"text": "Which is a 'Proper Noun'?", "options": ["India", "Country", "Boy", "City"], "correctAnswer": "India"},
            {"text": "Plural of 'Bus'?", "options": ["Buses", "Buss", "Busies", "Bus"], "correctAnswer": "Buses"},
            {"text": "Past tense of 'Play'?", "options": ["Played", "Playes", "Playing", "Play"], "correctAnswer": "Played"},
            {"text": "Identify the adjective: 'The big ball'.", "options": ["big", "ball", "The", "is"], "correctAnswer": "big"},
            {"text": "A bird lives in a ___.", "options": ["Nest", "Den", "Stable", "Kennel"], "correctAnswer": "Nest"},
            {"text": "Identify the animal.", "options": ["Giraffe", "Rose", "Pen", "Apple"], "correctAnswer": "Giraffe"},
            {"text": "Opposite of 'Old'?", "options": ["Young", "Big", "Strong", "Fast"], "correctAnswer": "Young"},
            {"text": "Which is a preposition?", "options": ["On", "Run", "Slow", "Boy"], "correctAnswer": "On"}
        ],
        "hard": [
            {"text": "Correct spelling?", "options": ["Elephant", "Elefant", "Elefent", "Elaphant"], "correctAnswer": "Elephant"},
            {"text": "Identify the conjunction.", "options": ["And", "Run", "Big", "On"], "correctAnswer": "And"},
            {"text": "Which is an abstract noun?", "options": ["Kindness", "Table", "Dog", "Delhi"], "correctAnswer": "Kindness"},
            {"text": "Meaning of 'Humble'?", "options": ["Modest/Polite", "Proud", "Angry", "Fast"], "correctAnswer": "Modest/Polite"},
            {"text": "Identify the Verb.", "options": ["Jump", "Blue", "Sweet", "Under"], "correctAnswer": "Jump"},
            {"text": "Antonym of 'Smooth'?", "options": ["Rough", "Soft", "Hard", "Big"], "correctAnswer": "Rough"},
            {"text": "A group of keys is a ___.", "options": ["Bunch", "Pack", "Flock", "Herd"], "correctAnswer": "Bunch"},
            {"text": "Identify the pronoun: 'They went to school'.", "options": ["They", "went", "to", "school"], "correctAnswer": "They"},
            {"text": "Past tense of 'Go'?", "options": ["Went", "Gone", "Goes", "Going"], "correctAnswer": "Went"},
            {"text": "Which is a 'Neuter' gender noun?", "options": ["Pencil", "Man", "Maid", "Uncle"], "correctAnswer": "Pencil"}
        ]
    },
    "maths": {
        "easy": [
            {"text": "2 + 3 = ?", "options": ["5", "4", "6", "3"], "correctAnswer": "5"},
            {"text": "5 - 2 = ?", "options": ["3", "2", "4", "1"], "correctAnswer": "3"},
            {"text": "What is 10 + 5?", "options": ["15", "10", "20", "5"], "correctAnswer": "15"},
            {"text": "Which is larger: 25 or 52?", "options": ["52", "25", "Equal", "None"], "correctAnswer": "52"},
            {"text": "4 \u00d7 2 = ?", "options": ["8", "6", "4", "10"], "correctAnswer": "8"},
            {"text": "Half of 20 is ___.", "options": ["10", "5", "15", "2"], "correctAnswer": "10"},
            {"text": "6 + 6 = ?", "options": ["12", "10", "15", "18"], "correctAnswer": "12"},
            {"text": "9 - 4 = ?", "options": ["5", "3", "4", "6"], "correctAnswer": "5"},
            {"text": "Count corners in a triangle.", "options": ["3", "4", "2", "5"], "correctAnswer": "3"},
            {"text": "What is 0 \u00d7 10?", "options": ["0", "10", "1", "100"], "correctAnswer": "0"}
        ],
        "medium": [
            {"text": "10 + 20 = ?", "options": ["30", "20", "40", "10"], "correctAnswer": "30"},
            {"text": "50 - 10 = ?", "options": ["40", "30", "50", "60"], "correctAnswer": "40"},
            {"text": "LCM of 2 and 4?", "options": ["4", "2", "6", "8"], "correctAnswer": "4"},
            {"text": "What is 5 \u00d7 3?", "options": ["15", "10", "20", "25"], "correctAnswer": "15"},
            {"text": "How many days in 2 weeks?", "options": ["14", "7", "10", "12"], "correctAnswer": "14"},
            {"text": "Next number: 5, 10, 15, ___?", "options": ["20", "18", "25", "22"], "correctAnswer": "20"},
            {"text": "12 + 8 = ?", "options": ["20", "18", "22", "10"], "correctAnswer": "20"},
            {"text": "What is half of 50?", "options": ["25", "15", "20", "10"], "correctAnswer": "25"},
            {"text": "A year has ___ seasons usually.", "options": ["4", "3", "5", "2"], "correctAnswer": "4"},
            {"text": "Which number is odd?", "options": ["5", "4", "6", "8"], "correctAnswer": "5"}
        ],
        "hard": [
            {"text": "100 - 50 = ?", "options": ["50", "40", "60", "30"], "correctAnswer": "50"},
            {"text": "Solve: 2 + 3 \u00d7 2", "options": ["8", "10", "7", "12"], "correctAnswer": "8"},
            {"text": "What is 10 \u00f7 5?", "options": ["2", "5", "10", "1"], "correctAnswer": "2"},
            {"text": "Quarter of 100?", "options": ["25", "50", "75", "10"], "correctAnswer": "25"},
            {"text": "Smallest 3-digit number?", "options": ["100", "101", "111", "900"], "correctAnswer": "100"},
            {"text": "Sum of 25 + 25?", "options": ["50", "40", "45", "60"], "correctAnswer": "50"},
            {"text": "How many faces in a cube?", "options": ["6", "4", "8", "12"], "correctAnswer": "6"},
            {"text": "Next number in 10, 20, 30, ___?", "options": ["40", "35", "50", "45"], "correctAnswer": "40"},
            {"text": "What is 20 \u00d7 4?", "options": ["80", "60", "100", "40"], "correctAnswer": "80"},
            {"text": "HCF of 4 and 8?", "options": ["4", "2", "8", "1"], "correctAnswer": "4"}
        ]
    },
    "science": {
        "easy": [
            {"text": "Plant that grows in the desert?", "options": ["Cactus", "Mango", "Apple", "Rose"], "correctAnswer": "Cactus"},
            {"text": "Animal that gives us wool?", "options": ["Sheep", "Lion", "Tiger", "Dog"], "correctAnswer": "Sheep"},
            {"text": "Eyelashes protect our ___.", "options": ["Eyes", "Ears", "Nose", "Hands"], "correctAnswer": "Eyes"},
            {"text": "Which is a planet?", "options": ["Earth", "Moon", "Sun", "Star"], "correctAnswer": "Earth"},
            {"text": "Which is a star?", "options": ["Sun", "Moon", "Earth", "Mars"], "correctAnswer": "Sun"},
            {"text": "Living things need ___.", "options": ["Air and Water", "Toys", "Money", "Cars"], "correctAnswer": "Air and Water"},
            {"text": "Baby of a horse?", "options": ["Foal", "Puppy", "Kitten", "Chick"], "correctAnswer": "Foal"},
            {"text": "Baby of a hen?", "options": ["Chick", "Calf", "Kid", "Foal"], "correctAnswer": "Chick"},
            {"text": "We get silk from ___.", "options": ["Silkworm", "Bee", "Ant", "Sheep"], "correctAnswer": "Silkworm"},
            {"text": "Fastest land animal?", "options": ["Cheetah", "Lion", "Horse", "Elephant"], "correctAnswer": "Cheetah"}
        ],
        "medium": [
            {"text": "Part of plant that makes food?", "options": ["Leaf", "Stem", "Root", "Flower"], "correctAnswer": "Leaf"},
            {"text": "Part of plant that carries water?", "options": ["Stem", "Leaf", "Fruit", "Root"], "correctAnswer": "Stem"},
            {"text": "Seed growing into a plant?", "options": ["Germination", "Flowering", "Dying", "Resting"], "correctAnswer": "Germination"},
            {"text": "National Tree of India?", "options": ["Banyan", "Peepal", "Neem", "Mango"], "correctAnswer": "Banyan"},
            {"text": "National Fruit of India?", "options": ["Mango", "Apple", "Grapes", "Orange"], "correctAnswer": "Mango"},
            {"text": "Which is an insect?", "options": ["Butterfly", "Lion", "Bird", "Fish"], "correctAnswer": "Butterfly"},
            {"text": "Animal with a hump?", "options": ["Camel", "Horse", "Donkey", "Cow"], "correctAnswer": "Camel"},
            {"text": "Bird's home?", "options": ["Nest", "Den", "Stable", "Kennel"], "correctAnswer": "Nest"},
            {"text": "Bee's home?", "options": ["Hive", "Nest", "Web", "Pond"], "correctAnswer": "Hive"},
            {"text": "Water changes to ice in a ___.", "options": ["Freezer", "Oven", "Pan", "Glass"], "correctAnswer": "Freezer"}
        ],
        "hard": [
            {"text": "Force that stops things?", "options": ["Friction", "Gravity", "Magnetic", "Electric"], "correctAnswer": "Friction"},
            {"text": "Force that pulls things down?", "options": ["Gravity", "Friction", "Magnetic", "Push"], "correctAnswer": "Gravity"},
            {"text": "Process of making food in plants?", "options": ["Photosynthesis", "Breathing", "Growing", "Eating"], "correctAnswer": "Photosynthesis"},
            {"text": "Boiling point of water?", "options": ["100 C", "0 C", "50 C", "200 C"], "correctAnswer": "100 C"},
            {"text": "Freezing point of water?", "options": ["0 C", "100 C", "32 C", "50 C"], "correctAnswer": "0 C"},
            {"text": "Sound travels in ___.", "options": ["All of these", "Air", "Water", "Solid"], "correctAnswer": "All of these"},
            {"text": "Light travels in a ___.", "options": ["Straight line", "Curved line", "Circle", "Zigzag"], "correctAnswer": "Straight line"},
            {"text": "Colors in a rainbow?", "options": ["7", "6", "5", "8"], "correctAnswer": "7"},
            {"text": "Largest mammal in the sea?", "options": ["Whale", "Shark", "Dolphin", "Fish"], "correctAnswer": "Whale"},
            {"text": "Scientist who discovered gravity?", "options": ["Newton", "Einstein", "Galileo", "Bose"], "correctAnswer": "Newton"}
        ]
    },
    "social-science": {
        "easy": [
            {"text": "Capital of India?", "options": ["New Delhi", "Mumbai", "Chennai", "Kolkata"], "correctAnswer": "New Delhi"},
            {"text": "Colors in Indian Flag?", "options": ["3", "4", "2", "5"], "correctAnswer": "3"},
            {"text": "Year of Independence?", "options": ["1947", "1950", "1942", "1960"], "correctAnswer": "1947"},
            {"text": "Republic Day date?", "options": ["Jan 26", "Aug 15", "Oct 2", "Nov 14"], "correctAnswer": "Jan 26"},
            {"text": "Independence Day date?", "options": ["Aug 15", "Jan 26", "Oct 2", "Nov 14"], "correctAnswer": "Aug 15"},
            {"text": "Gandhi Jayanti date?", "options": ["Oct 2", "Aug 15", "Jan 26", "Nov 14"], "correctAnswer": "Oct 2"},
            {"text": "Children's Day date?", "options": ["Nov 14", "Oct 2", "Jan 26", "Aug 15"], "correctAnswer": "Nov 14"},
            {"text": "Teacher's Day date in India?", "options": ["Sept 5", "Oct 2", "Nov 14", "Aug 15"], "correctAnswer": "Sept 5"},
            {"text": "National Anthem of India?", "options": ["Jana Gana Mana", "Vande Mataram", "Sare Jahan Se", "National Day"], "correctAnswer": "Jana Gana Mana"},
            {"text": "National Bird of India?", "options": ["Peacock", "Parrot", "Eagle", "Hen"], "correctAnswer": "Peacock"}
        ],
        "medium": [
            {"text": "Gateway of India is in ___.", "options": ["Mumbai", "Delhi", "Agra", "Chennai"], "correctAnswer": "Mumbai"},
            {"text": "Taj Mahal is in ___.", "options": ["Agra", "Mumbai", "Delhi", "Lucknow"], "correctAnswer": "Agra"},
            {"text": "Red Fort is in ___.", "options": ["Delhi", "Agra", "Mumbai", "Jaipur"], "correctAnswer": "Delhi"},
            {"text": "Pink City of India?", "options": ["Jaipur", "Jodhpur", "Udaipur", "Kota"], "correctAnswer": "Jaipur"},
            {"text": "Sun City of Rajasthan?", "options": ["Jodhpur", "Jaipur", "Bikaner", "Ajmer"], "correctAnswer": "Jodhpur"},
            {"text": "Silicon Valley of India?", "options": ["Bangalore", "Hyderabad", "Pune", "Chennai"], "correctAnswer": "Bangalore"},
            {"text": "National Animal of India?", "options": ["Tiger", "Lion", "Elephant", "Leopard"], "correctAnswer": "Tiger"},
            {"text": "National Fruit of India?", "options": ["Mango", "Apple", "Banana", "Grapes"], "correctAnswer": "Mango"},
            {"text": "Number of States in India?", "options": ["28", "25", "29", "30"], "correctAnswer": "28"},
            {"text": "First PM of India?", "options": ["Jawaharlal Nehru", "Indira Gandhi", "Modi", "Rajiv Gandhi"], "correctAnswer": "Jawaharlal Nehru"}
        ],
        "hard": [
            {"text": "Highest Peak in India?", "options": ["Kanchenjunga", "Everest", "K2", "Nanda Devi"], "correctAnswer": "Kanchenjunga"},
            {"text": "Longest River in India?", "options": ["Ganga", "Yamuna", "Godavari", "Narmada"], "correctAnswer": "Ganga"},
            {"text": "Smallest State in India?", "options": ["Goa", "Sikkim", "Tripura", "Kerala"], "correctAnswer": "Goa"},
            {"text": "Largest State in India?", "options": ["Rajasthan", "UP", "MP", "Maharashtra"], "correctAnswer": "Rajasthan"},
            {"text": "Who wrote national anthem?", "options": ["Rabindranath Tagore", "Bankim Chandra", "Sarojini Naidu", "Nehru"], "correctAnswer": "Rabindranath Tagore"},
            {"text": "Who wrote national song?", "options": ["Bankim Chandra", "Tagore", "Premchand", "Laxmi"], "correctAnswer": "Bankim Chandra"},
            {"text": "National Tree of India?", "options": ["Banyan", "Peepal", "Neem", "Mango"], "correctAnswer": "Banyan"},
            {"text": "National Flower of India?", "options": ["Lotus", "Rose", "Lily", "Sunflower"], "correctAnswer": "Lotus"},
            {"text": "Colors in flag from top?", "options": ["Saffron, White, Green", "Green, White, Saffron", "White, Saffron, Green", "None"], "correctAnswer": "Saffron, White, Green"},
            {"text": "Wheel in Indian flag?", "options": ["Ashoka Chakra", "Moon", "Sun", "Wheel"], "correctAnswer": "Ashoka Chakra"}
        ]
    },
    "hindi": {
        "easy": [
            {"text": "'आम' क्या है?", "options": ["फल", "सब्जी", "मिठाई", "फूल"], "correctAnswer": "फल"},
            {"text": "'माँ' का पर्यायवाची?", "options": ["माता", "पिता", "भाई", "बहन"], "correctAnswer": "माता"},
            {"text": "'पिता' का पर्यायवाची?", "options": ["जनक", "माता", "भाई", "बहन"], "correctAnswer": "जनक"},
            {"text": "घर का पर्यायवाची?", "options": ["गृह", "भोजन", "पानी", "आग"], "correctAnswer": "गृह"},
            {"text": "'पानी' का पर्यायवाची?", "options": ["जल", "आग", "धूल", "हवा"], "correctAnswer": "जल"},
            {"text": "पेड़ हमें क्या देते हैं?", "options": ["फल/छाया", "आग", "पत्थर", "कपड़े"], "correctAnswer": "फल/छाया"},
            {"text": "फूल का पर्यायवाची?", "options": ["पुष्प", "फल", "जड़", "मिट्टी"], "correctAnswer": "पुष्प"},
            {"text": "रंगों का नाम?", "options": ["लाल", "मेज", "कलम", "किताब"], "correctAnswer": "लाल"},
            {"text": "सूरज किधर से निकलता है?", "options": ["पूर्व", "पश्चिम", "उत्तर", "दक्षिण"], "correctAnswer": "पूर्व"},
            {"text": "चाँद कब निकलता है?", "options": ["रात", "दिन", "सुबह", "दोपहर"], "correctAnswer": "रात"}
        ],
        "medium": [
            {"text": "'बड़ा' का विलोम?", "options": ["छोटा", "लंबा", "मोटा", "भारी"], "correctAnswer": "छोटा"},
            {"text": "'दिन' का विलोम?", "options": ["रात", "सुबह", "शाम", "दोपहर"], "correctAnswer": "रात"},
            {"text": "'ऊपर' का विलोम?", "options": ["नीचे", "आज", "कल", "बाद"], "correctAnswer": "नीचे"},
            {"text": "'जल' का पर्यायवाची?", "options": ["पानी", "आग", "नभ", "धरा"], "correctAnswer": "पानी"},
            {"text": "संज्ञा का उदाहरण?", "options": ["राम", "खाना", "सोना", "उड़ना"], "correctAnswer": "राम"},
            {"text": "सर्वनाम का उदाहरण?", "options": ["मैं", "राम", "दिल्ली", "सुंदर"], "correctAnswer": "मैं"},
            {"text": "'लड़का' का बहुवचन?", "options": ["लड़के", "लड़कों", "लड़की", "लड़कियां"], "correctAnswer": "लड़के"},
            {"text": "'शेर' का स्त्रीलिंग?", "options": ["शेरनी", "शेर", "शेरिन", "माता"], "correctAnswer": "शेरनी"},
            {"text": "विशेषण का उदाहरण?", "options": ["सुंदर", "खेलना", "भाई", "घर"], "correctAnswer": "सुंदर"},
            {"text": "क्रिया का उदाहरण?", "options": ["खाना", "आम", "लाल", "वह"], "correctAnswer": "खाना"}
        ],
        "hard": [
            {"text": "'९-२-११ होना'?", "options": ["भाग जाना", "पकड़ना", "खेलना", "पढ़ना"], "correctAnswer": "भाग जाना"},
            {"text": "'आँख का तारा'?", "options": ["बहुत प्यारा", "दुश्मन", "अंधा", "कम तारा"], "correctAnswer": "बहुत प्यारा"},
            {"text": "विद्या + आलय = ?", "options": ["विद्यालय", "विद्याय", "आलय", "विद्य"], "correctAnswer": "विद्यालय"},
            {"text": "'गंगा' कौन सी संज्ञा है?", "options": ["व्यक्तिवाचक", "जातिवाचक", "भाववाचक", "समूहवाचक"], "correctAnswer": "व्यक्तिवाचक"},
            {"text": "वर्तमान काल का उदाहरण?", "options": ["वह खाता है", "वह खाया", "वह खाएगा", "खाओ"], "correctAnswer": "वह खाता है"},
            {"text": "'वीर' का स्त्रीलिंग?", "options": ["वीरांगना", "वीरता", "स्त्री", "माता"], "correctAnswer": "वीरांगना"},
            {"text": "'लड़का' का जातिवाचक संज्ञा?", "options": ["लड़का", "राम", "दिल्ली", "सुख"], "correctAnswer": "लड़का"},
            {"text": "शुद्ध शब्द?", "options": ["उज्ज्वल", "उजवल", "उजवल", "उज्जल"], "correctAnswer": "उज्ज्वल"},
            {"text": "'नभ' का पर्यायवाची?", "options": ["आकाश", "पाताल", "जल", "आग"], "correctAnswer": "आकाश"},
            {"text": "'अमृत' का विलोम?", "options": ["विष", "मीठा", "खट्टा", "जल"], "correctAnswer": "विष"}
        ]
    }
}

# Class 3 Data
class_3_data = {
    "english": {
        "easy": [
            {"text": "Which is an abstract noun?", "options": ["Honesty", "Book", "Boy", "Delhi"], "correctAnswer": "Honesty"},
            {"text": "Opposite of 'Success'?", "options": ["Failure", "Win", "Try", "Hope"], "correctAnswer": "Failure"},
            {"text": "Identify the pronoun: 'They are playing'.", "options": ["They", "are", "playing", "ball"], "correctAnswer": "They"},
            {"text": "Which word is a preposition?", "options": ["On", "Happy", "Run", "Sweet"], "correctAnswer": "On"},
            {"text": "Plural of 'Man'?", "options": ["Men", "Mans", "Manes", "Man"], "correctAnswer": "Men"},
            {"text": "Past tense of 'See'?", "options": ["Saw", "Seen", "Sees", "Seeing"], "correctAnswer": "Saw"},
            {"text": "Synonym of 'Silent'?", "options": ["Quiet", "Loud", "Fast", "Big"], "correctAnswer": "Quiet"},
            {"text": "A person who writes books?", "options": ["Author", "Poet", "Painter", "Singer"], "correctAnswer": "Author"},
            {"text": "Which is an adjective?", "options": ["Beautiful", "Quickly", "Sleep", "Under"], "correctAnswer": "Beautiful"},
            {"text": "I ___ a student.", "options": ["am", "is", "are", "do"], "correctAnswer": "am"}
        ],
        "medium": [
            {"text": "Which is a conjunction?", "options": ["Because", "Jump", "Happy", "Sweet"], "correctAnswer": "Because"},
            {"text": "Identify the adverb: 'He writes neatly'.", "options": ["neatly", "writes", "He", "is"], "correctAnswer": "neatly"},
            {"text": "Superlative of 'Good'?", "options": ["Best", "Better", "Goodest", "More good"], "correctAnswer": "Best"},
            {"text": "Collective noun for 'Fish'?", "options": ["School", "Pack", "Flock", "Herd"], "correctAnswer": "School"},
            {"text": "Identify the tense: 'I will eat'.", "options": ["Future", "Present", "Past", "None"], "correctAnswer": "Future"},
            {"text": "Which is a 'Proper Noun'?", "options": ["India", "Country", "Boy", "City"], "correctAnswer": "India"},
            {"text": "Use 'a' or 'an': ___ honest man.", "options": ["An", "A", "The", "Some"], "correctAnswer": "An"},
            {"text": "Antonym of 'Smooth'?", "options": ["Rough", "Soft", "Hard", "Big"], "correctAnswer": "Rough"},
            {"text": "Identify the Verb: 'The bell rings'.", "options": ["rings", "bell", "The", "loud"], "correctAnswer": "rings"},
            {"text": "A person who teaches is a ___.", "options": ["Teacher", "Doctor", "Farmer", "Driver"], "correctAnswer": "Teacher"}
        ],
        "hard": [
            {"text": "Which is a silent letter in 'Hymn'?", "options": ["n", "m", "h", "y"], "correctAnswer": "n"},
            {"text": "Identify the preposition: 'The bird flew over the house'.", "options": ["over", "flew", "bird", "house"], "correctAnswer": "over"},
            {"text": "Which is a 'Neuter' gender noun?", "options": ["Building", "King", "Maid", "Uncle"], "correctAnswer": "Building"},
            {"text": "Meaning of the idiom 'Under the weather'?", "options": ["Feeling sick", "Feeling happy", "Raining", "Sunny"], "correctAnswer": "Feeling sick"},
            {"text": "Identify the complex sentence.", "options": ["Because it was raining, we stayed home.", "We stayed home.", "It was raining and we stayed home.", "Stay home!"], "correctAnswer": "Because it was raining, we stayed home."},
            {"text": "Plural of 'Mouse'?", "options": ["Mice", "Mouses", "Micees", "None"], "correctAnswer": "Mice"},
            {"text": "What is 'Alliteration'?", "options": ["Repetition of consonant sounds", "Comparison", "Rhyme", "Sound words"], "correctAnswer": "Repetition of consonant sounds"},
            {"text": "Correct spelling?", "options": ["Business", "Bussiness", "Buissness", "Busness"], "correctAnswer": "Business"},
            {"text": "Antonym of 'Selfish'?", "options": ["Altruistic", "Kind", "Strong", "Fast"], "correctAnswer": "Altruistic"},
            {"text": "Identify the indirect object: 'He gave me a book'.", "options": ["me", "book", "He", "gave"], "correctAnswer": "me"}
        ]
    },
    "maths": {
        "easy": [
            {"text": "100 + 400 = ?", "options": ["500", "600", "400", "200"], "correctAnswer": "500"},
            {"text": "500 - 200 = ?", "options": ["300", "200", "400", "100"], "correctAnswer": "300"},
            {"text": "10 \u00d7 5 = ?", "options": ["50", "15", "5", "100"], "correctAnswer": "50"},
            {"text": "Which is larger: 100 or 99?", "options": ["100", "99", "Equal", "None"], "correctAnswer": "100"},
            {"text": "What is half of 100?", "options": ["50", "25", "75", "100"], "correctAnswer": "50"},
            {"text": "Count faces in a cube.", "options": ["6", "4", "8", "12"], "correctAnswer": "6"},
            {"text": "Place value of 7 in 712?", "options": ["700", "70", "7", "1"], "correctAnswer": "700"},
            {"text": "A circle has ___ sides.", "options": ["0", "1", "4", "Infinity"], "correctAnswer": "0"},
            {"text": "A week has ___ days.", "options": ["7", "5", "6", "10"], "correctAnswer": "7"},
            {"text": "Add: 25 + 25", "options": ["50", "40", "60", "45"], "correctAnswer": "50"}
        ],
        "medium": [
            {"text": "250 + 250 = ?", "options": ["500", "450", "550", "600"], "correctAnswer": "500"},
            {"text": "1000 - 1 = ?", "options": ["999", "900", "990", "1001"], "correctAnswer": "999"},
            {"text": "LCM of 2 and 5?", "options": ["10", "5", "2", "20"], "correctAnswer": "10"},
            {"text": "What is 10 \u00d7 10?", "options": ["100", "20", "10", "1000"], "correctAnswer": "100"},
            {"text": "How many months in half year?", "options": ["6", "12", "3", "4"], "correctAnswer": "6"},
            {"text": "Next number: 10, 20, 30, ___?", "options": ["40", "35", "50", "45"], "correctAnswer": "40"},
            {"text": "50 + 50 + 50 = ?", "options": ["150", "100", "200", "50"], "correctAnswer": "150"},
            {"text": "What is quarter of 60?", "options": ["15", "30", "20", "10"], "correctAnswer": "15"},
            {"text": "A year has ___ days usually.", "options": ["365", "366", "300", "400"], "correctAnswer": "365"},
            {"text": "Which number is even?", "options": ["42", "41", "43", "45"], "correctAnswer": "42"}
        ],
        "hard": [
            {"text": "100 \u00f7 4 = ?", "options": ["25", "20", "30", "50"], "correctAnswer": "25"},
            {"text": "Solve: 10 + 2 \u00d7 5", "options": ["20", "60", "15", "10"], "correctAnswer": "20"},
            {"text": "HCF of 10 and 20?", "options": ["10", "5", "20", "1"], "correctAnswer": "10"},
            {"text": "What is 20% of 200?", "options": ["40", "20", "60", "10"], "correctAnswer": "40"},
            {"text": "Number of edges in a cuboid?", "options": ["12", "6", "8", "4"], "correctAnswer": "12"},
            {"text": "Square root of 81?", "options": ["9", "8", "7", "10"], "correctAnswer": "9"},
            {"text": "If 1kg = 1000g, half kg = ___g.", "options": ["500", "250", "750", "100"], "correctAnswer": "500"},
            {"text": "Add: 1.5 + 2.5", "options": ["4.0", "3.0", "5.0", "1.5"], "correctAnswer": "4.0"},
            {"text": "What is 5 cubed?", "options": ["125", "15", "25", "75"], "correctAnswer": "125"},
            {"text": "Which number is a prime?", "options": ["11", "9", "12", "15"], "correctAnswer": "11"}
        ]
    },
    "science": {
        "easy": [
            {"text": "Part of plant that absorbs water?", "options": ["Root", "Leaf", "Fruit", "Flower"], "correctAnswer": "Root"},
            {"text": "Part of plant that makes food?", "options": ["Leaf", "Stem", "Root", "Flower"], "correctAnswer": "Leaf"},
            {"text": "Animal that lives on land and water?", "options": ["Frog", "Fish", "Dog", "Bird"], "correctAnswer": "Frog"},
            {"text": "Which is a fruit?", "options": ["Mango", "Carrot", "Potato", "Onion"], "correctAnswer": "Mango"},
            {"text": "Which is a vegetable?", "options": ["Carrot", "Apple", "Mango", "Banana"], "correctAnswer": "Carrot"},
            {"text": "Living things breathe in ___.", "options": ["Oxygen", "CO2", "Nitrogen", "Smoke"], "correctAnswer": "Oxygen"},
            {"text": "Living things breathe out ___.", "options": ["CO2", "Oxygen", "Nitrogen", "Food"], "correctAnswer": "CO2"},
            {"text": "Non-living thing example?", "options": ["Stone", "Cat", "Tree", "Bird"], "correctAnswer": "Stone"},
            {"text": "Main source of heat?", "options": ["Sun", "Moon", "Stars", "Cloud"], "correctAnswer": "Sun"},
            {"text": "We get milk from ___.", "options": ["Cow", "Hen", "Fish", "Bird"], "correctAnswer": "Cow"}
        ],
        "medium": [
            {"text": "Process of plants making food?", "options": ["Photosynthesis", "Breathing", "Cooking", "Resting"], "correctAnswer": "Photosynthesis"},
            {"text": "Green color in leaves due to ___.", "options": ["Chlorophyll", "Water", "Air", "Sunlight"], "correctAnswer": "Chlorophyll"},
            {"text": "Example of a Herbivore?", "options": ["Cow", "Lion", "Tiger", "Wolf"], "correctAnswer": "Cow"},
            {"text": "Example of a Carnivore?", "options": ["Lion", "Cow", "Rabbit", "Goat"], "correctAnswer": "Lion"},
            {"text": "Example of an Omnivore?", "options": ["Bear", "Cow", "Deer", "Sheep"], "correctAnswer": "Bear"},
            {"text": "Water cycle starts with ___.", "options": ["Evaporation", "Rain", "Snow", "Wind"], "correctAnswer": "Evaporation"},
            {"text": "Clouds are made of ___.", "options": ["Water vapor", "Cotton", "Smoke", "Dust"], "correctAnswer": "Water vapor"},
            {"text": "How many sense organs?", "options": ["5", "4", "6", "10"], "correctAnswer": "5"},
            {"text": "Hardest part of the body?", "options": ["Enamel/Teeth", "Skin", "Hair", "Nail"], "correctAnswer": "Enamel/Teeth"},
            {"text": "Boiling point of water?", "options": ["100 C", "0 C", "50 C", "10 C"], "correctAnswer": "100 C"}
        ],
        "hard": [
            {"text": "Planet closest to the sun?", "options": ["Mercury", "Venus", "Earth", "Mars"], "correctAnswer": "Mercury"},
            {"text": "The 'Red Planet' is ___.", "options": ["Mars", "Venus", "Saturn", "Jupiter"], "correctAnswer": "Mars"},
            {"text": "Largest planet in our system?", "options": ["Jupiter", "Saturn", "Earth", "Neptune"], "correctAnswer": "Jupiter"},
            {"text": "Bones in an adult human body?", "options": ["206", "300", "250", "100"], "correctAnswer": "206"},
            {"text": "Muscles in the human body?", "options": ["600+", "100", "200", "1000"], "correctAnswer": "600+"},
            {"text": "Blood is pumped by the ___.", "options": ["Heart", "Lungs", "Brain", "Stomach"], "correctAnswer": "Heart"},
            {"text": "Digestion starts in the ___.", "options": ["Mouth", "Stomach", "Liver", "Intestine"], "correctAnswer": "Mouth"},
            {"text": "Atmosphere contains mostly ___.", "options": ["Nitrogen", "Oxygen", "CO2", "Argon"], "correctAnswer": "Nitrogen"},
            {"text": "Acid rain is caused by ___.", "options": ["Pollution", "Rain", "Snow", "Sun"], "correctAnswer": "Pollution"},
            {"text": "Global warming is due to ___.", "options": ["Greenhouse gases", "Rain", "Trees", "Ice"], "correctAnswer": "Greenhouse gases"}
        ]
    },
    "social-science": {
        "easy": [
            {"text": "My country is ___.", "options": ["India", "England", "Japan", "USA"], "correctAnswer": "India"},
            {"text": "Capital of India?", "options": ["New Delhi", "Agra", "Chennai", "Mumbai"], "correctAnswer": "New Delhi"},
            {"text": "Current President of India?", "options": ["Droupadi Murmu", "Modi", "Kalam", "Patil"], "correctAnswer": "Droupadi Murmu"},
            {"text": "Current PM of India?", "options": ["Narendra Modi", "Rahul Gandhi", "Nehru", "Patel"], "correctAnswer": "Narendra Modi"},
            {"text": "National Flower of India?", "options": ["Lotus", "Rose", "Sun", "Lily"], "correctAnswer": "Lotus"},
            {"text": "National Fruit of India?", "options": ["Mango", "Apple", "Orange", "Banana"], "correctAnswer": "Mango"},
            {"text": "National Animal of India?", "options": ["Tiger", "Lion", "Cat", "Dog"], "correctAnswer": "Tiger"},
            {"text": "National Bird of India?", "options": ["Peacock", "Hen", "Crow", "Parrot"], "correctAnswer": "Peacock"},
            {"text": "Colors in Indian Flag?", "options": ["3", "4", "2", "5"], "correctAnswer": "3"},
            {"text": "Wheel in Indian Flag?", "options": ["Ashoka Chakra", "Circle", "Sun", "Moon"], "correctAnswer": "Ashoka Chakra"}
        ],
        "medium": [
            {"text": "Gateway of India location?", "options": ["Mumbai", "Delhi", "Chennai", "Kolkata"], "correctAnswer": "Mumbai"},
            {"text": "India Gate location?", "options": ["Delhi", "Mumbai", "Agra", "Jaipur"], "correctAnswer": "Delhi"},
            {"text": "Hawa Mahal location?", "options": ["Jaipur", "Jodhpur", "Ajmer", "Udaipur"], "correctAnswer": "Jaipur"},
            {"text": "Charminar location?", "options": ["Hyderabad", "Chennai", "Bangalore", "Pune"], "correctAnswer": "Hyderabad"},
            {"text": "Number of States in India?", "options": ["28", "29", "25", "30"], "correctAnswer": "28"},
            {"text": "Number of Union Territories?", "options": ["8", "7", "9", "6"], "correctAnswer": "8"},
            {"text": "First Woman PM of India?", "options": ["Indira Gandhi", "Sonia Gandhi", "Pratibha Patil", "None"], "correctAnswer": "Indira Gandhi"},
            {"text": "Iron Man of India?", "options": ["Sardar Patel", "Gandhi", "Nehru", "Bose"], "correctAnswer": "Sardar Patel"},
            {"text": "Father of Indian Constitution?", "options": ["Dr. Ambedkar", "Gandhi", "Nehru", "Patel"], "correctAnswer": "Dr. Ambedkar"},
            {"text": "Who wrote 'Discovery of India'?", "options": ["Nehru", "Tagore", "Gandhi", "Ambedkar"], "correctAnswer": "Nehru"}
        ],
        "hard": [
            {"text": "Highest Peak in India?", "options": ["Kanchenjunga", "Everest", "Nanda Devi", "K2"], "correctAnswer": "Kanchenjunga"},
            {"text": "Longest River in the world?", "options": ["Nile", "Amazon", "Ganga", "Mississippi"], "correctAnswer": "Nile"},
            {"text": "Longest River in India?", "options": ["Ganga", "Yamuna", "Brahmaputra", "Narmada"], "correctAnswer": "Ganga"},
            {"text": "Largest Ocean?", "options": ["Pacific", "Atlantic", "Indian", "Arctic"], "correctAnswer": "Pacific"},
            {"text": "Smallest Continent?", "options": ["Australia", "Europe", "Antarctica", "Africa"], "correctAnswer": "Australia"},
            {"text": "Largest Continent?", "options": ["Asia", "Africa", "N. America", "Europe"], "correctAnswer": "Asia"},
            {"text": "Deepest point in the ocean?", "options": ["Mariana Trench", "Bermuda", "Java Trench", "None"], "correctAnswer": "Mariana Trench"},
            {"text": "Number of time zones on Earth?", "options": ["24", "12", "10", "48"], "correctAnswer": "24"},
            {"text": "Zero longitude line?", "options": ["Prime Meridian", "Equator", "Tropics", "None"], "correctAnswer": "Prime Meridian"},
            {"text": "Tropic of Cancer passes through ___.", "options": ["India", "Australia", "UK", "USA"], "correctAnswer": "India"}
        ]
    },
    "hindi": {
        "easy": [
            {"text": "'आम' क्या है?", "options": ["फल", "सब्जी", "मिठाई", "फूल"], "correctAnswer": "फल"},
            {"text": "'सेब' किस रंग का होता है?", "options": ["लाल", "नीला", "पीला", "काला"], "correctAnswer": "लाल"},
            {"text": "'घर' का पर्यायवाची?", "options": ["आलय", "भोजन", "पानी", "आग"], "correctAnswer": "आलय"},
            {"text": "'पानी' का पर्यायवाची?", "options": ["जल", "आग", "धूल", "हवा"], "correctAnswer": "जल"},
            {"text": "सूरज कब निकलता है?", "options": ["दिन", "रात", "शाम", "दोपहर"], "correctAnswer": "दिन"},
            {"text": "चाँद कब निकलता है?", "options": ["रात", "दिन", "सुबह", "दोपहर"], "correctAnswer": "रात"},
            {"text": "पेड़ हमें क्या देते हैं?", "options": ["फल/छाया", "आग", "पत्थर", "लकड़ी"], "correctAnswer": "फल/छाया"},
            {"text": "फूल का पर्यायवाची?", "options": ["पुष्प", "फल", "जड़", "मिट्टी"], "correctAnswer": "पुष्प"},
            {"text": "'लाल' क्या है?", "options": ["रंग", "फल", "सब्जी", "पक्षी"], "correctAnswer": "रंग"},
            {"text": "'पीला' क्या है?", "options": ["रंग", "पशु", "घर", "मिट्टी"], "correctAnswer": "रंग"}
        ],
        "medium": [
            {"text": "'बड़ा' का विलोम?", "options": ["छोटा", "आज", "लंबा", "मोटा"], "correctAnswer": "छोटा"},
            {"text": "'दिन' का विलोम?", "options": ["रात", "सुबह", "शाम", "दोपहर"], "correctAnswer": "रात"},
            {"text": "'ऊपर' का विलोम?", "options": ["नीचे", "आज", "कल", "बाद"], "correctAnswer": "नीचे"},
            {"text": "'जल' का पर्यायवाची?", "options": ["पानी", "आग", "नभ", "धरा"], "correctAnswer": "पानी"},
            {"text": "'लड़का' का बहुवचन?", "options": ["लड़के", "लड़कों", "लड़की", "लड़कियां"], "correctAnswer": "लड़के"},
            {"text": "'शेर' का स्त्रीलिंग?", "options": ["शेरनी", "शेर", "शेरिन", "माता"], "correctAnswer": "शेरनी"},
            {"text": "संज्ञा का उदाहरण?", "options": ["राम", "खाना", "सोना", "उड़ना"], "correctAnswer": "राम"},
            {"text": "सर्वनाम का उदाहरण?", "options": ["मैं", "राम", "दिल्ली", "सुंदर"], "correctAnswer": "मैं"},
            {"text": "विशेषण का उदाहरण?", "options": ["सुंदर", "खेलना", "भाई", "घर"], "correctAnswer": "सुंदर"},
            {"text": "क्रिया का उदाहरण?", "options": ["खाना", "आम", "लाल", "वह"], "correctAnswer": "खाना"}
        ],
        "hard": [
            {"text": "'९-२-११ होना'?", "options": ["भाग जाना", "पकड़ना", "खेलना", "पढ़ना"], "correctAnswer": "भाग जाना"},
            {"text": "'आँख का तारा'?", "options": ["बहुत प्यारा", "दुश्मन", "अंधा", "कम तारा"], "correctAnswer": "बहुत प्यारा"},
            {"text": "विद्या + आलय = ?", "options": ["विद्यालय", "विद्याय", "आलय", "विद्य"], "correctAnswer": "विद्यालय"},
            {"text": "'हिमालय' कौन सी संज्ञा है?", "options": ["व्यक्तिवाचक", "जातिवाचक", "भाववाचक", "समूहवाचक"], "correctAnswer": "व्यक्तिवाचक"},
            {"text": "वर्तमान काल का उदाहरण?", "options": ["वह खाता है", "वह खाया", "वह खाएगा", "खाओ"], "correctAnswer": "वह खाता है"},
            {"text": "'राजा' का स्त्रीलिंग?", "options": ["रानी", "माता", "बहन", "स्त्री"], "correctAnswer": "रानी"},
            {"text": "'लड़का' का जातिवाचक संज्ञा?", "options": ["लड़का", "राम", "दिल्ली", "सुख"], "correctAnswer": "लड़का"},
            {"text": "शुद्ध शब्द?", "options": ["उज्वल", "उज्ज्वल", "उजवल", "उज्जल"], "correctAnswer": "उज्ज्वल"},
            {"text": "'अग्नि' का पर्यायवाची?", "options": ["आग", "पानी", "हवा", "मिट्टी"], "correctAnswer": "आग"},
            {"text": "'स्वर्ग' का विलोम?", "options": ["नरक", "जमीन", "आसमान", "पाताल"], "correctAnswer": "नरक"}
        ]
    }
}

# Class 4 Data
class_4_data = {
    "english": {
        "easy": [
            {"text": "Identify the collective noun: 'A flock of birds'.", "options": ["flock", "birds", "bird", "is"], "correctAnswer": "flock"},
            {"text": "Opposite of 'Near'?", "options": ["Far", "Close", "Up", "Sad"], "correctAnswer": "Far"},
            {"text": "Plural of 'Box'?", "options": ["Boxes", "Boxs", "Boxies", "Box"], "correctAnswer": "Boxes"},
            {"text": "Identify the pronoun: 'It is a sunny day'.", "options": ["It", "is", "sunny", "day"], "correctAnswer": "It"},
            {"text": "Which word is an adverb?", "options": ["Quickly", "Quick", "Run", "Fast (adj)"], "correctAnswer": "Quickly"},
            {"text": "A person who cures us?", "options": ["Doctor", "Painter", "Singer", "Pilot"], "correctAnswer": "Doctor"},
            {"text": "Synonym of 'Tiny'?", "options": ["Small", "Big", "High", "Deep"], "correctAnswer": "Small"},
            {"text": "Which is an animal?", "options": ["Elephant", "Rose", "Pen", "Apple"], "correctAnswer": "Elephant"},
            {"text": "Identify the color.", "options": ["Yellow", "Book", "Run", "Eat"], "correctAnswer": "Yellow"},
            {"text": "A bird flies with its ___.", "options": ["Wings", "Legs", "Tail", "Beak"], "correctAnswer": "Wings"}
        ],
        "medium": [
            {"text": "Use 'a' or 'an': ___ orange.", "options": ["An", "A", "The", "Some"], "correctAnswer": "An"},
            {"text": "Identify the tense: 'He went to school'.", "options": ["Past", "Present", "Future", "None"], "correctAnswer": "Past"},
            {"text": "Superlative of 'Fast'?", "options": ["Fastest", "Faster", "More fast", "Fast"], "correctAnswer": "Fastest"},
            {"text": "Which is a 'Common Noun'?", "options": ["City", "Delhi", "Ravi", "India"], "correctAnswer": "City"},
            {"text": "Past tense of 'Cook'?", "options": ["Cooked", "Cooks", "Cooking", "Cook"], "correctAnswer": "Cooked"},
            {"text": "Identify the adjective: 'The sweet cake'.", "options": ["sweet", "cake", "The", "is"], "correctAnswer": "sweet"},
            {"text": "A car is a ___ of transport.", "options": ["Mode", "Part", "Type", "Way"], "correctAnswer": "Mode"},
            {"text": "Which describes 'Happily'?", "options": ["Adverb", "Adjective", "Noun", "Verb"], "correctAnswer": "Adverb"},
            {"text": "Antonym of 'Brave'?", "options": ["Coward", "Strong", "Kind", "Fast"], "correctAnswer": "Coward"},
            {"text": "A bunch of ___.", "options": ["Grapes", "Birds", "Cows", "Wolves"], "correctAnswer": "Grapes"}
        ],
        "hard": [
            {"text": "Which word has a silent 'K'?", "options": ["Know", "King", "Kite", "Keep"], "correctAnswer": "Know"},
            {"text": "Identify the conjunction.", "options": ["But", "Big", "On", "Run"], "correctAnswer": "But"},
            {"text": "Which is a 'Neuter' gender noun?", "options": ["Table", "Man", "Maid", "Uncle"], "correctAnswer": "Table"},
            {"text": "Meaning of 'Vast'?", "options": ["Huge/Large", "Small", "Green", "Fast"], "correctAnswer": "Huge/Large"},
            {"text": "Identify the Verb.", "options": ["Study", "Blue", "Sweet", "Under"], "correctAnswer": "Study"},
            {"text": "Antonym of 'Rough'?", "options": ["Smooth", "Soft", "Hard", "Big"], "correctAnswer": "Smooth"},
            {"text": "Plural of 'Ox'?", "options": ["Oxen", "Oxs", "Oxies", "Ox"], "correctAnswer": "Oxen"},
            {"text": "Identify the pronoun: 'We love our country'.", "options": ["We", "love", "our", "country"], "correctAnswer": "We"},
            {"text": "Past tense of 'Write'?", "options": ["Wrote", "Written", "Writes", "Writing"], "correctAnswer": "Wrote"},
            {"text": "Identify the preposition.", "options": ["Through", "Fast", "Boy", "Run"], "correctAnswer": "Through"}
        ]
    },
    "maths": {
        "easy": [
            {"text": "500 + 500 = ?", "options": ["1000", "500", "1500", "2000"], "correctAnswer": "1000"},
            {"text": "1000 - 50 = ?", "options": ["950", "900", "850", "990"], "correctAnswer": "950"},
            {"text": "What is 10 \u00d7 4?", "options": ["40", "14", "4", "100"], "correctAnswer": "40"},
            {"text": "Which is smaller: 105 or 150?", "options": ["105", "150", "Equal", "None"], "correctAnswer": "105"},
            {"text": "12 \u00f7 2 = ?", "options": ["6", "2", "4", "10"], "correctAnswer": "6"},
            {"text": "Double of 25 is ___.", "options": ["50", "40", "60", "25"], "correctAnswer": "50"},
            {"text": "8 + 8 + 8 = ?", "options": ["24", "16", "20", "30"], "correctAnswer": "24"},
            {"text": "Next number: 2, 4, 6, 8, ___?", "options": ["10", "9", "11", "12"], "correctAnswer": "10"},
            {"text": "Corners in a rectangle.", "options": ["4", "3", "5", "6"], "correctAnswer": "4"},
            {"text": "What is 1 \u00d7 12?", "options": ["12", "1", "13", "11"], "correctAnswer": "12"}
        ],
        "medium": [
            {"text": "250 \u00d7 2 = ?", "options": ["500", "450", "550", "600"], "correctAnswer": "500"},
            {"text": "1 hour = ___ minutes.", "options": ["60", "100", "50", "12"], "correctAnswer": "60"},
            {"text": "LCM of 3 and 6?", "options": ["6", "3", "9", "12"], "correctAnswer": "6"},
            {"text": "What is 10 \u00d7 10 \u00f7 2?", "options": ["50", "100", "10", "20"], "correctAnswer": "50"},
            {"text": "How many days in leap year?", "options": ["366", "360", "365", "300"], "correctAnswer": "366"},
            {"text": "Next number: 1, 3, 5, 7, ___?", "options": ["9", "8", "10", "11"], "correctAnswer": "9"},
            {"text": "Double of 100 is ___.", "options": ["200", "150", "300", "100"], "correctAnswer": "200"},
            {"text": "Third of 30 is ___.", "options": ["10", "3", "30", "20"], "correctAnswer": "10"},
            {"text": "A right angle is ___ degrees.", "options": ["90", "180", "270", "360"], "correctAnswer": "90"},
            {"text": "Which number is even?", "options": ["100", "101", "103", "105"], "correctAnswer": "100"}
        ],
        "hard": [
            {"text": "500 \u00f7 5 = ?", "options": ["100", "10", "50", "500"], "correctAnswer": "100"},
            {"text": "Solve: 100 - 10 \u00d7 2", "options": ["80", "180", "90", "100"], "correctAnswer": "80"},
            {"text": "HCF of 6 and 12?", "options": ["6", "2", "3", "1"], "correctAnswer": "6"},
            {"text": "25% of 100 is ___.", "options": ["25", "50", "75", "100"], "correctAnswer": "25"},
            {"text": "Smallest 4-digit number?", "options": ["1000", "1001", "1111", "9000"], "correctAnswer": "1000"},
            {"text": "Average of 10 and 20?", "options": ["15", "10", "20", "30"], "correctAnswer": "15"},
            {"text": "Faces in a sphere?", "options": ["1 (Curved)", "0", "4", "6"], "correctAnswer": "1 (Curved)"},
            {"text": "Sum of 1/2 and 1/2?", "options": ["1", "1/4", "1/2", "2"], "correctAnswer": "1"},
            {"text": "What is 12 \u00d7 12?", "options": ["144", "124", "122", "134"], "correctAnswer": "144"},
            {"text": "Probability of heads in coin toss?", "options": ["1/2", "1/6", "1/4", "0"], "correctAnswer": "1/2"}
        ]
    },
    "science": {
        "easy": [
            {"text": "Plant that eats insects?", "options": ["Pitcher Plant", "Rose", "Mango", "Neem"], "correctAnswer": "Pitcher Plant"},
            {"text": "Animal that lives in land and water?", "options": ["Frog", "Fish", "Bird", "Cat"], "correctAnswer": "Frog"},
            {"text": "Animal that only eats plants?", "options": ["Herbivore", "Carnivore", "Omnivore", "Scavenger"], "correctAnswer": "Herbivore"},
            {"text": "Animal that eats both plants and meat?", "options": ["Omnivore", "Herbivore", "Carnivore", "Parasite"], "correctAnswer": "Omnivore"},
            {"text": "Part of plant that breathes through stomata?", "options": ["Leaf", "Stem", "Root", "Flower"], "correctAnswer": "Leaf"},
            {"text": "Example of a living thing?", "options": ["Tree", "Stone", "Chair", "Car"], "correctAnswer": "Tree"},
            {"text": "Example of a non-living thing?", "options": ["Chair", "Cat", "Bird", "Human"], "correctAnswer": "Chair"},
            {"text": "Largest bird in the world?", "options": ["Ostrich", "Eagle", "Peacock", "Hen"], "correctAnswer": "Ostrich"},
            {"text": "A flightless bird?", "options": ["Penguin", "Parrot", "Sparrow", "Crow"], "correctAnswer": "Penguin"},
            {"text": "We get paper from ___.", "options": ["Trees", "Animals", "Rocks", "Clouds"], "correctAnswer": "Trees"}
        ],
        "medium": [
            {"text": "Force that attracts iron?", "options": ["Magnetism", "Gravity", "Friction", "Push"], "correctAnswer": "Magnetism"},
            {"text": "Force that pulls an apple to the ground?", "options": ["Gravity", "Magnetism", "Air", "Light"], "correctAnswer": "Gravity"},
            {"text": "Boiling point of water?", "options": ["100 C", "0 C", "50 C", "200 C"], "correctAnswer": "100 C"},
            {"text": "Freezing point of water?", "options": ["0 C", "100 C", "32 C", "50 C"], "correctAnswer": "0 C"},
            {"text": "Water in the form of gas?", "options": ["Steam/Vapor", "Ice", "Liquid", "None"], "correctAnswer": "Steam/Vapor"},
            {"text": "Atmosphere provides us with ___.", "options": ["Oxygen", "Food", "Water", "Light"], "correctAnswer": "Oxygen"},
            {"text": "Solar energy comes from the ___.", "options": ["Sun", "Moon", "Stars", "Earth"], "correctAnswer": "Sun"},
            {"text": "Process of plants making food?", "options": ["Photosynthesis", "Breathing", "Cooking", "Resting"], "correctAnswer": "Photosynthesis"},
            {"text": "Digestion ends in the ___.", "options": ["Intestines", "Mouth", "Stomach", "Heart"], "correctAnswer": "Intestines"},
            {"text": "Light travels ___ than sound.", "options": ["Faster", "Slower", "Same", "Not at all"], "correctAnswer": "Faster"}
        ],
        "hard": [
            {"text": "Nearest galaxy to us?", "options": ["Andromeda", "Milky Way", "Orion", "Centauri"], "correctAnswer": "Andromeda"},
            {"text": "Planets in our solar system?", "options": ["8", "9", "7", "10"], "correctAnswer": "8"},
            {"text": "Smallest planet in the solar system?", "options": ["Mercury", "Mars", "Pluto", "Earth"], "correctAnswer": "Mercury"},
            {"text": "Largest planet in the solar system?", "options": ["Jupiter", "Saturn", "Neptune", "Uranus"], "correctAnswer": "Jupiter"},
            {"text": "Hottest planet in the solar system?", "options": ["Venus", "Mercury", "Mars", "Saturn"], "correctAnswer": "Venus"},
            {"text": "Earth's layer we live on?", "options": ["Crust", "Mantle", "Outer Core", "Inner Core"], "correctAnswer": "Crust"},
            {"text": "Center of the Earth?", "options": ["Core", "Crust", "Surface", "Shell"], "correctAnswer": "Core"},
            {"text": "Sound cannot travel in a ___.", "options": ["Vacuum", "Water", "Air", "Steel"], "correctAnswer": "Vacuum"},
            {"text": "Speed of light (approx)?", "options": ["300,000 km/s", "100,000 km/s", "50,000 km/s", "10,000 km/s"], "correctAnswer": "300,000 km/s"},
            {"text": "First man in space?", "options": ["Yuri Gagarin", "Neil Armstrong", "Rakesh Sharma", "Buzz Aldrin"], "correctAnswer": "Yuri Gagarin"}
        ]
    },
    "social-science": {
        "easy": [
            {"text": "My country is ___.", "options": ["India", "America", "Japan", "France"], "correctAnswer": "India"},
            {"text": "National Animal of India?", "options": ["Tiger", "Lion", "Elephant", "Cows"], "correctAnswer": "Tiger"},
            {"text": "National Flower of India?", "options": ["Lotus", "Rose", "Lily", "Daisy"], "correctAnswer": "Lotus"},
            {"text": "National Anthem of India?", "options": ["Jana Gana Mana", "Vande Mataram", "Sare Jahan Se", "National Day"], "correctAnswer": "Jana Gana Mana"},
            {"text": "Indian Flag is called ___.", "options": ["Tiranga", "Banner", "Standard", "Flag"], "correctAnswer": "Tiranga"},
            {"text": "Capital of India?", "options": ["New Delhi", "Mumbai", "Kolkata", "Chennai"], "correctAnswer": "New Delhi"},
            {"text": "India got independence in ___.", "options": ["1947", "1950", "1942", "1960"], "correctAnswer": "1947"},
            {"text": "Republic Day of India?", "options": ["Jan 26", "Aug 15", "Oct 2", "Nov 14"], "correctAnswer": "Jan 26"},
            {"text": "Gandhi Jayanti is on ___.", "options": ["Oct 2", "Aug 15", "Nov 14", "Jan 26"], "correctAnswer": "Oct 2"},
            {"text": "Children's Day is on ___.", "options": ["Nov 14", "Oct 2", "Jan 26", "Aug 15"], "correctAnswer": "Nov 14"}
        ],
        "medium": [
            {"text": "Gateway of India location?", "options": ["Mumbai", "Delhi", "Agra", "Jaipur"], "correctAnswer": "Mumbai"},
            {"text": "India Gate location?", "options": ["Delhi", "Mumbai", "Agra", "Kolkata"], "correctAnswer": "Delhi"},
            {"text": "Taj Mahal location?", "options": ["Agra", "Delhi", "Mumbai", "Pune"], "correctAnswer": "Agra"},
            {"text": "Charminar location?", "options": ["Hyderabad", "Chennai", "Bangalore", "Goa"], "correctAnswer": "Hyderabad"},
            {"text": "Pink City of India?", "options": ["Jaipur", "Udaipur", "Jodhpur", "Ajmer"], "correctAnswer": "Jaipur"},
            {"text": "Silicon Valley of India?", "options": ["Bangalore", "Hyderabad", "Pune", "Gurgaon"], "correctAnswer": "Bangalore"},
            {"text": "Number of States in India?", "options": ["28", "25", "29", "30"], "correctAnswer": "28"},
            {"text": "Number of Union Territories?", "options": ["8", "7", "9", "6"], "correctAnswer": "8"},
            {"text": "Highest Mountain Peak in world?", "options": ["Mt. Everest", "K2", "Mt. Fuji", "Lhotse"], "correctAnswer": "Mt. Everest"},
            {"text": "Highest Peak in India?", "options": ["Kanchenjunga", "Everest", "Nanda Devi", "Kamet"], "correctAnswer": "Kanchenjunga"}
        ],
        "hard": [
            {"text": "First PM of India?", "options": ["Jawaharlal Nehru", "Morarji Desai", "Indira Gandhi", "L.B. Shastri"], "correctAnswer": "Jawaharlal Nehru"},
            {"text": "First President of India?", "options": ["Dr. Rajendra Prasad", "Dr. Kalam", "S. Radhakrishnan", "Zakir Husain"], "correctAnswer": "Dr. Rajendra Prasad"},
            {"text": "First Woman PM of India?", "options": ["Indira Gandhi", "Pratibha Patil", "Sushma Swaraj", "Mamata Banerjee"], "correctAnswer": "Indira Gandhi"},
            {"text": "Iron Man of India?", "options": ["Sardar Patel", "Bose", "Gandhi", "Nehru"], "correctAnswer": "Sardar Patel"},
            {"text": "Father of Indian Constitution?", "options": ["Dr. Ambedkar", "Gandhi", "Rajendra Prasad", "Tagore"], "correctAnswer": "Dr. Ambedkar"},
            {"text": "Longest River in India?", "options": ["Ganga", "Yamuna", "Godavari", "Narmada"], "correctAnswer": "Ganga"},
            {"text": "Smallest State in India?", "options": ["Goa", "Sikkim", "Tripura", "Manipur"], "correctAnswer": "Goa"},
            {"text": "Largest State in India (Area)?", "options": ["Rajasthan", "MP", "Maharashtra", "UP"], "correctAnswer": "Rajasthan"},
            {"text": "Highest Population State?", "options": ["UP", "Bihar", "Maharashtra", "West Bengal"], "correctAnswer": "UP"},
            {"text": "Least Population State?", "options": ["Sikkim", "Goa", "Arunachal", "Mizoram"], "correctAnswer": "Sikkim"}
        ]
    },
    "hindi": {
        "easy": [
            {"text": "'आम' क्या है?", "options": ["फल", "सब्जी", "मिठाई", "फूल"], "correctAnswer": "फल"},
            {"text": "'सेब' का रंग?", "options": ["लाल", "नीला", "पीला", "सफ़ेद"], "correctAnswer": "लाल"},
            {"text": "'घर' का पर्यायवाची?", "options": ["गृह", "भोजन", "पानी", "आग"], "correctAnswer": "गृह"},
            {"text": "'पानी' का पर्यायवाची?", "options": ["जल", "आग", "धूल", "हवा"], "correctAnswer": "जल"},
            {"text": "सूरज किधर से निकलता है?", "options": ["पूर्व", "पश्चिम", "उत्तर", "दक्षिण"], "correctAnswer": "पूर्व"},
            {"text": "चाँद कब निकलता है?", "options": ["रात", "दिन", "सुबह", "दोपहर"], "correctAnswer": "रात"},
            {"text": "पेड़ हमें क्या देते हैं?", "options": ["फल/छाया", "आग", "पत्थर", "कपड़े"], "correctAnswer": "फल/छाया"},
            {"text": "फूल का पर्यायवाची?", "options": ["पुष्प", "फल", "जड़", "मिट्टी"], "correctAnswer": "पुष्प"},
            {"text": "'लाल' क्या है?", "options": ["रंग", "फल", "सब्जी", "पक्षी"], "correctAnswer": "रंग"},
            {"text": "'पीला' क्या है?", "options": ["रंग", "पशु", "घर", "मिट्टी"], "correctAnswer": "रंग"}
        ],
        "medium": [
            {"text": "'बड़ा' का विलोम?", "options": ["छोटा", "आज", "लंबा", "मोटा"], "correctAnswer": "छोटा"},
            {"text": "'दिन' का विलोम?", "options": ["रात", "सुबह", "शाम", "दोपहर"], "correctAnswer": "रात"},
            {"text": "'जल' का पर्यायवाची?", "options": ["पानी", "आग", "नभ", "धरा"], "correctAnswer": "पानी"},
            {"text": "संज्ञा का उदाहरण?", "options": ["हिमालय", "खाना", "सोना", "उड़ना"], "correctAnswer": "हिमालय"},
            {"text": "सर्वनाम का उदाहरण?", "options": ["हम", "राम", "दिल्ली", "सुंदर"], "correctAnswer": "हम"},
            {"text": "'लड़का' का स्त्रीलिंग?", "options": ["लड़की", "लड़के", "लड़कियां", "माता"], "correctAnswer": "लड़की"},
            {"text": "'किताब' का बहुवचन?", "options": ["किताबें", "किताबों", "किताब", "किताबी"], "correctAnswer": "किताबें"},
            {"text": "विशेषण का उदाहरण?", "options": ["सुंदर", "खेलना", "भाई", "घर"], "correctAnswer": "सुंदर"},
            {"text": "'९-२-११ होना'?", "options": ["भाग जाना", "पकड़ना", "खेलना", "पढ़ना"], "correctAnswer": "भाग जाना"},
            {"text": "शुद्ध शब्द चुनिए:", "options": ["उज्वल", "शुद्ध", "गलत", "सच"], "correctAnswer": "शुद्ध"}
        ],
        "hard": [
            {"text": "'आँख का तारा' अर्थ?", "options": ["बहुत प्यारा", "दुश्मन", "अंधा", "कम दिखना"], "correctAnswer": "बहुत प्यारा"},
            {"text": "विद्या + आलय = ?", "options": ["विद्यालय", "विद्याय", "आलय", "विद्य"], "correctAnswer": "विद्यालय"},
            {"text": "संज्ञा के कितने भेद?", "options": ["3", "5", "4", "2"], "correctAnswer": "3"},
            {"text": "सर्वनाम के कितने भेद?", "options": ["6", "4", "5", "7"], "correctAnswer": "6"},
            {"text": "वाक्य शुद्ध करें: 'मुझको फल खाना है'?", "options": ["मुझे फल खाना है", "मै फल खाया", "मुझ फल खाना", "None"], "correctAnswer": "मुझे फल खाना है"},
            {"text": "मिलान करें: फल --- ?", "options": ["आम", "कलम", "किताब", "घर"], "correctAnswer": "आम"},
            {"text": "भूतकाल का उदाहरण?", "options": ["वह गया", "वह जाता है", "वह जाएगा", "जाओ"], "correctAnswer": "वह गया"},
            {"text": "'देव' का स्त्रीलिंग?", "options": ["देवी", "माता", "बहन", "स्त्री"], "correctAnswer": "देवी"},
            {"text": "'चिड़िया' का बहुवचन?", "options": ["चिड़ियाँ", "चिड़िये", "चिड़ियों", "चिड़िया"], "correctAnswer": "चिड़ियाँ"},
            {"text": "'बादल' का पर्यायवाची?", "options": ["मेघ", "पानी", "आग", "नभ"], "correctAnswer": "मेघ"}
        ]
    }
}

# Class 5 Data
class_5_data = {
    "english": {
        "easy": [
            {"text": "Identify the collective noun: 'A herd of elephants'.", "options": ["herd", "elephants", "elephant", "is"], "correctAnswer": "herd"},
            {"text": "Opposite of 'Arrival'?", "options": ["Departure", "Wait", "End", "Go"], "correctAnswer": "Departure"},
            {"text": "Plural of 'City'?", "options": ["Cities", "Citys", "Cityes", "Cityies"], "correctAnswer": "Cities"},
            {"text": "Identify the adjective: 'The tall man'.", "options": ["tall", "man", "The", "is"], "correctAnswer": "tall"},
            {"text": "Which word is a conjunction?", "options": ["And", "Slow", "Very", "Up"], "correctAnswer": "And"},
            {"text": "Past tense of 'Know'?", "options": ["Knew", "Known", "Knows", "Knowing"], "correctAnswer": "Knew"},
            {"text": "Synonym of 'Happy'?", "options": ["Glad", "Sad", "Angry", "Fast"], "correctAnswer": "Glad"},
            {"text": "Opposite of 'Quick'?", "options": ["Slow", "Fast", "Up", "Big"], "correctAnswer": "Slow"},
            {"text": "Which is an animal?", "options": ["Lion", "Rose", "Pen", "Apple"], "correctAnswer": "Lion"},
            {"text": "A bird has ___.", "options": ["Wings", "Hands", "Horns", "Wheel"], "correctAnswer": "Wings"}
        ],
        "medium": [
            {"text": "Which is an abstract noun?", "options": ["Kindness", "Table", "Dog", "Delhi"], "correctAnswer": "Kindness"},
            {"text": "A person who flies space ships?", "options": ["Astronaut", "Pilot", "Driver", "Sailor"], "correctAnswer": "Astronaut"},
            {"text": "Which is an exclamation?", "options": ["Wow!", "Hello", "Bye", "Okay"], "correctAnswer": "Wow!"},
            {"text": "Superlative of 'Small'?", "options": ["Smallest", "Smaller", "More small", "Small"], "correctAnswer": "Smallest"},
            {"text": "Antonym of 'Smooth'?", "options": ["Rough", "Soft", "Hard", "Big"], "correctAnswer": "Rough"},
            {"text": "Plural of 'Leaf'?", "options": ["Leaves", "Leafs", "Leafes", "Leaf"], "correctAnswer": "Leaves"},
            {"text": "Identify the adverb: 'He writes neatly'.", "options": ["neatly", "writes", "He", "is"], "correctAnswer": "neatly"},
            {"text": "Use 'a' or 'an': ___ umbrella.", "options": ["An", "A", "The", "Some"], "correctAnswer": "An"},
            {"text": "Synonym of 'Tiny'?", "options": ["Small", "Huge", "Large", "Big"], "correctAnswer": "Small"},
            {"text": "Which is a conjunction?", "options": ["But", "Run", "Fast", "Happy"], "correctAnswer": "But"}
        ],
        "hard": [
            {"text": "Identify the silent letter in 'Honest'.", "options": ["H", "o", "n", "e"], "correctAnswer": "H"},
            {"text": "Meaning of 'Vulnerable'?", "options": ["Weak (easily hurt)", "Strong", "Fast", "Brave"], "correctAnswer": "Weak (easily hurt)"},
            {"text": "Identify the conjunction: 'Neither...nor'.", "options": ["Both words", "Neither", "nor", "None"], "correctAnswer": "Both words"},
            {"text": "Meaning of 'Call it a day'?", "options": ["Stop working", "Start working", "Good morning", "Next day"], "correctAnswer": "Stop working"},
            {"text": "Which is a complex sentence?", "options": ["Since it was raining, we stayed home.", "We stayed home.", "It was raining and we stayed home.", "Stay home!"], "correctAnswer": "Since it was raining, we stayed home."},
            {"text": "Correct spelling?", "options": ["Accommodation", "Acomodation", "Accomodation", "Acommodation"], "correctAnswer": "Accommodation"},
            {"text": "Antonym of 'Generous'?", "options": ["Selfish", "Kind", "Helpful", "Rich"], "correctAnswer": "Selfish"},
            {"text": "Identify the preposition: 'The bird flew over the hills'.", "options": ["over", "flew", "hills", "bird"], "correctAnswer": "over"},
            {"text": "Plural of 'Thesis'?", "options": ["Theses", "Thesises", "Thesis", "None"], "correctAnswer": "Theses"},
            {"text": "Identify the indirect object: 'He gave me a gift'.", "options": ["me", "gift", "He", "gave"], "correctAnswer": "me"}
        ]
    },
    "maths": {
        "easy": [
            {"text": "1000 + 1000 = ?", "options": ["2000", "1000", "3000", "4000"], "correctAnswer": "2000"},
            {"text": "2000 - 500 = ?", "options": ["1500", "1000", "500", "2000"], "correctAnswer": "1500"},
            {"text": "What is 10 \u00d7 10?", "options": ["100", "20", "10", "1000"], "correctAnswer": "100"},
            {"text": "Square root of 25?", "options": ["5", "4", "6", "10"], "correctAnswer": "5"},
            {"text": "Add: 250 + 250", "options": ["500", "450", "600", "550"], "correctAnswer": "500"},
            {"text": "Subtract: 100 - 10", "options": ["90", "80", "100", "10"], "correctAnswer": "90"},
            {"text": "What is 12 \u00d7 2?", "options": ["24", "14", "36", "12"], "correctAnswer": "24"},
            {"text": "Next number: 5, 10, 15, ___?", "options": ["20", "25", "30", "15"], "correctAnswer": "20"},
            {"text": "Corners in a hexagon?", "options": ["6", "5", "4", "3"], "correctAnswer": "6"},
            {"text": "Half of 100 is ___.", "options": ["50", "25", "75", "10"], "correctAnswer": "50"}
        ],
        "medium": [
            {"text": "LCM of 4 and 8?", "options": ["8", "4", "12", "16"], "correctAnswer": "8"},
            {"text": "What is 25% of 400?", "options": ["100", "50", "200", "10"], "correctAnswer": "100"},
            {"text": "Average of 10, 20, 30?", "options": ["20", "15", "30", "10"], "correctAnswer": "20"},
            {"text": "1/2 + 1/4 = ?", "options": ["3/4", "1/2", "1/4", "1"], "correctAnswer": "3/4"},
            {"text": "Perimeter of square (side=10)", "options": ["40", "20", "100", "10"], "correctAnswer": "40"},
            {"text": "Area of rectangle (L=10, W=5)", "options": ["50", "15", "30", "20"], "correctAnswer": "50"},
            {"text": "Solve: 2x = 50", "options": ["25", "50", "100", "10"], "correctAnswer": "25"},
            {"text": "Third of 90 is ___.", "options": ["30", "10", "20", "40"], "correctAnswer": "30"},
            {"text": "A right angle is ___ degrees.", "options": ["90", "180", "360", "45"], "correctAnswer": "90"},
            {"text": "Sum of angles in a triangle?", "options": ["180", "90", "360", "270"], "correctAnswer": "180"}
        ],
        "hard": [
            {"text": "HCF of 12 and 18?", "options": ["6", "2", "3", "12"], "correctAnswer": "6"},
            {"text": "Solve: 10 + 20 \u00f7 2", "options": ["20", "15", "25", "10"], "correctAnswer": "20"},
            {"text": "Area of square (side=10)?", "options": ["100", "40", "20", "10"], "correctAnswer": "100"},
            {"text": "Prime factors of 12?", "options": ["2, 2, 3", "2, 6", "3, 4", "1, 12"], "correctAnswer": "2, 2, 3"},
            {"text": "Volume of cube (side=3)", "options": ["27", "9", "18", "6"], "correctAnswer": "27"},
            {"text": "What is 15% of 200?", "options": ["30", "15", "20", "45"], "correctAnswer": "30"},
            {"text": "Simplify: (2+3) \u00d7 (10-5)", "options": ["25", "15", "50", "10"], "correctAnswer": "25"},
            {"text": "Square root of 144?", "options": ["12", "14", "10", "16"], "correctAnswer": "12"},
            {"text": "Ratio of 1m to 20cm?", "options": ["5:1", "1:5", "1:2", "2:1"], "correctAnswer": "5:1"},
            {"text": "Calculate SI: P=100, R=10, T=2", "options": ["20", "10", "100", "50"], "correctAnswer": "20"}
        ]
    },
    "science": {
        "easy": [
            {"text": "Plants capture energy from ___.", "options": ["Sun", "Moon", "Soil", "Water"], "correctAnswer": "Sun"},
            {"text": "Which gas is used for burning?", "options": ["Oxygen", "CO2", "Nitrogen", "Argon"], "correctAnswer": "Oxygen"},
            {"text": "What do we use to see?", "options": ["Eyes", "Ears", "Nose", "Hands"], "correctAnswer": "Eyes"},
            {"text": "Which is a living thing?", "options": ["Cat", "Stone", "Car", "Book"], "correctAnswer": "Cat"},
            {"text": "Part of plant underground?", "options": ["Root", "Stem", "Leaf", "Flower"], "correctAnswer": "Root"},
            {"text": "Water boils at ___ degrees.", "options": ["100", "0", "50", "200"], "correctAnswer": "100"},
            {"text": "Our closest star?", "options": ["Sun", "Moon", "Mars", "Venus"], "correctAnswer": "Sun"},
            {"text": "Animal that gives milk?", "options": ["Cow", "Lion", "Tiger", "Snake"], "correctAnswer": "Cow"},
            {"text": "We breathe in ___.", "options": ["Oxygen", "CO2", "Nitrogen", "Smoke"], "correctAnswer": "Oxygen"},
            {"text": "Fish breathe with ___.", "options": ["Gills", "Lungs", "Nose", "Skin"], "correctAnswer": "Gills"}
        ],
        "medium": [
            {"text": "Process of loss of water by plants?", "options": ["Transpiration", "Evaporation", "Photosynthesis", "Respiration"], "correctAnswer": "Transpiration"},
            {"text": "Air is a ___.", "options": ["Mixture", "Compound", "Element", "None"], "correctAnswer": "Mixture"},
            {"text": "Force that pulls to Earth?", "options": ["Gravity", "Magnetic", "Friction", "Electric"], "correctAnswer": "Gravity"},
            {"text": "Sound travels fastest in ___.", "options": ["Solid", "Liquid", "Gas", "Vacuum"], "correctAnswer": "Solid"},
            {"text": "Largest planet?", "options": ["Jupiter", "Saturn", "Earth", "Mars"], "correctAnswer": "Jupiter"},
            {"text": "Which vitamin from Sun?", "options": ["Vitamin D", "Vitamin A", "Vitamin C", "Vitamin K"], "correctAnswer": "Vitamin D"},
            {"text": "Change from ice to water is ___.", "options": ["Melting", "Freezing", "Boiling", "Cooling"], "correctAnswer": "Melting"},
            {"text": "Unit of force?", "options": ["Newton", "Joule", "Watt", "Meter"], "correctAnswer": "Newton"},
            {"text": "Main gas in air?", "options": ["Nitrogen", "Oxygen", "CO2", "Argon"], "correctAnswer": "Nitrogen"},
            {"text": "Earth rotates on its ___.", "options": ["Axis", "Orbit", "Path", "Ring"], "correctAnswer": "Axis"}
        ],
        "hard": [
            {"text": "Percentage of Nitrogen in air?", "options": ["78%", "21%", "0.03%", "1%"], "correctAnswer": "78%"},
            {"text": "Mitochondria is powerhouse of ___.", "options": ["Cell", "Tissue", "Body", "Atom"], "correctAnswer": "Cell"},
            {"text": "Who discovered Law of Gravity?", "options": ["Newton", "Einstein", "Galileo", "Tesla"], "correctAnswer": "Newton"},
            {"text": "pH of neutral water?", "options": ["7", "0", "14", "1"], "correctAnswer": "7"},
            {"text": "Refraction is bending of ___.", "options": ["Light", "Sound", "Water", "Heat"], "correctAnswer": "Light"},
            {"text": "Chemical formula of salt?", "options": ["NaCl", "H2O", "CO2", "O2"], "correctAnswer": "NaCl"},
            {"text": "Red blood cells carry ___.", "options": ["Oxygen", "Sugar", "Water", "Waste"], "correctAnswer": "Oxygen"},
            {"text": "Speed of Light (m/s)?", "options": ["3 x 10^8", "3 x 10^5", "1 x 10^8", "Sound speed"], "correctAnswer": "3 x 10^8"},
            {"text": "Earth's outer layer?", "options": ["Crust", "Mantle", "Core", "Atmosphere"], "correctAnswer": "Crust"},
            {"text": "Atomic number of Hydrogen?", "options": ["1", "2", "6", "8"], "correctAnswer": "1"}
        ]
    },
    "social-science": {
        "easy": [
            {"text": "Capital of India?", "options": ["New Delhi", "Mumbai", "Kolkata", "Chennai"], "correctAnswer": "New Delhi"},
            {"text": "Red Planet?", "options": ["Mars", "Venus", "Earth", "Jupiter"], "correctAnswer": "Mars"},
            {"text": "National Animal of India?", "options": ["Tiger", "Lion", "Elephant", "Leopard"], "correctAnswer": "Tiger"},
            {"text": "National Bird of India?", "options": ["Peacock", "Parrot", "Sparrow", "Eagle"], "correctAnswer": "Peacock"},
            {"text": "Largest Planet?", "options": ["Jupiter", "Saturn", "Earth", "Mars"], "correctAnswer": "Jupiter"},
            {"text": "Colors in Indian Flag?", "options": ["3", "4", "2", "1"], "correctAnswer": "3"},
            {"text": "Sun rises in the ___.", "options": ["East", "West", "North", "South"], "correctAnswer": "East"},
            {"text": "Identify the continent.", "options": ["Asia", "India", "Delhi", "Mumbai"], "correctAnswer": "Asia"},
            {"text": "National Flower of India?", "options": ["Lotus", "Rose", "Lily", "Sunflower"], "correctAnswer": "Lotus"},
            {"text": "First President of India?", "options": ["Rajendra Prasad", "Nehru", "Patel", "Bose"], "correctAnswer": "Rajendra Prasad"}
        ],
        "medium": [
            {"text": "Longest River in India?", "options": ["Ganga", "Yamuna", "Godavari", "Narmada"], "correctAnswer": "Ganga"},
            {"text": "India Republic Year?", "options": ["1950", "1947", "1952", "1960"], "correctAnswer": "1950"},
            {"text": "Gateway of India is in ___.", "options": ["Mumbai", "Delhi", "Agra", "Jaipur"], "correctAnswer": "Mumbai"},
            {"text": "Taj Mahal is in ___.", "options": ["Agra", "Delhi", "Lucknow", "Jaipur"], "correctAnswer": "Agra"},
            {"text": "Father of the Nation?", "options": ["Gandhiji", "Nehru", "Bose", "Patel"], "correctAnswer": "Gandhiji"},
            {"text": "Smallest State of India?", "options": ["Goa", "Sikkim", "Tripura", "Kerala"], "correctAnswer": "Goa"},
            {"text": "Largest State of India?", "options": ["Rajasthan", "UP", "MP", "Maharashtra"], "correctAnswer": "Rajasthan"},
            {"text": "Pink City of India?", "options": ["Jaipur", "Jodhpur", "Udaipur", "Kota"], "correctAnswer": "Jaipur"},
            {"text": "Silicon Valley of India?", "options": ["Bangalore", "Hyderabad", "Pune", "Chennai"], "correctAnswer": "Bangalore"},
            {"text": "Which is an island country?", "options": ["Sri Lanka", "India", "Nepal", "Bhutan"], "correctAnswer": "Sri Lanka"}
        ],
        "hard": [
            {"text": "Quit India Movement Year?", "options": ["1942", "1920", "1930", "1947"], "correctAnswer": "1942"},
            {"text": "Who wrote national anthem?", "options": ["Tagore", "Bankim Chandra", "Nehru", "Sarojini Naidu"], "correctAnswer": "Tagore"},
            {"text": "First Indian Woman in Space?", "options": ["Kalpana Chawla", "Sunita Williams", "Kiran Bedi", "Pratibha Patil"], "correctAnswer": "Kalpana Chawla"},
            {"text": "Standard Meridian of India?", "options": ["82.5 E", "80 E", "85 E", "90 E"], "correctAnswer": "82.5 E"},
            {"text": "Fundamental Duties Count?", "options": ["11", "10", "12", "6"], "correctAnswer": "11"},
            {"text": "Who invented Zero?", "options": ["Aryabhatta", "Bhaskara", "Varahamihira", "Ramanujan"], "correctAnswer": "Aryabhatta"},
            {"text": "Highest Peak in India?", "options": ["Kanchenjunga", "Everest", "K2", "Nanda Devi"], "correctAnswer": "Kanchenjunga"},
            {"text": "Continent with no countries?", "options": ["Antarctica", "Asia", "Europe", "Africa"], "correctAnswer": "Antarctica"},
            {"text": "Suez Canal connects ___.", "options": ["Med & Red Sea", "Indian & Pacific", "Arctic & Atlantic", "None"], "correctAnswer": "Med & Red Sea"},
            {"text": "Highest Waterfall in World?", "options": ["Angel Falls", "Niagara", "Victoria", "Jog"], "correctAnswer": "Angel Falls"}
        ]
    },
    "hindi": {
        "easy": [
            {"text": "'सेब' क्या है?", "options": ["फल", "सब्जी", "मिठाई", "फूल"], "correctAnswer": "फल"},
            {"text": "'माँ' का पर्यायवाची?", "options": ["माता", "पिता", "भाई", "बहन"], "correctAnswer": "माता"},
            {"text": "'पानी' का पर्यायवाची?", "options": ["जल", "आग", "धूल", "हवा"], "correctAnswer": "जल"},
            {"text": "सूरज किधर से निकलता है?", "options": ["पूर्व", "पश्चिम", "उत्तर", "दक्षिण"], "correctAnswer": "पूर्व"},
            {"text": "घर का पर्यायवाची?", "options": ["आलय", "भोजन", "पानी", "आग"], "correctAnswer": "आलय"},
            {"text": "'बिल्ली' एक ___ है।", "options": ["जानवर", "पक्षी", "कीड़ा", "पेड़"], "correctAnswer": "जानवर"},
            {"text": "फूल का पर्यायवाची?", "options": ["पुष्प", "फल", "जड़", "मिट्टी"], "correctAnswer": "पुष्प"},
            {"text": "रंगों का नाम?", "options": ["लाल", "मेज", "कलम", "किताब"], "correctAnswer": "लाल"},
            {"text": "पेड़ हमें क्या देते हैं?", "options": ["फल/छाया", "आग", "पत्थर", "कपड़े"], "correctAnswer": "फल/छाया"},
            {"text": "'सच' का विलोम?", "options": ["झूठ", "गलत", "बुरा", "आज"], "correctAnswer": "झूठ"}
        ],
        "medium": [
            {"text": "'बड़ा' का विलोम?", "options": ["छोटा", "लंबा", "मोटा", "भारी"], "correctAnswer": "छोटा"},
            {"text": "'दिन' का विलोम?", "options": ["रात", "सुबह", "शाम", "दोपहर"], "correctAnswer": "रात"},
            {"text": "'बादल' का पर्यायवाची?", "options": ["मेघ", "जल", "आग", "भूमि"], "correctAnswer": "मेघ"},
            {"text": "संज्ञा का उदाहरण?", "options": ["रवि", "खाना", "सोना", "उड़ना"], "correctAnswer": "रवि"},
            {"text": "सर्वनाम का उदाहरण?", "options": ["वह", "राम", "दिल्ली", "सुंदर"], "correctAnswer": "वह"},
            {"text": "'लड़का' का बहुवचन?", "options": ["लड़के", "लड़कों", "लड़की", "लड़कियां"], "correctAnswer": "लड़के"},
            {"text": "'शेर' का स्त्रीलिंग?", "options": ["शेरनी", "शेर", "शेरिन", "माता"], "correctAnswer": "शेरनी"},
            {"text": "'९-२-११ होना'?", "options": ["भाग जाना", "पकड़ना", "खेलना", "पढ़ना"], "correctAnswer": "भाग जाना"},
            {"text": "विशेषण का उदाहरण?", "options": ["सुंदर", "खेलना", "भाई", "घर"], "correctAnswer": "सुंदर"},
            {"text": "क्रिया का उदाहरण?", "options": ["खाना", "आम", "लाल", "वह"], "correctAnswer": "खाना"}
        ],
        "hard": [
            {"text": "'उदय' का विलोम?", "options": ["अस्त", "सुबह", "शाम", "आज"], "correctAnswer": "अस्त"},
            {"text": "'आकाश' का पर्यायवाची?", "options": ["नभ", "धरा", "जल", "आग"], "correctAnswer": "नभ"},
            {"text": "'अनोखा' का अर्थ?", "options": ["अजीब/अद्वितीय", "साधारण", "छोटा", "बड़ा"], "correctAnswer": "अजीब/अद्वितीय"},
            {"text": "विद्या + आलय = ?", "options": ["विद्यालय", "विद्याय", "आलय", "विद्य"], "correctAnswer": "विद्यालय"},
            {"text": "'अभिमान' में उपसर्ग?", "options": ["अभि", "मान", "अ", "अनी"], "correctAnswer": "अभि"},
            {"text": "'पढ़ाई' में प्रत्यय?", "options": ["आई", "पढ़", "प", "ई"], "correctAnswer": "आई"},
            {"text": "'आँख का तारा'?", "options": ["बहुत प्यारा", "दुश्मन", "अंधा", "कम तारा"], "correctAnswer": "बहुत प्यारा"},
            {"text": "वर्तमान काल का उदाहरण?", "options": ["वह खाता है", "वह खाया", "वह खाएगा", "खाओ"], "correctAnswer": "वह खाता है"},
            {"text": "सकर्मक क्रिया का उदाहरण?", "options": ["वह फल खाता है", "वह सोता है", "वह रोता है", "वह हँसता है"], "correctAnswer": "वह फल खाता है"},
            {"text": "शुद्ध शब्द?", "options": ["उज्ज्वल", "उजवल", "उज्वल", "उज्जल"], "correctAnswer": "उज्ज्वल"}
        ]
    }
}

add_class_data('class_1', class_1_data)
add_class_data('class_2', class_2_data)
add_class_data('class_3', class_3_data)
add_class_data('class_4', class_4_data)
add_class_data('class_5', class_5_data)

# Class 6 Data
class_6_data = {
    "english": {
        "easy": [
            {"text": "Which word is a noun?", "options": ["Honesty", "Run", "Slowly", "Very"], "correctAnswer": "Honesty"},
            {"text": "Opposite of 'Success'?", "options": ["Failure", "Win", "Try", "Hope"], "correctAnswer": "Failure"},
            {"text": "Identify the pronoun: 'They are playing'.", "options": ["They", "are", "playing", "ball"], "correctAnswer": "They"},
            {"text": "Which word is a preposition?", "options": ["On", "Happy", "Run", "Sweet"], "correctAnswer": "On"},
            {"text": "Plural of 'Fox'?", "options": ["Foxes", "Foxs", "Foxys", "Fox"], "correctAnswer": "Foxes"},
            {"text": "Past tense of 'See'?", "options": ["Saw", "Seen", "Sees", "Seeing"], "correctAnswer": "Saw"},
            {"text": "Synonym of 'Silent'?", "options": ["Quiet", "Loud", "Fast", "Big"], "correctAnswer": "Quiet"},
            {"text": "A person who writes books?", "options": ["Author", "Poet", "Painter", "Singer"], "correctAnswer": "Author"},
            {"text": "Which is an adjective?", "options": ["Beautiful", "Quickly", "Sleep", "Under"], "correctAnswer": "Beautiful"},
            {"text": "I ___ reading a book.", "options": ["am", "is", "are", "do"], "correctAnswer": "am"}
        ],
        "medium": [
            {"text": "Which is a conjunction?", "options": ["Because", "Jump", "Happy", "Sweet"], "correctAnswer": "Because"},
            {"text": "Identify the adverb: 'He writes neatly'.", "options": ["neatly", "writes", "He", "is"], "correctAnswer": "neatly"},
            {"text": "Superlative of 'Good'?", "options": ["Best", "Better", "Goodest", "More good"], "correctAnswer": "Best"},
            {"text": "Collective noun for 'Fish'?", "options": ["School", "Pack", "Flock", "Herd"], "correctAnswer": "School"},
            {"text": "Identify the tense: 'I have eaten'.", "options": ["Present Perfect", "Present Tense", "Past Tense", "Future"], "correctAnswer": "Present Perfect"},
            {"text": "Which is a 'Common Noun'?", "options": ["City", "Delhi", "Ravi", "India"], "correctAnswer": "City"},
            {"text": "Use 'a' or 'an': ___ honest man.", "options": ["An", "A", "The", "Some"], "correctAnswer": "An"},
            {"text": "Antonym of 'Smooth'?", "options": ["Rough", "Soft", "Hard", "Big"], "correctAnswer": "Rough"},
            {"text": "Identify the Verb: 'The sun shines'.", "options": ["shines", "sun", "The", "bright"], "correctAnswer": "shines"},
            {"text": "Which prefix makes 'Possible' opposite?", "options": ["Im", "Un", "Dis", "In"], "correctAnswer": "Im"}
        ],
        "hard": [
            {"text": "Which is a 'Neuter' gender?", "options": ["Table", "Maid", "Uncle", "Niece"], "correctAnswer": "Table"},
            {"text": "Identify the preposition: 'The cat jumped over the fence'.", "options": ["over", "jumped", "cat", "fence"], "correctAnswer": "over"},
            {"text": "Which is a complex sentence?", "options": ["I know that he is honest.", "He is honest.", "He is honest and kind.", "Wait!"], "correctAnswer": "I know that he is honest."},
            {"text": "What is the meaning of 'Call it a day'?", "options": ["Stop working", "Start working", "Good morning", "Next day"], "correctAnswer": "Stop working"},
            {"text": "Plural of 'Radius'?", "options": ["Radii", "Radiuses", "Both", "None"], "correctAnswer": "Radii"},
            {"text": "A figure of speech where 'Like' or 'As' is used?", "options": ["Simile", "Metaphor", "Personification", "Hyperbole"], "correctAnswer": "Simile"},
            {"text": "Which word has a silent 'P'?", "options": ["Psychology", "Phone", "Paper", "Pencil"], "correctAnswer": "Psychology"},
            {"text": "Meaning of 'Vulnerable'?", "options": ["Weak (easily hurt)", "Strong", "Fast", "Brave"], "correctAnswer": "Weak (easily hurt)"},
            {"text": "Identify the Conjunction: 'Neither...nor'.", "options": ["Both words", "Neither", "nor", "None"], "correctAnswer": "Both words"},
            {"text": "The phrase 'The apple of one's eye' means?", "options": ["Very dear", "A fruit eater", "A doctor", "Bad person"], "correctAnswer": "Very dear"}
        ]
    },
    "maths": {
        "easy": [
            {"text": "Smallest prime number?", "options": ["1", "2", "3", "5"], "correctAnswer": "2"},
            {"text": "Sum of 500 + 500?", "options": ["1000", "500", "1500", "2000"], "correctAnswer": "1000"},
            {"text": "Number of sides in a triangle?", "options": ["3", "4", "5", "6"], "correctAnswer": "3"},
            {"text": "What is 10 \u00d7 10?", "options": ["100", "10", "1000", "20"], "correctAnswer": "100"},
            {"text": "Value of 1/2 of 100?", "options": ["50", "25", "75", "100"], "correctAnswer": "50"},
            {"text": "Which number is even?", "options": ["4", "7", "9", "11"], "correctAnswer": "4"},
            {"text": "Place value of 6 in 612?", "options": ["6", "60", "600", "1"], "correctAnswer": "600"},
            {"text": "A circle has ___ angles.", "options": ["0", "180", "360", "90"], "correctAnswer": "0"},
            {"text": "How many millimeters in 1 centimeter?", "options": ["10", "100", "1000", "5"], "correctAnswer": "10"},
            {"text": "What is 100 \u00f7 4?", "options": ["20", "25", "30", "50"], "correctAnswer": "25"}
        ],
        "medium": [
            {"text": "Area of rectangle (L=5, W=2)?", "options": ["7", "10", "14", "15"], "correctAnswer": "10"},
            {"text": "Simplified form of 10/20?", "options": ["1/2", "2/1", "1/4", "5/10"], "correctAnswer": "1/2"},
            {"text": "What is 20% of 200?", "options": ["20", "40", "60", "80"], "correctAnswer": "40"},
            {"text": "LCM of 2, 3, 4?", "options": ["6", "8", "12", "24"], "correctAnswer": "12"},
            {"text": "Perimeter of square (side=10)?", "options": ["10", "20", "40", "100"], "correctAnswer": "40"},
            {"text": "Represent 0.75 as a fraction.", "options": ["3/4", "1/2", "7/5", "1/4"], "correctAnswer": "3/4"},
            {"text": "Solve: 2 + 5 \u00d7 2", "options": ["14", "12", "9", "10"], "correctAnswer": "12"},
            {"text": "How many degrees in a straight line?", "options": ["90", "180", "270", "360"], "correctAnswer": "180"},
            {"text": "If speed is 50km/h, distance in 3 hours?", "options": ["100", "150", "200", "50"], "correctAnswer": "150"},
            {"text": "What is the square of 9?", "options": ["18", "72", "81", "90"], "correctAnswer": "81"}
        ],
        "hard": [
            {"text": "HCF of 45 and 60?", "options": ["5", "15", "30", "45"], "correctAnswer": "15"},
            {"text": "Solve: x + 5 = 10", "options": ["5", "10", "15", "0"], "correctAnswer": "5"},
            {"text": "Volume of cuboid (L=2, W=3, H=4)?", "options": ["9", "12", "24", "48"], "correctAnswer": "24"},
            {"text": "Represent 1:4 as a percentage.", "options": ["10%", "20%", "25%", "40%"], "correctAnswer": "25%"},
            {"text": "What is the ratio of 30cm to 1m?", "options": ["3:1", "1:3", "3:10", "10:3"], "correctAnswer": "3:10"},
            {"text": "Which is an integers?", "options": ["-5", "2.5", "1/2", "0.9"], "correctAnswer": "-5"},
            {"text": "Sum of angles in a quadrilateral?", "options": ["180", "270", "360", "540"], "correctAnswer": "360"},
            {"text": "What is (1/2) \u00f7 (1/4)?", "options": ["2", "1/2", "1/8", "4"], "correctAnswer": "2"},
            {"text": "Cube root of 27?", "options": ["3", "9", "2", "6"], "correctAnswer": "3"},
            {"text": "Value of Pi (\u03c0) approx?", "options": ["3.14", "2.14", "4.14", "1.14"], "correctAnswer": "3.14"}
        ]
    },
    "science": {
        "easy": [
            {"text": "Carbohydrates provide us ___.", "options": ["Energy", "Water", "Oxygen", "Iron"], "correctAnswer": "Energy"},
            {"text": "Herbivores eat ___.", "options": ["Plants", "Meat", "Both", "None"], "correctAnswer": "Plants"},
            {"text": "Water exists in ___ states.", "options": ["3", "1", "2", "4"], "correctAnswer": "3"},
            {"text": "Which part of plant is under soil?", "options": ["Roots", "Leaves", "Stem", "Flower"], "correctAnswer": "Roots"},
            {"text": "Sun is a ___.", "options": ["Star", "Planet", "Moon", "Comet"], "correctAnswer": "Star"},
            {"text": "We get salt from ___.", "options": ["Sea water", "River water", "Rain", "Plants"], "correctAnswer": "Sea water"},
            {"text": "Humans breathe in ___.", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Methane"], "correctAnswer": "Oxygen"},
            {"text": "Example of a magnetic material?", "options": ["Iron", "Gold", "Silver", "Plastic"], "correctAnswer": "Iron"},
            {"text": "Light travels in ___.", "options": ["Straight lines", "Circles", "Zig-zags", "Waves only"], "correctAnswer": "Straight lines"},
            {"text": "Skeleton protects our ___.", "options": ["Internal organs", "Hair", "Nails", "Skin"], "correctAnswer": "Internal organs"}
        ],
        "medium": [
            {"text": "Vitamin C prevents ___.", "options": ["Scurvy", "Rickets", "Night-blindness", "Beriberi"], "correctAnswer": "Scurvy"},
            {"text": "The process of loss of water by plants?", "options": ["Transpiration", "Evaporation", "Photosynthesis", "Respiration"], "correctAnswer": "Transpiration"},
            {"text": "A device used to break an electric circuit?", "options": ["Switch", "Wire", "Bulb", "Battery"], "correctAnswer": "Switch"},
            {"text": "Objects that do not allow light to pass?", "options": ["Opaque", "Transparent", "Translucent", "Clear"], "correctAnswer": "Opaque"},
            {"text": "A compass needle points to ___.", "options": ["North-South", "East-West", "Up-Down", "Left-Right"], "correctAnswer": "North-South"},
            {"text": "Air is a ___.", "options": ["Mixture", "Compound", "Element", "None"], "correctAnswer": "Mixture"},
            {"text": "Joints help in ___.", "options": ["Movement", "Digestion", "Thinking", "Seeing"], "correctAnswer": "Movement"},
            {"text": "Plants capture energy from ___.", "options": ["Sun", "Moon", "Soil", "Water"], "correctAnswer": "Sun"},
            {"text": "Which gas is used for burning?", "options": ["Oxygen", "CO2", "Nitrogen", "Argon"], "correctAnswer": "Oxygen"},
            {"text": "The flat part of a leaf?", "options": ["Lamina", "Petiole", "Stem", "Vein"], "correctAnswer": "Lamina"}
        ],
        "hard": [
            {"text": "Percentage of Nitrogen in air?", "options": ["78%", "21%", "0.03%", "1%"], "correctAnswer": "78%"},
            {"text": "The SI unit of length is ___.", "options": ["Meter", "Centimeter", "Kilometer", "Inch"], "correctAnswer": "Meter"},
            {"text": "Ball and socket joint is in ___.", "options": ["Shoulder", "Knee", "Elbow", "Neck"], "correctAnswer": "Shoulder"},
            {"text": "The process of winnowing uses ___.", "options": ["Wind/Air", "Water", "Magnets", "Sieve"], "correctAnswer": "Wind/Air"},
            {"text": "Condensation is conversion of ___.", "options": ["Vapor to Liquid", "Liquid to Vapor", "Solid to Liquid", "Ice to Water"], "correctAnswer": "Vapor to Liquid"},
            {"text": "Which plant is a carnivorous plant?", "options": ["Pitcher plant", "Neem", "Mango", "Tulsi"], "correctAnswer": "Pitcher plant"},
            {"text": "Pins on a magnet have maximum force at ___.", "options": ["Poles", "Center", "Midway", "Nowhere"], "correctAnswer": "Poles"},
            {"text": "The protective layer of Earth from UV rays?", "options": ["Ozone", "Oxygen", "Nitrogen", "Space"], "correctAnswer": "Ozone"},
            {"text": "Refraction is the ___ of light.", "options": ["Bending", "Bouncing", "Stopping", "Coloring"], "correctAnswer": "Bending"},
            {"text": "Root nodules contain ___ bacteria.", "options": ["Nitrogen-fixing", "Oxygen-fixing", "Harmful", "Dead"], "correctAnswer": "Nitrogen-fixing"}
        ]
    },
    "social-science": {
        "easy": [
            {"text": "Earth is the ___ planet from Sun.", "options": ["Third", "First", "Second", "Fourth"], "correctAnswer": "Third"},
            {"text": "Who was the first Prime Minister of India?", "options": ["J.L. Nehru", "Gandhi", "S.C. Bose", "Indira Gandhi"], "correctAnswer": "J.L. Nehru"},
            {"text": "A globe is a ___ of Earth.", "options": ["Model", "Picture", "Drawing", "Story"], "correctAnswer": "Model"},
            {"text": "India got Independence in ___.", "options": ["1947", "1950", "1942", "1960"], "correctAnswer": "1947"},
            {"text": "Which is a major ocean?", "options": ["Pacific", "Ganges", "Amazon", "Sahara"], "correctAnswer": "Pacific"},
            {"text": "Democracy means rule by ___.", "options": ["People", "King", "Army", "God"], "correctAnswer": "People"},
            {"text": "Capital of India?", "options": ["New Delhi", "Mumbai", "Kolkata", "Chennai"], "correctAnswer": "New Delhi"},
            {"text": "Himalayas are in the ___ of India.", "options": ["North", "South", "East", "West"], "correctAnswer": "North"},
            {"text": "Early humans were ___.", "options": ["Hunters-Gatherers", "Engineers", "Doctors", "Farmers (later)"], "correctAnswer": "Hunters-Gatherers"},
            {"text": "The spinning of Earth is ___.", "options": ["Rotation", "Revolution", "Orbit", "Gravity"], "correctAnswer": "Rotation"}
        ],
        "medium": [
            {"text": "Line that divides Earth into North/South?", "options": ["Equator", "Prime Meridian", "Tropic of Cancer", "Axis"], "correctAnswer": "Equator"},
            {"text": "Vedas are written in ___.", "options": ["Sanskrit", "Hindi", "Tamil", "English"], "correctAnswer": "Sanskrit"},
            {"text": "How many states in India?", "options": ["28", "25", "29", "30"], "correctAnswer": "28"},
            {"text": "The blue planet is ___.", "options": ["Earth", "Mars", "Venus", "Jupiter"], "correctAnswer": "Earth"},
            {"text": "Gram Panchayat is headed by ___.", "options": ["Sarpanch", "Mayor", "Governor", "PM"], "correctAnswer": "Sarpanch"},
            {"text": "Manuscripts were written on ___.", "options": ["Palm leaf/Birch bark", "Paper", "Stone", "Plastic"], "correctAnswer": "Palm leaf/Birch bark"},
            {"text": "The coldest continent is ___.", "options": ["Antarctica", "Asia", "Africa", "Europe"], "correctAnswer": "Antarctica"},
            {"text": "A leap year has ___ days.", "options": ["366", "365", "300", "400"], "correctAnswer": "366"},
            {"text": "Ashoka was a ruler of ___ dynasty.", "options": ["Mauryan", "Gupta", "Mughal", "British"], "correctAnswer": "Mauryan"},
            {"text": "Discrimination means ___.", "options": ["Unfair treatment", "Equal treatment", "Helping others", "Fairness"], "correctAnswer": "Unfair treatment"}
        ],
        "hard": [
            {"text": "The Prime Meridian passes through ___.", "options": ["Greenwich", "Delhi", "New York", "Cairo"], "correctAnswer": "Greenwich"},
            {"text": "What is 'Suffrage'?", "options": ["Right to vote", "Right to property", "Suffering", "Tax"], "correctAnswer": "Right to vote"},
            {"text": "Which continent is an 'Island Continent'?", "options": ["Australia", "Africa", "South America", "Asia"], "correctAnswer": "Australia"},
            {"text": "Oldest Veda is ___.", "options": ["Rigveda", "Samaveda", "Yajurveda", "Atharvaveda"], "correctAnswer": "Rigveda"},
            {"text": "Magadha was located in present-day ___.", "options": ["Bihar", "Punjab", "Gujarat", "Kerala"], "correctAnswer": "Bihar"},
            {"text": "The gas that protects us from UV rays?", "options": ["Ozone", "Oxygen", "CO2", "Nitrogen"], "correctAnswer": "Ozone"},
            {"text": "Who is the 'Father of Indian Constitution'?", "options": ["B.R. Ambedkar", "Gandhi", "Nehru", "Patel"], "correctAnswer": "B.R. Ambedkar"},
            {"text": "The movement of Earth around the Sun?", "options": ["Revolution", "Rotation", "Spinning", "Orbit"], "correctAnswer": "Revolution"},
            {"text": "Indus Valley Civilization main cities?", "options": ["Harappa/Mohenjo-daro", "Delhi/Mumbai", "Kolkata/Chennai", "London/Paris"], "correctAnswer": "Harappa/Mohenjo-daro"},
            {"text": "What is 'Apartheid'?", "options": ["Racial separation", "Racial equality", "Freedom", "Unity"], "correctAnswer": "Racial separation"}
        ]
    },
    "hindi": {
        "easy": [
            {"text": "हिंदी वर्णमाला में कितने स्वर हैं?", "options": ["11", "33", "44", "25"], "correctAnswer": "11"},
            {"text": "'दिन' का विलोम शब्द क्या है?", "options": ["रात", "सुबह", "शाम", "दोपहर"], "correctAnswer": "रात"},
            {"text": "'पुष्प' का पर्यायवाची शब्द?", "options": ["फूल", "फल", "पेड़", "जड़"], "correctAnswer": "फूल"},
            {"text": "एक हाथ में कितनी उंगलियाँ होती हैं?", "options": ["पाँच", "चार", "छह", "दस"], "correctAnswer": "पाँच"},
            {"text": "'आम' कैसा फल है?", "options": ["मीठा", "खट्टा", "कड़वा", "तीखा"], "correctAnswer": "मीठा"},
            {"text": "हमारा राष्ट्रीय पक्षी कौन है?", "options": ["मोर", "तोता", "चिड़िया", "हंस"], "correctAnswer": "मोर"},
            {"text": "आसमान का रंग कैसा है?", "options": ["नीला", "लाल", "हरा", "काला"], "correctAnswer": "नीला"},
            {"text": "'क' के बाद कौन सा अक्षर आता है?", "options": ["ख", "ग", "घ", "च"], "correctAnswer": "ख"},
            {"text": "'सेब' क्या है?", "options": ["फल", "सब्जी", "फूल", "पेड़"], "correctAnswer": "फल"},
            {"text": "'बड़ा' का विलोम शब्द?", "options": ["छोटा", "आज", "कल", "मोठा"], "correctAnswer": "छोटा"}
        ],
        "medium": [
            {"text": "'आँख का तारा' मुहावरे का अर्थ?", "options": ["बहुत प्यारा", "दुश्मन", "अंधा", "कम दिखना"], "correctAnswer": "बहुत प्यारा"},
            {"text": "'लड़का' का स्त्रीलिंग क्या है?", "options": ["लड़की", "माता", "बहन", "स्त्री"], "correctAnswer": "लड़की"},
            {"text": "'बादल' का पर्यायवाची शब्द?", "options": ["मेघ", "सूरज", "पवन", "अग्नि"], "correctAnswer": "मेघ"},
            {"text": "'जीवन' का विलोम शब्द क्या है?", "options": ["मरण", "मृत्यु", "दोनों", "शांति"], "correctAnswer": "दोनों"},
            {"text": "संज्ञा के कितने भेद होते हैं?", "options": ["3", "4", "5", "2"], "correctAnswer": "3"},
            {"text": "'९-२-११ होना' मुहावरे का अर्थ?", "options": ["भाग जाना", "पकड़ना", "खेलना", "पढ़ना"], "correctAnswer": "भाग जाना"},
            {"text": "भाषा के कितने रूप होते हैं?", "options": ["2", "3", "4", "1"], "correctAnswer": "2"},
            {"text": "'ईमानदार' का विलोम शब्द?", "options": ["बेईमान", "झूठा", "चोर", "बुरा"], "correctAnswer": "बेईमान"},
            {"text": "'चमक' का पर्यायवाची शब्द?", "options": ["प्रभा", "अंधेरा", "रात", "दिन"], "correctAnswer": "प्रभा"},
            {"text": "विशेषण किसकी विशेषता बताता है?", "options": ["संज्ञा/सर्वनाम", "क्रिया", "नाम", "काम"], "correctAnswer": "संज्ञा/सर्वनाम"}
        ],
        "hard": [
            {"text": "'नाक में दम करना' मुहावरे का अर्थ?", "options": ["बहुत परेशान करना", "प्यार करना", "सुझाव देना", "खेलना"], "correctAnswer": "बहुत परेशान करना"},
            {"text": "'परोपकार' का क्या अर्थ है?", "options": ["दूसरों की भलाई", "अपना काम", "पढ़ाई", "खेल"], "correctAnswer": "दूसरों की भलाई"},
            {"text": "'अग्नि' का पर्यायवाची नहीं है:", "options": ["नीर", "आग", "पावक", "अनल"], "correctAnswer": "नीर"},
            {"text": "'आस्तिक' का विलोम शब्द क्या है?", "options": ["नास्तिक", "धार्मिक", "भक्त", "ज्ञानी"], "correctAnswer": "नास्तिक"},
            {"text": "सर्वनाम के कितने भेद होते हैं?", "options": ["6", "4", "5", "7"], "correctAnswer": "6"},
            {"text": "'जिसका कोई अंत न हो' के लिए एक शब्द?", "options": ["अनंत", "अमर", "अजर", "अमिट"], "correctAnswer": "अनंत"},
            {"text": "'हाथ मलना' मुहावरे का अर्थ?", "options": ["पछताना", "लिखना", "खेती करना", "सोना"], "correctAnswer": "पछताना"},
            {"text": "'अग्रज' का विलोम शब्द?", "options": ["अनुज", "भाई", "छोटा", "शिष्य"], "correctAnswer": "अनुज"},
            {"text": "क्रिया के मूल रूप को क्या कहते हैं?", "options": ["धातु", "शब्द", "स्वर", "व्यंजन"], "correctAnswer": "धातु"},
            {"text": "'गणतंत्र दिवस' कब मनाया जाता है?", "options": ["26 जनवरी", "15 अगस्त", "2 अक्टूबर", "14 नवम्बर"], "correctAnswer": "26 जनवरी"}
        ]
    }
}

add_class_data('class_6', class_6_data)

# Class 7 Data
class_7_data = {
    "english": {
        "easy": [
            {"text": "Which word is a noun?", "options": ["Honesty", "Run", "Fast", "Very"], "correctAnswer": "Honesty"},
            {"text": "Opposite of 'Success'?", "options": ["Failure", "Win", "Try", "Hope"], "correctAnswer": "Failure"},
            {"text": "Identify the pronoun: 'They are playing'.", "options": ["They", "are", "playing", "ball"], "correctAnswer": "They"},
            {"text": "Which word is a preposition?", "options": ["Under", "Happy", "Run", "Slowly"], "correctAnswer": "Under"},
            {"text": "Plural of 'Man'?", "options": ["Men", "Mans", "Manes", "Man"], "correctAnswer": "Men"},
            {"text": "Past tense of 'Go'?", "options": ["Went", "Gone", "Goes", "Going"], "correctAnswer": "Went"},
            {"text": "Synonym of 'Large'?", "options": ["Big", "Small", "Tiny", "Little"], "correctAnswer": "Big"},
            {"text": "Identify the adjective: 'The red car'.", "options": ["red", "car", "The", "is"], "correctAnswer": "red"},
            {"text": "I ___ a student.", "options": ["am", "is", "are", "do"], "correctAnswer": "am"},
            {"text": "Which is an animal?", "options": ["Tiger", "Apple", "Car", "Table"], "correctAnswer": "Tiger"}
        ],
        "medium": [
            {"text": "Which is a conjunction?", "options": ["And", "Blue", "Fast", "Jump"], "correctAnswer": "And"},
            {"text": "Identify the adverb: 'He runs quickly'.", "options": ["quickly", "runs", "He", "is"], "correctAnswer": "quickly"},
            {"text": "Superlative of 'Bad'?", "options": ["Worst", "Worse", "Baddest", "More bad"], "correctAnswer": "Worst"},
            {"text": "Collective noun for 'Soldiers'?", "options": ["Army", "Pack", "Flock", "Herd"], "correctAnswer": "Army"},
            {"text": "Identify the tense: 'I will eat'.", "options": ["Future", "Present", "Past", "None"], "correctAnswer": "Future"},
            {"text": "Which is a 'Proper Noun'?", "options": ["India", "Country", "State", "City"], "correctAnswer": "India"},
            {"text": "Use 'a' or 'an': ___ umbrella.", "options": ["An", "A", "The", "Some"], "correctAnswer": "An"},
            {"text": "Antonym of 'Smooth'?", "options": ["Rough", "Soft", "Hard", "Big"], "correctAnswer": "Rough"},
            {"text": "Identify the Verb: 'She sings sweetly'.", "options": ["sings", "She", "sweetly", "is"], "correctAnswer": "sings"},
            {"text": "A person who teaches is a ___.", "options": ["Teacher", "Doctor", "Farmer", "Driver"], "correctAnswer": "Teacher"}
        ],
        "hard": [
            {"text": "Which is a silent letter in 'Honest'?", "options": ["H", "o", "n", "e"], "correctAnswer": "H"},
            {"text": "Identify the preposition: 'The book is on the table'.", "options": ["on", "book", "is", "table"], "correctAnswer": "on"},
            {"text": "Which is a 'Neuter' gender noun?", "options": ["Building", "King", "Maid", "Uncle"], "correctAnswer": "Building"},
            {"text": "Meaning of the idiom 'Under the weather'?", "options": ["Feeling sick", "Feeling happy", "Raining", "Sunny"], "correctAnswer": "Feeling sick"},
            {"text": "Identify the complex sentence.", "options": ["Because it was raining, we stayed home.", "We stayed home.", "It was raining and we stayed home.", "Stay home!"], "correctAnswer": "Because it was raining, we stayed home."},
            {"text": "Plural of 'Thesis'?", "options": ["Theses", "Thesises", "Thesis", "None"], "correctAnswer": "Theses"},
            {"text": "What is 'Alliteration'?", "options": ["Repetition of same consonant sounds", "Comparing two things", "Rhyming", "Exaggeration"], "correctAnswer": "Repetition of same consonant sounds"},
            {"text": "Which word is spelled correctly?", "options": ["Accommodation", "Acomodation", "Accomodation", "Acommodation"], "correctAnswer": "Accommodation"},
            {"text": "Antonym of 'Benevolent'?", "options": ["Malevolent", "Kind", "Strong", "Fast"], "correctAnswer": "Malevolent"},
            {"text": "Identify the direct object: 'He gave me a pen'.", "options": ["pen", "me", "He", "gave"], "correctAnswer": "pen"}
        ]
    },
    "maths": {
        "easy": [
            {"text": "What is 7 + 8?", "options": ["14", "15", "16", "17"], "correctAnswer": "15"},
            {"text": "Smallest odd prime number?", "options": ["3", "1", "2", "5"], "correctAnswer": "3"},
            {"text": "Number of vertices in a square?", "options": ["4", "3", "5", "6"], "correctAnswer": "4"},
            {"text": "What is 12 \u00d7 12?", "options": ["124", "144", "24", "100"], "correctAnswer": "144"},
            {"text": "Value of 1/4 + 1/4?", "options": ["1/2", "1/4", "1/8", "1"], "correctAnswer": "1/2"},
            {"text": "Which number is even?", "options": ["10", "11", "13", "15"], "correctAnswer": "10"},
            {"text": "How many cents in 1 dollar?", "options": ["100", "10", "1000", "50"], "correctAnswer": "100"},
            {"text": "A triangle with all sides equal is ___.", "options": ["Equilateral", "Isosceles", "Scalene", "Right-angled"], "correctAnswer": "Equilateral"},
            {"text": "What is 10 \u00d7 0.5?", "options": ["5", "50", "0.5", "1"], "correctAnswer": "5"},
            {"text": "Solve: 100 - 50 - 10", "options": ["40", "50", "60", "30"], "correctAnswer": "40"}
        ],
        "medium": [
            {"text": "Area of square with side 5cm?", "options": ["20sq cm", "25sq cm", "10sq cm", "50sq cm"], "correctAnswer": "25sq cm"},
            {"text": "Solve: 2x = 20", "options": ["10", "20", "5", "40"], "correctAnswer": "10"},
            {"text": "LCM of 12 and 15?", "options": ["60", "30", "120", "180"], "correctAnswer": "60"},
            {"text": "What is 25% of 400?", "options": ["100", "50", "200", "10"], "correctAnswer": "100"},
            {"text": "Perimeter of rectangle (L=10, W=5)?", "options": ["30", "15", "50", "20"], "correctAnswer": "30"},
            {"text": "Average of 4, 8, 12?", "options": ["8", "4", "12", "6"], "correctAnswer": "8"},
            {"text": "Solve: 3 + 2 \u00d7 5", "options": ["13", "25", "15", "10"], "correctAnswer": "13"},
            {"text": "Convert 1/5 to percentage.", "options": ["20%", "10%", "50%", "5%"], "correctAnswer": "20%"},
            {"text": "Sum of angles in a triangle is ___ degrees.", "options": ["180", "90", "360", "270"], "correctAnswer": "180"},
            {"text": "If speed = 60km/h, distance in 1.5 hours?", "options": ["90km", "60km", "120km", "40km"], "correctAnswer": "90km"}
        ],
        "hard": [
            {"text": "HCF of 48 and 72?", "options": ["24", "12", "48", "6"], "correctAnswer": "24"},
            {"text": "Solve: x/2 + 5 = 15", "options": ["20", "10", "30", "40"], "correctAnswer": "20"},
            {"text": "Volume of cube with side 4cm?", "options": ["64", "16", "32", "48"], "correctAnswer": "64"},
            {"text": "Express 0.125 as a fraction.", "options": ["1/8", "1/4", "1/2", "1/10"], "correctAnswer": "1/8"},
            {"text": "Ratio of 500g to 2kg is ___.", "options": ["1:4", "4:1", "1:2", "2:1"], "correctAnswer": "1:4"},
            {"text": "Square root of 225?", "options": ["15", "25", "5", "12"], "correctAnswer": "15"},
            {"text": "Number of edges in a triangular prism?", "options": ["9", "6", "12", "5"], "correctAnswer": "9"},
            {"text": "If (a/b) = (c/d), then ad = ___.", "options": ["bc", "ad", "1", "0"], "correctAnswer": "bc"},
            {"text": "Calculate Simple Interest: P=1000, R=10%, T=1 year.", "options": ["100", "1000", "10", "50"], "correctAnswer": "100"},
            {"text": "Value of Pi (\u03c0) up to 2 decimal places?", "options": ["3.14", "3.16", "3.12", "3.00"], "correctAnswer": "3.14"}
        ]
    },
    "science": {
        "easy": [
            {"text": "Plants make food by ___.", "options": ["Photosynthesis", "Respiration", "Evaporation", "Digestion"], "correctAnswer": "Photosynthesis"},
            {"text": "Which plant is an insectivore?", "options": ["Pitcher plant", "Neem", "Rose", "Mango"], "correctAnswer": "Pitcher plant"},
            {"text": "Human body has ___ pairs of ribs.", "options": ["12", "10", "24", "11"], "correctAnswer": "12"},
            {"text": "Which gas is needed for breathing?", "options": ["Oxygen", "CO2", "Nitrogen", "Argon"], "correctAnswer": "Oxygen"},
            {"text": "Skeleton protects our ___.", "options": ["Internal organs", "Hair", "Skin", "Nails"], "correctAnswer": "Internal organs"},
            {"text": "Ice melts into water at ___.", "options": ["0\u00b0C", "100\u00b0C", "50\u00b0C", "10\u00b0C"], "correctAnswer": "0\u00b0C"},
            {"text": "Which part of plant absorbs water?", "options": ["Roots", "Leaves", "Stem", "Flower"], "correctAnswer": "Roots"},
            {"text": "The boiling point of water is ___.", "options": ["100\u00b0C", "0\u00b0C", "200\u00b0C", "50\u00b0C"], "correctAnswer": "100\u00b0C"},
            {"text": "A battery has ___ terminals.", "options": ["2", "1", "3", "4"], "correctAnswer": "2"},
            {"text": "The moon reflects light from ___.", "options": ["Sun", "Earth", "Stars", "Bulb"], "correctAnswer": "Sun"}
        ],
        "medium": [
            {"text": "Which organ filters waste from blood?", "options": ["Kidney", "Heart", "Lungs", "Brain"], "correctAnswer": "Kidney"},
            {"text": "Process of conversion of liquid to vapor?", "options": ["Evaporation", "Condensation", "Freezing", "Melting"], "correctAnswer": "Evaporation"},
            {"text": "A shadow is formed by ___ objects.", "options": ["Opaque", "Transparent", "Translucent", "Soft"], "correctAnswer": "Opaque"},
            {"text": "Which vitamin is made in our body by sunlight?", "options": ["Vitamin D", "Vitamin A", "Vitamin C", "Vitamin K"], "correctAnswer": "Vitamin D"},
            {"text": "Rusting of iron is a ___ change.", "options": ["Chemical", "Physical", "Both", "None"], "correctAnswer": "Chemical"},
            {"text": "Earth completes one rotation in ___.", "options": ["24 hours", "365 days", "1 month", "12 hours"], "correctAnswer": "24 hours"},
            {"text": "Which gas is used for extinguishing fire?", "options": ["Carbon Dioxide", "Oxygen", "Nitrogen", "Hydrogen"], "correctAnswer": "Carbon Dioxide"},
            {"text": "Sound cannot travel through ___.", "options": ["Vacuum", "Water", "Air", "Steel"], "correctAnswer": "Vacuum"},
            {"text": "Digestion begins in the ___.", "options": ["Mouth", "Stomach", "Intestine", "Liver"], "correctAnswer": "Mouth"},
            {"text": "Movement of plant roots towards water is ___.", "options": ["Hydrotropism", "Phototropism", "Geotropism", "None"], "correctAnswer": "Hydrotropism"}
        ],
        "hard": [
            {"text": "Percentage of Nitrogen in atmosphere?", "options": ["78%", "21%", "0.03%", "1%"], "correctAnswer": "78%"},
            {"text": "The power house of a cell is ___.", "options": ["Mitochondria", "Nucleus", "Ribosome", "Golgi Body"], "correctAnswer": "Mitochondria"},
            {"text": "Unit of atmospheric pressure is ___.", "options": ["Pascal/Bar", "Newton", "Joule", "Watt"], "correctAnswer": "Pascal/Bar"},
            {"text": "Acid found in lemons?", "options": ["Citric acid", "Acetic acid", "Lactic acid", "Butyric acid"], "correctAnswer": "Citric acid"},
            {"text": "The focal length of a plane mirror is ___.", "options": ["Infinity", "Zero", "10cm", "20cm"], "correctAnswer": "Infinity"},
            {"text": "Which gas completes the bulb filament protection?", "options": ["Argon", "Oxygen", "Hydrogen", "CO2"], "correctAnswer": "Argon"},
            {"text": "Human eye contains a ___ lens.", "options": ["Convex", "Concave", "Cylindrical", "None"], "correctAnswer": "Convex"},
            {"text": "The splitting of light into seven colors?", "options": ["Dispersion", "Reflection", "Refraction", "Bending"], "correctAnswer": "Dispersion"},
            {"text": "What is the pH of pure water?", "options": ["7", "1", "14", "0"], "correctAnswer": "7"},
            {"text": "The layer of atmosphere that contains Ozone?", "options": ["Stratosphere", "Troposphere", "Mesosphere", "Exosphere"], "correctAnswer": "Stratosphere"}
        ]
    },
    "social-science": {
        "easy": [
            {"text": "Who is called Father of the Nation?", "options": ["Mahatma Gandhi", "J.L. Nehru", "Subhash Bose", "Patel"], "correctAnswer": "Mahatma Gandhi"},
            {"text": "The Red Planet is ___.", "options": ["Mars", "Venus", "Earth", "Jupiter"], "correctAnswer": "Mars"},
            {"text": "Largest ocean in the world?", "options": ["Pacific", "Atlantic", "Indian", "Arctic"], "correctAnswer": "Pacific"},
            {"text": "Capital of India?", "options": ["New Delhi", "Mumbai", "Kolkata", "Chennai"], "correctAnswer": "New Delhi"},
            {"text": "Independence Day of India?", "options": ["August 15", "January 26", "October 2", "November 14"], "correctAnswer": "August 15"},
            {"text": "Who built the Taj Mahal?", "options": ["Shah Jahan", "Akbar", "Humayun", "Babar"], "correctAnswer": "Shah Jahan"},
            {"text": "Which is an island country?", "options": ["Sri Lanka", "India", "Nepal", "China"], "correctAnswer": "Sri Lanka"},
            {"text": "The sun rises in the ___.", "options": ["East", "West", "North", "South"], "correctAnswer": "East"},
            {"text": "World's largest desert?", "options": ["Sahara", "Gobi", "Thar", "Atacama"], "correctAnswer": "Sahara"},
            {"text": "How many continents are there?", "options": ["7", "5", "6", "8"], "correctAnswer": "7"}
        ],
        "medium": [
            {"text": "Where is the head office of UNO?", "options": ["New York", "London", "Paris", "Geneva"], "correctAnswer": "New York"},
            {"text": "Who initiated the Green Revolution?", "options": ["M.S. Swaminathan", "Verghese Kurien", "H. Khorana", "None"], "correctAnswer": "M.S. Swaminathan"},
            {"text": "Which is the smallest continent?", "options": ["Australia", "Europe", "Africa", "South America"], "correctAnswer": "Australia"},
            {"text": "Line that divides Earth into East/West?", "options": ["Prime Meridian", "Equator", "Tropic of Cancer", "Axis"], "correctAnswer": "Prime Meridian"},
            {"text": "The Parliament house is in ___.", "options": ["New Delhi", "Mumbai", "Kolkata", "Chennai"], "correctAnswer": "New Delhi"},
            {"text": "Who was the first President of India?", "options": ["Rajendra Prasad", "Nehru", "Radhakrishnan", "Patel"], "correctAnswer": "Rajendra Prasad"},
            {"text": "Official language of India as per Constitution?", "options": ["Hindi (Devanagari)", "English", "Sanskrit", "Tamil"], "correctAnswer": "Hindi (Devanagari)"},
            {"text": "Varanasi is located on the bank of ___.", "options": ["Ganges", "Yamuna", "Godavari", "Krishna"], "correctAnswer": "Ganges"},
            {"text": "The cold continent is ___.", "options": ["Antarctica", "Asia", "Africa", "Europe"], "correctAnswer": "Antarctica"},
            {"text": "Discovery of India was written by ___.", "options": ["J.L. Nehru", "Gandhi", "Tagore", "Premchand"], "correctAnswer": "J.L. Nehru"}
        ],
        "hard": [
            {"text": "Who gave the slogan 'Swaraj is my birthright'?", "options": ["Bal Gangadhar Tilak", "Gandhi", "Nehru", "Subhash Bose"], "correctAnswer": "Bal Gangadhar Tilak"},
            {"text": "What is the duration of Rajya Sabha member?", "options": ["6 years", "5 years", "2 years", "Lifetime"], "correctAnswer": "6 years"},
            {"text": "Oldest range of mountains in India?", "options": ["Aravallis", "Himalayas", "Vindhyas", "Sahyadri"], "correctAnswer": "Aravallis"},
            {"text": "When was the Quit India Movement started?", "options": ["1942", "1930", "1920", "1947"], "correctAnswer": "1942"},
            {"text": "The gas that gives protection against Sun's rays in Stratosphere?", "options": ["Ozone", "Oxygen", "Nitrogen", "CO2"], "correctAnswer": "Ozone"},
            {"text": "Who is the custodian of Indian Constitution?", "options": ["Supreme Court", "President", "PM", "Parliament"], "correctAnswer": "Supreme Court"},
            {"text": "The battle of Plassey was fought in ___.", "options": ["1757", "1857", "1764", "1526"], "correctAnswer": "1757"},
            {"text": "India's Standard Meridian passes through ___.", "options": ["Mirzapur", "Delhi", "Mumbai", "Chennai"], "correctAnswer": "Mirzapur"},
            {"text": "Who was the first Sikh Guru?", "options": ["Guru Nanak Dev", "Guru Gobind Singh", "Guru Arjan Dev", "Guru Teg Bahadur"], "correctAnswer": "Guru Nanak Dev"},
            {"text": "What is 'Apartheid' system?", "options": ["Racial discrimination", "Religious freedom", "Political equality", "None"], "correctAnswer": "Racial discrimination"}
        ]
    },
    "hindi": {
        "easy": [
            {"text": "'आज' का विलोम शब्द क्या है?", "options": ["कल", "परसों", "अतीत", "बाद"], "correctAnswer": "कल"},
            {"text": "'माँ' का पर्यायवाची शब्द?", "options": ["माता", "पिता", "भाई", "बहन"], "correctAnswer": "माता"},
            {"text": "एक साल में कितने महीने होते हैं?", "options": ["12", "10", "11", "13"], "correctAnswer": "12"},
            {"text": "'हाथी' को हिंदी में और क्या कहते हैं?", "options": ["गज", "घोड़ा", "शेर", "ऊँट"], "correctAnswer": "गज"},
            {"text": "'मीठा' का विलोम शब्द क्या है?", "options": ["कड़वा", "खट्टा", "नमकीन", "तीखा"], "correctAnswer": "कड़वा"},
            {"text": "भारत की राजधानी क्या है?", "options": ["नई दिल्ली", "मुंबई", "कोलकाता", "चेन्नई"], "correctAnswer": "नई दिल्ली"},
            {"text": "हम कान से क्या करते हैं?", "options": ["सुनते हैं", "देखते हैं", "सूँघते हैं", "खाते हैं"], "correctAnswer": "सुनते हैं"},
            {"text": "सूरज किधर से निकलता है?", "options": ["पूर्व", "पश्चिम", "उत्तर", "दक्षिण"], "correctAnswer": "पूर्व"},
            {"text": "मोर हमारा राष्ट्रीय ___ है।", "options": ["पक्षी", "पशु", "फूल", "पेड़"], "correctAnswer": "पक्षी"},
            {"text": "'जल' का पर्यायवाची क्या है?", "options": ["पानी", "आग", "धूल", "हवा"], "correctAnswer": "पानी"}
        ],
        "medium": [
            {"text": "'मछली' का बहुवचन क्या है?", "options": ["मछलियाँ", "मछलियों", "मछले", "मछलीये"], "correctAnswer": "मछलियाँ"},
            {"text": "'वीर' का विलोम शब्द क्या है?", "options": ["कायर", "डरपोक", "दोनों", "बहादुर"], "correctAnswer": "दोनों"},
            {"text": "'पुष्प' का पर्यायवाची शब्द?", "options": ["फूल", "फल", "पेड़", "जड़"], "correctAnswer": "फूल"},
            {"text": "'आँख दिखाना' मुहावरे का अर्थ?", "options": ["गुस्सा करना", "प्यार करना", "सुझाव देना", "खेलना"], "correctAnswer": "गुस्सा करना"},
            {"text": "विशेषण के कितने मुख्य चार भेद हैं?", "options": ["हाँ", "नहीं", "पता नहीं", "शायद"], "correctAnswer": "हाँ"},
            {"text": "'अ' किस प्रकार का स्वर है?", "options": ["ह्रस्व", "दीर्घ", "प्लुत", "कोई नहीं"], "correctAnswer": "ह्रस्व"},
            {"text": "'ईश्वर' का पर्यायवाची शब्द?", "options": ["भगवान", "दानव", "इंसान", "पशु"], "correctAnswer": "भगवान"},
            {"text": "'सफ़ेद' का विलोम शब्द?", "options": ["काला", "नीला", "लाल", "पीला"], "correctAnswer": "काला"},
            {"text": "'सुंदर' का पर्यायवाची शब्द?", "options": ["मनोरम", "बदसूरत", "गंदा", "छोटा"], "correctAnswer": "मनोरम"},
            {"text": "सर्वनाम के कितने भेद होते हैं?", "options": ["6", "4", "5", "7"], "correctAnswer": "6"}
        ],
        "hard": [
            {"text": "'दोहरा' लाभ होने के लिए मुहावरा क्या है?", "options": ["आम के आम गुठलियों के दाम", "नौ दिन चले अढाई कोस", "ऊँट के मुँह में जीरा", "एक और एक ग्यारह"], "correctAnswer": "आम के आम गुठलियों के दाम"},
            {"text": "'विद्वान' का स्त्रीलिंग शब्द क्या होगा?", "options": ["विदुषी", "विद्वानी", "माता", "पढ़ी-लिखी"], "correctAnswer": "विदुषी"},
            {"text": "'उन्नति' का विलोम शब्द क्या है?", "options": ["अवनति", "प्रगति", "विकास", "नीचे"], "correctAnswer": "अवनति"},
            {"text": "'जिसका कोई शत्रु न हो' के लिए एक शब्द?", "options": ["अजातशत्रु", "मित्र", "दुश्मन", "शांत"], "correctAnswer": "अजातशत्रु"},
            {"text": "'घी के दिए जलाना' मुहावरे का अर्थ?", "options": ["खुशियाँ मनाना", "रोशनी करना", "खाना बनाना", "पूजा करना"], "correctAnswer": "खुशियाँ मनाना"},
            {"text": "'हिमालय' का अर्थ क्या है?", "options": ["बर्फ का घर", "पत्थर का घर", "पेड़ का घर", "आग का घर"], "correctAnswer": "बर्फ का घर"},
            {"text": "'विद्यार्थी' का सही संधि विच्छेद?", "options": ["विद्या + अर्थी", "विद्य + अर्थी", "विद्य + आर्थी", "विद्या + आर्थी"], "correctAnswer": "विद्या + अर्थी"},
            {"text": "'आकाश' का विलोम शब्द?", "options": ["पाताल", "धरती", "समुद्र", "वायु"], "correctAnswer": "पाताल"},
            {"text": "क्रिया के मूल रूप को क्या कहते हैं?", "options": ["धातु", "शब्द", "स्वर", "व्यंजन"], "correctAnswer": "धातु"},
            {"text": "'सर्वज्ञ' का अर्थ क्या है?", "options": ["सब कुछ जानने वाला", "थोड़ा जानने वाला", "कुछ न जानने वाला", "ज्ञानी"], "correctAnswer": "सब कुछ जानने वाला"}
        ]
    }
}

add_class_data('class_7', class_7_data)

# Class 8 Data
class_8_data = {
    "english": {
        "easy": [
            {"text": "Which is an abstract noun?", "options": ["Bravery", "Table", "Boy", "Delhi"], "correctAnswer": "Bravery"},
            {"text": "Opposite of 'Victory'?", "options": ["Defeat", "Win", "Try", "Hope"], "correctAnswer": "Defeat"},
            {"text": "Identify the pronoun: 'She is reading'.", "options": ["She", "is", "reading", "book"], "correctAnswer": "She"},
            {"text": "Which word is a preposition?", "options": ["Between", "Happy", "Run", "Slowly"], "correctAnswer": "Between"},
            {"text": "Plural of 'Leaf'?", "options": ["Leaves", "Leafs", "Leafes", "Leaf"], "correctAnswer": "Leaves"},
            {"text": "Past tense of 'Speak'?", "options": ["Spoke", "Spoken", "Speaks", "Speaking"], "correctAnswer": "Spoke"},
            {"text": "Synonym of 'Silent'?", "options": ["Quiet", "Loud", "Fast", "Big"], "correctAnswer": "Quiet"},
            {"text": "A person who writes poems?", "options": ["Poet", "Author", "Painter", "Singer"], "correctAnswer": "Poet"},
            {"text": "Which is an adjective?", "options": ["Intelligent", "Quickly", "Sleep", "Under"], "correctAnswer": "Intelligent"},
            {"text": "I ___ writing a letter.", "options": ["am", "is", "are", "do"], "correctAnswer": "am"}
        ],
        "medium": [
            {"text": "Which is a conjunction?", "options": ["Although", "Jump", "Happy", "Sweet"], "correctAnswer": "Although"},
            {"text": "Identify the adverb: 'He writes beautifully'.", "options": ["beautifully", "writes", "He", "is"], "correctAnswer": "beautifully"},
            {"text": "Superlative of 'Busy'?", "options": ["Busiest", "Busier", "More busy", "Most busy"], "correctAnswer": "Busiest"},
            {"text": "Collective noun for 'Bees'?", "options": ["Swarm", "Pack", "Flock", "Herd"], "correctAnswer": "Swarm"},
            {"text": "Identify the tense: 'I have been reading'.", "options": ["Present Perfect Continuous", "Present Tense", "Past Tense", "Future"], "correctAnswer": "Present Perfect Continuous"},
            {"text": "Which is a 'Proper Noun'?", "options": ["Himalayas", "Mountain", "River", "City"], "correctAnswer": "Himalayas"},
            {"text": "Use 'a' or 'an': ___ honorable person.", "options": ["An", "A", "The", "Some"], "correctAnswer": "An"},
            {"text": "Antonym of 'Smooth'?", "options": ["Rough", "Soft", "Hard", "Big"], "correctAnswer": "Rough"},
            {"text": "Identify the Verb: 'The bell rings'.", "options": ["rings", "bell", "The", "loud"], "correctAnswer": "rings"},
            {"text": "A person who treats our teeth?", "options": ["Dentist", "Doctor", "Vet", "Painter"], "correctAnswer": "Dentist"}
        ],
        "hard": [
            {"text": "Which is a 'Neuter' gender noun?", "options": ["Pencil", "Man", "Maid", "Uncle"], "correctAnswer": "Pencil"},
            {"text": "Identify the preposition: 'The bird flew across the sky'.", "options": ["across", "flew", "bird", "sky"], "correctAnswer": "across"},
            {"text": "Identify the passive voice sentence.", "options": ["The letter was written by Ravi", "Ravi wrote a letter", "Ravi is writing", "Ravi will write"], "correctAnswer": "The letter was written by Ravi"},
            {"text": "Meaning of the idiom 'To burn the midnight oil'?", "options": ["Working late at night", "Cooking at night", "Sleeping early", "Using a lamp"], "correctAnswer": "Working late at night"},
            {"text": "Identify the complex sentence.", "options": ["Unless you work hard, you won't pass.", "Work hard.", "He worked hard and passed.", "Passed!"], "correctAnswer": "Unless you work hard, you won't pass."},
            {"text": "Plural of 'Phenomenon'?", "options": ["Phenomena", "Phenomenons", "Phenom", "None"], "correctAnswer": "Phenomena"},
            {"text": "What is an 'Oxymoron'?", "options": ["Contradictory terms side by side", "Repetition of words", "Rhyming", "Comparison"], "correctAnswer": "Contradictory terms side by side"},
            {"text": "Which word is spelled correctly?", "options": ["Questionnaire", "Questionaire", "Questionair", "Questionare"], "correctAnswer": "Questionnaire"},
            {"text": "Antonym of 'Altruistic'?", "options": ["Selfish", "Kind", "Helpful", "Rich"], "correctAnswer": "Selfish"},
            {"text": "Identify the indirect object: 'She showed us her photos'.", "options": ["us", "photos", "She", "showed"], "correctAnswer": "us"}
        ]
    },
    "maths": {
        "easy": [
            {"text": "What is 100 + 400?", "options": ["500", "600", "400", "200"], "correctAnswer": "500"},
            {"text": "Square root of 64?", "options": ["8", "6", "4", "7"], "correctAnswer": "8"},
            {"text": "Number of sides in a pentagon?", "options": ["5", "6", "4", "3"], "correctAnswer": "5"},
            {"text": "What is 9 \u00d7 0?", "options": ["0", "9", "90", "1"], "correctAnswer": "0"},
            {"text": "Value of 1/4 of 40?", "options": ["10", "20", "5", "8"], "correctAnswer": "10"},
            {"text": "Which number is prime?", "options": ["7", "4", "9", "10"], "correctAnswer": "7"},
            {"text": "Place value of 5 in 500?", "options": ["500", "50", "5", "1"], "correctAnswer": "500"},
            {"text": "A triangle has how many angles?", "options": ["3", "4", "2", "6"], "correctAnswer": "3"},
            {"text": "How many centimeters in 1 meter?", "options": ["100", "10", "1000", "50"], "correctAnswer": "100"},
            {"text": "What is 10 \u00d7 0.1?", "options": ["1", "10", "0.1", "0"], "correctAnswer": "1"}
        ],
        "medium": [
            {"text": "Area of rectangle (L=8, W=3)?", "options": ["24", "11", "22", "30"], "correctAnswer": "24"},
            {"text": "Simplified form of 15/45?", "options": ["1/3", "3/1", "1/5", "1/15"], "correctAnswer": "1/3"},
            {"text": "What is 10% of 1000?", "options": ["100", "10", "50", "200"], "correctAnswer": "100"},
            {"text": "LCM of 6 and 8?", "options": ["24", "48", "12", "14"], "correctAnswer": "24"},
            {"text": "Perimeter of square (side=5)?", "options": ["20", "15", "10", "25"], "correctAnswer": "20"},
            {"text": "Average of 10, 20, 30, 40?", "options": ["25", "20", "30", "15"], "correctAnswer": "25"},
            {"text": "Solve: 10 + 20 \u00f7 2", "options": ["20", "15", "25", "10"], "correctAnswer": "20"},
            {"text": "Sum of interior angles of a pentagon?", "options": ["540\u00b0", "360\u00b0", "180\u00b0", "720\u00b0"], "correctAnswer": "540\u00b0"},
            {"text": "Profit = Selling Price - ___.", "options": ["Cost Price", "Tax", "Loss", "Discount"], "correctAnswer": "Cost Price"},
            {"text": "Number of faces in a cube?", "options": ["6", "8", "12", "4"], "correctAnswer": "6"}
        ],
        "hard": [
            {"text": "HCF of 100 and 150?", "options": ["50", "25", "10", "100"], "correctAnswer": "50"},
            {"text": "Solve: 3x - 5 = 10", "options": ["5", "10", "15", "0"], "correctAnswer": "5"},
            {"text": "Volume of sphere formula?", "options": ["(4/3)\u03c0r\u00b3", "4\u03c0r\u00b2", "\u03c0r\u00b2h", "(1/3)\u03c0r\u00b2h"], "correctAnswer": "(4/3)\u03c0r\u00b3"},
            {"text": "A bike increases speed from 10m/s to 20m/s in 5s. Acceleration is ___.", "options": ["2m/s\u00b2", "4m/s\u00b2", "5m/s\u00b2", "10m/s\u00b2"], "correctAnswer": "2m/s\u00b2"},
            {"text": "Factorize: x\u00b2 - 4.", "options": ["(x-2)(x+2)", "(x-2)\u00b2", "(x+2)\u00b2", "x(x-4)"], "correctAnswer": "(x-2)(x+2)"},
            {"text": "Which is a rational number?", "options": ["2/3", "\u221a2", "\u03c0", "None"], "correctAnswer": "2/3"},
            {"text": "Value of root 2 approx?", "options": ["1.414", "1.732", "1.141", "2.141"], "correctAnswer": "1.414"},
            {"text": "Number of subsets of a set with 3 elements?", "options": ["8", "3", "6", "9"], "correctAnswer": "8"},
            {"text": "Calculate CI for P=100 annually. Rate 10% for 2 years.", "options": ["21", "20", "121", "10"], "correctAnswer": "21"},
            {"text": "Probability of getting an even number on a die roll?", "options": ["1/2", "1/3", "1/6", "2/3"], "correctAnswer": "1/2"}
        ]
    },
    "science": {
        "easy": [
            {"text": "Common salt is ___.", "options": ["Sodium Chloride", "Sodium Bicarbonate", "Calcium Chloride", "Magnesium"], "correctAnswer": "Sodium Chloride"},
            {"text": "Photosynthesis produces ___.", "options": ["Glucose and Oxygen", "CO2 and Water", "Starch only", "Nitrogen"], "correctAnswer": "Glucose and Oxygen"},
            {"text": "Human body has ___ chromosomes.", "options": ["46", "23", "44", "22"], "correctAnswer": "46"},
            {"text": "Which gas is used in soda water?", "options": ["CO2", "Oxygen", "Nitrogen", "Argon"], "correctAnswer": "CO2"},
            {"text": "Magnetite is a ___.", "options": ["Natural magnet", "Artificial magnet", "Copper ore", "Plastic"], "correctAnswer": "Natural magnet"},
            {"text": "Ice is ___ than water.", "options": ["Lighter (floats)", "Heavier", "Same weight", "Dense"], "correctAnswer": "Lighter (floats)"},
            {"text": "Which part of plant is responsible for reproduction?", "options": ["Flower", "Leaf", "Stem", "Root"], "correctAnswer": "Flower"},
            {"text": "Speed of light in vacuum?", "options": ["300,000 km/s", "150,000 km/s", "1,000 km/s", "Sound speed"], "correctAnswer": "300,000 km/s"},
            {"text": "Acid found in vinegar?", "options": ["Acetic acid", "Citric acid", "Hydrochloric", "Formic"], "correctAnswer": "Acetic acid"},
            {"text": "Metals are generally ___.", "options": ["Good conductors", "Bad conductors", "Insulators", "Soft"], "correctAnswer": "Good conductors"}
        ],
        "medium": [
            {"text": "Full form of AIDS?", "options": ["Acquired Immuno Deficiency Syndrome", "Acute Immuno Syndrome", "All India Disease Service", "Auto Immune Disease"], "correctAnswer": "Acquired Immuno Deficiency Syndrome"},
            {"text": "Which gas is released during photosynthesis?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Methane"], "correctAnswer": "Oxygen"},
            {"text": "Red Color of blood is due to ___.", "options": ["Hemoglobin", "Plasma", "WBC", "Platelets"], "correctAnswer": "Hemoglobin"},
            {"text": "The power of a lens is measured in ___.", "options": ["Diopters", "Meters", "Watts", "Newtons"], "correctAnswer": "Diopters"},
            {"text": "Which metal is liquid at room temperature?", "options": ["Mercury", "Gold", "Lead", "Aluminum"], "correctAnswer": "Mercury"},
            {"text": "Number of chambers in a human heart?", "options": ["4", "2", "3", "1"], "correctAnswer": "4"},
            {"text": "Unit of electric current is ___.", "options": ["Ampere", "Volt", "Ohm", "Watt"], "correctAnswer": "Ampere"},
            {"text": "The chemical used to purify water is ___.", "options": ["Chlorine", "Sugar", "Salt", "Iron"], "correctAnswer": "Chlorine"},
            {"text": "Digestion of protein begins in the ___.", "options": ["Stomach", "Mouth", "Intestine", "Liver"], "correctAnswer": "Stomach"},
            {"text": "Image formed by a plane mirror is ___.", "options": ["Virtual and erect", "Real and inverted", "Big", "Small"], "correctAnswer": "Virtual and erect"}
        ],
        "hard": [
            {"text": "Percentage of Oxygen in air?", "options": ["21%", "78%", "0.03%", "1%"], "correctAnswer": "21%"},
            {"text": "Universal donor blood group is ___.", "options": ["O-", "O+", "AB+", "AB-"], "correctAnswer": "O-"},
            {"text": "The hardest part of the human body is ___.", "options": ["Enamel", "Bone", "Skull", "Teeth base"], "correctAnswer": "Enamel"},
            {"text": "Which gland is called the Master Gland?", "options": ["Pituitary", "Thyroid", "Adrenal", "Pancreas"], "correctAnswer": "Pituitary"},
            {"text": "Velocity of sound is maximum in ___.", "options": ["Solids", "Liquids", "Gases", "Vacuum"], "correctAnswer": "Solids"},
            {"text": "Formation of rainbows is due to ___.", "options": ["Dispersion and Internal Reflection", "Reflection only", "Bouncing", "Shadow"], "correctAnswer": "Dispersion and Internal Reflection"},
            {"text": "Atomic Number of Oxygen is ___.", "options": ["8", "16", "6", "12"], "correctAnswer": "8"},
            {"text": "Device used to measure blood pressure?", "options": ["Sphygmomanometer", "Thermometer", "Stethoscope", "Barometer"], "correctAnswer": "Sphygmomanometer"},
            {"text": "The layer of atmosphere where planes fly?", "options": ["Stratosphere", "Troposphere", "Mesosphere", "Exosphere"], "correctAnswer": "Stratosphere"},
            {"text": "Full form of DNA?", "options": ["Deoxyribonucleic Acid", "Double Nucleic Acid", "Daily News Agency", "Deca Nucleic Acid"], "correctAnswer": "Deoxyribonucleic Acid"}
        ]
    },
    "social-science": {
        "easy": [
            {"text": "The First War of Independence started in ___.", "options": ["1857", "1947", "1757", "1920"], "correctAnswer": "1857"},
            {"text": "The nearest planet to Sun?", "options": ["Mercury", "Venus", "Earth", "Mars"], "correctAnswer": "Mercury"},
            {"text": "Highest mountain peak in the world?", "options": ["Mt. Everest", "K2", "Kangchenjunga", "Himalayas"], "correctAnswer": "Mt. Everest"},
            {"text": "Who is the Prime Minister of India?", "options": ["Narendra Modi", "Rahul Gandhi", "Amit Shah", "D. Murmu"], "correctAnswer": "Narendra Modi"},
            {"text": "Republic Day of India?", "options": ["January 26", "August 15", "October 2", "January 1"], "correctAnswer": "January 26"},
            {"text": "Largest state in India (Area)?", "options": ["Rajasthan", "UP", "MP", "Maharashtra"], "correctAnswer": "Rajasthan"},
            {"text": "The holy book of Hindus is ___.", "options": ["The Bhagavad Gita", "The Quran", "The Bible", "The Tipitaka"], "correctAnswer": "The Bhagavad Gita"},
            {"text": "The sun sets in the ___.", "options": ["West", "East", "North", "South"], "correctAnswer": "West"},
            {"text": "World's longest river is ___.", "options": ["Nile", "Amazon", "Ganges", "Mississippi"], "correctAnswer": "Nile"},
            {"text": "How many Union Territories in India?", "options": ["8", "7", "9", "28"], "correctAnswer": "8"}
        ],
        "medium": [
            {"text": "Where is the head office of UNESCO?", "options": ["Paris", "New York", "Geneva", "London"], "correctAnswer": "Paris"},
            {"text": "Who is the Father of Psychology?", "options": ["Wilhelm Wundt", "Freud", "Pavlov", "Jung"], "correctAnswer": "Wilhelm Wundt"},
            {"text": "Which is the largest continent?", "options": ["Asia", "Africa", "North America", "Europe"], "correctAnswer": "Asia"},
            {"text": "Line that divides Earth into North/South?", "options": ["Equator", "Prime Meridian", "Tropic of Cancer", "Axis"], "correctAnswer": "Equator"},
            {"text": "The Supreme court is in ___.", "options": ["New Delhi", "Mumbai", "Kolkata", "Chennai"], "correctAnswer": "New Delhi"},
            {"text": "Who was the first woman PM of India?", "options": ["Indira Gandhi", "Pratibha Patil", "S. Naidu", "None"], "correctAnswer": "Indira Gandhi"},
            {"text": "Major producer of tea in India?", "options": ["Assam", "Kerala", "Punjab", "Bihar"], "correctAnswer": "Assam"},
            {"text": "The Gateway of India is in ___.", "options": ["Mumbai", "Delhi", "Chennai", "Kolkata"], "correctAnswer": "Mumbai"},
            {"text": "The hottest continent is ___.", "options": ["Africa", "Asia", "Australia", "South America"], "correctAnswer": "Africa"},
            {"text": "Who wrote 'Wings of Fire'?", "options": ["A.P.J. Abdul Kalam", "Nehru", "Patel", "Prasad"], "correctAnswer": "A.P.J. Abdul Kalam"}
        ],
        "hard": [
            {"text": "Who gave the slogan 'Jai Hind'?", "options": ["Subhash Chandra Bose", "Gandhi", "Nehru", "Lal Bahadur Shastri"], "correctAnswer": "Subhash Chandra Bose"},
            {"text": "What is the age of majority in India?", "options": ["18", "21", "25", "16"], "correctAnswer": "18"},
            {"text": "Which is the highest waterfall in the world?", "options": ["Angel Falls", "Niagara", "Victoria", "Jog Falls"], "correctAnswer": "Angel Falls"},
            {"text": "When was the Non-Cooperation Movement started?", "options": ["1920", "1942", "1930", "1919"], "correctAnswer": "1920"},
            {"text": "The gas that gives protection against Sun's rays in Stratosphere?", "options": ["Ozone", "Oxygen", "Nitrogen", "CO2"], "correctAnswer": "Ozone"},
            {"text": "Who is the head of the Indian State?", "options": ["President", "PM", "CJ", "Speaker"], "correctAnswer": "President"},
            {"text": "The third battle of Panipat was fought in ___.", "options": ["1761", "1526", "1556", "1857"], "correctAnswer": "1761"},
            {"text": "The Greenwich Mean Time (GMT) is ___ behind IST.", "options": ["5.5 hours", "6 hours", "4 hours", "None"], "correctAnswer": "5.5 hours"},
            {"text": "Who founded the Brahmo Samaj?", "options": ["Raja Ram Mohan Roy", "Dayanand Saraswati", "Vivekananda", "Tagore"], "correctAnswer": "Raja Ram Mohan Roy"},
            {"text": "What is the Silicon Valley of India?", "options": ["Bangalore", "Hyderabad", "Pune", "Chennai"], "correctAnswer": "Bangalore"}
        ]
    },
    "hindi": {
        "easy": [
            {"text": "'दिन' का विलोम शब्द क्या है?", "options": ["रात", "सुबह", "शाम", "दोपहर"], "correctAnswer": "रात"},
            {"text": "'माँ' का पर्यायवाची शब्द?", "options": ["माता", "पिता", "भाई", "बहन"], "correctAnswer": "माता"},
            {"text": "एक साल में कितने महीने होते हैं?", "options": ["12", "10", "11", "13"], "correctAnswer": "12"},
            {"text": "'हाथी' को हिंदी में और क्या कहते हैं?", "options": ["गज", "घोड़ा", "शेर", "ऊँट"], "correctAnswer": "गज"},
            {"text": "'मीठा' का विलोम शब्द क्या है?", "options": ["कड़वा", "खट्टा", "नमकीन", "तीखा"], "correctAnswer": "कड़वा"},
            {"text": "भारत की राजधानी क्या है?", "options": ["नई दिल्ली", "मुंबई", "कोलकाता", "चेन्नई"], "correctAnswer": "नई दिल्ली"},
            {"text": "हम कान से क्या करते हैं?", "options": ["सुनते हैं", "देखते हैं", "सूँघते हैं", "खाते हैं"], "correctAnswer": "सुनते हैं"},
            {"text": "सूरज किधर से निकलता है?", "options": ["पूर्व", "पश्चिम", "उत्तर", "दक्षिण"], "correctAnswer": "पूर्व"},
            {"text": "मोर हमारा राष्ट्रीय ___ है।", "options": ["पक्षी", "पशु", "फूल", "पेड़"], "correctAnswer": "पक्षी"},
            {"text": "'जल' का पर्यायवाची क्या है?", "options": ["पानी", "आग", "धूल", "हवा"], "correctAnswer": "पानी"}
        ],
        "medium": [
            {"text": "'मछली' का बहुवचन क्या है?", "options": ["मछलियाँ", "मछलियों", "मछले", "मछलीये"], "correctAnswer": "मछलियाँ"},
            {"text": "'वीर' का विलोम शब्द क्या है?", "options": ["कायर", "डरपोक", "दोनों", "बहादुर"], "correctAnswer": "दोनों"},
            {"text": "'पुष्प' का पर्यायवाची शब्द?", "options": ["फूल", "फल", "पेड़", "जड़"], "correctAnswer": "फूल"},
            {"text": "'आँख दिखाना' मुहावरे का अर्थ?", "options": ["गुस्सा करना", "प्यार करना", "सुझाव देना", "खेलना"], "correctAnswer": "गुस्सा करना"},
            {"text": "विशेषण के कितने मुख्य चार भेद हैं?", "options": ["हाँ", "नहीं", "पता नहीं", "शायद"], "correctAnswer": "हाँ"},
            {"text": "'अ' किस प्रकार का स्वर है?", "options": ["ह्रस्व", "दीर्घ", "प्लुत", "कोई नहीं"], "correctAnswer": "ह्रस्व"},
            {"text": "'ईश्वर' का पर्यायवाची शब्द?", "options": ["भगवान", "दानव", "इंसान", "पशु"], "correctAnswer": "भगवान"},
            {"text": "'सफ़ेद' का विलोम शब्द?", "options": ["काला", "नीला", "लाल", "पीला"], "correctAnswer": "काला"},
            {"text": "'सुंदर' का पर्यायवाची शब्द?", "options": ["मनोरम", "बदसूरत", "गंदा", "छोटा"], "correctAnswer": "मनोरम"},
            {"text": "सर्वनाम के कितने भेद होते हैं?", "options": ["6", "4", "5", "7"], "correctAnswer": "6"}
        ],
        "hard": [
            {"text": "'दोहरा' लाभ होने के लिए मुहावरा क्या है?", "options": ["आम के आम गुठलियों के दाम", "नौ दिन चले अढाई कोस", "ऊँट के मुँह में जीरा", "एक और एक ग्यारह"], "correctAnswer": "आम के आम गुठलियों के दाम"},
            {"text": "'विद्वान' का स्त्रीलिंग शब्द क्या होगा?", "options": ["विदुषी", "विद्वानी", "माता", "पढ़ी-लिखी"], "correctAnswer": "विदुषी"},
            {"text": "'उन्नति' का विलोम शब्द क्या है?", "options": ["अवनति", "प्रगति", "विकास", "नीचे"], "correctAnswer": "अवनति"},
            {"text": "'जिसका कोई शत्रु न हो' के लिए एक शब्द?", "options": ["अजातशत्रु", "मित्र", "दुश्मन", "शांत"], "correctAnswer": "अजातशत्रु"},
            {"text": "'घी के दिए जलाना' मुहावरे का अर्थ?", "options": ["खुशियाँ मनाना", "रोशनी करना", "खाना बनाना", "पूजा करना"], "correctAnswer": "खुशियाँ मनाना"},
            {"text": "'हिमालय' का अर्थ क्या है?", "options": ["बर्फ का घर", "पत्थर का घर", "पेड़ का घर", "आग का घर"], "correctAnswer": "बर्फ का घर"},
            {"text": "'विद्यार्थी' का सही संधि विच्छेद?", "options": ["विद्या + अर्थी", "विद्य + अर्थी", "विद्य + आर्थी", "विद्या + आर्थी"], "correctAnswer": "विद्या + अर्थी"},
            {"text": "'आकाश' का विलोम शब्द?", "options": ["पाताल", "धरती", "समुद्र", "वायु"], "correctAnswer": "पाताल"},
            {"text": "क्रिया के मूल रूप को क्या कहते हैं?", "options": ["धातु", "शब्द", "स्वर", "व्यंजन"], "correctAnswer": "धातु"},
            {"text": "'सर्वज्ञ' का अर्थ क्या है?", "options": ["सब कुछ जानने वाला", "थोड़ा जानने वाला", "कुछ न जानने वाला", "ज्ञानी"], "correctAnswer": "सब कुछ जानने वाला"}
        ]
    }
}

add_class_data('class_8', class_8_data)

# Class 9 Data
class_9_data = {
    "english": {
        "easy": [
            {"text": "Which is an abstract noun?", "options": ["Bravery", "Book", "Boy", "Delhi"], "correctAnswer": "Bravery"},
            {"text": "Opposite of 'Victory'?", "options": ["Defeat", "Win", "Try", "Hope"], "correctAnswer": "Defeat"},
            {"text": "Identify the pronoun: 'She is reading'.", "options": ["She", "is", "reading", "book"], "correctAnswer": "She"},
            {"text": "Which word is a preposition?", "options": ["Under", "Happy", "Run", "Slowly"], "correctAnswer": "Under"},
            {"text": "Plural of 'Man'?", "options": ["Men", "Mans", "Manes", "Man"], "correctAnswer": "Men"},
            {"text": "Past tense of 'Go'?", "options": ["Went", "Gone", "Goes", "Going"], "correctAnswer": "Went"},
            {"text": "Synonym of 'Big'?", "options": ["Large", "Small", "Tiny", "Little"], "correctAnswer": "Large"},
            {"text": "Identify the adjective: 'The red car'.", "options": ["red", "car", "The", "is"], "correctAnswer": "red"},
            {"text": "I ___ a student.", "options": ["am", "is", "are", "do"], "correctAnswer": "am"},
            {"text": "Which is an animal?", "options": ["Tiger", "Apple", "Car", "Table"], "correctAnswer": "Tiger"}
        ],
        "medium": [
            {"text": "Which is a conjunction?", "options": ["But", "Blue", "Fast", "Jump"], "correctAnswer": "But"},
            {"text": "Identify the adverb: 'He runs fast'.", "options": ["fast", "runs", "He", "is"], "correctAnswer": "fast"},
            {"text": "Superlative of 'Good'?", "options": ["Best", "Better", "Goodest", "More good"], "correctAnswer": "Best"},
            {"text": "Collective noun for 'Soldiers'?", "options": ["Army", "Pack", "Flock", "Herd"], "correctAnswer": "Army"},
            {"text": "Identify the tense: 'I will eat'.", "options": ["Future", "Present", "Past", "None"], "correctAnswer": "Future"},
            {"text": "Which is a 'Proper Noun'?", "options": ["India", "Country", "State", "City"], "correctAnswer": "India"},
            {"text": "Use 'a' or 'an': ___ honest man.", "options": ["An", "A", "The", "Some"], "correctAnswer": "An"},
            {"text": "Antonym of 'Smooth'?", "options": ["Rough", "Soft", "Hard", "Big"], "correctAnswer": "Rough"},
            {"text": "Identify the Verb: 'She sings sweetly'.", "options": ["sings", "She", "sweetly", "is"], "correctAnswer": "sings"},
            {"text": "A person who teaches is a ___.", "options": ["Teacher", "Doctor", "Farmer", "Driver"], "correctAnswer": "Teacher"}
        ],
        "hard": [
            {"text": "Which is a silent letter in 'Honest'?", "options": ["H", "o", "n", "e"], "correctAnswer": "H"},
            {"text": "Identify the preposition: 'The book is on the table'.", "options": ["on", "book", "is", "table"], "correctAnswer": "on"},
            {"text": "Which is a 'Neuter' gender noun?", "options": ["House", "King", "Maid", "Uncle"], "correctAnswer": "House"},
            {"text": "Meaning of the idiom 'Under the weather'?", "options": ["Feeling sick", "Feeling happy", "Raining", "Sunny"], "correctAnswer": "Feeling sick"},
            {"text": "Identify the complex sentence.", "options": ["Since it was late, we left.", "We left.", "It was late and we left.", "Leave!"], "correctAnswer": "Since it was late, we left."},
            {"text": "Plural of 'Phenomenon'?", "options": ["Phenomena", "Phenomenons", "Phenomenas", "None"], "correctAnswer": "Phenomena"},
            {"text": "What is 'Alliteration'?", "options": ["Repetition of consonant sounds", "Comparison", "Rhyme", "Sound words"], "correctAnswer": "Repetition of consonant sounds"},
            {"text": "Correct spelling?", "options": ["Entrepreneur", "Enterpreneur", "Entreprenure", "Enterprenure"], "correctAnswer": "Entrepreneur"},
            {"text": "Antonym of 'Altruistic'?", "options": ["Selfish", "Kind", "Strong", "Fast"], "correctAnswer": "Selfish"},
            {"text": "Identify the indirect object: 'He gave me a book'.", "options": ["me", "book", "He", "gave"], "correctAnswer": "me"}
        ]
    },
    "maths": {
        "easy": [
            {"text": "Smallest natural number?", "options": ["1", "0", "2", "3"], "correctAnswer": "1"},
            {"text": "Value of 100 \u00d7 0.5?", "options": ["50", "5", "500", "10"], "correctAnswer": "50"},
            {"text": "Sum of angles in a triangle?", "options": ["180\u00b0", "360\u00b0", "90\u00b0", "270\u00b0"], "correctAnswer": "180\u00b0"},
            {"text": "Which number is even?", "options": ["24", "25", "27", "29"], "correctAnswer": "24"},
            {"text": "What is 10 squared?", "options": ["100", "20", "10", "1000"], "correctAnswer": "100"},
            {"text": "Square root of 81?", "options": ["9", "8", "7", "10"], "correctAnswer": "9"},
            {"text": "Formula for Area of Circle?", "options": ["\u03c0r\u00b2", "2\u03c0r", "\u03c0d", "\u03c0r\u00b2h"], "correctAnswer": "\u03c0r\u00b2"},
            {"text": "Which is a prime number?", "options": ["11", "12", "14", "15"], "correctAnswer": "11"},
            {"text": "Simplify: 10 + 20 \u00f7 2", "options": ["20", "15", "25", "10"], "correctAnswer": "20"},
            {"text": "What is 10% of 500?", "options": ["50", "5", "500", "100"], "correctAnswer": "50"}
        ],
        "medium": [
            {"text": "Area of rectangle (L=12, W=5)?", "options": ["60", "17", "34", "70"], "correctAnswer": "60"},
            {"text": "Solve: 2x + 10 = 30", "options": ["10", "20", "5", "40"], "correctAnswer": "10"},
            {"text": "LCM of 12 and 18?", "options": ["36", "72", "18", "12"], "correctAnswer": "36"},
            {"text": "What is 25% of 800?", "options": ["200", "100", "400", "80"], "correctAnswer": "200"},
            {"text": "Perimeter of square with side 10?", "options": ["40", "20", "100", "10"], "correctAnswer": "40"},
            {"text": "Average of 5, 10, 15?", "options": ["10", "5", "15", "30"], "correctAnswer": "10"},
            {"text": "Solve: (2 + 3) \u00d7 4", "options": ["20", "14", "18", "10"], "correctAnswer": "20"},
            {"text": "Convert 3/4 to percentage.", "options": ["75%", "50%", "25%", "100%"], "correctAnswer": "75%"},
            {"text": "Sum of interior angles of a quadrilateral?", "options": ["360\u00b0", "180\u00b0", "270\u00b0", "540\u00b0"], "correctAnswer": "360\u00b0"},
            {"text": "If speed = 60km/h, time = 2.5h, distance = ?", "options": ["150km", "120km", "180km", "60km"], "correctAnswer": "150km"}
        ],
        "hard": [
            {"text": "HCF of 45, 60 and 75?", "options": ["15", "5", "30", "45"], "correctAnswer": "15"},
            {"text": "Solve: x\u00b2 - 5x + 6 = 0", "options": ["(2, 3)", "(1, 6)", "(2, -3)", "(-2, -3)"], "correctAnswer": "(2, 3)"},
            {"text": "Volume of cylinder formula?", "options": ["\u03c0r\u00b2h", "2\u03c0rh", "\u03c0r\u00b2", "1/3\u03c0r\u00b2h"], "correctAnswer": "\u03c0r\u00b2h"},
            {"text": "Represent 0.333... as a fraction.", "options": ["1/3", "1/4", "3/10", "33/100"], "correctAnswer": "1/3"},
            {"text": "Ratio of 30cm to 2m?", "options": ["3:20", "20:3", "3:2", "30:2"], "correctAnswer": "3:20"},
            {"text": "Pythagoras Theorem for hypotenuse 'c'?", "options": ["c\u00b2 = a\u00b2 + b\u00b2", "c = a + b", "c\u00b2 = a\u00b2 - b\u00b2", "c = ab"], "correctAnswer": "c\u00b2 = a\u00b2 + b\u00b2"},
            {"text": "Number of faces in a triangular pyramid?", "options": ["4", "3", "5", "6"], "correctAnswer": "4"},
            {"text": "Simplified form of (a^m) \u00d7 (a^n)?", "options": ["a^(m+n)", "a^(mn)", "a^(m-n)", "a^m + a^n"], "correctAnswer": "a^(m+n)"},
            {"text": "Find Mean of first five whole numbers.", "options": ["2", "2.5", "3", "1.5"], "correctAnswer": "2"},
            {"text": "Value of root 2?", "options": ["1.414", "1.732", "2.141", "1.141"], "correctAnswer": "1.414"}
        ]
    },
    "science": {
        "easy": [
            {"text": "Smallest unit of life?", "options": ["Cell", "Tissue", "Organ", "Atom"], "correctAnswer": "Cell"},
            {"text": "Gas needed for photosynthesis?", "options": ["CO2", "Oxygen", "Nitrogen", "Hydrogen"], "correctAnswer": "CO2"},
            {"text": "pH of water?", "options": ["7", "1", "14", "0"], "correctAnswer": "7"},
            {"text": "Human bones count (Adult)?", "options": ["206", "300", "250", "200"], "correctAnswer": "206"},
            {"text": "Speed of Light?", "options": ["3 \u00d7 10^8 m/s", "3 \u00d7 10^5 m/s", "1 \u00d7 10^8 m/s", "Sound speed"], "correctAnswer": "3 \u00d7 10^8 m/s"},
            {"text": "Which gas is used in balloons?", "options": ["Helium", "Oxygen", "CO2", "Nitrogen"], "correctAnswer": "Helium"},
            {"text": "Ice melts at ___.", "options": ["0\u00b0C", "100\u00b0C", "50\u00b0C", "-10\u00b0C"], "correctAnswer": "0\u00b0C"},
            {"text": "Boiling point of water?", "options": ["100\u00b0C", "0\u00b0C", "212\u00b0F", "Both A & C"], "correctAnswer": "Both A & C"},
            {"text": "A magnet attracts ___.", "options": ["Iron", "Gold", "Silver", "Plastic"], "correctAnswer": "Iron"},
            {"text": "Chemical formula of Water?", "options": ["H2O", "CO2", "O2", "NaCl"], "correctAnswer": "H2O"}
        ],
        "medium": [
            {"text": "Force = Mass \u00d7 ___.", "options": ["Acceleration", "Velocity", "Distance", "Time"], "correctAnswer": "Acceleration"},
            {"text": "Which organ filters blood?", "options": ["Kidneys", "Lungs", "Heart", "Liver"], "correctAnswer": "Kidneys"},
            {"text": "SI unit of Energy?", "options": ["Joule", "Watt", "Newton", "Pascal"], "correctAnswer": "Joule"},
            {"text": "Chemical formula of Glucose?", "options": ["C6H12O6", "CO2", "NaCl", "H2O"], "correctAnswer": "C6H12O6"},
            {"text": "Which metal is liquid at RT?", "options": ["Mercury", "Gold", "Lead", "Bromine"], "correctAnswer": "Mercury"},
            {"text": "Number of chambers in heart?", "options": ["4", "2", "3", "1"], "correctAnswer": "4"},
            {"text": "Atomic number of Carbon?", "options": ["6", "12", "8", "1"], "correctAnswer": "6"},
            {"text": "Newton's 1st Law is Law of ___.", "options": ["Inertia", "Force", "Action/Reaction", "Gravity"], "correctAnswer": "Inertia"},
            {"text": "Main gas in air?", "options": ["Nitrogen (78%)", "Oxygen (21%)", "CO2", "Argon"], "correctAnswer": "Nitrogen (78%)"},
            {"text": "Mirror used for side-view in cars?", "options": ["Convex", "Concave", "Plane", "None"], "correctAnswer": "Convex"}
        ],
        "hard": [
            {"text": "Who discovered Electrons?", "options": ["J.J. Thomson", "Rutherford", "Goldstein", "Chadwick"], "correctAnswer": "J.J. Thomson"},
            {"text": "Mitochondria is powerhouse of ___.", "options": ["Cell", "Tissue", "Body", "Atom"], "correctAnswer": "Cell"},
            {"text": "Value of Gravitational constant 'G'?", "options": ["6.67 \u00d7 10^-11", "9.8", "6.63 \u00d7 10^-34", "3 \u00d7 10^8"], "correctAnswer": "6.67 \u00d7 10^-11"},
            {"text": "Full form of DNA?", "options": ["Deoxyribonucleic acid", "Double nucleic acid", "Daily news agency", "None"], "correctAnswer": "Deoxyribonucleic acid"},
            {"text": "Which acid is in our stomach?", "options": ["HCl", "H2SO4", "HNO3", "Acetic"], "correctAnswer": "HCl"},
            {"text": "Refractive index of diamond?", "options": ["2.42", "1.50", "1.33", "1.00"], "correctAnswer": "2.42"},
            {"text": "Plant tissue for water transport?", "options": ["Xylem", "Phloem", "Parenchyma", "Collenchyma"], "correctAnswer": "Xylem"},
            {"text": "Plant hormone for growth?", "options": ["Auxin", "Insulin", "Adrenaline", "Thyroxine"], "correctAnswer": "Auxin"},
            {"text": "Disease caused by lack of Vitamin C?", "options": ["Scurvy", "Rickets", "Beriberi", "Anemia"], "correctAnswer": "Scurvy"},
            {"text": "What is 1 Horse Power?", "options": ["746 Watts", "1000 Watts", "500 Watts", "250 Watts"], "correctAnswer": "746 Watts"}
        ]
    },
    "social-science": {
        "easy": [
            {"text": "Who is the Father of India?", "options": ["Gandhiji", "Nehru", "Bose", "Patel"], "correctAnswer": "Gandhiji"},
            {"text": "Red Planet?", "options": ["Mars", "Venus", "Earth", "Jupiter"], "correctAnswer": "Mars"},
            {"text": "Largest ocean?", "options": ["Pacific", "Atlantic", "Indian", "Arctic"], "correctAnswer": "Pacific"},
            {"text": "Capital of India?", "options": ["Delhi", "Mumbai", "Kolkata", "Chennai"], "correctAnswer": "Delhi"},
            {"text": "Independence year (India)?", "options": ["1947", "1950", "1942", "1960"], "correctAnswer": "1947"},
            {"text": "How many states in India?", "options": ["28", "25", "29", "30"], "correctAnswer": "28"},
            {"text": "Highest peak in India?", "options": ["Kanchenjunga", "Everest", "K2", "Nanda Devi"], "correctAnswer": "Kanchenjunga"},
            {"text": "The Sun rises in the ___.", "options": ["East", "West", "North", "South"], "correctAnswer": "East"},
            {"text": "World's largest desert?", "options": ["Sahara", "Gobi", "Thar", "Atacama"], "correctAnswer": "Sahara"},
            {"text": "How many continents?", "options": ["7", "5", "6", "8"], "correctAnswer": "7"}
        ],
        "medium": [
            {"text": "Where is UNO head office?", "options": ["New York", "London", "Paris", "Geneva"], "correctAnswer": "New York"},
            {"text": "Father of Green Revolution?", "options": ["Norman Borlaug", "M.S. Swaminathan", "Verghese Kurien", "None"], "correctAnswer": "Norman Borlaug"},
            {"text": "Smallest continent?", "options": ["Australia", "Europe", "Africa", "South America"], "correctAnswer": "Australia"},
            {"text": "Line dividing Earth North/South?", "options": ["Equator", "Prime Meridian", "Tropic of Cancer", "Axis"], "correctAnswer": "Equator"},
            {"text": "Parliament of India is in ___.", "options": ["Delhi", "Mumbai", "Kolkata", "Chennai"], "correctAnswer": "Delhi"},
            {"text": "First President of India?", "options": ["Rajendra Prasad", "Nehru", "Radhakrishnan", "Patel"], "correctAnswer": "Rajendra Prasad"},
            {"text": "Constitution Day of India?", "options": ["26 Nov", "26 Jan", "15 Aug", "2 Oct"], "correctAnswer": "26 Nov"},
            {"text": "The city of Temples is ___.", "options": ["Varanasi", "Delhi", "Mumbai", "Chennai"], "correctAnswer": "Varanasi"},
            {"text": "Coldest continent?", "options": ["Antarctica", "Asia", "Africa", "Europe"], "correctAnswer": "Antarctica"},
            {"text": "Blue Revolution is related to ___.", "options": ["Fish", "Milk", "Agriculture", "Petroleum"], "correctAnswer": "Fish"}
        ],
        "hard": [
            {"text": "Who gave slogan 'Swaraj is my birthright'?", "options": ["Tilak", "Gandhi", "Nehru", "Bose"], "correctAnswer": "Tilak"},
            {"text": "Majority age in India?", "options": ["18", "21", "25", "16"], "correctAnswer": "18"},
            {"text": "Highest waterfall in world?", "options": ["Angel Falls", "Niagara", "Victoria", "Jog"], "correctAnswer": "Angel Falls"},
            {"text": "When did French Revolution start?", "options": ["1789", "1750", "1800", "1850"], "correctAnswer": "1789"},
            {"text": "Gas protecting from UV rays?", "options": ["Ozone", "Oxygen", "CO2", "Nitrogen"], "correctAnswer": "Ozone"},
            {"text": "Who is head of Indian State?", "options": ["President", "PM", "Chief Justice", "Speaker"], "correctAnswer": "President"},
            {"text": "Battle of Panipat (1st) was in ___.", "options": ["1526", "1556", "1761", "1857"], "correctAnswer": "1526"},
            {"text": "Greenwich Mean Time (GMT) is in ___.", "options": ["UK", "USA", "India", "France"], "correctAnswer": "UK"},
            {"text": "Who founded Brahmo Samaj?", "options": ["Raja Ram Mohan Roy", "Dayanand Saraswati", "Vivekananda", "Tagore"], "correctAnswer": "Raja Ram Mohan Roy"},
            {"text": "The Silicon Valley of India?", "options": ["Bangalore", "Hyderabad", "Pune", "Chennai"], "correctAnswer": "Bangalore"}
        ]
    },
    "hindi": {
        "easy": [
            {"text": "'आज' का विलोम शब्द क्या है?", "options": ["कल", "परसों", "अतीत", "बाद"], "correctAnswer": "कल"},
            {"text": "'माता' का पर्यायवाची शब्द?", "options": ["माँ", "पिता", "भाई", "बहन"], "correctAnswer": "माँ"},
            {"text": "एक साल में कितने महीने होते हैं?", "options": ["12", "10", "11", "13"], "correctAnswer": "12"},
            {"text": "'हाथी' को हिंदी में और क्या कहते हैं?", "options": ["गज", "घोड़ा", "शेर", "ऊँट"], "correctAnswer": "गज"},
            {"text": "'मीठा' का विलोम शब्द क्या है?", "options": ["कड़वा", "खट्टा", "नमकीन", "तीखा"], "correctAnswer": "कड़वा"},
            {"text": "भारत की राजधानी क्या है?", "options": ["नई दिल्ली", "मुंबई", "कोलकाता", "चेन्नई"], "correctAnswer": "नई दिल्ली"},
            {"text": "हम कान से क्या करते हैं?", "options": ["सुनते हैं", "देखते हैं", "सूँघते हैं", "खाते हैं"], "correctAnswer": "सुनते हैं"},
            {"text": "सूरज किधर से निकलता है?", "options": ["पूर्व", "पश्चिम", "उत्तर", "दक्षिण"], "correctAnswer": "पूर्व"},
            {"text": "मोर हमारा राष्ट्रीय ___ है।", "options": ["पक्षी", "पशु", "फूल", "पेड़"], "correctAnswer": "पक्षी"},
            {"text": "'जल' का पर्यायवाची क्या है?", "options": ["पानी", "आग", "धूल", "हवा"], "correctAnswer": "पानी"}
        ],
        "medium": [
            {"text": "'मछली' का बहुवचन क्या है?", "options": ["मछलियाँ", "मछलियों", "मछले", "मछलीये"], "correctAnswer": "मछलियाँ"},
            {"text": "'वीर' का विलोम शब्द क्या है?", "options": ["कायर", "डरपोक", "दोनों", "बहादुर"], "correctAnswer": "दोनों"},
            {"text": "'पुष्प' का पर्यायवाची शब्द?", "options": ["फूल", "फल", "पेड़", "जड़"], "correctAnswer": "फूल"},
            {"text": "'आँख दिखाना' मुहावरे का अर्थ?", "options": ["गुस्सा करना", "प्यार करना", "सुझाव देना", "खेलना"], "correctAnswer": "गुस्सा करना"},
            {"text": "विशेषण के कितने मुख्य चार भेद हैं?", "options": ["हाँ", "नहीं", "पता नहीं", "शायद"], "correctAnswer": "हाँ"},
            {"text": "'अ' किस प्रकार का स्वर है?", "options": ["ह्रस्व", "दीर्घ", "प्लुत", "कोई नहीं"], "correctAnswer": "ह्रस्व"},
            {"text": "'ईश्वर' का पर्यायवाची शब्द?", "options": ["भगवान", "दानव", "इंसान", "पशु"], "correctAnswer": "भगवान"},
            {"text": "'सफ़ेद' का विलोम शब्द?", "options": ["काला", "नीला", "लाल", "पीला"], "correctAnswer": "काला"},
            {"text": "'सुंदर' का पर्यायवाची शब्द?", "options": ["मनोरम", "बदसूरत", "गंदा", "छोटा"], "correctAnswer": "मनोरम"},
            {"text": "सर्वनाम के कितने भेद होते हैं?", "options": ["6", "4", "5", "7"], "correctAnswer": "6"}
        ],
        "hard": [
            {"text": "'दोहरा' लाभ होने के लिए मुहावरा क्या है?", "options": ["आम के आम गुठलियों के दाम", "नौ दिन चले अढाई कोस", "ऊँट के मुँह में जीरा", "एक और एक ग्यारह"], "correctAnswer": "आम के आम गुठलियों के दाम"},
            {"text": "'विद्वान' का स्त्रीलिंग शब्द क्या होगा?", "options": ["विदुषी", "विद्वानी", "माता", "पढ़ी-लिखी"], "correctAnswer": "विदुषी"},
            {"text": "'उन्नति' का विलोम शब्द क्या है?", "options": ["अवनति", "प्रगति", "विकास", "नीचे"], "correctAnswer": "अवनति"},
            {"text": "'जिसका कोई शत्रु न हो' के लिए एक शब्द?", "options": ["अजातशत्रु", "मित्र", "दुश्मन", "शांत"], "correctAnswer": "अजातशत्रु"},
            {"text": "'घी के दिए जलाना' मुहावरे का अर्थ?", "options": ["खुशियाँ मनाना", "रोशनी करना", "खाना बनाना", "पूजा करना"], "correctAnswer": "खुशियाँ मनाना"},
            {"text": "'हिमालय' का अर्थ क्या है?", "options": ["बर्फ का घर", "पत्थर का घर", "पेड़ का घर", "आग का घर"], "correctAnswer": "बर्फ का घर"},
            {"text": "'विद्यार्थी' का सही संधि विच्छेद?", "options": ["विद्या + अर्थी", "विद्य + अर्थी", "विद्य + आर्थी", "विद्या + आर्थी"], "correctAnswer": "विद्या + अर्थी"},
            {"text": "'आकाश' का विलोम शब्द?", "options": ["पाताल", "धरती", "समुद्र", "वायु"], "correctAnswer": "पाताल"},
            {"text": "क्रिया के मूल रूप को क्या कहते हैं?", "options": ["धातु", "शब्द", "स्वर", "व्यंजन"], "correctAnswer": "धातु"},
            {"text": "'सर्वज्ञ' का अर्थ क्या है?", "options": ["सब कुछ जानने वाला", "थोड़ा जानने वाला", "कुछ न जानने वाला", "ज्ञानी"], "correctAnswer": "सब कुछ जानने वाला"}
        ]
    }
}

add_class_data('class_9', class_9_data)

# Class 10 Data
class_10_data = {
    "english": {
        "easy": [
            {"text": "Which is an abstract noun?", "options": ["Bravery", "Table", "Boy", "Delhi"], "correctAnswer": "Bravery"},
            {"text": "Opposite of 'Success'?", "options": ["Failure", "Win", "Try", "Hope"], "correctAnswer": "Failure"},
            {"text": "Identify the pronoun: 'They are playing'.", "options": ["They", "are", "playing", "ball"], "correctAnswer": "They"},
            {"text": "Which word is a preposition?", "options": ["Under", "Happy", "Run", "Slowly"], "correctAnswer": "Under"},
            {"text": "Plural of 'Man'?", "options": ["Men", "Mans", "Manes", "Man"], "correctAnswer": "Men"},
            {"text": "Past tense of 'Go'?", "options": ["Went", "Gone", "Goes", "Going"], "correctAnswer": "Went"},
            {"text": "Synonym of 'Big'?", "options": ["Large", "Small", "Tiny", "Little"], "correctAnswer": "Large"},
            {"text": "Identify the adjective: 'The red car'.", "options": ["red", "car", "The", "is"], "correctAnswer": "red"},
            {"text": "I ___ a student.", "options": ["am", "is", "are", "do"], "correctAnswer": "am"},
            {"text": "Which is an animal?", "options": ["Tiger", "Apple", "Car", "Table"], "correctAnswer": "Tiger"}
        ],
        "medium": [
            {"text": "Which is a conjunction?", "options": ["And", "Blue", "Fast", "Jump"], "correctAnswer": "And"},
            {"text": "Identify the adverb: 'He runs fast'.", "options": ["fast", "runs", "He", "is"], "correctAnswer": "fast"},
            {"text": "Superlative of 'Good'?", "options": ["Best", "Better", "Goodest", "More good"], "correctAnswer": "Best"},
            {"text": "Collective noun for 'Soldiers'?", "options": ["Army", "Pack", "Flock", "Herd"], "correctAnswer": "Army"},
            {"text": "Identify the tense: 'I will eat'.", "options": ["Future", "Present", "Past", "None"], "correctAnswer": "Future"},
            {"text": "Which is a 'Proper Noun'?", "options": ["India", "Country", "State", "City"], "correctAnswer": "India"},
            {"text": "Use 'a' or 'an': ___ umbrella.", "options": ["An", "A", "The", "Some"], "correctAnswer": "An"},
            {"text": "Antonym of 'Smooth'?", "options": ["Rough", "Soft", "Hard", "Big"], "correctAnswer": "Rough"},
            {"text": "Identify the Verb: 'She sings sweetly'.", "options": ["sings", "She", "sweetly", "is"], "correctAnswer": "sings"},
            {"text": "A person who teaches is a ___.", "options": ["Teacher", "Doctor", "Farmer", "Driver"], "correctAnswer": "Teacher"}
        ],
        "hard": [
            {"text": "Which is a silent letter in 'Honest'?", "options": ["H", "o", "n", "e"], "correctAnswer": "H"},
            {"text": "Identify the preposition: 'The book is on the table'.", "options": ["on", "book", "is", "table"], "correctAnswer": "on"},
            {"text": "Which is a 'Neuter' gender noun?", "options": ["Building", "King", "Maid", "Uncle"], "correctAnswer": "Building"},
            {"text": "Meaning of the idiom 'Under the weather'?", "options": ["Feeling sick", "Feeling happy", "Raining", "Sunny"], "correctAnswer": "Feeling sick"},
            {"text": "Identify the complex sentence.", "options": ["Because it was raining, we stayed home.", "We stayed home.", "It was raining and we stayed home.", "Stay home!"], "correctAnswer": "Because it was raining, we stayed home."},
            {"text": "Plural of 'Thesis'?", "options": ["Theses", "Thesises", "Thesis", "None"], "correctAnswer": "Theses"},
            {"text": "What is 'Alliteration'?", "options": ["Repetition of same consonant sounds", "Comparing two things", "Rhyming", "Exaggeration"], "correctAnswer": "Repetition of same consonant sounds"},
            {"text": "Which word is spelled correctly?", "options": ["Accommodation", "Acomodation", "Accomodation", "Acommodation"], "correctAnswer": "Accommodation"},
            {"text": "Antonym of 'Benevolent'?", "options": ["Malevolent", "Kind", "Strong", "Fast"], "correctAnswer": "Malevolent"},
            {"text": "Identify the direct object: 'He gave me a pen'.", "options": ["pen", "me", "He", "gave"], "correctAnswer": "pen"}
        ]
    },
    "maths": {
        "easy": [
            {"text": "What is 7 + 8?", "options": ["14", "15", "16", "17"], "correctAnswer": "15"},
            {"text": "Smallest odd prime number?", "options": ["3", "1", "2", "5"], "correctAnswer": "3"},
            {"text": "Number of vertices in a square?", "options": ["4", "3", "5", "6"], "correctAnswer": "4"},
            {"text": "What is 12 \u00d7 12?", "options": ["124", "144", "24", "100"], "correctAnswer": "144"},
            {"text": "Value of 1/4 + 1/4?", "options": ["1/2", "1/4", "1/8", "1"], "correctAnswer": "1/2"},
            {"text": "Which number is even?", "options": ["10", "11", "13", "15"], "correctAnswer": "10"},
            {"text": "How many cents in 1 dollar?", "options": ["100", "10", "1000", "50"], "correctAnswer": "100"},
            {"text": "A triangle with all sides equal is ___.", "options": ["Equilateral", "Isosceles", "Scalene", "Right-angled"], "correctAnswer": "Equilateral"},
            {"text": "What is 10 \u00d7 0.5?", "options": ["5", "50", "0.5", "1"], "correctAnswer": "5"},
            {"text": "Solve: 100 - 50 - 10", "options": ["40", "50", "60", "30"], "correctAnswer": "40"}
        ],
        "medium": [
            {"text": "Area of square with side 5cm?", "options": ["20sq cm", "25sq cm", "10sq cm", "50sq cm"], "correctAnswer": "25sq cm"},
            {"text": "Solve: 2x = 20", "options": ["10", "20", "5", "40"], "correctAnswer": "10"},
            {"text": "LCM of 12 and 15?", "options": ["60", "30", "120", "180"], "correctAnswer": "60"},
            {"text": "What is 25% of 400?", "options": ["100", "50", "200", "10"], "correctAnswer": "100"},
            {"text": "Perimeter of rectangle (L=10, W=5)?", "options": ["30", "15", "50", "20"], "correctAnswer": "30"},
            {"text": "Average of 4, 8, 12?", "options": ["8", "4", "12", "6"], "correctAnswer": "8"},
            {"text": "Solve: 3 + 2 \u00d7 5", "options": ["13", "25", "15", "10"], "correctAnswer": "13"},
            {"text": "Convert 1/5 to percentage.", "options": ["20%", "10%", "50%", "5%"], "correctAnswer": "20%"},
            {"text": "Sum of angles in a triangle is ___ degrees.", "options": ["180", "90", "360", "270"], "correctAnswer": "180"},
            {"text": "If speed = 60km/h, distance in 1.5 hours?", "options": ["90km", "60km", "120km", "40km"], "correctAnswer": "90km"}
        ],
        "hard": [
            {"text": "HCF of 48 and 72?", "options": ["24", "12", "48", "6"], "correctAnswer": "24"},
            {"text": "Solve: x/2 + 5 = 15", "options": ["20", "10", "30", "40"], "correctAnswer": "20"},
            {"text": "Volume of cube with side 4cm?", "options": ["64", "16", "32", "48"], "correctAnswer": "64"},
            {"text": "Express 0.125 as a fraction.", "options": ["1/8", "1/4", "1/2", "1/10"], "correctAnswer": "1/8"},
            {"text": "Ratio of 500g to 2kg is ___.", "options": ["1:4", "4:1", "1:2", "2:1"], "correctAnswer": "1:4"},
            {"text": "Square root of 225?", "options": ["15", "25", "5", "12"], "correctAnswer": "15"},
            {"text": "Number of edges in a triangular prism?", "options": ["9", "6", "12", "5"], "correctAnswer": "9"},
            {"text": "If (a/b) = (c/d), then ad = ___.", "options": ["bc", "ad", "1", "0"], "correctAnswer": "bc"},
            {"text": "Calculate Simple Interest: P=1000, R=10%, T=1 year.", "options": ["100", "1000", "10", "50"], "correctAnswer": "100"},
            {"text": "Value of Pi (\u03c0) up to 2 decimal places?", "options": ["3.14", "3.16", "3.12", "3.00"], "correctAnswer": "3.14"}
        ]
    },
    "science": {
        "easy": [
            {"text": "Smallest unit of life?", "options": ["Cell", "Tissue", "Organ", "Atom"], "correctAnswer": "Cell"},
            {"text": "Gas needed for photosynthesis?", "options": ["CO2", "Oxygen", "Nitrogen", "Hydrogen"], "correctAnswer": "CO2"},
            {"text": "pH of water?", "options": ["7", "1", "14", "0"], "correctAnswer": "7"},
            {"text": "Human bones count (Adult)?", "options": ["206", "300", "250", "200"], "correctAnswer": "206"},
            {"text": "Speed of Light?", "options": ["3 \u00d7 10^8 m/s", "3 \u00d7 10^5 m/s", "1 \u00d7 10^8 m/s", "Sound speed"], "correctAnswer": "3 \u00d7 10^8 m/s"},
            {"text": "Which gas is used in balloons?", "options": ["Helium", "Oxygen", "CO2", "Nitrogen"], "correctAnswer": "Helium"},
            {"text": "Ice melts at ___.", "options": ["0\u00b0C", "100\u00b0C", "50\u00b0C", "-10\u00b0C"], "correctAnswer": "0\u00b0C"},
            {"text": "Boiling point of water?", "options": ["100\u00b0C", "0\u00b0C", "212\u00b0F", "Both A & C"], "correctAnswer": "Both A & C"},
            {"text": "A magnet attracts ___.", "options": ["Iron", "Gold", "Silver", "Plastic"], "correctAnswer": "Iron"},
            {"text": "Chemical formula of Water?", "options": ["H2O", "CO2", "O2", "NaCl"], "correctAnswer": "H2O"}
        ],
        "medium": [
            {"text": "Force = Mass \u00d7 ___.", "options": ["Acceleration", "Velocity", "Distance", "Time"], "correctAnswer": "Acceleration"},
            {"text": "Which organ filters blood?", "options": ["Kidneys", "Lungs", "Heart", "Liver"], "correctAnswer": "Kidneys"},
            {"text": "SI unit of Energy?", "options": ["Joule", "Watt", "Newton", "Pascal"], "correctAnswer": "Joule"},
            {"text": "Chemical formula of Glucose?", "options": ["C6H12O6", "CO2", "NaCl", "H2O"], "correctAnswer": "C6H12O6"},
            {"text": "Which metal is liquid at RT?", "options": ["Mercury", "Gold", "Lead", "Bromine"], "correctAnswer": "Mercury"},
            {"text": "Number of chambers in heart?", "options": ["4", "2", "3", "1"], "correctAnswer": "4"},
            {"text": "Atomic number of Carbon?", "options": ["6", "12", "8", "1"], "correctAnswer": "6"},
            {"text": "Newton's 1st Law is Law of ___.", "options": ["Inertia", "Force", "Action/Reaction", "Gravity"], "correctAnswer": "Inertia"},
            {"text": "Main gas in air?", "options": ["Nitrogen (78%)", "Oxygen (21%)", "CO2", "Argon"], "correctAnswer": "Nitrogen (78%)"},
            {"text": "Mirror used for side-view in cars?", "options": ["Convex", "Concave", "Plane", "None"], "correctAnswer": "Convex"}
        ],
        "hard": [
            {"text": "Who discovered Electrons?", "options": ["J.J. Thomson", "Rutherford", "Goldstein", "Chadwick"], "correctAnswer": "J.J. Thomson"},
            {"text": "Mitochondria is powerhouse of ___.", "options": ["Cell", "Tissue", "Body", "Atom"], "correctAnswer": "Cell"},
            {"text": "Value of Gravitational constant 'G'?", "options": ["6.67 \u00d7 10^-11", "9.8", "6.63 \u00d7 10^-34", "3 \u00d7 10^8"], "correctAnswer": "6.67 \u00d7 10^-11"},
            {"text": "Full form of DNA?", "options": ["Deoxyribonucleic acid", "Double nucleic acid", "Daily news agency", "None"], "correctAnswer": "Deoxyribonucleic acid"},
            {"text": "Which acid is in our stomach?", "options": ["HCl", "H2SO4", "HNO3", "Acetic"], "correctAnswer": "HCl"},
            {"text": "Refractive index of diamond?", "options": ["2.42", "1.50", "1.33", "1.00"], "correctAnswer": "2.42"},
            {"text": "Plant tissue for water transport?", "options": ["Xylem", "Phloem", "Parenchyma", "Collenchyma"], "correctAnswer": "Xylem"},
            {"text": "Plant hormone for growth?", "options": ["Auxin", "Insulin", "Adrenaline", "Thyroxine"], "correctAnswer": "Auxin"},
            {"text": "Disease caused by lack of Vitamin C?", "options": ["Scurvy", "Rickets", "Beriberi", "Anemia"], "correctAnswer": "Scurvy"},
            {"text": "What is 1 Horse Power?", "options": ["746 Watts", "1000 Watts", "500 Watts", "250 Watts"], "correctAnswer": "746 Watts"}
        ]
    },
    "social-science": {
        "easy": [
            {"text": "Who is the Father of India?", "options": ["Gandhiji", "Nehru", "Bose", "Patel"], "correctAnswer": "Gandhiji"},
            {"text": "Red Planet?", "options": ["Mars", "Venus", "Earth", "Jupiter"], "correctAnswer": "Mars"},
            {"text": "Largest ocean?", "options": ["Pacific", "Atlantic", "Indian", "Arctic"], "correctAnswer": "Pacific"},
            {"text": "Capital of India?", "options": ["Delhi", "Mumbai", "Kolkata", "Chennai"], "correctAnswer": "Delhi"},
            {"text": "Independence year (India)?", "options": ["1947", "1950", "1942", "1960"], "correctAnswer": "1947"},
            {"text": "How many states in India?", "options": ["28", "25", "29", "30"], "correctAnswer": "28"},
            {"text": "Highest peak in India?", "options": ["Kanchenjunga", "Everest", "K2", "Nanda Devi"], "correctAnswer": "Kanchenjunga"},
            {"text": "The Sun rises in the ___.", "options": ["East", "West", "North", "South"], "correctAnswer": "East"},
            {"text": "World's largest desert?", "options": ["Sahara", "Gobi", "Thar", "Atacama"], "correctAnswer": "Sahara"},
            {"text": "How many continents?", "options": ["7", "5", "6", "8"], "correctAnswer": "7"}
        ],
        "medium": [
            {"text": "Where is UNO head office?", "options": ["New York", "London", "Paris", "Geneva"], "correctAnswer": "New York"},
            {"text": "Father of Green Revolution?", "options": ["Norman Borlaug", "M.S. Swaminathan", "Verghese Kurien", "None"], "correctAnswer": "Norman Borlaug"},
            {"text": "Smallest continent?", "options": ["Australia", "Europe", "Africa", "South America"], "correctAnswer": "Australia"},
            {"text": "Line dividing Earth North/South?", "options": ["Equator", "Prime Meridian", "Tropic of Cancer", "Axis"], "correctAnswer": "Equator"},
            {"text": "Parliament of India is in ___.", "options": ["Delhi", "Mumbai", "Kolkata", "Chennai"], "correctAnswer": "Delhi"},
            {"text": "First President of India?", "options": ["Rajendra Prasad", "Nehru", "Radhakrishnan", "Patel"], "correctAnswer": "Rajendra Prasad"},
            {"text": "Constitution Day of India?", "options": ["26 Nov", "26 Jan", "15 Aug", "2 Oct"], "correctAnswer": "26 Nov"},
            {"text": "The city of Temples is ___.", "options": ["Varanasi", "Delhi", "Mumbai", "Chennai"], "correctAnswer": "Varanasi"},
            {"text": "Coldest continent?", "options": ["Antarctica", "Asia", "Africa", "Europe"], "correctAnswer": "Antarctica"},
            {"text": "Blue Revolution is related to ___.", "options": ["Fish", "Milk", "Agriculture", "Petroleum"], "correctAnswer": "Fish"}
        ],
        "hard": [
            {"text": "Who gave slogan 'Swaraj is my birthright'?", "options": ["Tilak", "Gandhi", "Nehru", "Bose"], "correctAnswer": "Tilak"},
            {"text": "Majority age in India?", "options": ["18", "21", "25", "16"], "correctAnswer": "18"},
            {"text": "Highest waterfall in world?", "options": ["Angel Falls", "Niagara", "Victoria", "Jog"], "correctAnswer": "Angel Falls"},
            {"text": "When did French Revolution start?", "options": ["1789", "1750", "1800", "1850"], "correctAnswer": "1789"},
            {"text": "Gas protecting from UV rays?", "options": ["Ozone", "Oxygen", "CO2", "Nitrogen"], "correctAnswer": "Ozone"},
            {"text": "Who is head of Indian State?", "options": ["President", "PM", "Chief Justice", "Speaker"], "correctAnswer": "President"},
            {"text": "Battle of Panipat (1st) was in ___.", "options": ["1526", "1556", "1761", "1857"], "correctAnswer": "1526"},
            {"text": "Greenwich Mean Time (GMT) is in ___.", "options": ["UK", "USA", "India", "France"], "correctAnswer": "UK"},
            {"text": "Who founded Brahmo Samaj?", "options": ["Raja Ram Mohan Roy", "Dayanand Saraswati", "Vivekananda", "Tagore"], "correctAnswer": "Raja Ram Mohan Roy"},
            {"text": "The Silicon Valley of India?", "options": ["Bangalore", "Hyderabad", "Pune", "Chennai"], "correctAnswer": "Bangalore"}
        ]
    },
    "hindi": {
        "easy": [
            {"text": "'आज' का विलोम शब्द क्या है?", "options": ["कल", "परसों", "अतीत", "बाद"], "correctAnswer": "कल"},
            {"text": "'माता' का पर्यायवाची शब्द?", "options": ["माँ", "पिता", "भाई", "बहन"], "correctAnswer": "माँ"},
            {"text": "एक साल में कितने महीने होते हैं?", "options": ["12", "10", "11", "13"], "correctAnswer": "12"},
            {"text": "'हाथी' को हिंदी में और क्या कहते हैं?", "options": ["गज", "घोड़ा", "शेर", "ऊँट"], "correctAnswer": "गज"},
            {"text": "'मीठा' का विलोम शब्द क्या है?", "options": ["कड़वा", "खट्टा", "नमकीन", "तीखा"], "correctAnswer": "कड़वा"},
            {"text": "भारत की राजधानी क्या है?", "options": ["नई दिल्ली", "मुंबई", "कोलकाता", "चेन्नई"], "correctAnswer": "नई दिल्ली"},
            {"text": "हम कान से क्या करते हैं?", "options": ["सुनते हैं", "देखते हैं", "सूँघते हैं", "खाते हैं"], "correctAnswer": "सुनते हैं"},
            {"text": "सूरज किधर से निकलता है?", "options": ["पूर्व", "पश्चिम", "उत्तर", "दक्षिण"], "correctAnswer": "पूर्व"},
            {"text": "मोर हमारा राष्ट्रीय ___ है।", "options": ["पक्षी", "पशु", "फूल", "पेड़"], "correctAnswer": "पक्षी"},
            {"text": "'जल' का पर्यायवाची क्या है?", "options": ["पानी", "आग", "धूल", "हवा"], "correctAnswer": "पानी"}
        ],
        "medium": [
            {"text": "'मछली' का बहुवचन क्या है?", "options": ["मछलियाँ", "मछलियों", "मछले", "मछलीये"], "correctAnswer": "मछलियाँ"},
            {"text": "'वीर' का विलोम शब्द क्या है?", "options": ["कायर", "डरपोक", "दोनों", "बहादुर"], "correctAnswer": "दोनों"},
            {"text": "'पुष्प' का पर्यायवाची शब्द?", "options": ["फूल", "फल", "पेड़", "जड़"], "correctAnswer": "फूल"},
            {"text": "'आँख दिखाना' मुहावरे का अर्थ?", "options": ["गुस्सा करना", "प्यार करना", "सुझाव देना", "खेलना"], "correctAnswer": "गुस्सा करना"},
            {"text": "विशेषण के कितने मुख्य चार भेद हैं?", "options": ["हाँ", "नहीं", "पता नहीं", "शायद"], "correctAnswer": "हाँ"},
            {"text": "'अ' किस प्रकार का स्वर है?", "options": ["ह्रस्व", "दीर्घ", "प्लुत", "कोई नहीं"], "correctAnswer": "ह्रस्व"},
            {"text": "'ईश्वर' का पर्यायवाची शब्द?", "options": ["भगवान", "दानव", "इंसान", "पशु"], "correctAnswer": "भगवान"},
            {"text": "'सफ़ेद' का विलोम शब्द?", "options": ["काला", "नीला", "लाल", "पीला"], "correctAnswer": "काला"},
            {"text": "'सुंदर' का पर्यायवाची शब्द?", "options": ["मनोरम", "बदसूरत", "गंदा", "छोटा"], "correctAnswer": "मनोरम"},
            {"text": "सर्वनाम के कितने भेद होते हैं?", "options": ["6", "4", "5", "7"], "correctAnswer": "6"}
        ],
        "hard": [
            {"text": "'दोहरा' लाभ होने के लिए मुहावरा क्या है?", "options": ["आम के आम गुठलियों के दाम", "नौ दिन चले अढाई कोस", "ऊँट के मुँह में जीरा", "एक और एक ग्यारह"], "correctAnswer": "आम के आम गुठलियों के दाम"},
            {"text": "'विद्वान' का स्त्रीलिंग शब्द क्या होगा?", "options": ["विदुषी", "विद्वानी", "माता", "पढ़ी-लिखी"], "correctAnswer": "विदुषी"},
            {"text": "'उन्नति' का विलोम शब्द क्या है?", "options": ["अवनति", "प्रगति", "विकास", "नीचे"], "correctAnswer": "अवनति"},
            {"text": "'जिसका कोई शत्रु न हो' के लिए एक शब्द?", "options": ["अजातशत्रु", "मित्र", "दुश्मन", "शांत"], "correctAnswer": "अजातशत्रु"},
            {"text": "'घी के दिए जलाना' मुहावरे का अर्थ?", "options": ["खुशियाँ मनाना", "रोशनी करना", "खाना बनाना", "पूजा करना"], "correctAnswer": "खुशियाँ मनाना"},
            {"text": "'हिमालय' का अर्थ क्या है?", "options": ["बर्फ का घर", "पत्थर का घर", "पेड़ का घर", "आग का घर"], "correctAnswer": "बर्फ का घर"},
            {"text": "'विद्यार्थी' का सही संधि विच्छेद?", "options": ["विद्या + अर्थी", "विद्य + अर्थी", "विद्य + आर्थी", "विद्या + आर्थी"], "correctAnswer": "विद्या + अर्थी"},
            {"text": "'आकाश' का विलोम शब्द?", "options": ["पाताल", "धरती", "समुद्र", "वायु"], "correctAnswer": "पाताल"},
            {"text": "क्रिया के मूल रूप को क्या कहते हैं?", "options": ["धातु", "शब्द", "स्वर", "व्यंजन"], "correctAnswer": "धातु"},
            {"text": "'सर्वज्ञ' का अर्थ क्या है?", "options": ["सब कुछ जानने वाला", "थोड़ा जानने वाला", "कुछ न जानने वाला", "ज्ञानी"], "correctAnswer": "सब कुछ जानने वाला"}
        ]
    }
}

add_class_data('class_10', class_10_data)
