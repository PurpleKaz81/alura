#!/usr/bin/env python3.9

import hangman.hangman as hangman
import guessing_game.guessing2 as guessing2

while True:
    try:
        print("*************************************************************")
        print("********************** Choose Your Game! ********************")
        print("*************************************************************", "\n")

        print("Please type the number corresponding to the game you'd like to play:")
        print("[1] Hangman")
        print("[2] Guess the Number")
        print("[3] Quit.", "\n")

        game_choice = int(input("What game would you like to play?\n\n"))

        if game_choice == 1:
            hangman.play()
        elif game_choice == 2:
            guessing2.play()
        elif game_choice == 3:
            print("\nGoodbye, then...", "\U0001F984", "\n")
            print("***" * 10, "\n")
            break
        else:
            print("Oops! That's not a valid choice. Please choose 1, 2, or 3.", "\n")
    except ValueError:
        print("Oops! That's not a valid choice. Please choose 1, 2, or 3.", "\n")
