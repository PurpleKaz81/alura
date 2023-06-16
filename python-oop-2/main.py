from model import SmallNumberFormatter, Movie, Series
from products import products, new_movies, items, weekend

# print("Here's a list of all your products:", "\n")
# for index, product_key in enumerate(products):
#     product = products[product_key]
#     print(
#         f"{index + 1}) {product} ({product.type.lower()} id: {product.id})",
#         "\n")

# print("Here's a list of all your new movies:", "\n")
# for index, movie in enumerate(new_movies):
#     print(f"{index + 1}) {repr(movie)}", "\n")

# first_item = weekend[0]
# print(first_item)
# items_slice = weekend[2:4]
# for item in weekend:
#     if item.likes == 2 and "k" in item.name.lower():
#         print(item)

# if products["movie_3"] in weekend:
#     print("yes")

# print(f"Your collection has an average of {weekend.average_likes():.2f} likes.")
# print(f"Your total movie runtime is {weekend.total_movie_runtime()} minutes.")

# print(SmallNumberFormatter.format_small_numbers(len(weekend)).title())

# first_four_items = weekend[:4]
# for index, item in enumerate(first_four_items):
#     length_or_seasons = f"{item.length} min" if isinstance(item, Movie) else f"{SmallNumberFormatter.format_small_numbers(item.seasons)} seasons"
#     print(f"{index + 1} - {item.name}: {length_or_seasons}.")

# for item in weekend:
#     item.play() if item.year < 2000 and item.year > 1990 else ""
#     item.description if item.year < 2000 and item.year > 1990 else ""
#     print()

for item in weekend:
    item.play() if item.release_country == "France" else ""

print()
for item in weekend:
    item.play() if "USA" not in item.release_country else ""

print()
print(weekend.get_non_american())

print()
print(weekend.get_oldies())
