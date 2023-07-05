import random

ages = [12, 34, 56, 78, 90, 23, 45, 67, 89, 10]
for index, age in enumerate(ages, start=1):
    print(f"{index}: {age}")
print()

new_ages = {12, 65, 34, 56, 78, 90, 23, 45, 67, 89}
new_ages_list = list(new_ages)
for index, age in enumerate(new_ages_list, start=1):
    print(f"{index}: {age}")

characters = [
    'Haruto Nakamura',
    'Yui Saito',
    'Ryota Suzuki',
    'Miyu Tanaka',
    'Kaito Watanabe',
    'Hina Yamamoto',
    'Sota Yoshida',
    'Mei Nakamura',
    'Kenta Sato',
    'Rina Takahashi',
    'Hiroshi Yamada',
    'Yuna Suzuki'
    'Kou Shibasaki',
    'Chiaki Kuriyama',
    'Takashi Tsukamoto',
    'Takeshi Kitano',
    'Tatsuya Fujiwara',
    'Aki Maeda',
    'Tarō Yamamoto',
    'Masanobu Andō',
]

print("\nWho will make it out alive?\n")
for index, character in enumerate(characters, start=1):
    print(f"{index}: {character}")

print()

users = [
    ("Rafael", 23, 2000),
    ("Marcelo", 18, 2005),
    ("João", 19, 2002),
]

for user in users:
    print(
        f"{user[0]}, born in {user[2]}, is {user[1]} years old. {random.choice(characters)}'s his pen-pal."
    )
    print()

print(', '.join(user[0] for user in users))
print()

for name, age, year in users:
    print(f"{name}, {age}")
