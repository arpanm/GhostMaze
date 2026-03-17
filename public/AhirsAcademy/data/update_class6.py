import json
import os

class_6_data = {
    "english": {
        "easy": [
            {"text": "Which word is an abstract noun?", "options": ["Bravery", "Table", "London", "River"], "correctAnswer": "Bravery"},
            {"text": "What is the comparative form of 'Good'?", "options": ["Better", "Best", "Gooder", "More good"], "correctAnswer": "Better"},
            {"text": "Choose the correct article: 'She is _____ honorable person.'", "options": ["An", "A", "The", "No article needed"], "correctAnswer": "An"},
            {"text": "Which word is a synonym for 'Abundant'?", "options": ["Plentiful", "Scarce", "Rare", "Few"], "correctAnswer": "Plentiful"},
            {"text": "Select the correct plural form of 'Cactus'.", "options": ["Cacti", "Cactuses", "Cactus", "Cactiies"], "correctAnswer": "Cacti"},
            {"text": "Identify the tense: 'They play tennis every Sunday.'", "options": ["Simple Present", "Present Continuous", "Simple Past", "Future Tense"], "correctAnswer": "Simple Present"},
            {"text": "Find the odd one out.", "options": ["Quickly", "Slowly", "Happy", "Carefully"], "correctAnswer": "Happy"},
            {"text": "Which punctuation mark is used to separate items in a list?", "options": ["Comma (,)", "Exclamation Mark (!)", "Question Mark (?)", "Hyphen (-)"], "correctAnswer": "Comma (,)"},
            {"text": "Complete the idiom: 'A blessing in _____'", "options": ["Disguise", "Sky", "Clouds", "Rain"], "correctAnswer": "Disguise"},
            {"text": "What is the antonym of 'Arrogant'?", "options": ["Humble", "Proud", "Selfish", "Clever"], "correctAnswer": "Humble"}
        ],
        "medium": [
            {"text": "Identify the gerund in the sentence: 'Swimming is an excellent exercise.'", "options": ["Swimming", "Is", "Excellent", "Exercise"], "correctAnswer": "Swimming"},
            {"text": "Change into passive voice: 'The chef cooked a delicious meal.'", "options": ["A delicious meal was cooked by the chef.", "A delicious meal is cooked by the chef.", "The chef cooks a delicious meal.", "A delicious meal has been cooked by the chef."], "correctAnswer": "A delicious meal was cooked by the chef."},
            {"text": "Choose the correct relative pronoun: 'The man _____ car was stolen went to the police.'", "options": ["Whose", "Who", "Whom", "Which"], "correctAnswer": "Whose"},
            {"text": "What figure of speech is used in: 'The stars danced playfully in the moonlit sky.'?", "options": ["Personification", "Simile", "Metaphor", "Onomatopoeia"], "correctAnswer": "Personification"},
            {"text": "Identify the type of sentence: 'Although it was raining, we went for a walk.'", "options": ["Complex sentence", "Compound sentence", "Simple sentence", "Compound-complex sentence"], "correctAnswer": "Complex sentence"},
            {"text": "Fill in the correct preposition: 'He was acquitted _____ all charges.'", "options": ["Of", "From", "For", "With"], "correctAnswer": "Of"},
            {"text": "What does the root word 'Chron' mean?", "options": ["Time", "Color", "Measure", "Light"], "correctAnswer": "Time"},
            {"text": "Which of these words is spelled incorrectly?", "options": ["Accommodate", "Embarrass", "Occassion", "Recommend"], "correctAnswer": "Occassion"},
            {"text": "Find the meaning of the idiom 'To beat around the bush'.", "options": ["To avoid getting to the point", "To search thoroughly", "To garden", "To hit someone"], "correctAnswer": "To avoid getting to the point"},
            {"text": "Which conjunction is used to express a condition?", "options": ["If", "And", "Or", "Because"], "correctAnswer": "If"}
        ],
        "hard": [
            {"text": "Identify the dangling modifier in the following sentence.", "options": ["Hoping to excuse the absence, the note was written and signed by his mother.", "Hoping to excuse the absence, his mother wrote and signed the note.", "His mother, hoping to excuse the absence, wrote and signed the note.", "The note was written by his mother, hoping to excuse the absence."], "correctAnswer": "Hoping to excuse the absence, the note was written and signed by his mother."},
            {"text": "What is an 'Oxymoron'?", "options": ["A figure of speech combining contradictory terms", "A word that imitates the sound it represents", "An exaggeration used for emphasis", "A comparison without using 'like' or 'as'"], "correctAnswer": "A figure of speech combining contradictory terms"},
            {"text": "Identify the mood of the verb in: 'I suggest that he study for the exam.'", "options": ["Subjunctive", "Indicative", "Imperative", "Interrogative"], "correctAnswer": "Subjunctive"},
            {"text": "Which of these is a portmanteau word (a blend of two words)?", "options": ["Motel", "Television", "Internet", "Smartphone"], "correctAnswer": "Motel"},
            {"text": "Change into indirect speech: The captain said to his soldiers, 'Stand at ease.'", "options": ["The captain commanded his soldiers to stand at ease.", "The captain requested his soldiers to stand at ease.", "The captain said to his soldiers that they should stand at ease.", "The captain commanded his soldiers that stand at ease."], "correctAnswer": "The captain commanded his soldiers to stand at ease."},
            {"text": "Provide one word substitute for: 'A person who hates mankind.'", "options": ["Misanthrope", "Philanthropist", "Optimist", "Pessimist"], "correctAnswer": "Misanthrope"},
            {"text": "Identify the error: 'None of the two brothers are coming to the party.'", "options": ["Use 'Neither' instead of 'None' and 'is' instead of 'are'", "Use 'is' instead of 'are'", "Use 'brother' instead of 'brothers'", "The sentence is correct"], "correctAnswer": "Use 'Neither' instead of 'None' and 'is' instead of 'are'"},
            {"text": "Which rhetorical device is used here: 'Ask not what your country can do for you; ask what you can do for your country.'?", "options": ["Chiasmus", "Hyperbole", "Alliteration", "Simile"], "correctAnswer": "Chiasmus"},
            {"text": "Find the correct active voice sequence for: 'The bridge has been crossed by the marching army.'", "options": ["The marching army has crossed the bridge.", "The marching army crossed the bridge.", "The marching army is crossing the bridge.", "The marching army was crossing the bridge."], "correctAnswer": "The marching army has crossed the bridge."},
            {"text": "What is the meaning of the Latin phrase 'Bona fide'?", "options": ["In good faith / Genuine", "From the beginning", "For this purpose", "Before noon"], "correctAnswer": "In good faith / Genuine"}
        ]
    },
    "maths": {
        "easy": [
            {"text": "Write the numeral for: Three million, four hundred fifty thousand, two hundred ten.", "options": ["3,450,210", "3,045,210", "30,450,210", "3,450,010"], "correctAnswer": "3,450,210"},
            {"text": "What is the Roman numeral for 55?", "options": ["LV", "VL", "XXXXXV", "LIV"], "correctAnswer": "LV"},
            {"text": "Evaluate: 15 + (−8)", "options": ["7", "23", "-7", "-23"], "correctAnswer": "7"},
            {"text": "Which of the following is an improper fraction?", "options": ["7/4", "3/8", "1/2", "5/9"], "correctAnswer": "7/4"},
            {"text": "What is 20% of 150?", "options": ["30", "15", "20", "45"], "correctAnswer": "30"},
            {"text": "A line segment has how many endpoints?", "options": ["Two", "One", "None", "Three"], "correctAnswer": "Two"},
            {"text": "Solve: 5x = 35. What is the value of x?", "options": ["7", "6", "8", "5"], "correctAnswer": "7"},
            {"text": "Find the LCM of 12 and 15.", "options": ["60", "30", "120", "45"], "correctAnswer": "60"},
            {"text": "Which quadrilateral has all sides equal and all angles equal to 90 degrees?", "options": ["Square", "Rhombus", "Rectangle", "Trapezium"], "correctAnswer": "Square"},
            {"text": "What is the absolute value of -42?", "options": ["42", "-42", "0", "1"], "correctAnswer": "42"}
        ],
        "medium": [
            {"text": "If x - 3 = 12, what is the value of x + 5?", "options": ["20", "15", "17", "10"], "correctAnswer": "20"},
            {"text": "Convert 3/8 into a decimal.", "options": ["0.375", "0.333", "0.83", "0.25"], "correctAnswer": "0.375"},
            {"text": "The ratio of boys to girls in a class is 3:2. If there are 30 students in total, how many girls are there?", "options": ["12", "18", "15", "10"], "correctAnswer": "12"},
            {"text": "A supplementary angle of 75 degrees is:", "options": ["105 degrees", "15 degrees", "90 degrees", "25 degrees"], "correctAnswer": "105 degrees"},
            {"text": "Simplify: 18 - [ 4 + 2 × ( 5 - 3 ) ]", "options": ["10", "14", "8", "6"], "correctAnswer": "10"},
            {"text": "What is the HCF of 28, 42, and 56?", "options": ["14", "7", "2", "28"], "correctAnswer": "14"},
            {"text": "Express 750 ml as a fraction of 2 liters.", "options": ["3/8", "3/4", "1/4", "5/8"], "correctAnswer": "3/8"},
            {"text": "Find the area of a right-angled triangle with base 8 cm and height 6 cm.", "options": ["24 sq cm", "48 sq cm", "14 sq cm", "30 sq cm"], "correctAnswer": "24 sq cm"},
            {"text": "Simplify the expression: 3x + 4y - 2x + 5y", "options": ["x + 9y", "5x + 9y", "x - y", "3x + y"], "correctAnswer": "x + 9y"},
            {"text": "A machine produces 1200 items in 8 hours. How many items will it produce in 5 hours?", "options": ["750", "800", "600", "500"], "correctAnswer": "750"}
        ],
        "hard": [
            {"text": "Two numbers are in the ratio 3:5. If their sum is 96, what is the larger number?", "options": ["60", "36", "48", "72"], "correctAnswer": "60"},
            {"text": "Calculate the perimeter of a regular hexagon, if its area consists of 6 equilateral triangles of side 4 cm each.", "options": ["24 cm", "12 cm", "36 cm", "16 cm"], "correctAnswer": "24 cm"},
            {"text": "If 15 men can complete a job in 20 days, how many men would be required to complete the same job in 12 days?", "options": ["25 men", "30 men", "18 men", "20 men"], "correctAnswer": "25 men"},
            {"text": "Solve for x: (2x - 3) / 4 = x / 3", "options": ["4.5", "9", "6", "3"], "correctAnswer": "4.5"},
            {"text": "A shopkeeper marks an article 40% above its cost price and then allows a discount of 20%. Find his profit percentage.", "options": ["12%", "20%", "15%", "8%"], "correctAnswer": "12%"},
            {"text": "Find the value of 'y' if the numbers 12, 16, y, and 24 are in proportion.", "options": ["18", "20", "15", "14"], "correctAnswer": "18"},
            {"text": "The inner dimensions of a closed wooden box are 10cm x 8cm x 6cm. The wood is 1cm thick all around. Find the outer volume of the box.", "options": ["960 cubic cm", "480 cubic cm", "1200 cubic cm", "800 cubic cm"], "correctAnswer": "960 cubic cm"},
            {"text": "Simplify: [(1/2) ÷ (1/4)] × [(2/3) + (1/6)]", "options": ["5/3", "4/3", "2/3", "1"], "correctAnswer": "5/3"},
            {"text": "What is the sum of the interior angles of a regular octagon?", "options": ["1080 degrees", "720 degrees", "900 degrees", "1440 degrees"], "correctAnswer": "1080 degrees"},
            {"text": "If a : b = 2 : 3 and b : c = 4 : 5, find the ratio a : c.", "options": ["8 : 15", "6 : 15", "2 : 5", "8 : 12"], "correctAnswer": "8 : 15"}
        ]
    },
    "hindi": {
        "easy": [
            {"text": "हिंदी वर्णमाला में संयुक्त व्यंजन कितने हैं?", "options": ["4 (क्ष, त्र, ज्ञ, श्र)", "3", "5", "2"], "correctAnswer": "4 (क्ष, त्र, ज्ञ, श्र)"},
            {"text": "'सत्य' का विलोम शब्द क्या है?", "options": ["असत्य", "झूठ", "पाप", "क्रोध"], "correctAnswer": "असत्य"},
            {"text": "जिस शब्द के कई अर्थ निकलते हों, उसे क्या कहते हैं?", "options": ["अनेकार्थी शब्द", "पर्यायवाची शब्द", "विलोम शब्द", "एकार्थी शब्द"], "correctAnswer": "अनेकार्थी शब्द"},
            {"text": "'आकाश' का पर्यायवाची शब्द नहीं है:", "options": ["पाताल", "नभ", "गगन", "व्योम"], "correctAnswer": "पाताल"},
            {"text": "इनमें से कौन सा शब्द शुद्ध है?", "options": ["आशीर्वाद", "आशिर्वाद", "आशीर्बाद", "अशीर्वाद"], "correctAnswer": "आशीर्वाद"},
            {"text": "क्रिया के मूल रूप को क्या कहते हैं?", "options": ["धातु", "मूल", "संज्ञा", "विभक्ति"], "correctAnswer": "धातु"},
            {"text": "कारक के कितने भेद होते हैं?", "options": ["आठ", "छह", "सात", "पांच"], "correctAnswer": "आठ"},
            {"text": "'पुस्तकालय' शब्द में कौन सी संधि है?", "options": ["दीर्घ संधि", "गुण संधि", "वृद्धि संधि", "यण संधि"], "correctAnswer": "दीर्घ संधि"},
            {"text": "'कमल' का पर्यायवाची शब्द है:", "options": ["जलज", "अनल", "पवन", "अंबर"], "correctAnswer": "जलज"},
            {"text": "संज्ञा के स्थान पर प्रयोग होने वाले शब्दों को क्या कहते हैं?", "options": ["सर्वनाम", "विशेषण", "क्रिया", "अव्यय"], "correctAnswer": "सर्वनाम"}
        ],
        "medium": [
            {"text": "रचना के आधार पर वाक्य के कितने भेद होते हैं?", "options": ["तीन (सरल, संयुक्त, मिश्र)", "चार", "दो", "पांच"], "correctAnswer": "तीन (सरल, संयुक्त, मिश्र)"},
            {"text": "'हाथ मलना' मुहावरे का सही अर्थ क्या है?", "options": ["पछताना", "सर्दी लगना", "क्रोधित होना", "तैयारी करना"], "correctAnswer": "पछताना"},
            {"text": "इनमें से कौन सा शब्द बहुव्रीहि समास का उदाहरण है?", "options": ["दशानन (दस हैं मुख जिसके - रावण)", "राजपुत्र", "प्रतिदिन", "चौराहा"], "correctAnswer": "दशानन (दस हैं मुख जिसके - रावण)"},
            {"text": "'अतिथि' शब्द का विलोम क्या होगा?", "options": ["आतिथेय", "मेहमान", "सज्जन", "शत्रु"], "correctAnswer": "आतिथेय"},
            {"text": "इनमें से कौन सा वाक्य अशुद्ध है?", "options": ["मेरे को बाज़ार जाना है।", "मुझे बाज़ार जाना है।", "राम ने खाना खाया।", "सीता गीत गाती है।"], "correctAnswer": "मेरे को बाज़ार जाना है।"},
            {"text": "जिस छंद के प्रत्येक चरण में समान मात्राएं होती हैं, उसे क्या कहते हैं?", "options": ["सम मात्रिक छंद", "विषम मात्रिक छंद", "वर्णिक छंद", "मुक्तक छंद"], "correctAnswer": "सम मात्रिक छंद"},
            {"text": "'यथाशक्ति' में कौन सा समास है?", "options": ["अव्ययीभाव", "तत्पुरुष", "कर्मधारय", "द्वंद्व"], "correctAnswer": "अव्ययीभाव"},
            {"text": "वीर रस का स्थायी भाव क्या है?", "options": ["उत्साह", "शोक", "रति", "भय"], "correctAnswer": "उत्साह"},
            {"text": "संधि विच्छेद कीजिए: 'महर्षि'", "options": ["महा + ऋषि", "मह + ऋषि", "महि + ऋषि", "महो + ऋषि"], "correctAnswer": "महा + ऋषि"},
            {"text": "जो ईश्वर में विश्वास नहीं रखता, उसे क्या कहते हैं?", "options": ["नास्तिक", "आस्तिक", "पाखंडी", "संत"], "correctAnswer": "नास्तिक"}
        ],
        "hard": [
            {"text": "अलंकार पहचानें: 'कनक कनक ते सौ गुनी मादकता अधिकाय।'", "options": ["यमक अलंकार", "अनुप्रास अलंकार", "श्लेष अलंकार", "रूपक अलंकार"], "correctAnswer": "यमक अलंकार"},
            {"text": "'गोदान' नामक प्रसिद्ध उपन्यास की रचना किसने की है?", "options": ["मुंशी प्रेमचंद", "जयशंकर प्रसाद", "सूर्यकांत त्रिपाठी निराला", "महादेवी वर्मा"], "correctAnswer": "मुंशी प्रेमचंद"},
            {"text": "'निर्वाचित' शब्द में कौन सा प्रत्यय लगा है?", "options": ["इत", "त", "चित", "वाचित"], "correctAnswer": "इत"},
            {"text": "इनमें से कौन सा शब्द तत्सम नहीं है?", "options": ["रात", "रात्रि", "सूर्य", "अग्नि"], "correctAnswer": "रात"},
            {"text": "'अंधे के हाथ बटेर लगना' लोकोक्ति का अर्थ है:", "options": ["अयोग्य व्यक्ति को कोई मूल्यवान वस्तु मिल जाना", "अंधे व्यक्ति का शिकार करना", "अचानक अमीर हो जाना", "बिना मेहनत के फल मिलना"], "correctAnswer": "अयोग्य व्यक्ति को कोई मूल्यवान वस्तु मिल जाना"},
            {"text": "वाच्य के भेद पहचानें: 'राम द्वारा पुस्तक पढ़ी जाती है।'", "options": ["कर्मवाच्य", "कर्तृवाच्य", "भाववाच्य", "इनमें से कोई नहीं"], "correctAnswer": "कर्मवाच्य"},
            {"text": "'नदी' का पर्यायवाची नहीं है:", "options": ["सरोवर", "सरिता", "तरंगिणी", "तटिनी"], "correctAnswer": "सरोवर"},
            {"text": "उपसर्ग पहचानें: 'अत्यधिक'", "options": ["अति", "अ", "अत्य", "अत्यध्"], "correctAnswer": "अति"},
            {"text": "'अज' शब्द के अनेकार्थी शब्द क्या हैं?", "options": ["ब्रह्मा, बकरा, दशरथ के पिता", "आसमान, हवा, पानी", "कमल, मोती, मछली", "सोना, धतूरा, गेहूं"], "correctAnswer": "ब्रह्मा, बकरा, दशरथ के पिता"},
            {"text": "इनमें से कौन सा वाक्य मिश्र वाक्य है?", "options": ["जो लड़का वहां खड़ा है, वह मेरा भाई है।", "राम खेलता है और श्याम पढ़ता है।", "मोहन बाज़ार गया।", "सूर्य उदय होने पर कुहासा जाता रहा।"], "correctAnswer": "जो लड़का वहां खड़ा है, वह मेरा भाई है।"}
        ]
    },
    "science": {
        "easy": [
            {"text": "What is the SI unit of distance?", "options": ["Meter", "Kilometer", "Centimeter", "Millimeter"], "correctAnswer": "Meter"},
            {"text": "Which part of a plant conducts water from the roots to the leaves?", "options": ["Stem (Xylem)", "Leaves", "Flowers", "Phloem"], "correctAnswer": "Stem (Xylem)"},
            {"text": "What is the process of making yarn from fibers called?", "options": ["Spinning", "Weaving", "Knitting", "Ginning"], "correctAnswer": "Spinning"},
            {"text": "Which vitamin deficiency causes night blindness?", "options": ["Vitamin A", "Vitamin B", "Vitamin C", "Vitamin D"], "correctAnswer": "Vitamin A"},
            {"text": "A magnet has how many poles?", "options": ["Two (North and South)", "One", "Three", "Four"], "correctAnswer": "Two (North and South)"},
            {"text": "What type of change is the melting of ice?", "options": ["Physical Change", "Chemical Change", "Irreversible Change", "Biological Change"], "correctAnswer": "Physical Change"},
            {"text": "Which animal is known as the 'Ship of the Desert'?", "options": ["Camel", "Horse", "Elephant", "Donkey"], "correctAnswer": "Camel"},
            {"text": "Materials through which light can pass completely are called:", "options": ["Transparent", "Translucent", "Opaque", "Reflective"], "correctAnswer": "Transparent"},
            {"text": "The bony framework inside our body is called the:", "options": ["Skeleton", "Muscular System", "Nervous System", "Digestive System"], "correctAnswer": "Skeleton"},
            {"text": "What does a habitat provide for an animal?", "options": ["Food, water, and shelter", "Only food", "Only water", "Entertainment"], "correctAnswer": "Food, water, and shelter"}
        ],
        "medium": [
            {"text": "Which of the following is an example of a reversible change?", "options": ["Folding a piece of paper", "Baking a cake", "Burning wood", "Rusting of iron"], "correctAnswer": "Folding a piece of paper"},
            {"text": "What is the process of separating a heavier component from a lighter component in a mixture using wind called?", "options": ["Winnowing", "Threshing", "Sieving", "Handpicking"], "correctAnswer": "Winnowing"},
            {"text": "Name the type of joint present in our knee.", "options": ["Hinge Joint", "Ball and Socket Joint", "Pivot Joint", "Gliding Joint"], "correctAnswer": "Hinge Joint"},
            {"text": "Which part of the flower develops into a fruit?", "options": ["Ovary", "Petal", "Sepal", "Stamen"], "correctAnswer": "Ovary"},
            {"text": "Why do electric wires have a plastic coating?", "options": ["Plastic is an insulator", "To make them look colorful", "To make them heavier", "Plastic is a conductor"], "correctAnswer": "Plastic is an insulator"},
            {"text": "The deficiency of Iron in our diet leads to which disease?", "options": ["Anemia", "Scurvy", "Rickets", "Goiter"], "correctAnswer": "Anemia"},
            {"text": "What happens when the North pole of a magnet is brought near the North pole of another magnet?", "options": ["They repel each other", "They attract each other", "Nothing happens", "They stick together permanently"], "correctAnswer": "They repel each other"},
            {"text": "Which of these is a carnivorous plant?", "options": ["Pitcher Plant", "Rose", "Sunflower", "Cactus"], "correctAnswer": "Pitcher Plant"},
            {"text": "What type of motion is exhibited by a pendulum clock?", "options": ["Periodic Motion", "Rectilinear Motion", "Circular Motion", "Random Motion"], "correctAnswer": "Periodic Motion"},
            {"text": "What is the composition of Nitrogen gas in the Earth's atmosphere?", "options": ["About 78%", "About 21%", "About 1%", "About 50%"], "correctAnswer": "About 78%"}
        ],
        "hard": [
            {"text": "The process of settling down of heavier insoluble particles at the bottom of a liquid is called:", "options": ["Sedimentation", "Decantation", "Filtration", "Evaporation"], "correctAnswer": "Sedimentation"},
            {"text": "Which test is used to confirm the presence of starch in a food item?", "options": ["Iodine Test", "Benedict's Test", "Biuret Test", "Litmus Test"], "correctAnswer": "Iodine Test"},
            {"text": "What prevents food from entering the windpipe?", "options": ["Epiglottis", "Larynx", "Pharynx", "Trachea"], "correctAnswer": "Epiglottis"},
            {"text": "A pinhole camera forms an image based on which principle of light?", "options": ["Rectilinear propagation of light", "Reflection of light", "Refraction of light", "Dispersion of light"], "correctAnswer": "Rectilinear propagation of light"},
            {"text": "Identify the incorrect statement about magnets.", "options": ["Monopole magnets exist naturally.", "Magnetic force is strongest at the poles.", "Like poles repel, unlike poles attract.", "A freely suspended magnet rests in the North-South direction."], "correctAnswer": "Monopole magnets exist naturally."},
            {"text": "Which component of soil helps in improving its water holding capacity and fertility?", "options": ["Humus", "Sand", "Clay", "Gravel"], "correctAnswer": "Humus"},
            {"text": "What causes land breeze and sea breeze near coastal areas?", "options": ["Convection currents in the air", "Conduction of heat in water", "Radiation of heat from the sun", "Rotation of the Earth"], "correctAnswer": "Convection currents in the air"},
            {"text": "In the human body, the rib cage protects the:", "options": ["Heart and Lungs", "Brain", "Kidneys", "Stomach"], "correctAnswer": "Heart and Lungs"},
            {"text": "Which fibre is known as the 'Golden Fibre'?", "options": ["Jute", "Cotton", "Silk", "Nylon"], "correctAnswer": "Jute"},
            {"text": "The shadow of an object is entirely dark because:", "options": ["Light cannot pass through an opaque object.", "Light bends around an opaque object.", "The object absorbs all light.", "The object reflects light perfectly."], "correctAnswer": "Light cannot pass through an opaque object."}
        ]
    },
    "social-science": {
        "easy": [
            {"text": "Which planet is known as the 'Blue Planet'?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "correctAnswer": "Earth"},
            {"text": "Who is the head of the Gram Panchayat in a village?", "options": ["Sarpanch", "Mayor", "Chief Minister", "District Collector"], "correctAnswer": "Sarpanch"},
            {"text": "What is the shape of the Earth?", "options": ["Geoid (Spherical, slightly flattened at poles)", "Perfect Sphere", "Flat", "Oval"], "correctAnswer": "Geoid (Spherical, slightly flattened at poles)"},
            {"text": "Which imaginary line divides the Earth into the Northern and Southern Hemispheres?", "options": ["Equator", "Tropic of Cancer", "Prime Meridian", "Arctic Circle"], "correctAnswer": "Equator"},
            {"text": "Who wrote the Indian epic, the Ramayana?", "options": ["Valmiki", "Ved Vyas", "Tulsidas", "Kalidasa"], "correctAnswer": "Valmiki"},
            {"text": "What are the four cardinal directions?", "options": ["North, South, East, West", "Up, Down, Left, Right", "Northeast, Northwest, Southeast, Southwest", "Forward, Backward, Left, Right"], "correctAnswer": "North, South, East, West"},
            {"text": "Which is the largest continent in the world?", "options": ["Asia", "Africa", "North America", "Europe"], "correctAnswer": "Asia"},
            {"text": "In the Paleolithic Age, early humans were primarily:", "options": ["Hunter-gatherers", "Farmers", "Traders", "Kings"], "correctAnswer": "Hunter-gatherers"},
            {"text": "What is the capital of India?", "options": ["New Delhi", "Mumbai", "Kolkata", "Chennai"], "correctAnswer": "New Delhi"},
            {"text": "A book containing maps is called an:", "options": ["Atlas", "Encyclopedia", "Dictionary", "Almanac"], "correctAnswer": "Atlas"}
        ],
        "medium": [
            {"text": "The Harappan Civilization belonged to which age?", "options": ["Bronze Age", "Iron Age", "Stone Age", "Golden Age"], "correctAnswer": "Bronze Age"},
            {"text": "What does 'Democracy' mean?", "options": ["Rule by the people", "Rule by a king", "Rule by the military", "Rule by a few rich people"], "correctAnswer": "Rule by the people"},
            {"text": "Which longitude determines the Indian Standard Time (IST)?", "options": ["82°30' E", "80° E", "0°", "180°"], "correctAnswer": "82°30' E"},
            {"text": "Which Maurya ruler gave up war after winning the Kalinga war?", "options": ["Ashoka", "Chandragupta Maurya", "Bindusara", "Bimbisara"], "correctAnswer": "Ashoka"},
            {"text": "Local self-government in urban areas (cities) is called:", "options": ["Municipal Corporation", "Gram Panchayat", "Zila Parishad", "State Government"], "correctAnswer": "Municipal Corporation"},
            {"text": "The movement of the Earth around the Sun is known as:", "options": ["Revolution", "Rotation", "Precession", "Spinning"], "correctAnswer": "Revolution"},
            {"text": "What is the main occupation of people living in rural India?", "options": ["Agriculture", "IT Services", "Manufacturing", "Banking"], "correctAnswer": "Agriculture"},
            {"text": "Which of the Vedas is the oldest?", "options": ["Rigveda", "Samaveda", "Yajurveda", "Atharvaveda"], "correctAnswer": "Rigveda"},
            {"text": "The Earth takes approximately how much time to complete one rotation on its axis?", "options": ["24 hours", "365 days", "12 hours", "1 month"], "correctAnswer": "24 hours"},
            {"text": "Who established the Mughal Empire in India?", "options": ["Babar", "Akbar", "Humayun", "Aurangzeb"], "correctAnswer": "Babar"}
        ],
        "hard": [
            {"text": "In the context of Harappan civilization, what was the 'Great Bath'?", "options": ["A large rectangular tank in a courtyard likely used for special religious baths", "The king's personal swimming pool", "A large reservoir for agriculture", "A public laundry area"], "correctAnswer": "A large rectangular tank in a courtyard likely used for special religious baths"},
            {"text": "A 0° longitude is the Prime Meridian. What is the 180° longitude called?", "options": ["International Date Line", "Equator", "Tropic of Capricorn", "Arctic Circle"], "correctAnswer": "International Date Line"},
            {"text": "Who was the Greek ambassador who visited the court of Chandragupta Maurya and wrote 'Indica'?", "options": ["Megasthenes", "Fa-Hien", "Hiuen Tsang", "Alexander"], "correctAnswer": "Megasthenes"},
            {"text": "What is 'Prejudice' in the context of civics?", "options": ["Judging other people negatively or seeing them as inferior without knowing them", "Treating everyone equally", "Celebrating diversity", "Forming a government"], "correctAnswer": "Judging other people negatively or seeing them as inferior without knowing them"},
            {"text": "The Himalayan Mountains are what type of mountains?", "options": ["Young Fold Mountains", "Block Mountains", "Volcanic Mountains", "Residual Mountains"], "correctAnswer": "Young Fold Mountains"},
            {"text": "In Jainism, a person who attained enlightenment and spread the teaching is called a Tirthankara. Who was the 24th Tirthankara?", "options": ["Mahavira", "Rishabhanatha", "Parshvanatha", "Gautama Buddha"], "correctAnswer": "Mahavira"},
            {"text": "What is the term for a piece of land that is surrounded by water on three sides?", "options": ["Peninsula", "Island", "Isthmus", "Strait"], "correctAnswer": "Peninsula"},
            {"text": "During which solstice does the Northern Hemisphere experience its longest day and shortest night?", "options": ["Summer Solstice", "Winter Solstice", "Vernal Equinox", "Autumnal Equinox"], "correctAnswer": "Summer Solstice"},
            {"text": "Who drafted the Indian Constitution and is known as the Father of the Indian Constitution?", "options": ["Dr. B. R. Ambedkar", "Jawaharlal Nehru", "Dr. Rajendra Prasad", "Mahatma Gandhi"], "correctAnswer": "Dr. B. R. Ambedkar"},
            {"text": "Which level of government in India is responsible for maintaining the railway network?", "options": ["Central (Union) Government", "State Government", "Local Government", "Private companies"], "correctAnswer": "Central (Union) Government"}
        ]
    }
}

def main():
    bank_path = '/Users/arpan1.mukherjee/code/GhostMaze/public/AhirsAcademy/data/question_bank.json'
    
    with open(bank_path, 'r', encoding='utf-8') as f:
        question_bank = json.load(f)
        
    question_bank['class_6'] = class_6_data
    
    with open(bank_path, 'w', encoding='utf-8') as f:
        json.dump(question_bank, f, indent=4, ensure_ascii=False)
        
    print("Successfully injected broad and complex questions for all 5 subjects in Class 6!")

if __name__ == '__main__':
    main()
