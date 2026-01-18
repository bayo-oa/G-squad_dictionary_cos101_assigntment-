yoruba_Dictionary= {
    "Hello":"bawo",
    "Come":"ma bo",
    "go":"lo",
    "Thank you":"",
    "Water":"omi",
    "Food":"ounje",
    "Mother":"Iya",
    "Father":"baba",
    "sister":"ati mi",
    "brother":"boda",
    "girl":"o bi rin",
    "boy":"o ku rin",
    "House":"ile",
    "Book":"iwe",
    "School":"i le i we",
    "Child":"omo",
    "Man":"oku",
    "Woman":"ara bi rin",
    "Sun":"o run",
    "Moon":"osupa",
    "Star":"i rawo",
    "Love":"ife",
    "car":"o ko",
    "clothe":"a sooke",
    "phone":"e ro iba ni soro",
    "clothe":"a sooke",
    "God":"Olorun",
    "Friend":"ore",
    "Name":"oruko",
    "Market":"oja",
    "good morning":"E kaaro",
    "good afternoon":"E kaasan",
    "good evening":"E kurole",
    "good night":"O daaro",
}

while True:
    word = input("Enter an English word to translate to Yoruba (or type 'exit' to quit): ").strip()

    if word == "":
        print("Please enter an English word to translate to Yoruba.")
        continue

    if word.lower() == "exit":
        print("Goodbye!")
        break

    translation = dictionary.get(word)

    if translation:
        print(f"The Yoruba translation of '{word}' is '{translation}'.")
    else:
        print("Word not found in the dictionary.")