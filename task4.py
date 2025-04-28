# Task 4 - Rock-Paper-Scissors Game
import random

def play_game():
    user_score = 0
    computer_score = 0
    choices = ['rock', 'paper', 'scissors']
    beats = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }

    print("=" * 40)
    print("Welcome to Rock-Paper-Scissors!")
    print("Game Rules:")
    print("- Rock beats Scissors")
    print("- Scissors beats Paper")
    print("- Paper beats Rock")
    print("=" * 40 + "\n")

    while True:
        # Get user input with validation
        while True:
            user_choice = input("Choose (R)ock, (P)aper, (S)cissors: ").lower()
            if user_choice in ['r', 'rock']:
                user_choice = 'rock'
                break
            if user_choice in ['p', 'paper']:
                user_choice = 'paper'
                break
            if user_choice in ['s', 'scissors']:
                user_choice = 'scissors'
                break
            print("Invalid choice! Please try again.")

        # Generate computer choice
        computer_choice = random.choice(choices)

        # Determine winner
        if user_choice == computer_choice:
            result = 'tie'
        elif beats[user_choice] == computer_choice:
            result = 'user'
            user_score += 1
        else:
            result = 'computer'
            computer_score += 1

        # Display results
        print("\n" + "=" * 40)
        print(f"Your choice: {user_choice.capitalize()}")
        print(f"Computer's choice: {computer_choice.capitalize()}")

        if result == 'tie':
            print("It's a tie!")
        else:
            print(f"{result.capitalize()} wins!")

        print(f"\nScore: You {user_score} - Computer {computer_score}")
        print("=" * 40 + "\n")

        # Play again prompt
        while True:
            replay = input("Play again? (Y/N): ").lower()
            if replay in ['y', 'n', 'yes', 'no']:
                break
            print("Invalid input! Please enter Y/N")
        
        if replay in ['n', 'no']:
            print("\nFinal Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
