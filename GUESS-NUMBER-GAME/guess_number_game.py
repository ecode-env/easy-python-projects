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

# Example usage:
def computer_guess(x):
guess(10)
