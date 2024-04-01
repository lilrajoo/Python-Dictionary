# Import necessary modules
import json  # Used for loading JSON data
from difflib import get_close_matches  # Used for finding similar words

# Load the dictionary data from a JSON file
data = json.load(open("C:/NP/python stuff/app 1/data.json"))

# Define a function to translate a word
def translate(w):
    # Normalize the word to lowercase for case-insensitive matching
    w = w.lower()

    # Check for exact matches in different cases
    if w in data:  # Check for exact match in lowercase
        return data[w]
    elif w.title() in data:  # Check for title case (e.g., "Apple")
        return data[w.title()]
    elif w.upper() in data:  # Check for uppercase (e.g., "USA")
        return data[w.upper()]

    # If no exact match found, try finding close matches
    elif len(get_close_matches(w, data.keys())) > 0:
        # Get the closest match and prompt the user for confirmation
        yn = input(f"Did you mean {get_close_matches(w, data.keys())[0]} instead? Enter Y if yes, or N if no: ")
        if yn.upper() == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn.upper() == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."

    # If no match or close match found, indicate the word doesn't exist
    else:
        return "The word doesn't exist. Please double check it."

# Get input from the user
word = input("Enter word: ")

# Translate the word using the translate function
output = translate(word)

# Print the translation, handling both single values and lists
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)