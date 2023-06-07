class Movie:
    def __init__(self, name, year, length):
        self.name = name.title()
        self.year = year
        self.length = length
        self.likes = 0

    def add_like(self):
        self.likes += 1

class Series:
    def __init__(self, name, year, seasons):
        self.name = name.title()
        self.year = year
        self.seasons = seasons
        self.likes = 0

    def add_like(self):
        self.likes += 1

avengers = Movie("Avengers", 2009, 160)
for _ in range(3):
    avengers.add_like()
print(f"{avengers.name} is a movie from {avengers.year} with a {avengers.length}-minute runtime. Likes: {avengers.likes}", "\n")

sopranos = Series("Sopranos", 1999, 6)
for _ in range(2):
    sopranos.add_like()
print(f"{sopranos.name} started in {sopranos.year} and ran for {sopranos.seasons} seasons. Likes: {sopranos.likes}", "\n")
