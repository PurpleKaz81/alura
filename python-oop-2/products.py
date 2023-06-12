from model import Movie, Series

products = {
    "movie_1": Movie("Avengers", 2009, 160),
    "series_1": Series("Sopranos", 1999, 6),
    "movie_2": Movie("Sentinelle", 1992, 139)
}

products["movie_1"].add_like(3)
products["movie_1"].name = "the AveNgers"
products["series_1"].add_like(2)
products["movie_2"].add_like(0)
products["movie_2"].name = "la sentinelLe"
