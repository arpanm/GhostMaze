import json
import os

class_5_data = {
    "english": {
        "easy": [
            {"text": "Which word is a synonym for 'brave'?", "options": ["Courageous", "Fearful", "Timid", "Weak"], "correctAnswer": "Courageous"},
            {"text": "Identify the type of noun for the word 'Happiness'.", "options": ["Abstract Noun", "Proper Noun", "Collective Noun", "Material Noun"], "correctAnswer": "Abstract Noun"},
            {"text": "What is the past participle of 'write'?", "options": ["Written", "Wrote", "Writing", "Writes"], "correctAnswer": "Written"},
            {"text": "Which prefix changes 'Connect' to its opposite?", "options": ["Dis-", "Un-", "Re-", "Mis-"], "correctAnswer": "Dis-"},
            {"text": "Select the correct article: 'He is _____ honest man.'", "options": ["An", "A", "The", "No article needed"], "correctAnswer": "An"},
            {"text": "Choose the correctly spelled word.", "options": ["Environment", "Enviroment", "Enviornment", "Environemnt"], "correctAnswer": "Environment"},
            {"text": "What does the root word 'Bio' mean?", "options": ["Life", "Earth", "Star", "Water"], "correctAnswer": "Life"},
            {"text": "Which punctuation mark is used to show possession (e.g., the book belonging to John)?", "options": ["Apostrophe (')", "Comma (,)", "Hyphen (-)", "Colon (:)"], "correctAnswer": "Apostrophe (')"},
            {"text": "Find the odd word out.", "options": ["Cautious", "Careful", "Alert", "Reckless"], "correctAnswer": "Reckless"},
            {"text": "Which part of speech connects words, phrases, or clauses?", "options": ["Conjunction", "Preposition", "Interjection", "Adverb"], "correctAnswer": "Conjunction"}
        ],
        "medium": [
            {"text": "Identify the figure of speech: 'The wind whispered through the trees.'", "options": ["Personification", "Simile", "Metaphor", "Hyperbole"], "correctAnswer": "Personification"},
            {"text": "Choose the correct preposition: 'He is completely engrossed _____ his studies.'", "options": ["In", "With", "At", "From"], "correctAnswer": "In"},
            {"text": "What is the meaning of the idiom 'To let the cat out of the bag'?", "options": ["To reveal a secret", "To buy a pet", "To lose something", "To get angry"], "correctAnswer": "To reveal a secret"},
            {"text": "Change the voice: 'The mechanic is fixing the car.'", "options": ["The car is being fixed by the mechanic.", "The car was fixed by the mechanic.", "The car has been fixed by the mechanic.", "The car is fixed by the mechanic."], "correctAnswer": "The car is being fixed by the mechanic."},
            {"text": "Which of these is a complex sentence?", "options": ["Although I was tired, I finished the work.", "I was tired, but I finished the work.", "I was tired and I finished the work.", "I finished the work simply."], "correctAnswer": "Although I was tired, I finished the work."},
            {"text": "What does the suffix '-able' in 'Predictable' mean?", "options": ["Capable of being", "Full of", "Without", "Study of"], "correctAnswer": "Capable of being"},
            {"text": "Identify the tense: 'By next year, she will have graduated from college.'", "options": ["Future Perfect", "Future Continuous", "Simple Future", "Present Perfect"], "correctAnswer": "Future Perfect"},
            {"text": "Find the antonym for 'Optimistic'.", "options": ["Pessimistic", "Hopeful", "Positive", "Confident"], "correctAnswer": "Pessimistic"},
            {"text": "Choose the correct homophone: 'The knight rode his _____ horse into battle.'", "options": ["Mettlesome", "Meddlesome", "Metalsome", "Medalsome"], "correctAnswer": "Mettlesome"},
            {"text": "Complete the analogy: 'Odometer is to Mileage as Compass is to _____'", "options": ["Direction", "Speed", "Weight", "Time"], "correctAnswer": "Direction"}
        ],
        "hard": [
            {"text": "Which clause is italicized in: 'The book <i>that I borrowed from the library</i> is overdue.'?", "options": ["Adjective Clause", "Noun Clause", "Adverb Clause", "Independent Clause"], "correctAnswer": "Adjective Clause"},
            {"text": "Provide one word substitute for: 'A list of books, sources, and articles used in research.'", "options": ["Bibliography", "Biography", "Autobiography", "Calligraphy"], "correctAnswer": "Bibliography"},
            {"text": "Identify the grammatical error: 'Each of the students have submitted their assignments on time.'", "options": ["'have' should be 'has' and 'their' should be 'his/her'", "'submitted' should be 'submit'", "'assignments' should be 'assignment'", "No error"], "correctAnswer": "'have' should be 'has' and 'their' should be 'his/her'"},
            {"text": "What figure of speech uses exaggeration for emphasis, like 'I've told you a million times!'?", "options": ["Hyperbole", "Oxymoron", "Onomatopoeia", "Alliteration"], "correctAnswer": "Hyperbole"},
            {"text": "Change into indirect speech: The teacher said to the boy, 'Why are you late?'", "options": ["The teacher asked the boy why he was late.", "The teacher asked the boy why was he late.", "The teacher told the boy why he is late.", "The teacher asked the boy why are you late."], "correctAnswer": "The teacher asked the boy why he was late."},
            {"text": "What does the foreign phrase 'Ad hoc' mean?", "options": ["For this specific purpose", "From the beginning", "According to value", "In good faith"], "correctAnswer": "For this specific purpose"},
            {"text": "Choose the correct verb form: 'If I _____ a bird, I would fly across the ocean.'", "options": ["Were", "Was", "Am", "Will be"], "correctAnswer": "Were"},
            {"text": "Identify the dangling modifier in these options.", "options": ["Walking down the street, the trees looked beautiful.", "Walking down the street, I saw beautiful trees.", "I saw beautiful trees walking down the street.", "The trees looked beautiful to me."], "correctAnswer": "Walking down the street, the trees looked beautiful."},
            {"text": "Which rhetorical device involves placing two opposite or contrasting ideas together? (e.g., 'Bittersweet')", "options": ["Oxymoron", "Metaphor", "Pun", "Assonance"], "correctAnswer": "Oxymoron"},
            {"text": "Find the correct synthesis of these sentences: 'He is very poor. He cannot buy a car.'", "options": ["He is too poor to buy a car.", "He is so poor that he cannot buy a car.", "He is very poor so he cannot buy a car.", "All of the above"], "correctAnswer": "All of the above"}
        ]
    },
    "maths": {
        "easy": [
            {"text": "What is the place value of 5 in the decimal 12.356?", "options": ["Hundredths", "Tenths", "Thousandths", "Tens"], "correctAnswer": "Hundredths"},
            {"text": "Convert the fraction 3/4 to a percentage.", "options": ["75%", "25%", "50%", "34%"], "correctAnswer": "75%"},
            {"text": "What is the rule to determine if a number is divisible by 3?", "options": ["The sum of its digits must be divisible by 3", "It must end in an even number", "It must end in 0 or 5", "The last two digits must be divisible by 3"], "correctAnswer": "The sum of its digits must be divisible by 3"},
            {"text": "A right angle measures exactly ___ degrees.", "options": ["90", "180", "45", "360"], "correctAnswer": "90"},
            {"text": "Multiply 0.5 by 100.", "options": ["50", "5", "500", "0.05"], "correctAnswer": "50"},
            {"text": "Find the perimeter of a rectangle with length 12 cm and breadth 5 cm.", "options": ["34 cm", "60 cm", "17 cm", "24 cm"], "correctAnswer": "34 cm"},
            {"text": "What is the lowest common multiple (LCM) of 6 and 8?", "options": ["24", "48", "12", "2"], "correctAnswer": "24"},
            {"text": "Write 2,500,000 in words (Indian System).", "options": ["Twenty-five Lakhs", "Two Million Five Hundred Thousand", "Two Crore Fifty Lakhs", "Twenty-five Thousands"], "correctAnswer": "Twenty-five Lakhs"},
            {"text": "Calculate the area of a square with a side of 9 meters.", "options": ["81 sq m", "36 sq m", "18 sq m", "810 sq m"], "correctAnswer": "81 sq m"},
            {"text": "Reduce the fraction 16/24 to its lowest terms.", "options": ["2/3", "4/6", "8/12", "1/2"], "correctAnswer": "2/3"}
        ],
        "medium": [
            {"text": "Evaluate: 4 + 5 × 2 - 3", "options": ["11", "15", "5", "21"], "correctAnswer": "11"},
            {"text": "The HCF of two numbers is 4 and their LCM is 24. If one number is 8, what is the other?", "options": ["12", "6", "16", "20"], "correctAnswer": "12"},
            {"text": "Convert 125% to a fraction in simplest form.", "options": ["5/4", "1/4", "5/8", "4/5"], "correctAnswer": "5/4"},
            {"text": "An angle greater than 180 degrees but less than 360 degrees is called a/an ________.", "options": ["Reflex Angle", "Obtuse Angle", "Straight Angle", "Complete Angle"], "correctAnswer": "Reflex Angle"},
            {"text": "If the price of a shirt is Rs 500 and it has a 20% discount, what is the selling price?", "options": ["Rs 400", "Rs 100", "Rs 480", "Rs 450"], "correctAnswer": "Rs 400"},
            {"text": "A car travels 300 km on 15 liters of petrol. How much petrol is needed to travel 500 km?", "options": ["25 liters", "30 liters", "20 liters", "35 liters"], "correctAnswer": "25 liters"},
            {"text": "Find the volume of a cuboid with length 10 cm, width 5 cm, and height 2 cm.", "options": ["100 cubic cm", "50 cubic cm", "20 cubic cm", "1000 cubic cm"], "correctAnswer": "100 cubic cm"},
            {"text": "The sum of the angles in a triangle is always ___ degrees.", "options": ["180", "360", "90", "270"], "correctAnswer": "180"},
            {"text": "Solve: 3/5 + 1/4", "options": ["17/20", "4/9", "8/20", "4/20"], "correctAnswer": "17/20"},
            {"text": "If noon is 12:00 PM, what time is 18:45 in the 12-hour format?", "options": ["6:45 PM", "6:45 AM", "8:45 PM", "4:45 PM"], "correctAnswer": "6:45 PM"}
        ],
        "hard": [
            {"text": "If a rectangular tank is 2 m long, 1.5 m wide, and 1 m deep, what is its capacity in liters? (Hint: 1 cubic meter = 1000 liters)", "options": ["3000 liters", "300 liters", "1500 liters", "2000 liters"], "correctAnswer": "3000 liters"},
            {"text": "Rahul bought a bicycle for Rs 1200 and sold it for Rs 1500. Calculate his profit percentage.", "options": ["25%", "20%", "30%", "15%"], "correctAnswer": "25%"},
            {"text": "The average of 5 numbers is 20. If 4 of the numbers are 15, 25, 10, and 30, what is the 5th number?", "options": ["20", "25", "10", "15"], "correctAnswer": "20"},
            {"text": "Solve for x: (x / 4) + 5 = 12", "options": ["28", "24", "16", "32"], "correctAnswer": "28"},
            {"text": "What is the difference between the sum of the first 10 even numbers and the sum of the first 10 odd numbers?", "options": ["10", "20", "100", "50"], "correctAnswer": "10"},
            {"text": "A wire is bent into the shape of a square of area 121 sq cm. If the same wire is bent into a circle, what is its circumference? (Take π ≈ 22/7)", "options": ["44 cm", "22 cm", "88 cm", "66 cm"], "correctAnswer": "44 cm"},
            {"text": "Simplify: 2½ × 3¼", "options": ["8⅛", "6½", "5¾", "7⅛"], "correctAnswer": "8⅛"},
            {"text": "At what rate of simple interest will a sum of money double itself in 10 years?", "options": ["10%", "5%", "8%", "12%"], "correctAnswer": "10%"},
            {"text": "Three bells toll at intervals of 12, 15, and 20 minutes. If they toll together at 10:00 AM, when will they next toll together?", "options": ["11:00 AM", "11:30 AM", "12:00 PM", "10:45 AM"], "correctAnswer": "11:00 AM"},
            {"text": "Find the value of 0.008 ÷ 0.02", "options": ["0.4", "0.04", "4", "0.004"], "correctAnswer": "0.4"}
        ]
    },
    "hindi": {
        "easy": [
            {"text": "वर्णों के व्यवस्थित समूह को क्या कहते हैं?", "options": ["वर्णमाला", "शब्द", "वाक्य", "निबंध"], "correctAnswer": "वर्णमाला"},
            {"text": "भाषा के कितने मुख्य रूप होते हैं?", "options": ["दो (मौखिक और लिखित)", "तीन", "चार", "एक"], "correctAnswer": "दो (मौखिक और लिखित)"},
            {"text": "'कमल' शब्द के लिए सही पर्यायवाची चुनें।", "options": ["जलज", "अनल", "पवन", "अंबर"], "correctAnswer": "जलज"},
            {"text": "'उदय' शब्द का विलोम क्या होगा?", "options": ["अस्त", "शाम", "सवेरा", "अंत"], "correctAnswer": "अस्त"},
            {"text": "जो चित्र बनाता है उसे चित्रकार कहते हैं, तो जो कविता लिखता है उसे क्या कहते हैं?", "options": ["कवि", "लेखक", "नाट्यकार", "शिल्पकार"], "correctAnswer": "कवि"},
            {"text": "'ईदगाह' कहानी किसने लिखी है?", "options": ["मुंशी प्रेमचंद", "रवींद्रनाथ टैगोर", "महादेवी वर्मा", "जयशंकर प्रसाद"], "correctAnswer": "मुंशी प्रेमचंद"},
            {"text": "संज्ञा के कितने मुख्य भेद होते हैं?", "options": ["तीन (व्यक्तिवाचक, जातिवाचक, भाववाचक)", "चार", "पांच", "दो"], "correctAnswer": "तीन (व्यक्तिवाचक, जातिवाचक, भाववाचक)"},
            {"text": "भारत का राष्ट्रीय गान 'जन-गण-मन' गाने में लगभग कितना समय लगता है?", "options": ["52 सेकंड", "1 मिनट", "45 सेकंड", "60 सेकंड"], "correctAnswer": "52 सेकंड"},
            {"text": "'नदी' का बहुवचन क्या है?", "options": ["नदियाँ", "नदियें", "नदीयों", "नदिया"], "correctAnswer": "नदियाँ"},
            {"text": "हमारे शरीर में खून को शरीर भर में कौन पहुंचाता है?", "options": ["हृदय (Heart)", "फेफड़े", "दिमाग", "पेट"], "correctAnswer": "हृदय (Heart)"}
        ],
        "medium": [
            {"text": "'अकल का दुश्मन' मुहावरे का क्या अर्थ है?", "options": ["मूर्ख / बेवकूफ", "चतुर", "दुश्मन", "दोस्त"], "correctAnswer": "मूर्ख / बेवकूफ"},
            {"text": "सर्वनाम के कितने भेद होते हैं?", "options": ["छह", "पांच", "चार", "आठ"], "correctAnswer": "छह"},
            {"text": "कारक के चिह्न को क्या कहते हैं?", "options": ["विभक्ति / परसर्ग", "काल", "वचन", "लिंग"], "correctAnswer": "विभक्ति / परसर्ग"},
            {"text": "इनमें से कौन सा शब्द विशेषण है? 'वह बहुत मीठा आम खा रहा है।'", "options": ["मीठा", "आम", "खा", "वह"], "correctAnswer": "मीठा"},
            {"text": "संधि विच्छेद कीजिए: 'स्वागत'", "options": ["सु + आगत", "स्व + आगत", "स्वा + गत", "स + वागत"], "correctAnswer": "सु + आगत"},
            {"text": "'आविष्कार' का अर्थ क्या होता है?", "options": ["नई चीज़ की खोज / निर्माण", "परिवर्तन", "विनाश", "चोरी"], "correctAnswer": "नई चीज़ की खोज / निर्माण"},
            {"text": "इनमें से कौन सा वाक्य शुद्ध है?", "options": ["मैंने आज स्कूल नहीं जाना है।", "मुझे आज स्कूल नहीं जाना है।", "मेरे को स्कूल नहीं जाना है।", "मैं स्कूल नहीं जाना है आज।"], "correctAnswer": "मुझे आज स्कूल नहीं जाना है।"},
            {"text": "जिस अव्यय शब्द से काम करने के तरीके (manner) का पता चले उसे क्या कहते हैं?", "options": ["रीतिवाचक क्रियाविशेषण", "कालवाचक क्रियाविशेषण", "स्थानवाचक क्रियाविशेषण", "परिमाणवाचक क्रियाविशेषण"], "correctAnswer": "रीतिवाचक क्रियाविशेषण"},
            {"text": "'परोपकार' में कौन सा उपसर्ग लगा है?", "options": ["पर", "परो", "उप", "कार"], "correctAnswer": "पर"},
            {"text": "जिसका कोई शत्रु पैदा न हुआ हो, उसे क्या कहते हैं?", "options": ["अजातशत्रु", "मित्रता", "अडिग", "निडर"], "correctAnswer": "अजातशत्रु"}
        ],
        "hard": [
            {"text": "'पीतांबर' शब्द में कौन सा समास है? (पीला है अंबर जिसका - विष्णु)", "options": ["बहुव्रीहि", "अव्ययीभाव", "द्वंद्व", "तत्पुरुष"], "correctAnswer": "बहुव्रीहि"},
            {"text": "अलंकार पहचानें: 'तरनि तनूजा तट तमाल तरुवर बहु छाए।'", "options": ["अनुप्रास अलंकार", "यमक अलंकार", "श्लेष अलंकार", "उपमा अलंकार"], "correctAnswer": "अनुप्रास अलंकार"},
            {"text": "रामधारी सिंह 'दिनकर' द्वारा रचित प्रसिद्ध महाकाव्य कौन सा है?", "options": ["रश्मिरथी / कुरुक्षेत्र", "कामायनी", "रामचरितमानस", "साकेत"], "correctAnswer": "रश्मिरथी / कुरुक्षेत्र"},
            {"text": "वाक्यों के अंग कितने होते हैं?", "options": ["दो (उद्देश्य और विधेय)", "तीन", "चार", "पांच"], "correctAnswer": "दो (उद्देश्य और विधेय)"},
            {"text": "इनमें से कौन सा शब्द 'तत्सम' नहीं है?", "options": ["आग", "अग्नि", "सूर्य", "हस्त"], "correctAnswer": "आग"},
            {"text": "'कमल' का पर्यायवाची शब्द नहीं है:", "options": ["राजीव", "अंबुद", "जलज", "नीरज"], "correctAnswer": "अंबुद"},
            {"text": "छंद के मुख्य कितने प्रकार होते हैं?", "options": ["दो (मात्रिक और वर्णिक)", "तीन", "चार", "छह"], "correctAnswer": "दो (मात्रिक और वर्णिक)"},
            {"text": "'उल्टे उस्तरे से मूंडना' मुहावरे का क्या अर्थ है?", "options": ["बुरी तरह ठगना", "सिर के बाल काटना", "खतरे में डालना", "उल्टा काम करना"], "correctAnswer": "बुरी तरह ठगना"},
            {"text": "इनमें से किस रस का स्थायी भाव 'शोक' है?", "options": ["करुण रस", "रौद्र रस", "वीर रस", "भयानक रस"], "correctAnswer": "करुण रस"},
            {"text": "अव्ययीभाव समास का उदाहरण चुनें।", "options": ["प्रतिदिन", "राजकुमार", "चराचर", "दशानन"], "correctAnswer": "प्रतिदिन"}
        ]
    },
    "evs": {
        "easy": [
            {"text": "Which gas do plants release during photosynthesis?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Methane"], "correctAnswer": "Oxygen"},
            {"text": "Which state of matter has a definite shape and a definite volume?", "options": ["Solid", "Liquid", "Gas", "Plasma"], "correctAnswer": "Solid"},
            {"text": "The Sun is a/an ________.", "options": ["Star", "Planet", "Satellite", "Comet"], "correctAnswer": "Star"},
            {"text": "Which instrument is used to measure the temperature of the human body?", "options": ["Clinical Thermometer", "Barometer", "Stethoscope", "Microscope"], "correctAnswer": "Clinical Thermometer"},
            {"text": "Tigers are primarily found in which type of habitat in India?", "options": ["Forests", "Deserts", "Oceans", "Polar ice caps"], "correctAnswer": "Forests"},
            {"text": "Which internal organ is responsible for pumping blood throughout the body?", "options": ["Heart", "Brain", "Lungs", "Kidneys"], "correctAnswer": "Heart"},
            {"text": "What is the process of changing solid ice into liquid water called?", "options": ["Melting", "Freezing", "Evaporation", "Condensation"], "correctAnswer": "Melting"},
            {"text": "Which of these is considered a 'cash crop' in India?", "options": ["Cotton", "Wheat", "Rice", "Maize"], "correctAnswer": "Cotton"},
            {"text": "What do we call the fast-moving air?", "options": ["Wind", "Cloud", "Storm", "Vapor"], "correctAnswer": "Wind"},
            {"text": "The Earth takes approximately how many days to complete one revolution around the Sun?", "options": ["365.25 days", "364 days", "366 days", "360 days"], "correctAnswer": "365.25 days"}
        ],
        "medium": [
            {"text": "What causes the change of seasons on Earth?", "options": ["The tilt of the Earth's axis and its revolution", "The Earth's rotation on its axis", "The varying distance of the Earth from the Sun", "Changes in the Sun's temperature"], "correctAnswer": "The tilt of the Earth's axis and its revolution"},
            {"text": "Which component of food helps in building and repairing body tissues?", "options": ["Proteins", "Carbohydrates", "Fats", "Vitamins"], "correctAnswer": "Proteins"},
            {"text": "What is the process called when seeds begin to grow into young plants?", "options": ["Germination", "Pollination", "Dispersal", "Fertilization"], "correctAnswer": "Germination"},
            {"text": "Goiter is a disease caused by the deficiency of which mineral?", "options": ["Iodine", "Iron", "Calcium", "Phosphorus"], "correctAnswer": "Iodine"},
            {"text": "Which type of simple machine consists of a grooved wheel with a rope or cable running along the groove?", "options": ["Pulley", "Lever", "Inclined Plane", "Wedge"], "correctAnswer": "Pulley"},
            {"text": "In a food chain, what role do green plants play?", "options": ["Producers", "Primary Consumers", "Secondary Consumers", "Decomposers"], "correctAnswer": "Producers"},
            {"text": "What is the main function of the white blood cells (WBCs) in our body?", "options": ["To fight infection and disease", "To carry oxygen", "To help blood clot", "To transport nutrients"], "correctAnswer": "To fight infection and disease"},
            {"text": "Which layer of the atmosphere contains the ozone layer that protects us from UV rays?", "options": ["Stratosphere", "Troposphere", "Mesosphere", "Thermosphere"], "correctAnswer": "Stratosphere"},
            {"text": "Which state in India is famous for the Kaziranga National Park and its one-horned rhinoceros?", "options": ["Assam", "Madhya Pradesh", "Rajasthan", "Kerala"], "correctAnswer": "Assam"},
            {"text": "The force that resists the motion of one object moving over another is called ________.", "options": ["Friction", "Gravity", "Magnetism", "Inertia"], "correctAnswer": "Friction"}
        ],
        "hard": [
            {"text": "Which joint in the human body allows movement in all directions (like a joystick)?", "options": ["Ball and Socket Joint", "Hinge Joint", "Pivot Joint", "Gliding Joint"], "correctAnswer": "Ball and Socket Joint"},
            {"text": "During an earthquake, the point on the Earth's surface directly above the focus is called the ________.", "options": ["Epicenter", "Fault line", "Magnitude", "Core"], "correctAnswer": "Epicenter"},
            {"text": "Which vitamin is synthesized in our body when our skin is exposed to early morning sunlight?", "options": ["Vitamin D", "Vitamin A", "Vitamin C", "Vitamin B12"], "correctAnswer": "Vitamin D"},
            {"text": "What is the phenomenon called when the Moon comes completely between the Sun and the Earth, casting a shadow on the Earth?", "options": ["Solar Eclipse", "Lunar Eclipse", "Tides", "Phases of the Moon"], "correctAnswer": "Solar Eclipse"},
            {"text": "What is the process of extracting metals from their ores called?", "options": ["Metallurgy", "Refining", "Distillation", "Mining"], "correctAnswer": "Metallurgy"},
            {"text": "Which blood group is known as the 'Universal Donor'?", "options": ["O Negative", "AB Positive", "A Positive", "B Negative"], "correctAnswer": "O Negative"},
            {"text": "Name the tiny pores present on the surface of leaves that help in the exchange of gases.", "options": ["Stomata", "Chloroplasts", "Xylem", "Phloem"], "correctAnswer": "Stomata"},
            {"text": "What is the term for animals that are active primarily during the night?", "options": ["Nocturnal", "Diurnal", "Crepuscular", "Arboreal"], "correctAnswer": "Nocturnal"},
            {"text": "If a substance turns blue litmus paper red, it indicates that the substance is ________.", "options": ["Acidic", "Basic / Alkaline", "Neutral", "Salty"], "correctAnswer": "Acidic"},
            {"text": "Which renewable source of energy is generated by utilizing the kinetic energy of flowing water?", "options": ["Hydroelectric Energy", "Geothermal Energy", "Biomass Energy", "Tidal Energy"], "correctAnswer": "Hydroelectric Energy"}
        ]
    }
}

def main():
    bank_path = '/Users/arpan1.mukherjee/code/GhostMaze/public/AhirsAcademy/data/question_bank.json'
    
    with open(bank_path, 'r', encoding='utf-8') as f:
        question_bank = json.load(f)
        
    question_bank['class_5'] = class_5_data
    
    with open(bank_path, 'w', encoding='utf-8') as f:
        json.dump(question_bank, f, indent=4, ensure_ascii=False)
        
    print("Successfully injected sophisticated and thought-provoking questions for Class 5!")

if __name__ == '__main__':
    main()
