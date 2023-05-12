#!/usr/bin/env python3.9

import hangman.hangman as hangman
import guessing_game.guessing2 as guessing2


def pick_game():
    already_played = False

    while True:
        try:
            print("*************************************************************")
            print("********************** Choose Your Game! ********************")
            print("*************************************************************", "\n")

            print(
                "Please type the number corresponding to the game you'd like to play:\n",
                "- [1] Hangman",
                "- [2] Guess the Number",
                "- [3] Quit.",
                sep="\n",
                end="\n\n",
            )

            if already_played:
                game_choice = int(input("What game would you like to play?\n\n"))
            else:
                game_choice = int(input("Which one will it be?\n\n"))
                already_played = True

            if game_choice == 1:
                hangman.play()
            elif game_choice == 2:
                guessing2.play()
            elif game_choice == 3:
                print("\nGoodbye, then...", "\U0001F984", "\n")
                print("***" * 10, "\n")
                break
            else:
                print(
                    "Oops! That's not a valid choice. Please choose 1, 2, or 3.", "\n"
                )
        except ValueError:
            print("Oops! That's not a valid choice. Please choose 1, 2, or 3.", "\n")


if __name__ == "__main__":
    print("***" * 10, "This is the main menu!", "***" * 10, "\n")
    pick_game()
