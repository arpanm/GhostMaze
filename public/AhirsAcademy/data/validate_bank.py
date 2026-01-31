import json
import os
from collections import Counter

BANK_PATH = '/Users/arpan1.mukherjee/code/GhostMaze/AhirsAcademy/data/question_bank.json'

def validate_bank():
    if not os.path.exists(BANK_PATH):
        print(f"Error: {BANK_PATH} not found.")
        return

    with open(BANK_PATH, 'r') as f:
        try:
            bank = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON format: {e}")
            return

    print(f"{'Class':<10} | {'Subject':<15} | {'Diff':<10} | {'Count':<5} | {'Status'}")
    print("-" * 60)

    all_errors = []
    total_questions = 0

    for class_key, subs in bank.items():
        for sub_key, diffs in subs.items():
            for diff_key, questions in diffs.items():
                count = len(questions)
                total_questions += count
                status = "OK"
                errors = []

                # Check for duplicates
                q_texts = [q.get('text', '').strip() for q in questions]
                duplicates = [item for item, count in Counter(q_texts).items() if count > 1]
                if duplicates:
                    status = "ERROR"
                    errors.append(f"Duplicates: {len(duplicates)}")

                # Structural/Answer Validation
                for i, q in enumerate(questions):
                    # Check keys
                    missing = [k for k in ['text', 'options', 'correctAnswer'] if k not in q]
                    if missing:
                        status = "ERROR"
                        errors.append(f"Q#{i} Missing keys: {missing}")
                    
                    # Check answer validity
                    if 'options' in q and 'correctAnswer' in q:
                        if q['correctAnswer'] not in q['options']:
                            status = "ERROR"
                            errors.append(f"Q#{i} Invalid Answer: '{q['correctAnswer']}' not in options")
                    
                    # Check options count
                    if 'options' in q and len(q['options']) != 4:
                        status = "ERROR"
                        errors.append(f"Q#{i} Option count: {len(q['options'])}")

                error_str = ", ".join(errors) if errors else "OK"
                print(f"{class_key:<10} | {sub_key:<15} | {diff_key:<10} | {count:<5} | {error_str}")
                
                if errors:
                    all_errors.append(f"{class_key}.{sub_key}.{diff_key}: {error_str}")

    print("-" * 60)
    print(f"Total Questions: {total_questions}")
    
    if all_errors:
        print("\nSUMMARY OF ERRORS:")
        for err in all_errors:
            print(f"- {err}")
    else:
        print("\nAll checks passed! No duplicates, valid structures, and valid answers.")

if __name__ == "__main__":
    validate_bank()
