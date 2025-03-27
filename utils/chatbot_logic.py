import pandas as pd
from fuzzywuzzy import process

def load_advisory_data(file_path, encoding="utf-8", on_bad_lines='skip'):
    try:
        # Load CSV
        advisory_data = pd.read_csv(file_path, encoding=encoding, on_bad_lines=on_bad_lines)
        
        # Ensure required columns exist
        if 'Question' not in advisory_data.columns or 'Answer' not in advisory_data.columns:
            raise KeyError("CSV file must contain 'Question' and 'Answer' columns.")

        # Clean data: Remove extra spaces, newlines, and ensure lowercase keys
        advisory_dict = {q.strip().lower().replace("\n", "").replace("\r", ""): a.strip()
                         for q, a in zip(advisory_data['Question'].astype(str), 
                                         advisory_data['Answer'].astype(str))}
        
        return advisory_dict
    except Exception as e:
        print(f"Error loading advisory data: {e}")
        return {}

def get_best_match(user_input, advisory_dict):
    if not advisory_dict:
        return "Advisory data is empty or could not be loaded."
    
    questions = list(advisory_dict.keys())

    if not questions:
        return "No advisory questions available."

    # Convert user input to lowercase and strip spaces
    user_input = user_input.strip().lower()

    # Find the best match
    result = process.extractOne(user_input, questions)

    if result:
        best_match, score = result

        # Debugging prints
        print(f"Best match: '{best_match}' with score: {score}")
        print(f"Available questions: {list(advisory_dict.keys())[:5]}")  # Print first 5 keys

        best_match = best_match.strip().lower()
        if score > 80:
            return advisory_dict.get(best_match, "Sorry, I couldn't find a suitable answer.")

    return "Sorry, I couldn't find a suitable answer. Please try rephrasing your question."
