#!/usr/bin/env python3.9

import hangman.hangman as hangman
import guessing_game.guessing2 as guessing2

while True:
    try:
        print("***" * 10)
        print("*****", "Choose Your Game!", "*****")
        print("***" * 10, "\n")

        print("[1]: Hangman", "[2]: Guess The Number", "[3]: Quit.", sep="\n", end="\n")
        game = input("\nWhich game would you like to play?\n\n")
        game = int(game)
        if game == 1:
            hangman.play()
        if game == 2:
            guessing2.play()
        elif game == 3:
            print("\nGoodbye, then...", "\U0001F984", "\n")
            break
        else:
            print("Please type either 1, 2, or 3.")
    except ValueError:
        print("Please type either 1, 2, or 3.\n")
