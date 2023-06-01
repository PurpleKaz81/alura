class Client:

    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    # getter properties
    @property
    def first_name(self):
        return self.__first_name.title()

    @property
    def last_name(self):
        return self.__last_name.title()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
