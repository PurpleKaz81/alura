#!/usr/bin/env python3.9

already_played = False

while True:
    if not already_played:
        print()
        print("***" * 3, "Welcome to Hangman! Guess the letters, guess the word!", "***" * 3, "\n")

        for _ in range(3):
            answer = input("Type [y] for yes and [n] for no.\n\n")
            print()

            if answer == "n":
                print("Goodbye, then...", "\U0001F984", "\n")
                print("***" * 10, "\n")
                break
            elif answer == "y":
                break
            else:
                print("Just y or n, buddy.", "\n")

        if answer == "n":
            break

print("***" * 10, "Game Over!", "\n")
