import random

print("***" * 10, "\n")

print("Guess the number between 1 and 10")

tries_left = 3
tries_taken = 0
while tries_left > 0:
    guess = int(input("Type in your guess: "))
    print("You typed:", guess)

    correct_number = random.randint(1, 10)
    if (guess == correct_number):
        print("Nailed it!")
        break
    else:
        print("Wrong!")
        tries_left -= 1
        tries_taken += 1
        print("You have", tries_left, "tries left.",)
    # end if
print("Game O-VER!")
if (tries_left == 0):
    print("You lose. Your life is over")
else:
    tries_taken += 1
    print("Congrats! You won in", tries_taken, "tries.")
# end if

print("\n", "***" * 10, "\n")
