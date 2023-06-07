class Movie:
    def __init__(self, name, year, length):
        self.__name = name.title()
        self.year = year
        self.length = length
        self.__likes = 0

    #getter properties
    @property
    def name(self):
        return self.__name

    @property
    def likes(self):
        return self.__likes

    #setter properties
    @name.setter
    def name(self, name):
        if name is None or name == "":
            raise ValueError("Gotta have a name!")
        else:
            return self.__name

    @likes.setter
    def likes(self, amount):
        if amount is None or amount == "":
            raise ValueError("Give us an actual amount")
        elif amount < 0:
            raise ValueError("There are no negative likes")
        else:
            return self.__likes

    #instance methods
    def add_like(self, occurrences):
        self.__likes += occurrences

class Series:
    def __init__(self, name, year, seasons):
        self.__name = name.title()
        self.year = year
        self.seasons = seasons
        self.__likes = 0

    #getter properties
    @property
    def name(self):
        return self.__name

    @property
    def likes(self):
        return self.__likes

    #setter properties
    @name.setter
    def name(self, name):
        if name is None or name == "":
            raise ValueError("Gotta have a name!")
        else:
            return self.__name

    @likes.setter
    def likes(self, amount):
        if amount is None or amount == "":
            raise ValueError("Give us an actual amount")
        elif amount < 0:
            raise ValueError("There are no negative likes")
        else:
            return self.__likes

    #instance methods
    def add_like(self, occurrences):
        self.__likes += occurrences

avengers = Movie("Avengers", 2009, 160)
avengers.add_like(3)
print(f"{avengers.name} is a movie from {avengers.year} with a {avengers.length}-minute runtime. Likes: {avengers.likes}", "\n")

sopranos = Series("Sopranos", 1999, 6)
sopranos.add_like(2)
print(f"{sopranos.name} started in {sopranos.year} and ran for {sopranos.seasons} seasons. Likes: {sopranos.likes}", "\n")