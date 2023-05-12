#!/usr/bin/env python3.9

import subprocess

choices = {
    1: ["python3", "hangman/hangman.py"],
    2: ["python3", "guessing-game/guessing2.py"],
    3: "quit",
}

while True:
    try:
        print("***" * 10)
        print("*****", "Choose Your Game!", "*****")
        print("***" * 10, "\n")

        print("[1]: Hangman", "[2]: Guess The Number", "[3]: Quit.", sep="\n", end="\n")
        game = input("\nWhich game would you like to play?\n\n")
        game = int(game)
        if game in {1, 2}:
            subprocess.run(choices[game])
        elif game == 3:
            print("\nGoodbye, then...", "\U0001F984", "\n")
            break
        else:
            print("Please type either 1, 2, or 3.")
    except ValueError:
        print("Please type either 1, 2, or 3.\n")
