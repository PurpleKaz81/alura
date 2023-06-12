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
    def name(self, new_name):
        if new_name is None or new_name == "":
            raise ValueError("Gotta have a name!")
        else:
            self.__name = new_name.title()

    @likes.setter
    def likes(self, new_amount):
        if not isinstance(new_amount, int):
            raise TypeError("Amount of likes needs to be an integer.")
        elif new_amount < 0:
            raise ValueError("There are no negative likes.")
        else:
            self.__likes = new_amount

    #instance methods
    def add_like(self, occurrences):
        if occurrences < 0:
            raise ValueError("Can't decrement likes.")
        new_likes = self.__likes + occurrences
        self.likes = new_likes

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
    def name(self, new_name):
        if new_name is None or new_name == "":
            raise ValueError("Gotta have a name!")
        else:
            self.__name = new_name.title()

    @likes.setter
    def likes(self, new_amount):
        if not isinstance(new_amount, int):
            raise TypeError("Amount of likes needs to be an integer.")
        elif new_amount < 0:
            raise ValueError("There are no negative likes.")
        else:
            self.__likes = new_amount

    #instance methods
    def add_like(self, occurrences):
        if occurrences < 0:
            raise ValueError("Can't decrement likes.")
        new_likes = self.__likes + occurrences
        self.likes = new_likes

avengers = Movie("Avengers", 2009, 160)
avengers.add_like(3)
avengers.name = "the AveNgers"
print(f"{avengers.name} is a movie from {avengers.year} with a {avengers.length}-minute runtime. Likes: {avengers.likes}", "\n")

sopranos = Series("Sopranos", 1999, 6)
sopranos.add_like(2)
print(f"{sopranos.name} started in {sopranos.year} and ran for {sopranos.seasons} seasons. Likes: {sopranos.likes}", "\n")
