import random

def roll_dice():
    """Simulate rolling a six-sided dice."""
    return random.randint(1, 6)

def play_dice_game():
    print("Welcome to the Dice Game!")
    print("Press Enter to roll the dice...")

    input("Player, roll your dice! (Press Enter)")
    player_roll = roll_dice()
    print(f"You rolled: {player_roll}")

    input("Computer is rolling its dice... (Press Enter)")
    computer_roll = roll_dice()
    print(f"Computer rolled: {computer_roll}")

    # Determine the winner
    if player_roll > computer_roll:
        print("Congratulations! You win!")
    elif player_roll < computer_roll:
        print("Oh no! The computer wins!")
    else:
        print("It's a tie! Play again!")

# Run the game
if __name__ == "__main__":
    play_dice_game()
