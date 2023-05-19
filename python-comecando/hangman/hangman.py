#!/usr/bin/env python3.9

import random


def goodbye():
    print("\nGoodbye, then...", "\U0001F984", "\n")
    print("***" * 10, "\n")


def print_success_message(secret_word):
    print(
        "\U0001F525 " * 3,
        f"That's right! The word is {secret_word}! You're not going to \U0001F480",
        "\U0001F525 " * 3,
        "\n",
    )


def print_failure_message(secret_word):
    print(
        "\U0001F62D " * 3,
        "\n\nYou lost, love. But it's ok, you're only \U0001F480",
        "\n",
    )
    print(f"The word was {secret_word}", "\U0001F44B " * 3, "\n")


def wrong_guess_messages(errors, guess):
    print(f"\nThat's incorrect! The word does not contain {guess}.")
    print(f"\nYou have {6 - errors} tries left.", "\n")


def get_user_confirmation_prompt(prompt):
    while True:
        answer = input(prompt)

        if answer == "n":
            goodbye()
            return False
        elif answer == "y":
            return True
        else:
            print("\nJust y or n, buddy.", "\n")


def start_or_continue_game(already_played):
    if already_played:
        prompt = "Would you like to play again? (y/n) "
    else:
        prompt = "Would you like to play Hangman? (y/n) "
        already_played = True

    return get_user_confirmation_prompt(prompt), already_played


def select_secret_word():
    with open("dictionaries/American/2of12.txt") as f:
        words = [word.strip() for word in f.readlines() if set(word.strip()).issubset(set("abcdefghijklmnopqrstuvwxyz' "))]
    return random.choice(words).strip()


def get_valid_guess(guessed_letters):
    while True:
        guess = input("Guess a letter: ").strip().lower()

        if len(guess) > 1:
            print("\nJust one entry, buddy.", "\n")
        elif len(guess) == 0:
            print("\nNo empty guesses, buddy.", "\n")
        elif not guess.isalpha():
            print("\nJust letters, buddy.", "\n")
        elif guess in guessed_letters:
            print("\nYou already guessed that letter, buddy.", "\n")
        else:
            return guess


def guess_is_letter(guess, secret_word, correct_guesses):
    found = False
    for index, letter in enumerate(secret_word):
        if guess == letter:
            correct_guesses[index] = letter
            found = True
    return found


def correct_guess(guess, secret_word, correct_guesses):
    if found := guess_is_letter(guess, secret_word, correct_guesses):
        if correct_guesses.count("_") > 0:
            print()
            print("".join(correct_guesses), "\n")
        elif correct_guesses.count("_") == 0:
            success = True
            print()
            print_success_message(secret_word)
            return True
    return False


def error_or_failure(errors, guess, hanged, secret_word, game_on):
    hanged = False
    game_on = True
    errors += 1
    if errors < 6:
        wrong_guess_messages(errors, guess)
    elif errors == 6:
        hanged = True
        print()
        print_failure_message(secret_word)
        game_on = False
    return hanged, game_on, errors


def continue_game(correct_guesses, game_on, success):
    if game_on:
        remaining_letters = correct_guesses.count("_")
        if remaining_letters > 0:
            print(
                f"There are {remaining_letters} letters left to guess, \U0001F9C1.",
                "\n",
            )
        else:
            success = True
            print("\U0001F973 " * 3, "You win!", "\U0001F973 " * 3, "\n")
            game_on = False
    return game_on, success


def play():
    already_played = False
    print("***" * 10, "\n")

    found = False

    while True:
        game_on, already_played = start_or_continue_game(already_played)

        if not game_on:
            break

        secret_word = select_secret_word()
        # print(secret_word)

        print()
        hanged = False
        errors = 0
        success = False
        correct_guesses = [char if char in [" ", "-", "'"] else "_" for char in secret_word]
        guessed_letters = []

        while game_on and not hanged and not success:
            guess = get_valid_guess(guessed_letters)

            guessed_letters.append(guess)

            if guess in secret_word:
                success = correct_guess(guess, secret_word, correct_guesses)
            else:
                hanged, game_on, errors = error_or_failure(errors, guess, hanged, secret_word, game_on)

            game_on, success = continue_game(correct_guesses, game_on, success)


print("Game Over!", "\n")

if __name__ == "__main__":
    print("*" * 10, "Hangman is being run directly!", "*" * 10, "\n")
    play()
