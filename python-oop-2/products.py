from model import Movie, Series, Playlist

products = {
    "movie_1": Movie("Avengers", 2009, 160),
    "series_1": Series("Sopranos", 1999, 6),
    "movie_2": Movie("Sentinelle", 1992, 139),
    "movie_3": Movie("Scream", 1996, 111),
    "series_2": Series("The Wire", 2002, 5),
}

products["movie_1"].add_like(3)
products["movie_1"].name = "the AveNgers"
products["series_1"].add_like(2)
products["movie_2"].add_like(0)
products["movie_2"].name = "la sentinelLe"
products["movie_3"].add_like(9)
products["series_2"].add_like(4)

new_movies = [
    Movie("The Godfather", 1972, 175),
    Movie("The Dark Knight", 2008, 152),
    Movie("Honey, I Shrunk the Kids", 1989, 93),
]

new_movies[0].add_like(5)
new_movies[1].add_like(7)
new_movies[2].add_like(2)

items = list(products.values()) + new_movies
weekend = Playlist("Weekend", items)
