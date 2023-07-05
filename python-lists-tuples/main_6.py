# give me a list with 10 ages from 0 to 100
ages = [21, 34, 56, 78, 90, 23, 45, 67, 89, 10]
abs_value = lambda age: abs(age - 50)
sorted_ages = sorted(ages, key=abs_value, reverse=True)
print(sorted_ages)
print()

# give me a list with ten numbers from 1 to 100
numbers = [67, 89, 10, 21, 34, 56, 78, 90, 23, 45]
sorted_numbers = list(reversed(sorted(numbers)))
print(', '.join(str(number) for number in numbers))

# give me a list with 10 first names
first_names = [
    'Haruto',
    'Yui',
    'Ryota',
    'Miyu',
    'Kaito',
    'Hina',
    'Sota',
    'Mei',
    'Kenta',
    'Rina',
]
print()

first_names.sort(key=lambda name: name[:], reverse=True)
print(', '.join(first_names))
print()

for age, first_name in zip(ages, first_names):
    print(f"{first_name} is {age} years old.") if age < 85 else print(
        f"{first_name} is {age} years old. Death is knocking.")
    print()
