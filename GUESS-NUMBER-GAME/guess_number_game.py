import random


def guess(x):
    """A simple number guessing game where the user guesses a random number between 1 and x."""
    random_number = random.randint(1, x)  # Generate a random number
    guess_number = None  # Initialize guess variable

    while guess_number != random_number:
        guess_number = int(input(f"Guess a number between 1 and {x}: "))  # User input

        if guess_number < random_number:
            print("Too low. Try again.")
        elif guess_number > random_number:
            print("Too high. Try again.")

    print("Congratulations! You guessed the correct number 🎉")


def computer_guess(x):
    """A guessing game where the computer tries to guess the user's number."""
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':  # Loop until the computer guesses correctly
        if low != high:
            guess_number = random.randint(low, high)  # Computer makes a guess
        else:
            guess_number = low
        feedback = input(f"Is {guess_number} too high (H), too low (L), or correct (C)? ").lower()

        if feedback == 'h':
            high = guess_number - 1  # Adjust upper bound
        elif feedback == 'l':
            low = guess_number + 1  # Adjust lower bound

    print(f"Yay! The computer guessed your number, {guess_number}, correctly! 🎉")


computer_guess(100)

#guess(10)
