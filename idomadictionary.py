idoma_dictionary = {
    "Hello":"abayole",
    "Thank you":"unma",
    "Water":"enkpo",
    "Food":"odire",
    "Mother":"ene",
    "Father":"ada",
    "House":"ole",
    "Book":"okpa",
    "School":"inokpa",
    "Child":"oyi",
    "plate":"ogo",
    "spoon":"ebu",
    "Sun":"eno",
    "Moon":"oya",
    "Star":"enyinyowo",
    "Love":"ihotu",
    "Friend":"okobia",
    "God":"ocho",
    "Name":"iye",
    "Market":"ohi",
}

while True:
    word = input("Enter an English word to translate to idoma (or type 'exit' to exit): ").strip()

    if word == "":
        print("Please enter an English word to translate to idoma.")
        continue

    if word.lower() == "exit":
        print("Goodbye!")
        break
    if word.islower():
        word = word.title()

    translation = idoma_dictionary.get(word)

    if translation:
        print(f"The Idoma translation of '{word}' is '{translation}'.")
    else:
        print("word not found in the dictionary.")