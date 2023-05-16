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
