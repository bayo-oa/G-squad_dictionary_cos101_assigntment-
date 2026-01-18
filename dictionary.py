
english_to_hausa = {
    "house": "gida", "water": "ruwa", "food": "abinci", "book": "littafi","school": "makaranta", "sun": "rana", "moon": "wata", "star": "tawo", "boy": "yaro",
    "girl": "yarinya", "father": "uba", "mother": "uwa","friend": "aboki", "work": "aiki", "road": "hanya", "go": "tafi", "come": "zo", "sleep": "bari",
    "name": "suna", "tree": "itace"
}
print ("G-squad language dictionary")
print ("Hi There 👋")
print ("Available English word you can translate to ")
for i, word in enumerate(english_to_hausa.keys(), start=4):
    
   print(f"{i}. {word}")
    

print("press 'Q' to quit")



    
while True:
    word = input("What English word do you want to translate to Hausa ").lower().strip()
    
    if word.lower() == "q":
        print("goodbye")
        break
   
    
    if word in english_to_hausa:
        print (f"The hausa  translation of {word} is: '{english_to_hausa[word]}'")
        
    else:
        print (f"sorry, '{word}' is not in the dictionary")
    
   
    


