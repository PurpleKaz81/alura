# dictionary with ten names and their ages
people = {
    "Rafael": 41,
    "Anne": 28,
    "Jen": 32,
    "Satan": 2000000,
    "Frank": 12,
    "Sally": 19,
    "Bob": 42,
    "Sue": 21,
    "Jill": 32,
    "Jack": 32,
}

names = sorted(people.keys())
ages = sum(people.values())

if len(names) > 2:
    names[-1] = f"and {names[-1]}"

# print list of all names with no ages
print(f"These are the people on the trip: {', '.join(names)}. Their age is approximately {ages:.2e} years put together.")
