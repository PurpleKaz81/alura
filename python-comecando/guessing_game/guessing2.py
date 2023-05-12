#!/usr/bin/env python3.9

import random


def play():
    already_played = False

    print()
    print("***" * 10, "\n")

    while True:
        if not already_played:
            print("Welcome to Guess The Number! Wanna play?", "\n")

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

        while True:
            levels = {
                1: 6,
                2: 4,
                3: 3,
                4: 1,
            }

            print("\nWhich level would you like to play?", "\n")

            game_continue = True
            level = input(
                "Type [1] for easy, [2] for medium, [3] for hard, [4] for veteran, or [q] to quit.\n\n"
            )

            if level == "q":
                game_continue = False
                print("\nGoodbye, then...", "\U0001F984", "\n")
                break

            try:
                level = int(level)
                if level in levels:
                    total_tries = levels[level]
                    break
            except ValueError:
                print("\nOnly 1, 2, 3, or q, babe.")

        if not game_continue:
            break

        print()
        print("***" * 10, "\n")
        print(
            "Good luck! And don't fall below -5 points or you lose forever \U0001F630",
            "\n",
        )
        print("Guess the number between 1 and 10", "\n")

        tries_left = total_tries
        tries_taken = 0
        integer_set = set(range(1, 11))
        guessed_numbers = []
        correct_number = random.randint(1, 10)
        print(correct_number)

        points = 10

        while tries_left > 0 and points > -5:
            guess = input("\nType in your guess: \n\n")
            try:
                guess = int(guess)
                correct = guess == correct_number
                tries_statement = f"Try {tries_taken + 1} of {total_tries}. You have {tries_left - 1} tries left."

                if guess not in integer_set:
                    print("\nOnly whole numbers between 1 and 10, champ.", "\n")
                elif guess in guessed_numbers:
                    print("\nYou already guessed that number. Try again.", "\n")
                elif correct:
                    print()
                    print(
                        "\U0001F3AF " * 3,
                        "Nailed it!",
                        "\U0001F3AF " * 3,
                        f"You get {points} points!",
                        "\n",
                    )
                    break
                else:
                    lost_points = abs(correct_number - guess)
                    if points - lost_points > -5:
                        greater_than = guess > correct_number
                        smaller_than = guess < correct_number
                        if greater_than:
                            print()
                            if tries_left > 1:
                                print(
                                    "\u2B07\ufe0f  " * 3,
                                    "Hmmm, a lower lower...",
                                    "\u2B07\ufe0f  " * 3,
                                    "\n",
                                )
                            tries_left -= 1
                            tries_taken += 1
                            if tries_left > 0:
                                print(tries_statement)
                        elif smaller_than:
                            print()
                            if tries_left > 1:
                                print(
                                    "\u2B06\ufe0f  " * 3,
                                    "A little higher, love...",
                                    "\u2B06\ufe0f  " * 3,
                                    "\n",
                                )
                            tries_left -= 1
                            tries_taken += 1
                            if tries_left > 0:
                                print(tries_statement)
                        points -= lost_points
                    else:
                        print(
                            "\nGame O-VER! You fell below -5 points. All is lost. Go home \U0001F44B",
                            "\n",
                        )
                        game_continue = False
                        break

                guessed_numbers.append(guess)

                if tries_left == 0:
                    break

            except ValueError:
                try:
                    float(guess)
                    print("\nType in a whole number, please.", "\n")

                except ValueError:
                    print("\nType in a number, buddy.", "\n")

        if not game_continue:
            break

        print("\nGame O-VER!")

        if tries_left == 0:
            print(
                f"You lose. There is meaning in nothing \U0001F603 and you have {points} points.",
                "\n",
            )
        else:
            tries_taken += 1
            print(f"\nCongrats! You won in {tries_taken} tries.", "\n")

        for _ in range(3):
            answer = input(
                "Wanna play again, pumpkin? Type [y] for yes and [n] for no.\n\n"
            )
            if answer == "n":
                print("\nGoodbye, then...", "\U0001F984", "\n")
                break
            elif answer == "y":
                already_played = True
                break
            else:
                print("Do us a solid and type in [y] or [n].\n")

        print("***" * 10, "\n")

        if answer == "n":
            break


if __name__ == "__main__":
    print("***" * 10, "Guess the Number is being run directly!", "***" * 10, "\n")
    play()
