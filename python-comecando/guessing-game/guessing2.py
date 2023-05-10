#!/usr/bin/env python3.9

import random

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
                break
            elif answer == "y":
                break
            else:
                print("Invalid input.", "\n")

        if answer == "n":
            break

    print("***" * 10, "\n")
    print("Guess the number between 1 and 10", "\n")

    total_tries = 3
    tries_left = 3
    tries_taken = 0
    guessed_numbers = []
    correct_number = random.randint(1, 10)

    while tries_left > 0:
        guess = input("\nType in your guess: \n\n")
        try:
            guess = int(guess)
            correct = guess == correct_number
            greater_than = guess > correct_number
            smaller_than = guess < correct_number
            tries_statement = f"Try {tries_taken + 1} of {total_tries}. You have {tries_left - 1} tries left."

            if guess < 1 or guess > 10:
                print("\nOnly whole numbers between 1 and 10, champ.", "\n")
            elif guess in guessed_numbers:
                print("\nYou already guessed that number. Try again.", "\n")
            elif correct:
                print()
                print("\U0001F3AF " * 3, "Nailed it!", "\U0001F3AF " * 3, "\n")
                break
            else:
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

            guessed_numbers.append(guess)

            if tries_left == 0:
                break

        except ValueError:
            try:
                float(guess)
                print("\nType in a whole number, please.", "\n")

            except ValueError:
                print("\nType in a number, buddy.", "\n")

    print("Game O-VER!", "\n")
    if tries_left == 0:
        print("You lose. There is meaning in nothing \U0001F603", "\n")
    else:
        tries_taken += 1
        print("Congrats! You won in", tries_taken, "tries.", "\n")

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
