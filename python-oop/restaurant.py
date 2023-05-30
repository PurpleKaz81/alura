from collections import Counter


class Restaurant:
    _instances = []

    def __init__(self, name, cuisine_type, price_range, total_seats, open_time,
                 close_time, address, rating, delivery_service, menu, chef):
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
        self.chef = chef

        self._instances.append(self)

    def _parse_open_close_time(self):  # sourcery skip: raise-specific-error
        try:
            open_time = int(self.open_time[:-2])
            close_time = int(self.close_time[:-2])

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

    @classmethod
    def do_deliver(cls):
        result = [
            restaurant.name for restaurant in cls._instances
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


def most_expensive(restaurants):
    prices = [restaurant.price_range for restaurant in restaurants]
    max_price = max(prices)
    most_expensive = [
        restaurant.name for restaurant in restaurants
        if restaurant.price_range == max_price
    ]
    if len(most_expensive) > 2:
        main_names = ", ".join(most_expensive[:-1])
        last_name = most_expensive[-1]
        return f"The most expensive restaurants are {main_names}, and {last_name}."
    elif len(most_expensive) == 2:
        return f"The most expensive restaurants are {most_expensive[0]} and {most_expensive[1]}."
    elif len(most_expensive) == 1:
        return f"The most expensive restaurant is {most_expensive[0]}."
    else:
        return "Everything's mysteriously cheap now."


def intimacy(restaurants):
    restaurants_sorted = sorted(restaurants, key=lambda x: x.total_seats)
    least_seating = [restaurant.name for restaurant in restaurants_sorted[:3]]
    most_seating = [restaurant.name for restaurant in restaurants_sorted[-3:]]

    if len(least_seating) > 1:
        least_seating_str = ', '.join(
            least_seating[:-1]) + ', and ' + least_seating[-1]
    else:
        least_seating_str = least_seating[0]

    if len(most_seating) > 1:
        most_seating_str = ', '.join(
            most_seating[:-1]) + ', and ' + most_seating[-1]
    else:
        most_seating_str = most_seating[0]

    return f"{least_seating_str} are the restaurants with the most intimate setting. {most_seating_str} are great for family events, however, since they seat more people."


def most_popular_cuisine_type(restaurants):
    cuisine_types = [restaurant.cuisine_type for restaurant in restaurants]
    cuisine_type_count = {}
    for cuisine_type in cuisine_types:
        if cuisine_type in cuisine_type_count:
            cuisine_type_count[cuisine_type] += 1
        else:
            cuisine_type_count[cuisine_type] = 1
    return max(cuisine_type_count, key=cuisine_type_count.get)


def least_popular_cuisine_type(restaurants):
    cuisine_types = [restaurant.cuisine_type for restaurant in restaurants]
    cuisine_type_count = {}
    for cuisine_type in cuisine_types:
        if cuisine_type in cuisine_type_count:
            cuisine_type_count[cuisine_type] += 1
        else:
            cuisine_type_count[cuisine_type] = 1
    return min(cuisine_type_count, key=cuisine_type_count.get)


def most_popular_menu_item(restaurants):
    menu_items = [
        item for restaurant in restaurants for item in restaurant.menu
    ]
    menu_items_count = Counter(menu_items)
    return menu_items_count.most_common(1)[0][0].lower()


restaurant1 = Restaurant(
    "Crustacean", "Vietnamese", "$$$", 50, "5PM", "10PM", "123 Main St", 4.5,
    True, ["Shrimp", "Noodle Soup"],
    ["Chef Nguyen", "Nguyen Van A", "5'6", "Culinary Institute of America"])

restaurant2 = Restaurant(
    "Green Lotus", "Thai", "$", 40, "11AM", "11PM", "456 High St", 4.5, True,
    ["Pad Thai", "Tom Yum Soup"],
    ["Chef Somsak", "Somsak Boonkam", "5'7", "Le Cordon Bleu"])

restaurant3 = Restaurant(
    "Sunset", "Indian", "$", 60, "11AM", "11PM", "789 Broadway", 4.8, True,
    ["Biryani", "Butter Chicken"], [
        "Chef Sharma", "Ramesh Sharma", "6'0",
        "Institute of Hotel Management, Catering & Nutrition, Pusa"
    ])

restaurant4 = Restaurant(
    "Italian Star", "Italian", "$$$", 30, "5PM", "11PM", "321 Geo St", 4.3,
    False, ["Pasta", "Pizza"],
    ["Chef Martini", "Gianluca Martini", "5'8", "ALMA Scuola di Cucina"])

restaurant5 = Restaurant(
    "Samurai House", "Japanese", "$$$$$", 100, "5PM", "10PM", "654 Call Rd",
    4.9, True, ["Sushi", "Ramen"],
    ["Chef Yamada", "Yamada Taro", "5'5", "Tsukiji Cooking School"])

restaurant6 = Restaurant("Pepito's", "Mexican", "$", 50, "11AM", "10PM",
                         "987 Park St", 4.1, True, ["Tacos", "Burritos"], [
                             "Chef Gonzalez", "Jose Gonzalez", "5'8",
                             "Escuela de Gastronomía Mexicana"
                         ])

restaurant7 = Restaurant(
    "La Gourmandise", "French", "$$$$", 20, "6PM", "12AM", "951 Aria Rd", 4.7,
    False, ["Foie Gras", "Croissant"],
    ["Chef Lefevre", "Jean Lefevre", "6'1", "École Grégoire-Ferrandi"])

restaurant8 = Restaurant(
    "Athenian", "Greek", "$$", 75, "11AM", "11PM", "521 Metro St", 4.4, True,
    ["Gyros", "Moussaka"],
    ["Chef Papadopoulos", "George Papadopoulos", "5'10", "Le Monde Institute"])

restaurant9 = Restaurant(
    "Viking", "Scandinavian", "$$$$", 10, "6PM", "1AM", "846 Fjord St", 4.6,
    False, ["Gravlax", "Swedish Meatballs"],
    ["Chef Thomsen", "Ottis Thomsen", "6'2", "Oslo Culinary Academy"])

restaurant10 = Restaurant(
    "Herbs & Spice", "Vegetarian", "$$", 80, "11AM", "11PM", "213 Main St",
    4.2, True, ["Salad", "Veggie Burger"],
    ["Chef Green", "Emma Green", "5'9", "Natural Gourmet Institute"])

restaurant11 = Restaurant(
    "Burger Palace", "American", "$$$$", 50, "11AM", "11AM", "123 Main St",
    2.5, True, ["Burger", "Fries"],
    ["Chef Johnson", "John Johnson", "5'11", "Culinary Institute of America"])

restaurant12 = Restaurant(
    "Veggie Grill", "Vegetarian", "$$", 50, "11AM", "11PM", "123 Main St", 4.5,
    True, ["Burger", "Fries"],
    ["Chef Patel", "Anita Patel", "5'5", "Natural Gourmet Institute"])

restaurant13 = Restaurant(
    "Veggie Heaven", "Vegetarian", "$$$$$", 50, "11AM", "11PM", "123 Main St",
    4.5, True, ["Burger", "Fries"],
    ["Chef Kim", "Min-Jae Kim", "5'7", "Natural Gourmet Institute"])

restaurant14 = Restaurant(
    "Veggie House", "Vegetarian", "$$$", 50, "11AM", "11PM", "123 Main St",
    4.5, True, ["Burger", "Fries"],
    ["Chef Brown", "Oliver Brown", "6'1", "Natural Gourmet Institute"])

restaurant15 = Restaurant(
    "Burger King", "American", "$$", 50, "11AM", "11PM", "123 Main St", 4.5,
    True, ["Burger", "Fries"],
    ["Chef Smith", "William Smith", "5'10", "Culinary Institute of America"])

restaurants = [
    restaurant1, restaurant2, restaurant3, restaurant4, restaurant5,
    restaurant6, restaurant7, restaurant8, restaurant9, restaurant10,
    restaurant11, restaurant12, restaurant13, restaurant14, restaurant15
]

print(Restaurant.do_deliver())
print()
print(restaurant7.hours_a_day_open())
print()
print(
    f"The average rating for the restaurants on the list was {average_rating(restaurants):.2f}. It could have been better, but {restaurant11.name}'s a real piece of shit."
)
print()
print(f"The mean rating is {mean_rating(restaurants):.2f}.")
print()
print(cheapest(restaurants))
print()
print(most_expensive(restaurants))
print()
print(intimacy(restaurants))
print()
print(
    f"The most popular cuisine type is {most_popular_cuisine_type(restaurants)}."
)
print()
print(
    f"The least popular type of cuisine is {least_popular_cuisine_type(restaurants)}."
)
print()
print(
    f"The most popular menu items among the restaurants is {most_popular_menu_item(restaurants)}."
)
