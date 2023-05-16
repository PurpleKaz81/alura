#!/usr/bin/env python3.9


def goodbye():
    print("Goodbye, then...", "\U0001F984", "\n")
    print("***" * 10, "\n")


def want_to_play():
    while True:
        answer = input("Wanna play? Type [y] for yes and [n] for no.\n\n")
        print()

        if answer == "n":
            goodbye()
            return False
        elif answer == "y":
            return True
        else:
            print("Just y or n, buddy.", "\n")
            return False

def wanna_play_again():
    while True:
        answer = input("Wanna play again? Type [y] for yes and [n] for no.\n\n")
        print()

        if answer == "n":
            goodbye()
            return False
        elif answer == "y":
            return True
        else:
            print("Just y or n, buddy.", "\n")
            return False

def play():
    already_played = False


    print()
    print("***" * 10, "\n")


    while True:
        hanged = False
        success = False
        secret_word = "banana"
        correct_guesses = ["_", "_", "_", "_", "_", "_"]
        if not already_played:
            print("Welcome to Hangman!", "\n")

        if not want_to_play():
            break

        while not hanged and not success:
            guess = input("Guess a letter: ").strip().lower()
            found = False

            for index, letter in enumerate(secret_word):
                if guess == letter:
                    correct_guesses[index] = letter
                    found = True

            print()
            print(correct_guesses, "\n")

            if not found:
                print(f"{guess} not found in word.", "\n")

            if "_" not in correct_guesses:
                success = True
                print("\U0001F973 " * 3, "You won!", "\U0001F973 " * 3, "\n")

        if not already_played:
            already_played = True

        if not wanna_play_again():
            break

print("Game Over!", "\n")

if __name__ == "__main__":
    print("***" * 10, "Hangman is being run directly!", "***" * 10, "\n")
    play()
