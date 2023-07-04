from math import sqrt
import random

ages = [random.randint(18, 45) for _ in range(3)]
print(ages)

ages.extend([27, 44, 33])
print(ages)

last_item = ages.pop()
print(last_item)

ages.insert(3, 31)
print(ages)

ages.append("po")
print(ages)

print()

for index, element in enumerate(ages):
    if isinstance(element, int):
        print(f"{index + 1}: {element}")

print()

double_ages = [element * 2 for element in ages if isinstance(element, int)]
for index, new_element in enumerate(double_ages):
    if isinstance(new_element, int):
        print(f"{index + 1}: {new_element}")

print()

numbers = list(range(1, 6))
doubled_numbers = [number * 2 for number in numbers]
square_rooted_numbers = [sqrt(number) for number in doubled_numbers]
rounded_numbers = [round(x, 5) for x in square_rooted_numbers]
formatted_rounded_numbers = [f"{x:.2f}" if x.is_integer() else f"{x:.2f}" for x in rounded_numbers]
for index, element in enumerate(formatted_rounded_numbers):
    print(f"{index + 1}: {element}")

print()

new_formatted_rounded_numbers = [
    (float(element) * 100) for element in formatted_rounded_numbers
]
for index, element in enumerate(new_formatted_rounded_numbers):
    print(f"{index + 1}: {element:.0f}")

print()

def get_factors(n):
    return ', '.join([str(x) for x in range(1, n + 1) if n % x == 0])

for index, element in enumerate(new_formatted_rounded_numbers):
    print(f"{index + 1}: {element:.2f}")
    element = int(element)
    print(f"Factors: {get_factors(element)}")

print()

ages_2 = [18, 76, 33]
def next_age(age):
    return age + 1
new_ages = [str(next_age(age)) for age in ages_2 if age > 70]
print(', '.join(new_ages))

def prints_ages(age_list = None):
    if age_list is None:
        age_list = []
    return len(age_list)

age_list = [12, 45, 67, 44]
print(prints_ages(age_list))

numbers_3 = [1, 20, 3, 3, 15, 11, 11, 19]
numbers_3 = list(set(numbers_3))
print(numbers_3)
