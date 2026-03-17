import json
import os

class_1_data = {
    "english": {
        "easy": [
            {"text": "Which word is an action you can do with a pencil?", "options": ["Write", "Drink", "Sleep", "Run"], "correctAnswer": "Write"},
            {"text": "What does a caterpillar transform into?", "options": ["Butterfly", "Spider", "Frog", "Bird"], "correctAnswer": "Butterfly"},
            {"text": "Which of these words rhymes with 'Cat'?", "options": ["Hat", "Dog", "Car", "Ball"], "correctAnswer": "Hat"},
            {"text": "If today is Monday, what day is tomorrow?", "options": ["Tuesday", "Sunday", "Friday", "Wednesday"], "correctAnswer": "Tuesday"},
            {"text": "What do we call the person who treats sick people?", "options": ["Doctor", "Teacher", "Farmer", "Driver"], "correctAnswer": "Doctor"},
            {"text": "Choose the word with the correct spelling.", "options": ["Apple", "Aple", "Appel", "Apel"], "correctAnswer": "Apple"},
            {"text": "What covers a bird's body to help it fly?", "options": ["Feathers", "Fur", "Scales", "Shell"], "correctAnswer": "Feathers"},
            {"text": "Which of these is a wild animal?", "options": ["Lion", "Cow", "Dog", "Cat"], "correctAnswer": "Lion"},
            {"text": "What do we wear on our hands when it's cold?", "options": ["Gloves", "Socks", "Shoes", "Hats"], "correctAnswer": "Gloves"},
            {"text": "Complete the phrase: 'As slow as a...'", "options": ["Snail", "Cheetah", "Rabbit", "Horse"], "correctAnswer": "Snail"}
        ],
        "medium": [
            {"text": "What is the opposite of 'Strong'?", "options": ["Weak", "Fast", "Brave", "Tall"], "correctAnswer": "Weak"},
            {"text": "Which of these words is a noun (naming word)?", "options": ["Tree", "Jump", "Quickly", "Beautiful"], "correctAnswer": "Tree"},
            {"text": "Which punctuation mark comes at the end of a question?", "options": ["Question Mark (?)", "Full Stop (.)", "Comma (,)", "Exclamation Mark (!)"], "correctAnswer": "Question Mark (?)"},
            {"text": "Find the odd one out.", "options": ["Table", "Chair", "Desk", "Apple"], "correctAnswer": "Apple"},
            {"text": "What is a baby frog called?", "options": ["Tadpole", "Kitten", "Puppy", "Cub"], "correctAnswer": "Tadpole"},
            {"text": "If 'Hot' changes to 'Cold', what does 'Day' change to?", "options": ["Night", "Morning", "Evening", "Sun"], "correctAnswer": "Night"},
            {"text": "Select the correct plural form of 'Child'.", "options": ["Children", "Childs", "Childes", "Childrens"], "correctAnswer": "Children"},
            {"text": "Which letter is missing: C _ T?", "options": ["A", "B", "O", "E"], "correctAnswer": "A"},
            {"text": "Which sense helps us hear a bell ring?", "options": ["Hearing", "Sight", "Touch", "Taste"], "correctAnswer": "Hearing"},
            {"text": "What room in a house do you use to cook food?", "options": ["Kitchen", "Bedroom", "Bathroom", "Living Room"], "correctAnswer": "Kitchen"}
        ],
        "hard": [
            {"text": "Identify the describing word (adjective) in the sentence: 'The red car is fast.'", "options": ["Red", "Car", "The", "Is"], "correctAnswer": "Red"},
            {"text": "Which of the following describes an 'Island'?", "options": ["Land surrounded by water", "A huge mountain", "A deep forest", "A flying object"], "correctAnswer": "Land surrounded by water"},
            {"text": "What do you call a story that is not real?", "options": ["Fiction", "Fact", "News", "History"], "correctAnswer": "Fiction"},
            {"text": "Rearrange the letters 'P A T E L' to form a word related to food.", "options": ["PLATE", "LEAPT", "PLEAT", "PETAL"], "correctAnswer": "PLATE"},
            {"text": "What is the home of a bee called?", "options": ["Hive", "Nest", "Den", "Burrow"], "correctAnswer": "Hive"},
            {"text": "What word means the same as 'Enormous'?", "options": ["Huge", "Tiny", "Quick", "Smart"], "correctAnswer": "Huge"},
            {"text": "If a group of fish is a 'school', what is a group of cows called?", "options": ["Herd", "Flock", "Pack", "Swarm"], "correctAnswer": "Herd"},
            {"text": "Choose the correct preposition: 'The cat is hiding _____ the table.'", "options": ["Under", "At", "Of", "To"], "correctAnswer": "Under"},
            {"text": "What do you call the frozen form of water?", "options": ["Ice", "Vapor", "Cloud", "Rain"], "correctAnswer": "Ice"},
            {"text": "Which animal is known to have a trunk and large ears?", "options": ["Elephant", "Giraffe", "Tiger", "Bear"], "correctAnswer": "Elephant"}
        ]
    },
    "maths": {
        "easy": [
            {"text": "If you have 3 apples and buy 2 more, how many do you have?", "options": ["5", "4", "6", "1"], "correctAnswer": "5"},
            {"text": "Which number comes just before 10?", "options": ["9", "11", "8", "12"], "correctAnswer": "9"},
            {"text": "How many legs does a spider have?", "options": ["8", "6", "4", "10"], "correctAnswer": "8"},
            {"text": "What shape has exactly three straight sides?", "options": ["Triangle", "Square", "Circle", "Rectangle"], "correctAnswer": "Triangle"},
            {"text": "Which is the largest number: 7, 2, 9, or 4?", "options": ["9", "7", "4", "2"], "correctAnswer": "9"},
            {"text": "If a pizza is cut into 4 equal slices and you eat 1, how many are left?", "options": ["3", "4", "2", "5"], "correctAnswer": "3"},
            {"text": "What is 10 + 0?", "options": ["10", "0", "1", "100"], "correctAnswer": "10"},
            {"text": "How many days are there in a week?", "options": ["7", "5", "6", "8"], "correctAnswer": "7"},
            {"text": "Which hand on a clock moves the fastest?", "options": ["Second Hand", "Minute Hand", "Hour Hand", "They move the same"], "correctAnswer": "Second Hand"},
            {"text": "What is the sum of 5 and 5?", "options": ["10", "5", "0", "15"], "correctAnswer": "10"}
        ],
        "medium": [
            {"text": "If you have a 10 rupee coin and buy a candy for 4 rupees, what is your change?", "options": ["6 rupees", "5 rupees", "4 rupees", "7 rupees"], "correctAnswer": "6 rupees"},
            {"text": "What comes next in the pattern: 2, 4, 6, ___?", "options": ["8", "7", "9", "10"], "correctAnswer": "8"},
            {"text": "How many wheels do 3 bicycles have in total?", "options": ["6", "4", "8", "5"], "correctAnswer": "6"},
            {"text": "Which object is heavier: A single feather or a brick?", "options": ["A brick", "A feather", "They weigh the same", "None"], "correctAnswer": "A brick"},
            {"text": "What is 15 minus 7?", "options": ["8", "7", "9", "6"], "correctAnswer": "8"},
            {"text": "How many tens are there in the number 42?", "options": ["4", "2", "42", "6"], "correctAnswer": "4"},
            {"text": "If half of a pie is taken away, how much pie is left?", "options": ["One Half", "One Quarter", "One Whole", "None"], "correctAnswer": "One Half"},
            {"text": "Which shape looks like an egg?", "options": ["Oval", "Circle", "Square", "Rectangle"], "correctAnswer": "Oval"},
            {"text": "What is 3 + 3 + 3?", "options": ["9", "6", "12", "3"], "correctAnswer": "9"},
            {"text": "Which number is an odd number?", "options": ["3", "2", "4", "6"], "correctAnswer": "3"}
        ],
        "hard": [
            {"text": "If Tom is taller than Jerry, and Jerry is taller than Spike, who is the shortest?", "options": ["Spike", "Jerry", "Tom", "They are equal"], "correctAnswer": "Spike"},
            {"text": "How many months in a year have exactly 31 days?", "options": ["7", "6", "5", "4"], "correctAnswer": "7"},
            {"text": "Your class starts at 9:00 AM and ends at 2:00 PM. How many hours are you in class?", "options": ["5 hours", "4 hours", "6 hours", "3 hours"], "correctAnswer": "5 hours"},
            {"text": "I have 4 corners, but not all my sides are equal. What shape am I?", "options": ["Rectangle", "Square", "Triangle", "Circle"], "correctAnswer": "Rectangle"},
            {"text": "What is double of 7?", "options": ["14", "12", "15", "10"], "correctAnswer": "14"},
            {"text": "A spider has 8 legs. An ant has 6 legs. How many legs do they have together?", "options": ["14", "12", "2", "16"], "correctAnswer": "14"},
            {"text": "If you take away the number 5 from 20 twice, what is left?", "options": ["10", "15", "5", "0"], "correctAnswer": "10"},
            {"text": "Which is greater: three 10-rupee notes or two 20-rupee notes?", "options": ["Two 20-rupee notes", "Three 10-rupee notes", "They are equal", "Cannot be determined"], "correctAnswer": "Two 20-rupee notes"},
            {"text": "There are 12 eggs in a dozen. How many eggs are in half a dozen?", "options": ["6", "12", "4", "8"], "correctAnswer": "6"},
            {"text": "What number do you get if you add the number of fingers on two hands to the number of toes on two feet?", "options": ["20", "10", "30", "15"], "correctAnswer": "20"}
        ]
    },
    "hindi": {
        "easy": [
            {"text": "इनमें से कौन सा जानवर जंगल का राजा कहलाता है?", "options": ["शेर", "बंदर", "हाथी", "भालू"], "correctAnswer": "शेर"},
            {"text": "आसमान का रंग कैसा होता है?", "options": ["नीला", "लाल", "हरा", "काला"], "correctAnswer": "नीला"},
            {"text": "रात को आसमान में क्या चमकता है?", "options": ["तारे", "सूरज", "पेड़", "पहाड़"], "correctAnswer": "तारे"},
            {"text": "हम पानी किस बर्तन से पीते हैं?", "options": ["गिलास", "तवा", "कड़ाही", "छलनी"], "correctAnswer": "गिलास"},
            {"text": "कौन सा पक्षी मीठा गाता है?", "options": ["कोयल", "कौआ", "चील", "गिद्ध"], "correctAnswer": "कोयल"},
            {"text": "दीपावली पर हम क्या जलाते हैं?", "options": ["दीये", "कागज़", "लकड़ी", "किताब"], "correctAnswer": "दीये"},
            {"text": "हम बारिश से बचने के लिए क्या इस्तेमाल करते हैं?", "options": ["छाता", "चश्मा", "जूते", "घड़ी"], "correctAnswer": "छाता"},
            {"text": "कुत्ते की आवाज़ को क्या कहते हैं?", "options": ["भौंकना", "दहाड़ना", "मिमियाना", "टर्टराना"], "correctAnswer": "भौंकना"},
            {"text": "भारत का राष्ट्रीय फूल कौन सा है?", "options": ["कमल", "गुलाब", "गेंदा", "चमेली"], "correctAnswer": "कमल"},
            {"text": "दिन में हमें रोशनी किससे मिलती है?", "options": ["सूरज", "चांद", "तारे", "जुगनू"], "correctAnswer": "सूरज"}
        ],
        "medium": [
            {"text": "इनमें से कौन सा फल खट्टा होता है?", "options": ["नींबू", "केला", "पपीता", "तरबूज"], "correctAnswer": "नींबू"},
            {"text": "'मोटा' शब्द का उल्टा (विलोम) क्या होगा?", "options": ["पतला", "लंबा", "छोटा", "भारी"], "correctAnswer": "पतला"},
            {"text": "इनमें से कौन सा साधन हवा में उड़ता है?", "options": ["हवाई जहाज", "रेलगाड़ी", "बस", "नाव"], "correctAnswer": "हवाई जहाज"},
            {"text": "होली का त्योहार किस चीज़ से खेला जाता है?", "options": ["रंग", "पटाखे", "दीपक", "राखी"], "correctAnswer": "रंग"},
            {"text": "हफ्ते का पहला दिन कौन सा होता है?", "options": ["सोमवार", "रविवार", "मंगलवार", "शनिवार"], "correctAnswer": "सोमवार"},
            {"text": "इनमें से किस जानवर की सूंड होती है?", "options": ["हाथी", "ऊंट", "घोड़ा", "जिराफ़"], "correctAnswer": "हाथी"},
            {"text": "आंखों से हम क्या करते हैं?", "options": ["देखते हैं", "सुनते हैं", "खाते हैं", "सूंघते हैं"], "correctAnswer": "देखते हैं"},
            {"text": "'लड़का' का स्त्रीलिंग क्या होगा?", "options": ["लड़की", "औरत", "माता", "बहन"], "correctAnswer": "लड़की"},
            {"text": "किताबें पढ़ने के लिए हम कहाँ जाते हैं?", "options": ["पुस्तकालय (स्कूल)", "दुकान", "अस्पताल", "पार्क"], "correctAnswer": "पुस्तकालय (स्कूल)"},
            {"text": "इनमें से कौन सा रंग तिरंगे में नहीं होता?", "options": ["काला", "केसरिया", "सफेद", "हरा"], "correctAnswer": "काला"}
        ],
        "hard": [
            {"text": "'आसमान से बातें करना' मुहावरे का क्या अर्थ है?", "options": ["बहुत ऊंचा होना", "हवा में उड़ना", "बकवास करना", "नीचे गिरना"], "correctAnswer": "बहुत ऊंचा होना"},
            {"text": "हमारे शरीर में साँस लेने के लिए कौन सा अंग प्रमुख है?", "options": ["फेफड़े", "पेट", "दिमाग", "हाथ"], "correctAnswer": "फेफड़े"},
            {"text": "'सूर्य' का पर्यायवाची शब्द चुनें।", "options": ["रवि", "शशि", "गगन", "मेघ"], "correctAnswer": "रवि"},
            {"text": "अगर सोमवार के बाद मंगलवार आता है, तो शुक्रवार के बाद क्या आएगा?", "options": ["शनिवार", "रविवार", "गुरुवार", "बुधवार"], "correctAnswer": "शनिवार"},
            {"text": "बर्फ से बने घर को क्या कहते हैं?", "options": ["इग्लू", "तंबू", "किबला", "महल"], "correctAnswer": "इग्लू"},
            {"text": "'मिठाई' शब्द का बहुवचन क्या होगा?", "options": ["मिठाइयां", "मिठास", "मिठायें", "मीठा"], "correctAnswer": "मिठाइयां"},
            {"text": "भारत का राष्ट्रीय गान कौन सा है?", "options": ["जन गण मन", "वंदे मातरम", "सारे जहाँ से अच्छा", " विजयी विश्व तिरंगा प्यारा"], "correctAnswer": "जन गण मन"},
            {"text": "इनमें से कौन सा व्यंजन दूध से नहीं बनता?", "options": ["रोटी", "पनीर", "दही", "मक्खन"], "correctAnswer": "रोटी"},
            {"text": "किस जानवर को 'रेगिस्तान का जहाज़' कहा जाता है?", "options": ["ऊंट", "घोड़ा", "हाथी", "चीता"], "correctAnswer": "ऊंट"},
            {"text": "सही वाक्य चुनें।", "options": ["राम खाना खाता है।", "राम खाना खाती है।", "राम खाना खाते है।", "राम खाना खाओ है।"], "correctAnswer": "राम खाना खाता है।"}
        ]
    }
}

def main():
    bank_path = '/Users/arpan1.mukherjee/code/GhostMaze/public/AhirsAcademy/data/question_bank.json'
    
    with open(bank_path, 'r', encoding='utf-8') as f:
        question_bank = json.load(f)
        
    question_bank['class_1'] = class_1_data
    
    with open(bank_path, 'w', encoding='utf-8') as f:
        json.dump(question_bank, f, indent=4, ensure_ascii=False)
        
    print("Successfully deep-injected beautifully crafted tricky questions for Class 1!")

if __name__ == '__main__':
    main()
