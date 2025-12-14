igbo_dictionary = {
    "Hello": "Ndewo",
    "Thank you":"Imela",
    "Water":"Mmiri",
    "Food": "Nri",
    "Mother": "Nne",
    "Father": "Nna",
    "House": "Ulo",
    "Book": "Akwukwọ",
    "School": "Ụlọ akwụkwọ",
    "Child": "Nwa",
    "Man": "Mmadu nwoke",
    "Woman": "Mmadu nwanyi",
    "Sun": "Anwu",
    "Moon": "Onwa",
    "Star": "Kpakpando",
    "Love": "Ifunanya",
    "God": "Chukwu",
    "Friend": "Enyi",
    "Name": "Aha",
    "Market": "Ahia"
}

while True:
    # Changed input to ensure consistency with dictionary keys (initial capital letter)
    word = input("Enter an English word to translate to Igbo (or type 'exit' to quit): ").strip()

    if word == "":
        print("Please enter an English word to translate.")
        continue

    if word.lower() == "exit":
        print("Goodbye!")
        break
    
    # Check for lowercase input and convert it to title case for lookup
    if word.islower():
        word = word.title()
        
    # --- FIX APPLIED HERE: Changed 'dictionary' to 'igbo_dictionary' ---
    translation = igbo_dictionary.get(word) 

    if translation:
        print(f"The Igbo translation of '{word}' is '{translation}'.")
    else:
        print("Word not found in the dictionary.")