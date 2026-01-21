import streamlit as st

#removed import dictionary as the data is defined below
#added choice selection for languages

choice = st.selectbox("language",("Hausa", "Yoruba", "Igbo", "Igala", "Idoma"))
# Your dictionary
hausa = {
        "house": "gida",
        "water": "ruwa",
        "food": "abinci",
        "book": "littafi",
        "school": "makaranta",
        "sun": "rana",
        "moon": "wata",
        "star": "tawo",
        "boy": "yaro",
        "girl": "yarinya",
        "father": "uba",
        "mother": "uwa",
        "friend": "aboki",
        "work": "aiki",
        "road": "hanya",
        "go": "tafi",
        "come": "zo",
        "sleep": "bari",
        "name": "suna",
        "tree": "itace"
    } #removed comma here
igala = {
        "hello": "Aneje",
        "thank you": "Ameyo",
        "water": "Ama",
        "food": "Uja",
        "mother": "Nne",
        "father": "Apa",
        "house": "Uno",
        "book": "Ekpulu",
        "school": "Uno ekpulu",
        "child": "Omo",
        "sun": "Ogene",
        "moon": "Ogida",
        "star": "Ukwu",
        "love": "Ifunanya",
        "god": "Ojo",
        "friend": "Oyi",
        "name": "Izina",
        "market": "Uloja"
    } #removed comma here
idoma = {
        "hello": "abayole",
        "thank you": "unma",
        "water": "enkpo",
        "food": "odire",
        "mother": "ene",
        "father": "ada",
        "house": "ole",
        "book": "okpa",
        "school": "inokpa",
        "child": "oyi",
        "sun": "eno",
        "moon": "oya",
        "star": "enyinyowo",
        "love": "ihotu",
        "friend": "okobia",
        "god": "ocho",
        "name": "iye",
        "market": "ohi"
    } #removed comma here
igbo = {
        "hello": "Ndewo",
        "thank you": "Imela",
        "water": "Mmiri",
        "food": "Nri",
        "mother": "Nne",
        "father": "Nna",
        "house": "Ulo",
        "book": "Akwukwọ",
        "school": "Ụlọ akwụkwọ",
        "child": "Nwa",
        "sun": "Anwu",
        "moon": "Onwa",
        "star": "Kpakpando",
        "love": "Ifunanya",
        "god": "Chukwu",
        "friend": "Enyi",
        "name": "Aha",
        "market": "Ahia"
    } #removed comma here
yoruba = {
        "hello": "bawo",
        "come": "ma bo",
        "go": "lo",
        "water": "omi",
        "food": "ounje",
        "mother": "iya",
        "father": "baba",
        "house": "ile",
        "book": "iwe",
        "school": "ile iwe",
        "child": "omo",
        "sun": "orun",
        "moon": "osupa",
        "star": "irawo",
        "love": "ife",
        "god": "olorun",
        "friend": "ore",
        "name": "oruko",
        "market": "oja",
        "good morning": "E kaaro",
        "good afternoon": "E kaasan",
        "good evening": "E kurole",
        "good night": "O daaro"
    } #removed comma here

def search_dictionary(your_word, dictionary):
    
    return dictionary.get(your_word, "Word not found")


if choice == "Hausa":
    dictionary = hausa
elif choice == "Igala":
    dictionary = igala
elif choice == "Idoma":
    dictionary = idoma    
elif choice == "Igbo":
    dictionary = igbo
elif choice == "Yoruba":
    dictionary = yoruba

your_word = st.text_input("Enter an English word to translate").lower()

if st.button("search"):
    translation = search_dictionary(your_word, dictionary)
    