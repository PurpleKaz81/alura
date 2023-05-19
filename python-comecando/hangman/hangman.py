#!/usr/bin/env python3.9

import random


def goodbye():
    print("Goodbye, then...", "\U0001F984", "\n")
    print("***" * 10, "\n")


def get_user_confirmation_prompt(prompt):
    while True:
        answer = input(prompt)

        if answer == "n":
            goodbye()
            return False
        elif answer == "y":
            return True
        else:
            print("Just y or n, buddy.", "\n")

def select_secret_word():
    with open("dictionaries/American/2of12.txt") as f:
        words = f.readlines()
    return random.choice(words).strip()


def play():
    already_played = False

    print()
    print("***" * 10, "\n")

    secret_word = select_secret_word()

    while True:
        game_on = True
        hanged = False
        errors = 0
        success = False
        correct_guesses = ["_" for _ in secret_word]
        guessed_letters = []

        if not already_played:
            print("Welcome to Hangman!", "\n")
            if get_user_confirmation_prompt():
                already_played = True
            else:
                break
        elif not get_user_confirmation_prompt():
            break

        while game_on and not hanged and not success:
            guess = input("Guess a letter: ").strip().lower()
            found = False

            if guess.isdigit():
                print("\nNo numbers, please.", "\n")
                continue

            if not guess:
                print("\nNo empty guesses, please.", "\n")
                continue

            if guess in guessed_letters:
                print("\nYou already guessed that letter.", "\n")
                continue

            guessed_letters.append(guess)

            if guess in secret_word:
                for index, letter in enumerate(secret_word):
                    if guess == letter:
                        correct_guesses[index] = letter
                        found = True
                if correct_guesses.count("_") > 0:
                    print()
                    print("".join(correct_guesses), "\n")
                elif correct_guesses.count("_") == 0:
                    success = True
                    print()
                    print(
                        "\U0001F525 " * 3,
                        f"That's right! The word is {secret_word}!",
                        "\U0001F525 " * 3,
                        "\n",
                    )
            else:
                errors += 1
                if errors < 6:
                    print(f"\nThat's incorrect! You have {6 - errors} tries left.")
                    print(f"\nThe word does not contain {guess}.", "\n")
                else:
                    hanged = True
                    print()
                    print(
                        "\U0001F62D " * 3,
                        "\n\nYou lost, love. But it's ok, you're only \U0001F480",
                        "\n",
                    )
                    print(f"The word was {secret_word}", "\U0001F44B " * 3, "\n")
                    game_on = False
                    break

            if game_on:
                remaining_letters = correct_guesses.count("_")
                if remaining_letters > 0:
                    print(
                        f"There are {remaining_letters} letters left to guess, \U0001F9C1.",
                        "\n",
                    )
                else:
                    success = True
                    print("\U0001F973 " * 3, "You won!", "\U0001F973 " * 3, "\n")
                    game_on = False


print("Game Over!", "\n")

if __name__ == "__main__":
    print("*" * 10, "Hangman is being run directly!", "*" * 10, "\n")
    play()
