import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    if '_' or ' ' in word:
        word = random.choice(words)
    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letter in the word
    alphabet = set(string.ascii_uppercase)
    used_letter = set()

    # getting user input
    user_latter = input('Guess a letter: ').upper()

