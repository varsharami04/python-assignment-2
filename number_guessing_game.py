# number_guessing_game.py

import random

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 7
    attempts_used = 0

    print("\nI have selected a number between 1 and 100.")
    print("You have 7 attempts to guess it!")

    while attempts > 0:
        try:
            guess = int(input("\nEnter your guess: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        attempts_used += 1
        attempts -= 1

        if guess == secret_number:
            print(f"\n🎉 Congratulations! You guessed it in {attempts_used} attempts!")
            return
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")

        if attempts > 0:
            print(f"Attempts remaining: {attempts}")
        else:
            print("\n❌ You failed to guess the number.")
            print(f"The correct number was: {secret_number}")


def main():
    print("=== NUMBER GUESSING GAME ===")

    while True:
        play_game()
        play_again = input("\nDo you want to play again? (yes/no): ").lower()

        if play_again != "yes":
            print("Thanks for playing! Goodbye 👋")
            break


if __name__ == "__main__":
    main()