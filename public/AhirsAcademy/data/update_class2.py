import json
import os

class_2_data = {
    "english": {
        "easy": [
            {"text": "Which word is an action verb?", "options": ["Running", "Happy", "Table", "Blue"], "correctAnswer": "Running"},
            {"text": "Identify the proper noun in this sentence: 'Delhi is a big city.'", "options": ["Delhi", "Is", "Big", "City"], "correctAnswer": "Delhi"},
            {"text": "What is the past tense of 'Go'?", "options": ["Went", "Goed", "Going", "Gone"], "correctAnswer": "Went"},
            {"text": "Select the correct article: 'I saw ___ elephant at the zoo.'", "options": ["An", "A", "The", "No article needed"], "correctAnswer": "An"},
            {"text": "Which of these words is a pronoun?", "options": ["He", "Dog", "Fast", "Play"], "correctAnswer": "He"},
            {"text": "What does a baker do?", "options": ["Bakes bread", "Fixes cars", "Catches thieves", "Grows crops"], "correctAnswer": "Bakes bread"},
            {"text": "Which is the correct spelling?", "options": ["Beautiful", "Beutiful", "Beautifull", "Buitiful"], "correctAnswer": "Beautiful"},
            {"text": "Find the odd word out based on meaning.", "options": ["Cold", "Freezing", "Chilly", "Boiling"], "correctAnswer": "Boiling"},
            {"text": "What do we call the person who flies an airplane?", "options": ["Pilot", "Captain", "Driver", "Sailor"], "correctAnswer": "Pilot"},
            {"text": "Which word rhymes with 'Light'?", "options": ["Night", "Late", "Look", "Lake"], "correctAnswer": "Night"}
        ],
        "medium": [
            {"text": "Which word is an adjective in: 'The brave soldier fought well.'?", "options": ["Brave", "Soldier", "Fought", "Well"], "correctAnswer": "Brave"},
            {"text": "Complete the sentence: 'She went to the market ___ buy some fruits.'", "options": ["To", "For", "By", "With"], "correctAnswer": "To"},
            {"text": "What is the opposite of 'Arrive'?", "options": ["Depart", "Come", "Reach", "Stay"], "correctAnswer": "Depart"},
            {"text": "If a female horse is a mare, what is a young horse called?", "options": ["Foal", "Calf", "Cub", "Kid"], "correctAnswer": "Foal"},
            {"text": "Identify the incorrect plural form.", "options": ["Mouses", "Men", "Teeth", "Children"], "correctAnswer": "Mouses"},
            {"text": "What does the abbreviation 'Mr.' stand for?", "options": ["Mister", "Master", "Mayor", "Major"], "correctAnswer": "Mister"},
            {"text": "Which of these is a compound word?", "options": ["Toothbrush", "Elephants", "Running", "Quickly"], "correctAnswer": "Toothbrush"},
            {"text": "What do you call a book about a real person's life?", "options": ["Biography", "Fiction", "Comic", "Poetry"], "correctAnswer": "Biography"},
            {"text": "Which of these is a synonym for 'Silent'?", "options": ["Quiet", "Noisy", "Loud", "Fast"], "correctAnswer": "Quiet"},
            {"text": "Fill in the blank with the correct preposition: 'The cat jumped ___ the wall.'", "options": ["Over", "In", "Under", "Between"], "correctAnswer": "Over"}
        ],
        "hard": [
            {"text": "Which of the following sentences is in the future tense?", "options": ["I will go to the park.", "I went to the park.", "I am going to the park.", "I go to the park."], "correctAnswer": "I will go to the park."},
            {"text": "Choose the correct homophone: 'I need to ___ some bread for breakfast.'", "options": ["Buy", "By", "Bye", "Bough"], "correctAnswer": "Buy"},
            {"text": "Identify the adverb in the sentence: 'The turtle moved slowly.'", "options": ["Slowly", "Moved", "Turtle", "The"], "correctAnswer": "Slowly"},
            {"text": "If 'Quick' becomes 'Quickly', what does 'Happy' become?", "options": ["Happily", "Happyly", "Hapily", "Happiness"], "correctAnswer": "Happily"},
            {"text": "What is a group of stars forming a pattern called?", "options": ["Constellation", "Galaxy", "Solar System", "Planet"], "correctAnswer": "Constellation"},
            {"text": "Which part of a sentence tells us what the subject is doing?", "options": ["Verb / Predicate", "Noun", "Adjective", "Preposition"], "correctAnswer": "Verb / Predicate"},
            {"text": "What prefix can be added to the word 'Happy' to mean the opposite?", "options": ["Un-", "Dis-", "Re-", "Mis-"], "correctAnswer": "Un-"},
            {"text": "Find the conjunction in: 'I wanted to play, but it started raining.'", "options": ["But", "Play", "Started", "Wanted"], "correctAnswer": "But"},
            {"text": "What is the meaning of the idiom 'It is raining cats and dogs'?", "options": ["It is raining heavily.", "Animals are falling from the sky.", "It is drizzling.", "There is a storm with loud thunder."], "correctAnswer": "It is raining heavily."},
            {"text": "Which word has exactly three syllables?", "options": ["Beautiful", "Dog", "Apple", "Table"], "correctAnswer": "Beautiful"}
        ]
    },
    "maths": {
        "easy": [
            {"text": "What is 20 + 35?", "options": ["55", "45", "65", "50"], "correctAnswer": "55"},
            {"text": "How many tens are in the number 84?", "options": ["8", "4", "80", "12"], "correctAnswer": "8"},
            {"text": "Which number is an even number?", "options": ["14", "17", "21", "9"], "correctAnswer": "14"},
            {"text": "If you have 3 quarters, how many pieces do you have?", "options": ["3", "4", "2", "6"], "correctAnswer": "3"},
            {"text": "What comes next in the pattern: 5, 10, 15, 20, ___?", "options": ["25", "21", "30", "24"], "correctAnswer": "25"},
            {"text": "What shape has 6 sides?", "options": ["Hexagon", "Pentagon", "Octagon", "Square"], "correctAnswer": "Hexagon"},
            {"text": "If one dozen is 12, how many is half a dozen?", "options": ["6", "24", "10", "8"], "correctAnswer": "6"},
            {"text": "What is 40 - 15?", "options": ["25", "35", "20", "30"], "correctAnswer": "25"},
            {"text": "Which is the smallest number: 99, 101, 89, or 110?", "options": ["89", "99", "101", "110"], "correctAnswer": "89"},
            {"text": "How many months are there in 2 years?", "options": ["24", "12", "36", "48"], "correctAnswer": "24"}
        ],
        "medium": [
            {"text": "What is 7 multiplied by 3?", "options": ["21", "24", "18", "10"], "correctAnswer": "21"},
            {"text": "If a train starts at 4:30 PM and the journey takes 2 hours, at what time does it arrive?", "options": ["6:30 PM", "5:30 PM", "7:30 PM", "6:00 PM"], "correctAnswer": "6:30 PM"},
            {"text": "Which number is formed by 3 hundreds, 4 tens, and 5 ones?", "options": ["345", "543", "305", "435"], "correctAnswer": "345"},
            {"text": "What is 100 minus 45?", "options": ["55", "65", "45", "50"], "correctAnswer": "55"},
            {"text": "How many sides does a pentagon have?", "options": ["5", "6", "8", "4"], "correctAnswer": "5"},
            {"text": "If one notebook costs 20 rupees, how much do 4 notebooks cost?", "options": ["80", "60", "100", "40"], "correctAnswer": "80"},
            {"text": "Which fraction represents a half?", "options": ["1/2", "1/4", "1/3", "2/3"], "correctAnswer": "1/2"},
            {"text": "If you add the number of days in a normal February to 10, what do you get?", "options": ["38", "39", "40", "41"], "correctAnswer": "38"},
            {"text": "What is 36 divided by 6?", "options": ["6", "7", "5", "8"], "correctAnswer": "6"},
            {"text": "What place value is the '7' in the number 273?", "options": ["Tens", "Hundreds", "Ones", "Thousands"], "correctAnswer": "Tens"}
        ],
        "hard": [
            {"text": "If a farmer has 15 cows and 12 chickens, how many total legs are on the farm?", "options": ["84", "27", "60", "72"], "correctAnswer": "84"},
            {"text": "What is the product of 9 and 8?", "options": ["72", "81", "64", "70"], "correctAnswer": "72"},
            {"text": "Ravi has rs 100. He buys a toy for rs 45 and a pen for rs 25. How much money is left with him?", "options": ["rs 30", "rs 40", "rs 20", "rs 50"], "correctAnswer": "rs 30"},
            {"text": "What comes next in the sequence: 3, 6, 12, 24, ___?", "options": ["48", "36", "30", "40"], "correctAnswer": "48"},
            {"text": "What is 1000 minus 250?", "options": ["750", "850", "650", "500"], "correctAnswer": "750"},
            {"text": "A rectangular block has how many faces?", "options": ["6", "4", "8", "12"], "correctAnswer": "6"},
            {"text": "If today is the 3rd of the month and it is a Monday, what date will next Monday be?", "options": ["10th", "11th", "9th", "12th"], "correctAnswer": "10th"},
            {"text": "Which number gives the same result when multiplied by 10 as it does when added to 9?", "options": ["1", "0", "2", "3"], "correctAnswer": "1"},
            {"text": "If you have 4 quarters of an apple, how many whole apples do you have?", "options": ["1", "4", "2", "None"], "correctAnswer": "1"},
            {"text": "Which of these numbers is perfectly divisible by 5?", "options": ["85", "82", "99", "74"], "correctAnswer": "85"}
        ]
    },
    "hindi": {
        "easy": [
            {"text": "हिंदी वर्णमाला में कुल कितने स्वर होते हैं?", "options": ["11", "13", "33", "25"], "correctAnswer": "11"},
            {"text": "'कमल' शब्द में कितने अक्षर हैं?", "options": ["3", "2", "4", "1"], "correctAnswer": "3"},
            {"text": "'पेड़' का पर्यायवाची शब्द क्या है?", "options": ["वृक्ष", "फूल", "पत्ता", "जड़"], "correctAnswer": "वृक्ष"},
            {"text": "इनमें से कौन सा शब्द शुद्ध (सही) है?", "options": ["सूरज", "सुरज", "सूूरज", "शूरज"], "correctAnswer": "सूरज"},
            {"text": "'काला' रंग का उल्टा (विलोम) क्या है?", "options": ["सफ़ेद", "लाल", "हरा", "पीला"], "correctAnswer": "सफ़ेद"},
            {"text": "जिस पर हम लिखते हैं, उसे क्या कहते हैं?", "options": ["कागज़", "दीवार", "पत्ता", "कपड़ा"], "correctAnswer": "कागज़"},
            {"text": "त्योहारों का देश किसे कहा जाता है?", "options": ["भारत", "चीन", "जापान", "अमेरिका"], "correctAnswer": "भारत"},
            {"text": "सप्ताह में 'बुधवार' के बाद क्या आता है?", "options": ["गुरुवार", "मंगलवार", "शुक्रवार", "सोमवार"], "correctAnswer": "गुरुवार"},
            {"text": "हाथी का बच्चा क्या कहलाता है?", "options": ["कलभ (Baby Elephant)", "बछड़ा", "शावक", "पिल्ला"], "correctAnswer": "कलभ (Baby Elephant)"},
            {"text": "हम कहाँ से ज्ञान प्राप्त करते हैं?", "options": ["विद्यालय (स्कूल)", "दुकान", "बाज़ार", "खेत"], "correctAnswer": "विद्यालय (स्कूल)"}
        ],
        "medium": [
            {"text": "संज्ञा के स्थान पर आने वाले शब्द क्या कहलाते हैं?", "options": ["सर्वनाम", "विशेषण", "क्रिया", "अव्यय"], "correctAnswer": "सर्वनाम"},
            {"text": "'सुंदर' शब्द का विलोम क्या है?", "options": ["कुरूप / बदसूरत", "अच्छा", "मधुर", "तेज़"], "correctAnswer": "कुरूप / बदसूरत"},
            {"text": "किस मौसम में हम ऊनी कपड़े पहनते हैं?", "options": ["सर्दियों में", "गर्मियों में", "बरसात में", "वसंत में"], "correctAnswer": "सर्दियों में"},
            {"text": "इनमें से कौन सा शब्द विशेषण (describing word) है?", "options": ["लाल", "किताब", "दौड़ना", "मोहन"], "correctAnswer": "लाल"},
            {"text": "'नदी' का बहुवचन क्या होगा?", "options": ["नदियाँ", "नदीयों", "नदिएँ", "नदियें"], "correctAnswer": "नदियाँ"},
            {"text": "राष्ट्रीय ध्वज (तिरंगा) में कितने रंग होते हैं (चक्र छोड़कर)?", "options": ["3", "4", "2", "5"], "correctAnswer": "3"},
            {"text": "दिवाली का त्योहार किस महीने में आता है?", "options": ["कार्तिक (अक्टूबर/नवंबर)", "चैत्र (मार्च)", "माघ (जनवरी)", "श्रावण (अगस्त)"], "correctAnswer": "कार्तिक (अक्टूबर/नवंबर)"},
            {"text": "'घोड़ा' क्या करता है?", "options": ["हिनहिनाता है", "भोंकता है", "दहाड़ता है", "रंभाता है"], "correctAnswer": "हिनहिनाता है"},
            {"text": "हमें बड़ों का क्या करना चाहिए?", "options": ["आदर (सम्मान)", "अपमान", "गुस्सा", "अनदेखा"], "correctAnswer": "आदर (सम्मान)"},
            {"text": "जो कपड़े धोता है उसे क्या कहते हैं?", "options": ["धोबी", "मोची", "दर्जी", "नाई"], "correctAnswer": "धोबी"}
        ],
        "hard": [
            {"text": "'आंखों का तारा' मुहावरे का अर्थ क्या है?", "options": ["बहुत प्यारा", "आंखों में दर्द", "आसमान का तारा", "बहुत दूर"], "correctAnswer": "बहुत प्यारा"},
            {"text": "स्त्रीलिंग शब्द चुनें।", "options": ["गाय", "बैल", "शेर", "ऊंट"], "correctAnswer": "गाय"},
            {"text": "कौन सा शब्द 'जल' का पर्यायवाची नहीं है?", "options": ["अनल", "पानी", "नीर", "सलिल"], "correctAnswer": "अनल"},
            {"text": "'मछली जल की रानी है', इस वाक्य में संज्ञा शब्द कितने हैं?", "options": ["3 (मछली, जल, रानी)", "2", "1", "4"], "correctAnswer": "3 (मछली, जल, रानी)"},
            {"text": "जो कभी ना मरे, उसे क्या कहते हैं?", "options": ["अमर", "अजर", "अनंत", "ईश्वर"], "correctAnswer": "अमर"},
            {"text": "दिए गए शब्दों में से कौन सा क्रिया (verb) है?", "options": ["खेलना", "सुंदर", "कलम", "आसमान"], "correctAnswer": "खेलना"},
            {"text": "किस त्योहार पर हम एक-दूसरे को रंग लगाते हैं?", "options": ["होली", "दिवाली", "ईद", "क्रिसमस"], "correctAnswer": "होली"},
            {"text": "'पवन' शब्द का अर्थ क्या है?", "options": ["हवा", "आग", "धरती", "आसमान"], "correctAnswer": "हवा"},
            {"text": "इनमें से कौन सा शब्द एक वचन है?", "options": ["किताब", "कलमें", "चूहे", "लड़के"], "correctAnswer": "किताब"},
            {"text": "उचित शब्द से वाक्य भरें: 'राम ने रावण को _____ मारा।'", "options": ["से", "ने", "पर", "को"], "correctAnswer": "से"}
        ]
    }
}

def main():
    bank_path = '/Users/arpan1.mukherjee/code/GhostMaze/public/AhirsAcademy/data/question_bank.json'
    
    with open(bank_path, 'r', encoding='utf-8') as f:
        question_bank = json.load(f)
        
    question_bank['class_2'] = class_2_data
    
    with open(bank_path, 'w', encoding='utf-8') as f:
        json.dump(question_bank, f, indent=4, ensure_ascii=False)
        
    print("Successfully injected Class 2 tough questions!")

if __name__ == '__main__':
    main()
