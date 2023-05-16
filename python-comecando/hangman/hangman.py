#!/usr/bin/env python3.9


def goodbye():
    print("\nGoodbye, then...", "\U0001F984", "\n")
    print("***" * 10, "\n")


def want_to_play():
    while True:
        answer = input("Type [y] for yes and [n] for no.\n\n")
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
        if not already_played:
            print("Welcome to Hangman!", "\n")

        if not want_to_play():
            break

print("Game Over!", "\n")

if __name__ == "__main__":
    print("***" * 10, "Hangman is being run directly!", "***" * 10, "\n")
    play()
