import json
import os

class_4_data = {
    "english": {
        "easy": [
            {"text": "Which part of speech describes a noun?", "options": ["Adjective", "Verb", "Adverb", "Preposition"], "correctAnswer": "Adjective"},
            {"text": "What is the subject of this sentence: 'The clever fox outsmarted the dog.'", "options": ["The clever fox", "Outsmarted", "The dog", "Clever"], "correctAnswer": "The clever fox"},
            {"text": "Which word is a synonym for 'wealthy'?", "options": ["Rich", "Poor", "Healthy", "Smart"], "correctAnswer": "Rich"},
            {"text": "What is the past tense of 'Catch'?", "options": ["Caught", "Catched", "Catching", "Catches"], "correctAnswer": "Caught"},
            {"text": "Identify the proper noun: 'We went to the zoo in Mumbai.'", "options": ["Mumbai", "We", "Zoo", "Went"], "correctAnswer": "Mumbai"},
            {"text": "Which of these is an article?", "options": ["An", "On", "In", "At"], "correctAnswer": "An"},
            {"text": "Complete the proverb: 'An apple a day keeps the _____ away.'", "options": ["Doctor", "Teacher", "Thief", "Hunger"], "correctAnswer": "Doctor"},
            {"text": "Which word has the correct spelling?", "options": ["Receive", "Recieve", "Receve", "Reseive"], "correctAnswer": "Receive"},
            {"text": "What do we call a person who writes poems?", "options": ["Poet", "Author", "Novelist", "Artist"], "correctAnswer": "Poet"},
            {"text": "Identify the antonym for 'Giant'.", "options": ["Tiny", "Huge", "Strong", "Fierce"], "correctAnswer": "Tiny"}
        ],
        "medium": [
            {"text": "Find the adverb in: 'The sun shone brightly over the mountains.'", "options": ["Brightly", "Shone", "Sun", "Over"], "correctAnswer": "Brightly"},
            {"text": "Which conjunction best completes the sentence: 'I wanted to go out, _____ it was raining heavily.'", "options": ["But", "And", "Or", "Because"], "correctAnswer": "But"},
            {"text": "Choose the correct collective noun: 'A _____ of lions.'", "options": ["Pride", "Flock", "Herd", "Swarm"], "correctAnswer": "Pride"},
            {"text": "Identify the tense: 'They have been playing football for two hours.'", "options": ["Present Perfect Continuous", "Present Continuous", "Simple Past", "Future Continuous"], "correctAnswer": "Present Perfect Continuous"},
            {"text": "What does the idiom 'Break a leg' mean?", "options": ["Good luck", "To get hurt", "To dance", "Stop walking"], "correctAnswer": "Good luck"},
            {"text": "Select the correct homophone: 'I cannot _____ the pin on the floor.'", "options": ["See", "Sea", "Se", "Cee"], "correctAnswer": "See"},
            {"text": "Form an abstract noun from the word 'Honest'.", "options": ["Honesty", "Honestly", "Honestness", "Honesting"], "correctAnswer": "Honesty"},
            {"text": "Which punctuation is missing: 'I bought apples bananas and oranges.'", "options": ["Comma (,)", "Exclamation (!)", "Question Mark (?)", "Apostrophe (')"], "correctAnswer": "Comma (,)"},
            {"text": "Choose the most suitable preposition: 'The cat jumped _____ the fence.'", "options": ["Over", "Under", "In", "At"], "correctAnswer": "Over"},
            {"text": "Which figure of speech is used here: 'He is as brave as a lion.'?", "options": ["Simile", "Metaphor", "Personification", "Hyperbole"], "correctAnswer": "Simile"}
        ],
        "hard": [
            {"text": "Identify the predicate in the sentence: 'The mysterious old house at the end of the street was finally sold.'", "options": ["was finally sold", "The mysterious old house", "at the end of the street", "The mysterious old house at the end of the street"], "correctAnswer": "was finally sold"},
            {"text": "Change into indirect speech: She said, 'I am reading a novel.'", "options": ["She said that she was reading a novel.", "She says that she is reading a novel.", "She said that she is reading a novel.", "She said I am reading a novel."], "correctAnswer": "She said that she was reading a novel."},
            {"text": "Find the correctly punctuated sentence.", "options": ["\"Hurry up!\" shouted the captain. \"We are leaving!\"", "\"Hurry up\" shouted the captain. \"we are leaving!\"", "Hurry up! Shouted the captain. We are leaving!", "\"Hurry up!\" Shouted the captain. \"We are leaving!\""], "correctAnswer": "\"Hurry up!\" shouted the captain. \"We are leaving!\""},
            {"text": "What is the meaning of the prefix 'multi-' as in 'multinational'?", "options": ["Many", "One", "Below", "After"], "correctAnswer": "Many"},
            {"text": "Which sentence contains a transitive verb?", "options": ["The boy kicked the ball.", "The dog barked loudly.", "She slept for ten hours.", "The sun rises in the east."], "correctAnswer": "The boy kicked the ball."},
            {"text": "Choose the correct word to complete the analogy: 'Bird is to Fly as Fish is to _____'?", "options": ["Swim", "Water", "Gills", "Fin"], "correctAnswer": "Swim"},
            {"text": "Identify the relative pronoun: 'The book which you gave me is interesting.'", "options": ["Which", "The", "You", "Me"], "correctAnswer": "Which"},
            {"text": "What type of sentence is this: 'Please close the door.'?", "options": ["Imperative", "Declarative", "Interrogative", "Exclamatory"], "correctAnswer": "Imperative"},
            {"text": "Replace the underlined phrase with a single word: 'He gave an answer that <u>could not be understood</u>.'", "options": ["Incomprehensible", "Intelligent", "Invisible", "Incredible"], "correctAnswer": "Incomprehensible"},
            {"text": "Find the error in the sentence: 'Neither of the boys have brought their books.'", "options": ["'have' should be 'has'", "'their' should be 'there'", "'boys' should be 'boy'", "The sentence is correct"], "correctAnswer": "'have' should be 'has'"}
        ]
    },
    "maths": {
        "easy": [
            {"text": "What is the place value of 7 in the number 4,732?", "options": ["700", "70", "7000", "7"], "correctAnswer": "700"},
            {"text": "What is 15 multiplied by 10?", "options": ["150", "105", "1500", "15"], "correctAnswer": "150"},
            {"text": "Which number is a multiple of both 2 and 5?", "options": ["10", "15", "12", "7"], "correctAnswer": "10"},
            {"text": "If a rectangle has a length of 8 cm and width of 4 cm, what is its perimeter?", "options": ["24 cm", "32 cm", "12 cm", "16 cm"], "correctAnswer": "24 cm"},
            {"text": "What is 500 minus 125?", "options": ["375", "475", "325", "425"], "correctAnswer": "375"},
            {"text": "Which fraction is the largest?", "options": ["3/4", "1/4", "2/4", "They are equal"], "correctAnswer": "3/4"},
            {"text": "How many days are in the month of August?", "options": ["31", "30", "28", "29"], "correctAnswer": "31"},
            {"text": "What comes next: 10, 20, 30, 40, ___?", "options": ["50", "45", "60", "100"], "correctAnswer": "50"},
            {"text": "Find the sum of 1234 and 4321.", "options": ["5555", "5545", "5455", "5655"], "correctAnswer": "5555"},
            {"text": "What shape has exactly 8 sides?", "options": ["Octagon", "Hexagon", "Pentagon", "Decagon"], "correctAnswer": "Octagon"}
        ],
        "medium": [
            {"text": "Find the lowest common multiple (LCM) of 4 and 6.", "options": ["12", "24", "10", "8"], "correctAnswer": "12"},
            {"text": "If a train travels 60 km in 1 hour, how far will it travel in 3.5 hours at the same speed?", "options": ["210 km", "180 km", "200 km", "220 km"], "correctAnswer": "210 km"},
            {"text": "Convert 3.5 kilograms into grams.", "options": ["3500 g", "350 g", "35000 g", "35 g"], "correctAnswer": "3500 g"},
            {"text": "What is the area of a square with a side length of 7 cm?", "options": ["49 sq cm", "28 sq cm", "14 sq cm", "21 sq cm"], "correctAnswer": "49 sq cm"},
            {"text": "Solve: 48 ÷ 6 + 4", "options": ["12", "8", "4", "10"], "correctAnswer": "12"},
            {"text": "Which of these is a prime number?", "options": ["11", "9", "15", "21"], "correctAnswer": "11"},
            {"text": "What is the decimal equivalent of the fraction 1/2?", "options": ["0.5", "0.2", "0.25", "0.1"], "correctAnswer": "0.5"},
            {"text": "If you buy 3 books costing Rs 45 each, and give a Rs 200 note, what is your change?", "options": ["Rs 65", "Rs 55", "Rs 75", "Rs 135"], "correctAnswer": "Rs 65"},
            {"text": "A clock shows 3:45. What time will it be in 40 minutes?", "options": ["4:25", "4:15", "4:30", "4:05"], "correctAnswer": "4:25"},
            {"text": "What is the highest common factor (HCF) of 12 and 18?", "options": ["6", "3", "2", "36"], "correctAnswer": "6"}
        ],
        "hard": [
            {"text": "A rope is 10 m 45 cm long. A piece of 3 m 80 cm is cut from it. What is the remaining length?", "options": ["6 m 65 cm", "7 m 35 cm", "6 m 25 cm", "7 m 65 cm"], "correctAnswer": "6 m 65 cm"},
            {"text": "Solve: (15 × 4) - (36 ÷ 9)", "options": ["56", "60", "54", "50"], "correctAnswer": "56"},
            {"text": "A rectangular garden has an area of 120 sq meters. If the length is 12 meters, what is its perimeter?", "options": ["44 meters", "22 meters", "10 meters", "60 meters"], "correctAnswer": "44 meters"},
            {"text": "If 5 workers can build a wall in 10 days, how long would it take 10 workers working at the same rate?", "options": ["5 days", "20 days", "15 days", "2 days"], "correctAnswer": "5 days"},
            {"text": "Find the sum of all prime numbers between 10 and 20.", "options": ["60", "58", "41", "77"], "correctAnswer": "60"},
            {"text": "Which of the following fractions is equivalent to 0.75?", "options": ["3/4", "1/4", "4/5", "7/10"], "correctAnswer": "3/4"},
            {"text": "What is the difference between the largest 4-digit number and the smallest 3-digit number?", "options": ["9899", "9900", "9000", "9890"], "correctAnswer": "9899"},
            {"text": "An angle measuring 135 degrees is called a/an ________ angle.", "options": ["Obtuse", "Acute", "Right", "Straight"], "correctAnswer": "Obtuse"},
            {"text": "If 1/4 of a number is 15, what is the number?", "options": ["60", "30", "45", "120"], "correctAnswer": "60"},
            {"text": "A water tank is 3/5 full. If it contains 60 liters of water, what is its total capacity?", "options": ["100 liters", "150 liters", "80 liters", "120 liters"], "correctAnswer": "100 liters"}
        ]
    },
    "hindi": {
        "easy": [
            {"text": "हिंदी भाषा की लिपि क्या है?", "options": ["देवनागरी", "रोमन", "गुरुमुखी", "ब्राह्मी"], "correctAnswer": "देवनागरी"},
            {"text": "'सूरज' का पर्यायवाची (समानार्थी) शब्द क्या है?", "options": ["दिनकर", "शशि", "तारा", "गगन"], "correctAnswer": "दिनकर"},
            {"text": "'सुख' का विलोम शब्द चुनें।", "options": ["दुख", "उदासी", "शांति", "क्रोध"], "correctAnswer": "दुख"},
            {"text": "इनमें से कौन सा शब्द शुद्ध (Spelling) है?", "options": ["बीमारी", "बिमारी", "बीमरी", "बिमारी"], "correctAnswer": "बीमारी"},
            {"text": "भारत के प्रथम प्रधानमंत्री कौन थे?", "options": ["पंडित जवाहरलाल नेहरू", "महात्मा गांधी", "लाला लाजपत राय", "भगत सिंह"], "correctAnswer": "पंडित जवाहरलाल नेहरू"},
            {"text": "जो चित्र बनाता हो उसे क्या कहते हैं?", "options": ["चित्रकार", "गीतकार", "कहानीकार", "मूर्तिकार"], "correctAnswer": "चित्रकार"},
            {"text": "'आसमान' का रंग कैसा होता है?", "options": ["नीला", "पीला", "लाल", "हरा"], "correctAnswer": "नीला"},
            {"text": "'मामा' का स्त्रीलिंग क्या होगा?", "options": ["मामी", "मौसी", "बुआ", "चाची"], "correctAnswer": "मामी"},
            {"text": "ईद का मुख्य पकवान क्या होता है?", "options": ["सेवइयां", "लड्डू", "जलेबी", "गुझिया"], "correctAnswer": "सेवइयां"},
            {"text": "सप्ताह में कितने दिन होते हैं?", "options": ["7", "6", "5", "8"], "correctAnswer": "7"}
        ],
        "medium": [
            {"text": "जिस शब्द से किसी काम के करने या होने का पता चले, उसे क्या कहते हैं?", "options": ["क्रिया", "संज्ञा", "सर्वनाम", "विशेषण"], "correctAnswer": "क्रिया"},
            {"text": "इनमें से तत्सम शब्द (मूल संस्कृत) कौन सा है?", "options": ["अग्नि", "आग", "पानी", "हाथ"], "correctAnswer": "अग्नि"},
            {"text": "'नौ दो ग्यारह होना' मुहावरे का अर्थ क्या है?", "options": ["भाग जाना", "गिनती करना", "धोखा देना", "मिल जाना"], "correctAnswer": "भाग जाना"},
            {"text": "विशेषण शब्द चुनें: 'काला कुत्ता भौंक रहा है।'", "options": ["काला", "कुत्ता", "भौंक", "रहा है"], "correctAnswer": "काला"},
            {"text": "संधि विच्छेद करें: 'हिमालय'", "options": ["हिम + आलय", "हिमाल + य", "हिमा + लय", "हिम + आालय"], "correctAnswer": "हिम + आलय"},
            {"text": "इनमें से भाववाचक संज्ञा कौन सी है?", "options": ["बचपन", "बच्चा", "खेल", "मैदान"], "correctAnswer": "बचपन"},
            {"text": "हमारा राष्ट्रीय गान 'जन-गण-मन' किसने लिखा था?", "options": ["रवींद्रनाथ टैगोर", "बंकिम चंद्र चटर्जी", "महात्मा गांधी", "सुभाष चंद्र बोस"], "correctAnswer": "रवींद्रनाथ टैगोर"},
            {"text": "'आंखों में धूल झोंकना' मुहावरे का अर्थ:", "options": ["धोखा देना", "आंखों में दर्द होना", "रेत फेंकना", "मदद करना"], "correctAnswer": "धोखा देना"},
            {"text": "उचित विराम चिह्न (Punctuation) चुनें: 'क्या तुम कल आओगे_'", "options": ["प्रश्नवाचक चिह्न (?)", "पूर्ण विराम (।)", "अल्पविराम (,)", "विस्मयादिबोधक (!)"], "correctAnswer": "प्रश्नवाचक चिह्न (?)"},
            {"text": "जो ईश्वर को न मानता हो, उसे क्या कहते हैं?", "options": ["नास्तिक", "आस्तिक", "संत", "पापी"], "correctAnswer": "नास्तिक"}
        ],
        "hard": [
            {"text": "'गगनचुंबी' शब्द में कौन सा समास है?", "options": ["तत्पुरुष", "कर्मधारय", "द्वंद्व", "बहुव्रीहि"], "correctAnswer": "तत्पुरुष"},
            {"text": "नीचे दिए गए वाक्यों में से अशुद्ध वाक्य पहचानें।", "options": ["राम ने रावण को मारा।", "मेरे को यह किताब चाहिए।", "वह स्कूल जा रहा है।", "सीता गाना गाती है।"], "correctAnswer": "मेरे को यह किताब चाहिए।"},
            {"text": "जिसके हृदय में दया न हो, उसे क्या कहते हैं?", "options": ["निर्दय", "कठोर", "पाषाण", "जालिम"], "correctAnswer": "निर्दय"},
            {"text": "इनमें से कौन सा शब्द उपसर्ग 'नि' से नहीं बना है?", "options": ["निडर", "निकम्मा", "निवास", "नियम"], "correctAnswer": "निकम्मा"},
            {"text": "सही कहावत पूरी करें: 'अधजल गगरी _____।'", "options": ["छलकत जाए", "खलकती जाए", "पलटत जाए", "गिरत जाए"], "correctAnswer": "छलकत जाए"},
            {"text": "'सरोज' का संधि विच्छेद क्या होगा?", "options": ["सर: + ज", "सर + ओज", "सरो + ज", "सर् + ओज"], "correctAnswer": "सर: + ज"},
            {"text": "'पवन' शब्द में कौन सी संधि है?", "options": ["अयादि संधि", "यण संधि", "गुण संधि", "दीर्घ संधि"], "correctAnswer": "अयादि संधि"},
            {"text": "इनमें से रूढ़ शब्द कौन सा है?", "options": ["पानी", "विद्यार्थी", "पंकज", "जलज"], "correctAnswer": "पानी"},
            {"text": "'कमल' का पर्यायवाची नहीं है:", "options": ["वारिद", "जलज", "नीरज", "पंकज"], "correctAnswer": "वारिद"},
            {"text": "वाच्य के कितने प्रकार होते हैं?", "options": ["तीन (कर्तृ, कर्म, भाव)", "दो", "चार", "पांच"], "correctAnswer": "तीन (कर्तृ, कर्म, भाव)"}
        ]
    },
    "evs": {
        "easy": [
            {"text": "Which plant gives us medicine to cure malaria?", "options": ["Cinchona", "Neem", "Tulsi", "Aloe Vera"], "correctAnswer": "Cinchona"},
            {"text": "Which sense helps an eagle spot its prey from very high up?", "options": ["Sight (Vision)", "Hearing", "Smell", "Touch"], "correctAnswer": "Sight (Vision)"},
            {"text": "What do we call a person who travels in space?", "options": ["Astronaut", "Astronomer", "Pilot", "Scientist"], "correctAnswer": "Astronaut"},
            {"text": "Which gas do we breathe in to stay alive?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "correctAnswer": "Oxygen"},
            {"text": "Where does a camel store fat to survive in the desert?", "options": ["In its hump", "In its stomach", "In its legs", "In its neck"], "correctAnswer": "In its hump"},
            {"text": "Which of these is a renewable source of energy?", "options": ["Solar Energy", "Coal", "Petrol", "Natural Gas"], "correctAnswer": "Solar Energy"},
            {"text": "Which animal is a marsupial and carries its baby in a pouch?", "options": ["Kangaroo", "Monkey", "Bear", "Elephant"], "correctAnswer": "Kangaroo"},
            {"text": "What does a green traffic light mean?", "options": ["Go", "Stop", "Wait", "Slow Down"], "correctAnswer": "Go"},
            {"text": "What do we call the young one of a frog?", "options": ["Tadpole", "Caterpillar", "Calf", "Fry"], "correctAnswer": "Tadpole"},
            {"text": "What do herbivores primarily eat?", "options": ["Plants", "Meat", "Insects", "Both Plants and Meat"], "correctAnswer": "Plants"}
        ],
        "medium": [
            {"text": "Which part of the respiratory system helps in taking in oxygen and giving out carbon dioxide?", "options": ["Lungs", "Heart", "Kidneys", "Stomach"], "correctAnswer": "Lungs"},
            {"text": "Which of these birds cannot fly but can run very fast?", "options": ["Ostrich", "Eagle", "Penguin", "Parrot"], "correctAnswer": "Ostrich"},
            {"text": "What process occurs when water vapor cools down and turns back into liquid water?", "options": ["Condensation", "Evaporation", "Melting", "Freezing"], "correctAnswer": "Condensation"},
            {"text": "Deficiency of Vitamin C causes which disease?", "options": ["Scurvy", "Rickets", "Beriberi", "Night Blindness"], "correctAnswer": "Scurvy"},
            {"text": "What kind of teeth are used for tearing food?", "options": ["Canines", "Incisors", "Molars", "Premolars"], "correctAnswer": "Canines"},
            {"text": "Which famous Indian monument changes its color under moonlight?", "options": ["Taj Mahal", "Red Fort", "Qutub Minar", "India Gate"], "correctAnswer": "Taj Mahal"},
            {"text": "What are the two main types of root systems in plants?", "options": ["Tap root and Fibrous root", "Underground and Aerial", "Thick and Thin", "Green and Brown"], "correctAnswer": "Tap root and Fibrous root"},
            {"text": "What force pulls objects towards the Earth?", "options": ["Gravity", "Friction", "Magnetism", "Pressure"], "correctAnswer": "Gravity"},
            {"text": "What is the natural satellite of the Earth?", "options": ["The Moon", "The Sun", "Mars", "A comet"], "correctAnswer": "The Moon"},
            {"text": "Which component of soil is made of dead and decaying plants and animals?", "options": ["Humus / Organic matter", "Sand", "Clay", "Gravel"], "correctAnswer": "Humus / Organic matter"}
        ],
        "hard": [
            {"text": "What is the green pigment in leaves that helps capture sunlight for photosynthesis?", "options": ["Chlorophyll", "Hemoglobin", "Melanin", "Carotene"], "correctAnswer": "Chlorophyll"},
            {"text": "In the human digestive system, where does the maximum absorption of nutrients take place?", "options": ["Small Intestine", "Stomach", "Large Intestine", "Esophagus"], "correctAnswer": "Small Intestine"},
            {"text": "State the phenomenon where animals go into a deep winter sleep to survive cold weather.", "options": ["Hibernation", "Migration", "Aestivation", "Incubation"], "correctAnswer": "Hibernation"},
            {"text": "Which instrument is used to see very tiny organisms that cannot be seen with the naked eye?", "options": ["Microscope", "Telescope", "Periscope", "Kaleidoscope"], "correctAnswer": "Microscope"},
            {"text": "What is the name of the imaginary line that divides the Earth into the Northern and Southern Hemispheres?", "options": ["The Equator", "The Tropic of Cancer", "The Prime Meridian", "The Tropic of Capricorn"], "correctAnswer": "The Equator"},
            {"text": "The ozone layer protects us from which harmful rays of the Sun?", "options": ["Ultraviolet (UV) Rays", "Infrared Rays", "Gamma Rays", "X-Rays"], "correctAnswer": "Ultraviolet (UV) Rays"},
            {"text": "What type of simple machine is a seesaw?", "options": ["Lever", "Pulley", "Inclined Plane", "Wheel and Axle"], "correctAnswer": "Lever"},
            {"text": "Which disease is transmitted by the bite of the female Anopheles mosquito?", "options": ["Malaria", "Dengue", "Typhoid", "Cholera"], "correctAnswer": "Malaria"},
            {"text": "What is the chemical symbol for Water?", "options": ["H2O", "CO2", "O2", "NaCl"], "correctAnswer": "H2O"},
            {"text": "Name the process by which soil is carried away by wind or water.", "options": ["Soil Erosion", "Weathering", "Deposition", "Conservation"], "correctAnswer": "Soil Erosion"}
        ]
    }
}

def main():
    bank_path = '/Users/arpan1.mukherjee/code/GhostMaze/public/AhirsAcademy/data/question_bank.json'
    
    with open(bank_path, 'r', encoding='utf-8') as f:
        question_bank = json.load(f)
        
    question_bank['class_4'] = class_4_data
    
    with open(bank_path, 'w', encoding='utf-8') as f:
        json.dump(question_bank, f, indent=4, ensure_ascii=False)
        
    print("Successfully injected brilliant and deep questions for Class 4!")

if __name__ == '__main__':
    main()
