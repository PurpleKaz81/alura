print("***" * 5, "\n")

print("Welcome to the guessing game!", "\n")

print("***" * 5, "\n")

secret_number = 42

guess = int(input("Type your guess: "))

print("\n")

print("You typed", guess, "\n")

print("Nailed it!" if secret_number == guess else "WROOOONG!")

print("\n")

