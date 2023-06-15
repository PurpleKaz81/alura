from model import Movie, Series, Playlist

products = {
    "movie_1": Movie("Avengers", 2009, 160, "USA"),
    "series_1": Series("Sopranos", 1999, 6, "USA", "HBO"),
    "movie_2": Movie("Sentinelle", 1992, 139, "France"),
    "movie_3": Movie("Scream", 1996, 111, "USA"),
    "series_2": Series("Dynasty", 1991, 8, "USA", "ABC"),
}

products["movie_1"].add_like(3)
products["movie_1"].name = "the AveNgers"
products["series_1"].add_like(2)
products["movie_2"].add_like(0)
products["movie_2"].name = "la sentinelLe"
products["movie_3"].add_like(9)
products["series_2"].add_like(4)

new_movies = [
    Movie("Carlota Joaquina", 1994, 120, "Brazil"),
    Movie("L'Empire des Sens", 1976, 108, "France"),
    Movie("Honey, I Shrunk the Kids", 1989, 93, "USA"),
]

new_movies[0].add_like(4)
new_movies[1].add_like(6)
new_movies[2].add_like(2)

items = list(products.values()) + new_movies
weekend = Playlist("Weekend", items)
