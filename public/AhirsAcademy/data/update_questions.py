import json
import os
import requests
import time

def generate_questions_for_class_subject_difficulty(cls, subject, diff, existing_questions):
    prompt = f"""You are an expert curriculum designer and teacher for India's CBSE board.

I need you to generate 20 VERY TOUGH and COMPREHENSIVE multiple-choice questions for Class {cls.replace('class_', '')} for the subject {subject.capitalize()}. 
The difficulty level is '{diff}'. Even for 'easy', make it conceptually rich. For 'hard', make it extremely challenging, requiring deep thought common sense, or advanced application of concepts for that age group.
Do not repeat concepts. Make sure the questions reflect real-world applications or deep theoretical understanding. 

Return ONLY a JSON array of 20 objects. Each object must have:
- "text": The question string
- "options": An array of exactly 4 strings
- "correctAnswer": The string of the correct option

DO NOT wrap in markdown blocks like ```json. Just return the raw JSON array.
"""
    
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=AIzaSyCeCArTxIyT3ch_QNJDUJYFjaRO0TOq910"
    
    try:
        response = requests.post(
            url,
            headers={'Content-Type': 'application/json'},
            json={
                "contents": [{"parts":[{"text": prompt}]}],
                "generationConfig": {
                    "temperature": 0.8,
                    "maxOutputTokens": 4000
                }
            }
        )
        data = response.json()
        if 'candidates' not in data:
            print(f"API Error Response: {data}")
            return []
            
        raw_text = data['candidates'][0]['content']['parts'][0]['text']
        raw_text = raw_text.replace('```json', '').replace('```', '').strip()
        
        start_idx = raw_text.find('[')
        end_idx = raw_text.rfind(']')
        if start_idx != -1 and end_idx != -1:
            clean_json = raw_text[start_idx:end_idx+1]
            return json.loads(clean_json)
    except Exception as e:
        print(f"Error generating {cls} {subject} {diff}: {e}")
        return []
    
    return []

def main():
    bank_path = '/Users/arpan1.mukherjee/code/GhostMaze/public/AhirsAcademy/data/question_bank.json'
    
    with open(bank_path, 'r') as f:
        question_bank = json.load(f)
        
    classes_to_update = ['class_1', 'class_2', 'class_3', 'class_4', 'class_5', 'class_6', 'class_7', 'class_8']
    
    for cls in classes_to_update:
        if cls not in question_bank:
            continue
            
        print(f"Updating {cls}...")
        for subject in question_bank[cls].keys():
            for diff in ['easy', 'medium', 'hard']:
                print(f"  Fetching new questions for {subject} - {diff}...")
                new_qs = generate_questions_for_class_subject_difficulty(cls, subject, diff, question_bank[cls][subject][diff])
                if new_qs and len(new_qs) > 0:
                    # Replace the old basic questions with these new comprehensive ones
                    question_bank[cls][subject][diff] = new_qs
                time.sleep(2) # rate limit
                
        # Save progressively to not lose data
        with open(bank_path, 'w') as f:
            json.dump(question_bank, f, indent=4, ensure_ascii=False)
            
    print("Done!")

if __name__ == '__main__':
    main()
