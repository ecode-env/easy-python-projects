import random

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissor: ").lower()
    computer = random.choice(['r', 'p', 's'])

    print(f"Computer chose: {computer}")  # Show computer's choice

    if user == computer:
        return "It's a tie!"

    if is_win(user, computer):  # Pass arguments to is_win()
        return "You won!"

    return "You lost!"


def is_win(player, opponent):

    """Returns True if the player beats the opponent."""

    if (player == 'r' and opponent == 's') or \
       (player == 's' and opponent == 'p') or \
       (player == 'p' and opponent == 'r'):

        return True

    return False  # Explicitly return False when the player doesn't win

# Run the game

print(play())
