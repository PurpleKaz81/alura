import random

print(random.random())

random_number = random.random() * 100

print(int(random_number))

print(random_number)

print(round(random_number, 2))

print(round(random.random() * 100))

print(round(random.random() * 101))

# return array with all cards in a deck of cards (52 cards)
deck = "ace, two, three, four, five, six, seven, eight, nine, ten, jack, queen, king".split(", ")
deck = [card.replace("", "") for card in deck]
random.shuffle(deck)
print(deck)

# return string with all unix codes for keycaps
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
random.shuffle(numbers)

player_1 = random.sample(numbers, 5)
player_2 = random.sample(numbers, 5)

print(player_1)
print(player_2)

player_1_sum = sum(player_1)
player_2_sum = sum(player_2)

print(player_1_sum)
print(player_2_sum)

if player_1_sum > player_2_sum:
    print("Player 1 wins!")
elif player_1_sum < player_2_sum:
    print("Player 2 wins!")
else:
    print("It's a tie!")

