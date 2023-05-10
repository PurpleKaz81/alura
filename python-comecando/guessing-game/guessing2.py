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

    max_tries = 3
    tries_left = 3
    tries_taken = 1

    guessed_numbers = []
    correct_number = random.randint(1, 10)

    for tries_taken in range(max_tries):
        tries_statement = print(
            f"Try {tries_taken + 1} of {max_tries}. You have {tries_left} tries left."
        )
        guess = input("\nType in your guess: \n\n")
        try:
            guess = int(guess)
            integer_set = set(range(1, 11))
            correct = guess == correct_number
            greater_than = guess > correct_number
            smaller_than = guess < correct_number

            if guess not in integer_set:
                print("\nOnly whole numbers between 1 and 10, champ.", "\n")
            elif guess in guessed_numbers:
                print("\nYou already guessed that number. Try again.", "\n")
            else:
                print("\nYou typed:", guess, "\n")

                if correct:
                    print("\U0001F3AF " * 3, "Nailed it!", "\U0001F3AF " * 3)
                    break
                else:
                    if greater_than:
                        print(
                            "\u2B07\ufe0f  " * 3,
                            "Hmmm, a lower lower...",
                            "\u2B07\ufe0f  " * 3,
                            "\n",
                        )
                        tries_left -= 1
                        tries_taken += 1
                        if tries_left > 0:
                            tries_statement
                    elif smaller_than:
                        print(
                            "\u2B06\ufe0f  " * 3,
                            "A little higher, love...",
                            "\u2B06\ufe0f  " * 3,
                            "\n",
                        )
                        tries_left -= 1
                        tries_taken += 1
                        if tries_left > 0:
                            tries_statement

                        guessed_numbers.append(guess)
        except ValueError:
            try:
                float(guess)
                print("\nType in a whole number, please.", "\n")

            except ValueError:
                print("\nType in a number, buddy.", "\n")

    print("\nGame O-VER!", "\n")

    if tries_left == 0:
        print("You lose. There is meaning in nothing \U0001F603", "\n")
    else:
        tries_taken += 1
        print(f"Congrats! You won in {tries_taken} tries.", "\n")

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
            print("\nDo us a solid and type in [y] or [n].\n")

    print("***" * 10, "\n")

    if answer == "n":
        break
