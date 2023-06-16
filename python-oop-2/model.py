from abc import ABC, abstractmethod, abstractproperty


class SmallNumberFormatter:
    WORDS = {
        number: word
        for number, word in enumerate(
            'zero one two three four five six seven eight nine ten'.split(), 0)
    }

    @staticmethod
    def format_small_numbers(number):
        return SmallNumberFormatter.WORDS.get(number, str(number))


class Likeable:

    def __init__(self):
        self._likes = 0

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

    def add_like(self, occurrences):
        if occurrences < 0:
            raise ValueError("Can't decrement likes.")
        self.likes += occurrences

    def _add_trashcan_icon(self):
        return f" - \U0001F5D1" if self.likes == 0 else ""


class Identifiable:
    _id_tracker = 0

    def __init__(self):
        self._id = self.new_id()

    @property
    def id(self):
        return self._id

    @classmethod
    def new_id(cls):
        cls._id_tracker += 1
        return cls._id_tracker


class Watchable(Likeable, Identifiable):

    def __init__(self, name, year):
        Likeable.__init__(self)
        self._name = name.title()
        self.year = year

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
    def type(self):
        return self.__class__.__name__

    @abstractmethod
    def play(self):
        print("Implement this method in a subclass.")
        raise NotImplementedError("Subclass must implement abstract method")

    @property
    @abstractmethod
    def description(self):
        print("Implement this method in a subclass.")
        raise NotImplementedError("Subclass must implement abstract method")


class ReleasedItem:

    def __init__(self, release_country, network):
        self.release_country = release_country
        self.network = network


class Movie(Watchable, ReleasedItem):

    def __init__(self, name, year, length, release_country, network=None):
        Watchable.__init__(self, name, year)
        ReleasedItem.__init__(self, release_country, network)
        Identifiable.__init__(self)
        self.length = length

    def __str__(self):
        trash = self._add_trashcan_icon()
        return f"{self.name} ({self.year}) - {self.length} min - {self.likes} likes{trash}"

    def play(self):
        print(f"Playing movie: {self.name} ({self.year})")

    @property
    def description(self):
        return f"This movie is called {self.name} and it's {self.length} minutes long."


class Series(Watchable, ReleasedItem):

    def __init__(self, name, year, seasons, release_country, network):
        Watchable.__init__(self, name, year)
        ReleasedItem.__init__(self, release_country, network)
        Identifiable.__init__(self)
        self.seasons = seasons

    def __str__(self):
        formatted_seasons = SmallNumberFormatter.format_small_numbers(
            self.seasons)
        trash = self._add_trashcan_icon()
        return f"{self.name} ({self.year}) - {formatted_seasons} seasons - {self.likes} likes{trash}"

    def play(self):
        print(f"Playing series: {self.name} ({self.year})")

    @property
    def description(self):
        return f"This series is called {self.name} and it ran for {SmallNumberFormatter.format_small_numbers(self.seasons)} seasons."


class Playlist:

    def __init__(self, name, items):
        self.name = name
        self.items = items

    def __str__(self):
        formatted_size = SmallNumberFormatter.format_small_numbers(
            len(self.items) if len(self.items) >= 10 else len(self.items))
        playlist_str = f"Here's your {self.name} playlist with {formatted_size} items total:\n\n"
        for index, item in enumerate(self.items):
            network_str = f", {item.network}" if isinstance(item,
                                                            Series) else ""
            playlist_str += f"{index + 1}) {item} ({item.type.lower()} id: {item.id}, {item.release_country}{network_str})\n"
        return playlist_str

    def __getitem__(self, item):
        return self.items[item]

    def __contains__(self, item):
        return item in self.items

    def __len__(self):
        return len(self.items)

    def average_likes(self):
        return sum(item.likes for item in self.items) / len(self.items) if len(
            self.items) > 0 else 0

    def total_movie_runtime(self):
        return sum(item.length for item in self.items
                   if isinstance(item, Movie))

    def get_non_american(self):
        non_american_items = [
            item for item in self.items if item.release_country != "USA"
        ]
        return Playlist(f"{self.name} (International)", non_american_items)

    def get_oldies(self):
        oldies_items = [item for item in self.items if item.year < 1990]
        return Playlist(f"{self.name} (Oldies)", oldies_items)
