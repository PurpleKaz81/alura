class Watchable:
    _id_tracker = 0

    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0
        self._id = self.new_id()

    def __str__(self):
        return f"{self.name} ({self.year}) - {self.likes} likes"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, year={self.year}, likes={self.likes}, id={self.id})"

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

    @property
    def type(self):
        return self.__class__.__name__

    @classmethod
    def new_id(cls):
        cls._id_tracker += 1
        return cls._id_tracker

    def add_like(self, occurrences):
        if occurrences < 0:
            raise ValueError("Can't decrement likes.")
        self.likes += occurrences

    def _add_trashcan_icon(self):
        return f" - \U0001F5D1" if self.likes == 0 else ""


class Movie(Watchable):

    def __init__(self, name, year, length):
        super().__init__(name, year)
        self.length = length

    def __str__(self):
        trash = self._add_trashcan_icon()
        return f"{self.name} ({self.year}) - {self.length} min - {self.likes} likes {trash}"


class Series(Watchable):

    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        formatted_seasons = SmallNumberFormatter.format_small_numbers(
            self.seasons)
        trash = self._add_trashcan_icon()
        return f"{self.name} ({self.year}) - {formatted_seasons} seasons - {self.likes} likes {trash}"


class SmallNumberFormatter:
    WORDS = {
        number: word
        for number, word in enumerate(
            'zero one two three four five six seven eight nine ten'.split(), 0)
    }

    @staticmethod
    def format_small_numbers(number):
        return SmallNumberFormatter.WORDS.get(number, str(number))
