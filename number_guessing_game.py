"""Number guessing game: guess a random number from 1 to 100."""

import random


LOWEST_NUMBER = 1
HIGHEST_NUMBER = 100


def play_game() -> None:
    """Run one number guessing game."""
    answer = random.randint(LOWEST_NUMBER, HIGHEST_NUMBER)
    rounds = 0

    print(f"Guess a number from {LOWEST_NUMBER} to {HIGHEST_NUMBER}.")

    while True:
        user_input = input("Your guess: ").strip()

        try:
            guess = int(user_input)
        except ValueError:
            print("Please enter a whole number.")
            continue

        if not LOWEST_NUMBER <= guess <= HIGHEST_NUMBER:
            print(
                f"Please enter a number between {LOWEST_NUMBER} and "
                f"{HIGHEST_NUMBER}."
            )
            continue

        rounds += 1

        if guess < answer:
            print("Your guess is smaller than the answer.")
        elif guess > answer:
            print("Your guess is larger than the answer.")
        else:
            print(f"Correct! You got it in {rounds} round(s).")
            break


if __name__ == "__main__":
    # Guessing the midpoint of the remaining range each time is binary search.
    # It guarantees the answer in at most 7 rounds for numbers from 1 to 100.
    play_game()
