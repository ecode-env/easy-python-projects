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

import os
import subprocess
from datetime import datetime

# Set your name and email if needed
# subprocess.run(['git', 'config', 'user.name', 'your_username'])
# subprocess.run(['git', 'config', 'user.email', 'your_email@example.com'])

# Create a file to track the commits
file_name = "commit_spam.txt"

# Get today's date in the right format
today = datetime.now().strftime("%Y-%m-%d")

for i in range(1, 71):  # 1 to 70
    with open(file_name, "a") as file:
        file.write(f"Commit number {i} on {today}\n")

    subprocess.run(["git", "add", file_name])
    subprocess.run(["git", "commit", "--date", f"{today}T12:00:00", "-m", f"Commit {i} - feeling under the weather 🌧️"])

print("✅ Done making 70 commits!")

# After script finishes, don't forget to push
print("\nNow run: git push origin main (or master)")
