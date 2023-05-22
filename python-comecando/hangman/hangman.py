#!/usr/bin/env python3.9

import contextlib
import random
import os
import signal
import sys


words = []
used_words = []


def print_message1(message):
    print(f"{message}\n")


def print_message2(message):
    print(f"\n{message}")


def print_message3(message):
    print(f"\n{message}\n")


def print_welcome_message():
    print_message1("***" * 10)
    print_message1("Welcome to Hangman! \U0001F3AE")
    print_message1("***" * 10)


def goodbye():
    print_message2("Goodbye, then... \U0001F984")
    print_message3("***" * 10)


def print_success_message(secret_word):
    success_message = (
        "\U0001F525 " * 3
        + f"That's right! The word is {secret_word}! You're not going to \U0001F480 "
    )
    print_message1(success_message)


def print_failure_message(secret_word):
    failure_message = (
        "\U0001F62D " * 3 + "You lost, love. But it's ok, you're only \U0001F480 "
    )
    secret_world_reveal = f"The word was {secret_word} " + "\U0001F44B " * 3
    final_message = failure_message + secret_world_reveal
    print_message1(final_message)


def wrong_guess_messages(errors, guess):
    print_message2(f"That's incorrect! The word does not contain {guess}.")
    print_message3(f"You have {6 - errors} tries left, \U0001F9C1")


def get_user_confirmation_prompt(prompt):
    while True:
        answer = input(prompt)

        if answer == "n":
            goodbye()
            return False
        elif answer == "y":
            return True
        else:
            print_message3("Just y or n, buddy.")


def start_or_continue_game(already_played):
    if already_played:
        prompt = "Would you like to play again? Type [y] for yes or [n] for no: "
    else:
        prompt = "Would you like to play Hangman? Type [y] for yes or [n] for no: "
        already_played = True

    return get_user_confirmation_prompt(prompt), already_played


def load_words():
    global words
    with open("dictionaries/American/2of12.txt") as f:
        words = [
            word.strip()
            for word in f.readlines()
            if set(word.strip()).issubset(set("abcdefghijklmnopqrstuvwxyz'- "))
        ]


def select_secret_word():
    global words, used_words
    if not words:
        load_words()

    secret_word = random.choice(words)
    words.remove(secret_word)
    used_words.append(secret_word)
    return secret_word


def create_used_words_file():
    with open("dictionaries/American/used_words.txt", "w") as file:
        for word in used_words:
            file.write(word + "\n")


def delete_used_words_file():
    with contextlib.suppress(FileNotFoundError):
        os.remove("dictionaries/American/used_words.txt")


def get_valid_guess(guessed_letters):
    while True:
        guess = input("Guess a letter: ").strip().lower()

        if len(guess) > 1:
            print_message3("Just one entry, buddy.")
        elif len(guess) == 0:
            print_message3("No empty guesses, buddy.")
        elif not guess.isalpha():
            print_message3("Just letters, buddy.")
        elif guess in guessed_letters:
            print_message3("You already guessed that letter, buddy.")
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
            print_message1(f"There are {remaining_letters} letters left to guess")
        else:
            success = True
            print_message1("\U0001F973 " * 3 + "You win!" + "\U0001F973 " * 3)
            game_on = False
    return game_on, success


def play():
    global words, used_words
    load_words()
    already_played = False
    print_welcome_message()

    found = False

    while True:
        game_on, already_played = start_or_continue_game(already_played)

        if not game_on:
            break

        secret_word = select_secret_word()
        # print()
        # print(secret_word)

        create_used_words_file()

        print()
        hanged = False
        errors = 0
        success = False
        correct_guesses = [
            char if char in [" ", "-", "'"] else "_" for char in secret_word
        ]

        print_message1(f"Let's do this! You've got {6 - errors} tries!")
        print("".join(correct_guesses), "\n")

        guessed_letters = []

        while game_on and not hanged and not success:
            guess = get_valid_guess(guessed_letters)

            guessed_letters.append(guess)

            if guess in secret_word:
                success = correct_guess(guess, secret_word, correct_guesses)
            else:
                hanged, game_on, errors = error_or_failure(
                    errors, guess, hanged, secret_word, game_on
                )

            game_on, success = continue_game(correct_guesses, game_on, success)

    delete_used_words_file()


def handle_sigint(sig, frame):
    delete_used_words_file()
    print()
    print_message3("Interrupted, cleaning up and exiting...")
    sys.exit(0)


# Set up SIGINT handler
signal.signal(signal.SIGINT, handle_sigint)


if __name__ == "__main__":
    print_message3("Hangman is being run directly!")
    play()
