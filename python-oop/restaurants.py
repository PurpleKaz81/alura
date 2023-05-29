class Restaurant:

    def __init__(self, name, cuisine_type, price_range, total_seats, open_time,
                 close_time, address, rating, delivery_service, menu):
        self.name = name
        self.cuisine_type = cuisine_type
        self.price_range = price_range
        self.total_seats = total_seats
        self.open_time = open_time
        self.close_time = close_time
        self.address = address
        self.rating = rating
        self.delivery_service = delivery_service
        self.menu = menu

    def _parse_open_close_time(self):  # sourcery skip: raise-specific-error
        try:
            open_time = int(self.open_time[:-2]) % 12
            close_time = int(self.close_time[:-2]) % 12

            if self.open_time[-2:] == "PM":
                open_time += 12
            if self.close_time[-2:] == "PM":
                close_time += 12

            # Handling closing time after midnight
            if close_time <= open_time:
                close_time += 24

            return open_time, close_time
        except ValueError as e:
            raise Exception("Invalid time format") from e

    def hours_a_day_open(self):
        try:
            open_time, close_time = self._parse_open_close_time()
            total_hours_open = close_time - open_time

            if total_hours_open == 24:
                return f"{self.name} is open 24 hours"
            else:
                return f"{self.name} is open from {self.open_time} to {self.close_time}. That's {total_hours_open} hours a day!"
        except Exception as e:
            return str(e)


def do_deliver(restaurants):
    result = [
        restaurant.name for restaurant in restaurants
        if restaurant.delivery_service == True
    ]
    if len(result) > 2:
        main_names = ", ".join(result[:-1])
        last_name = result[-1]
        return f"{main_names}, and {last_name}"
    elif len(result) == 2:
        return f"{result[0]} and {result[1]}"
    elif len(result) == 1:
        return f"{result[0]}"
    else:
        return "Guess no one delivers, huh?"
    return "\n".join(result)


def average_rating(restaurants):
    return sum(restaurant.rating
               for restaurant in restaurants) / len(restaurants or 1)


def mean_rating(restaurants):
    ratings = [restaurant.rating for restaurant in restaurants]
    min_rating = min(ratings)
    max_rating = max(ratings)
    filtered_restaurants = [
        restaurant for restaurant in restaurants
        if restaurant.rating not in [max(ratings), min(ratings)]
    ]
    return average_rating(filtered_restaurants)


def cheapest(restaurants):
    prices = [restaurant.price_range for restaurant in restaurants]
    min_price = min(prices)
    cheapest = [
        restaurant.name for restaurant in restaurants
        if restaurant.price_range == min_price
    ]
    if len(cheapest) > 2:
        main_names = ", ".join(cheapest[:-1])
        last_name = cheapest[-1]
        return f"The cheapest restaurants are {main_names}, and {last_name}."
    elif len(cheapest) == 2:
        return f"The cheapest restaurants are {cheapest[0]} and {cheapest[1]}."
    elif len(cheapest) == 1:
        return f"The cheapest restaurant is {cheapest[0]}."
    else:
        return "There are no cheap restaurants left in this world."



restaurant1 = Restaurant("Crustacean", "Vietnamese", "$$$", 50, "5PM", "10PM",
                         "123 Main St", 4.5, True, ["Shrimp", "Noodle Soup"])

restaurant2 = Restaurant("Green Lotus", "Thai", "$$", 40, "11AM", "11PM",
                         "456 High St", 4.5, True,
                         ["Pad Thai", "Tom Yum Soup"])

restaurant3 = Restaurant("Sunset", "Indian", "$", 60, "11AM", "11PM",
                         "789 Broadway", 4.8, True,
                         ["Biryani", "Butter Chicken"])

restaurant4 = Restaurant("Italian Star", "Italian", "$$$", 30, "5PM", "11PM",
                         "321 Geo St", 4.3, False, ["Pasta", "Pizza"])

restaurant5 = Restaurant("Samurai House", "Japanese", "$$$", 100, "5PM",
                         "10PM", "654 Call Rd", 4.9, True, ["Sushi", "Ramen"])

restaurant6 = Restaurant("Pepito's", "Mexican", "$", 50, "11AM", "10PM",
                         "987 Park St", 4.1, True, ["Tacos", "Burritos"])

restaurant7 = Restaurant("La Gourmandise", "French", "$$$$", 20, "6PM", "12AM",
                         "951 Aria Rd", 4.7, False, ["Foie Gras", "Croissant"])

restaurant8 = Restaurant("Athenian", "Greek", "$$", 75, "11AM", "11PM",
                         "521 Metro St", 4.4, True, ["Gyros", "Moussaka"])

restaurant9 = Restaurant("Viking", "Scandinavian", "$$$$", 10, "6PM", "1AM",
                         "846 Fjord St", 4.6, False,
                         ["Gravlax", "Swedish Meatballs"])

restaurant10 = Restaurant("Herbs & Spice", "Vegetarian", "$$", 80, "11AM",
                          "11PM", "213 Main St", 4.2, True,
                          ["Salad", "Veggie Burger"])

restaurant11 = Restaurant("Burger Palace", "American", "$$", 50, "11AM",
                          "11AM", "123 Main St", 2.5, True,
                          ["Burger", "Fries"])

restaurants = [
    restaurant1, restaurant2, restaurant3, restaurant4, restaurant5,
    restaurant6, restaurant7, restaurant8, restaurant9, restaurant10, restaurant11
]

print(do_deliver(restaurants))
print()
print(restaurant11.hours_a_day_open())
print()
print(
    f"The average rating for the restaurants on the list was {average_rating(restaurants):.2f}. It woulda been better, but {restaurant11.name}'s a real piece of shit'."
)
print()
print(f"The mean rating is {mean_rating(restaurants):.2f}.")
print()
print(cheapest(restaurants))
