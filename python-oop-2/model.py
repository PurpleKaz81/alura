class Watchable:

    def __init__(self, name, year):
        self.__name = name.title()
        self.year = year
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


class Movie(Watchable):

    def __init__(self, name, year, length):
        super().__init__(name, year)
        self.length = length


class Series(Watchable):

    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    #static methods
    @staticmethod
    def format_small_numbers(number):
        numbers_to_words = {
            1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine',
            10: 'ten'
        }
        return numbers_to_words.get(number, number)


avengers = Movie("Avengers", 2009, 160)
avengers.add_like(3)
avengers.name = "the AveNgers"
print(
    f"{avengers.name} is a movie from {avengers.year} with a {avengers.length}-minute runtime. Likes: {avengers.likes}",
    "\n")

sopranos = Series("Sopranos", 1999, 6)
sopranos.add_like(2)
print(
    f"{sopranos.name} started in {sopranos.year} and ran for {Series.format_small_numbers(sopranos.seasons)} seasons. Likes: {sopranos.likes}",
    "\n")
