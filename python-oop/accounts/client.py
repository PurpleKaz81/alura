class Client:

    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    # dunder methods
    def __str__(self):
        return f"{self.full_name}"

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

    # setter properties
    @first_name.setter
    def first_name(self, first_name):
        print("calling first_name setter")
        self.__first_name = first_name

    @last_name.setter
    def last_name(self, last_name):
        print("calling last_name setter")
        self.__last_name = last_name

    @full_name.setter
    def full_name(self, full_name):
        first_name, last_name = full_name.split(" ", 1)
        self.__first_name = first_name
        self.__last_name = last_name
