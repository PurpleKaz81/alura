class Watchable:
    #class variable for tracking id's
    _id_tracker = 0

    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0
        self._id = self.new_id()

    #dunder methods
    def __str__(self, name, year):
        return f"{self.name} ({self.year})"

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

    def add_like(self, occurrences):
        if occurrences < 0:
            raise ValueError("Can't decrement likes.")
        self.likes += occurrences

    @property
    def id(self):
        return self._id

    #class methods
    @classmethod
    def new_id(cls):
        cls._id_tracker += 1
        return cls._id_tracker


class Movie(Watchable):

    def __init__(self, name, year, length):
        super().__init__(name, year)
        self.length = length


class Series(Watchable):

    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons


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
print(
    f"{avengers.name} (Movie ID: {avengers.id}) is a movie from {avengers.year} with a {avengers.length}-minute runtime. Likes: {avengers.likes}",
    "\n")

sopranos = Series("Sopranos", 1999, 6)
sopranos.add_like(2)
print(
    f"{sopranos.name} (Series ID: {sopranos.id}) started in {sopranos.year} and ran for {SmallNumberFormatter.format_small_numbers(sopranos.seasons)} seasons. Likes: {sopranos.likes}",
    "\n")

sentinelle = Movie("Sentinelle", 1992, 139)
sentinelle.add_like(0)
sentinelle.name = "la sentinelLe"
print(
    f"{sentinelle.name} (Movie ID: {sentinelle.id}) is a movie from {sentinelle.year} with a {sentinelle.length}-minute runtime. It has {sentinelle.likes} likes cuz it's trash.",
)

movies_and_series = [avengers, sopranos, sentinelle]
for index, product in enumerate(movies_and_series):
    print()
    details = f"{product.length} minutes" if isinstance(
        product, Movie
    ) else f"{SmallNumberFormatter.format_small_numbers(product.seasons)} seasons"
    trash = "- \U0001F5D1" if product.likes == 0 else ""
    print(
        f"{index + 1}) {product.name} - {details} - {product.year} - {product.likes} {trash}"
    )
