#!/usr/bin/env python3.9

import random

print("***" * 10, "\n")
print("Guess the number between 1 and 10")

tries_left = 3
tries_taken = 0
guessed_numbers = []
while tries_left > 0:
    guess = input("Type in your guess: ")
    try:
        guess = int(guess)
        if guess < 1 or guess > 10:
            print("Only whole numbers between 1 and 10, champ.")
        elif guess in guessed_numbers:
            print("You already guessed that number. Try again.")
        else:
            print("You typed:", guess)

            correct_number = random.randint(1, 10)
            if guess == correct_number:
                print("Nailed it!")
                break
            elif guess > correct_number:
                print("Hmmm, a little smaller...")
                tries_left -= 1
                tries_taken += 1
            else:
                print("A little higher, love...")
                tries_left -= 1
                tries_taken += 1
                print(
                    "You have",
                    tries_left,
                    "tries left.",
                )

            guessed_numbers.append(guess)
    except ValueError:
        try:
            float(guess)
            print("Type in a whole number, please.")

        except ValueError:
            print("Type in a number, buddy.")

print("Game O-VER!")
if tries_left == 0:
    print("You lose. There is meaning in nothing \U0001F603")
else:
    tries_taken += 1
    print("Congrats! You won in", tries_taken, "tries.")

print("\n", "***" * 10, "\n")
