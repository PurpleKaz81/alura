#  create a person class
# create a person object
# give each person a first and last name, height, weight, favorite movie, and favorite sexual position


class Person:

    def __init__(self, first_name, last_name, height, weight, favorite_movie,
                 favorite_sexual_position) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.height = height
        self.weight = weight
        self.favorite_movie = favorite_movie
        self.favorite_sexual_position = favorite_sexual_position

    def print_info(self):
        # return each attribute of the person object
        return f"First Name: {self.first_name}\nLast Name: {self.last_name}\nHeight: {self.height}\nWeight: {self.weight}\nFavorite Movie: {self.favorite_movie}\nFavorite Sexual Position: {self.favorite_sexual_position}"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


def guest_list(persons):
    guests = [person.full_name() for person in persons]
    if len(guests) > 2:
        main_names = ", ".join(guests[:-1])
        last_name = guests[-1]
        return f"{main_names}, and {last_name}"
    elif len(guests) == 2:
        return f"{guests[0]} and {guests[1]}"
    elif guests:
        return guests[0]
    else:
        return "No guests tonight"


def total_weight(persons):
    return sum(int(person.weight) for person in persons)


# function to see which movie has greater frequency between guests
def favorite_movie(persons):
    movies = [person.favorite_movie for person in persons]
    movie_count = {}
    for movie in movies:
        if movie in movie_count:
            movie_count[movie] += 1
        else:
            movie_count[movie] = 1
    return max(movie_count, key=movie_count.get)


def hair_color_frequency(persons):
    hairs = [person.hair_color for person in persons]
    hair_count = {}
    for hair in hairs:
        if hair in hair_count:
            hair_count[hair] += 1
        else:
            hair_count[hair] = 1
    return max(hair_count, key=hair_count.get)


def total_weight(persons):
    return sum(int(person.weight) for person in persons)


def weight_average(persons):
    average_weight = int(total_weight(persons) / len(persons))
    return f"The guests together weigh {total_weight(persons)} pounds and average {average_weight}."


# create persons 1-5
person1 = Person("John", "Silva", "6'2", "180", "The Godfather", "Missionary")
person2 = Person("Jane", "dos Santos", "5'8", "120", "The Notebook", "Doggy")
person3 = Person("Jack", "Allyman", "5'10", "150", "The Godfather", "Cowgirl")
person4 = Person("Jill", "Silverstein", "5'5", "110", "The Notebook",
                 "Reverse Cowgirl")
person5 = Person("James", "Jameson", "6'0", "200", "The Godfather",
                 "Missionary")

# return all five persons, but include their hair color. Make sure one color is more frequent
# than the others
person1.hair_color = "brown"
person2.hair_color = "blonde"
person3.hair_color = "brown"
person4.hair_color = "brown"
person5.hair_color = "brown"

persons = [person1, person2, person3, person4, person5]

print(f"Guest list for the party tonight: {guest_list(persons)}.")
print()
print(f"Together, the guests weigh {total_weight(persons)} pounds.")
print()
print(f"The most popular movie among guests is {favorite_movie(persons)}.")
print()
print(f"Pretty much all the guests have {hair_color_frequency(persons)} hair.")
print()
print(weight_average(persons))
