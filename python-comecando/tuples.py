# days of the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

friday_index = days.index("Friday")
days.insert(friday_index, "A Celebration of Rebecca Black's Life and Work")
days.remove("Friday")
days[-2:] = [", and ".join(days[-2:])]

print(f"The days of the week are {', '.join(days)}.")

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

# This won't work
# days.append("Celebration of Rebecca Black's Life and Work")

print(f"The week still has {len(days)} days: {', '.join(days)}.")

# turn a tuple into a list
days = list(days)

friday_index = days.index("Friday")
days.insert(friday_index, "Squiggles")
days.remove("Friday")
days[-2:] = [", and ".join(days[-2:])]

print(f"The days of the week are {', '.join(days)}.")

# three points on a graph to graph a right triangle
point1 = (0, 0)
point2 = (3, 0)
point3 = (0, 4)
triangle = [point1, point2, point3]

# command to draw this triangle in terminal with print(), lines included
print("\n".join(["".join(["*" if (x, y) in triangle else " " for x in range(4)]) for y in range(5)]))

employee1 = ("Rafael", 41)
employee2 = ("Anne", 28)
employee3 = ("Jen", 32)

employees = [employee1, employee2, employee3]
print(employees)
print(f"{employees[0][0]} is {employees[0][1]} years old, {employees[0][1] - employees[1][1]} years older than {employees[1][0]}, who is {employees[1][1]}.")

total_age = sum(employee[1] for employee in employees)
print(f"The employees' total age is {total_age}.")

employee4 = ("Satan", 666)
employees_copy = employees.copy()

employees_copy.append(employee4)

print(f"These four employees will work here forever: {', '.join(employee[0] for employee in employees_copy[:-1])}, and {employees_copy[-1][0]}.")

employees_copy_tuple = tuple(employees_copy)

print(tuple(employees_copy_tuple))
