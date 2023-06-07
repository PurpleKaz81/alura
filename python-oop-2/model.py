class Movie:
    def __init__(self, name, year, length):
        self.name = name
        self.year = year
        self.length = length

class Series:
    def __init__(self, name, year, seasons):
        self.name = name
        self.year = year
        self.seasons = seasons

avengers = Movie("Avengers", 2009, 160)
print(avengers.name)

sopranos = Series("Sopranos", 1999, 6)
print(f"{sopranos.name} started in {sopranos.year} and ran for {sopranos.seasons} seasons.")
