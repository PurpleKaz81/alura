import random

print("***" * 10, "\n")
print("Guess the number between 1 and 10")

tries_left = 3
tries_taken = 0
while tries_left > 0:
    guess = input("Type in your guess: ")
    try:
        guess = int(guess)
        print("You typed:", guess)

        correct_number = random.randint(1, 10)
        if guess == correct_number:
            print("Nailed it!")
            break
        else:
            print("Wrong!")
            tries_left -= 1
            tries_taken += 1
            print(
                "You have",
                tries_left,
                "tries left.",
            )
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
