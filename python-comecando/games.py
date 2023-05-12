#!/usr/bin/env python3.9

import hangman.hangman as hangman
import guessing_game.guessing2 as guessing2

def print_menu():
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
def invalid_choice():
    print("\nOops! That's not a valid choice. Please choose 1, 2, or 3.", "\n")

def question_option(already_played):
    while True:
        try:
            if already_played:
                game_choice = int(input("What game would you like to play?\n\n"))
            else:
                game_choice = int(input("Which one will it be?\n\n"))
                already_played = True
            return game_choice, already_played
        except ValueError:
            invalid_choice()

def goodbye():
    print("\nGoodbye, then...", "\U0001F984", "\n")
    print("***" * 10, "\n")

def pick_game():
    already_played = False
    games = {1: hangman.play, 2: guessing2.play}

    while True:
        try:
            print_menu()

            game_choice, already_played = question_option(already_played)

            if game_choice in games:
                games[game_choice]()
            elif game_choice == 3:
                goodbye()
                break
            else:
                invalid_choice()
        except ValueError:
            invalid_choice()

if __name__ == "__main__":
    print()
    print("This is the main menu!", "\n")
    pick_game()
