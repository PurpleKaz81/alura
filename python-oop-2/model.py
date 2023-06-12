class Watchable:
    #class variable for tracking id's
    _id_tracker = 0

    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0
        self._id = self.new_id()

    #dunder methods
    def __str__(self):
        return f"{self.name} ({self.year})"

    # getters and setters
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not new_name:
            raise ValueError("Gotta have a name!")
        self._name = new_name.title()

    @property
    def likes(self):
        return self._likes

    @likes.setter
    def likes(self, new_amount):
        if not isinstance(new_amount, int):
            raise TypeError("Amount of likes needs to be an integer.")
        if new_amount < 0:
            raise ValueError("There are no negative likes.")
        self._likes = new_amount

    @property
    def id(self):
        return self._id

    #class methods
    @classmethod
    def new_id(cls):
        cls._id_tracker += 1
        return cls._id_tracker

    # instance methods
    def add_like(self, occurrences):
        if occurrences < 0:
            raise ValueError("Can't decrement likes.")
        self.likes += occurrences

    @property
    def type(self):
        return self.__class__.__name__

class Movie(Watchable):

    def __init__(self, name, year, length):
        super().__init__(name, year)
        self.length = length

    def print_info(self):
        trash = "- \U0001F5D1" if product.likes == 0 else ""
        return f"{self.name} ({self.year}) - {self.length} min - {self.likes} {trash}"


class Series(Watchable):

    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def print_info(self):
        formatted_seasons = SmallNumberFormatter.format_small_numbers(
            self.seasons)
        trash = "- \U0001F5D1" if product.likes == 0 else ""
        return f"{self.name} ({self.year}) - {formatted_seasons} seasons - {self.likes} {trash}"


class SmallNumberFormatter:
    #static methods
    WORDS = {
        number: word
        for number, word in enumerate(
            'zero one two three four five six seven eight nine ten'.split(), 0)
    }

    @staticmethod
    def format_small_numbers(number):
        return SmallNumberFormatter.WORDS.get(number, str(number))


avengers = Movie("Avengers", 2009, 160)
avengers.add_like(3)
avengers.name = "the AveNgers"

sopranos = Series("Sopranos", 1999, 6)
sopranos.add_like(2)

sentinelle = Movie("Sentinelle", 1992, 139)
sentinelle.add_like(0)
sentinelle.name = "la sentinelLe"

movies_and_series = [avengers, sopranos, sentinelle]
for index, product in enumerate(movies_and_series):
    print(f"{index + 1}) {product.print_info()} - ({product.type} id: {product.id})", "\n")
