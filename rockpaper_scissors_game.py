import random


def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    wins = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
    return "user" if wins[user_choice] == computer_choice else "computer"


def main():
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0

    print("=== Rock, Paper, Scissors Game ===")
    print("Rules: Rock beats Scissors, Scissors beat Paper, Paper beats Rock.")

    while True:
        user_input = (
            input("\nChoose rock, paper, or scissors (or 'quit' to exit): ")
            .strip()
            .lower()
        )

        if user_input == "quit":
            print("\nFinal Scoreboard:")
            print(f"User: {user_score} | Computer: {computer_score}")
            print("Thanks for playing!")
            break

        if user_input not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_input = random.choice(choices)
        print(f"\nYou chose: {user_input.capitalize()}")
        print(f"Computer chose: {computer_input.capitalize()}")

        result = get_winner(user_input, computer_input)
        if result == "tie":
            print("It's a tie!")
        elif result == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Current Score -> User: {user_score} | Computer: {computer_score}")

        play_again = input("\nPlay another round? (y/n): ").strip().lower()
        if play_again != "y":
            print("\nFinal Scoreboard:")
            print(f"User: {user_score} | Computer: {computer_score}")
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
