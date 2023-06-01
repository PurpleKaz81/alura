from client import Client


class Account:
    accounts = {}

    # initialization
    def __init__(self, number, holder: Client, balance, limit=1000):
        self.__number = number
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit
        # Account.accounts.append(self) # list
        Account.accounts[number] = self  # dictionary

    # dunder methods
    def __str__(self):
        return f"Account: {self.__number}, Holder: {self.__holder}, Balance: {self.__balance}, Limit: {self.__limit}"

    # getter properties
    @property
    def number(self):
        return self.__number

    @property
    def holder(self):
        return self.__holder

    @property
    def balance(self):
        return self.__balance

    @property
    def limit(self):
        return self.__limit

    # setter properties
    @limit.setter
    def limit(self, value):
        if value < 0:
            raise ValueError("You can't have a negative limit.")
        else:
            self.__limit = value

    # utility functions
    @staticmethod
    def format_value(value, account_number=None):
        if account_number is not None and account_number == value:
            return str(value)

        if isinstance(value, float) or not isinstance(value, str):
            return "US${:,.2f}".format(value)
        else:
            return value

    # instance methods
    def client_info(self):
        result = "Here's the client's information:\n"
        account_info = {
            "number": self.number,
            "holder": self.holder,
            "balance": self.format_value(self.balance),
            "limit": self.format_value(self.limit)
        }
        for index, (key, value) in enumerate(account_info.items(), start=1):
            result += f"{index}) {key}: {value}\n"
        return result

    def print_client_info(self):
        print(self.client_info())

    def deposit(self, value):
        if value > 0:
            self.__balance += value
        else:
            print("You must deposit a positive value.")

    def withdraw(self, value):
        if value < 0:
            raise ValueError("You wanna give us money?!")
        return

        if value > (self.__balance + self.__limit):
            raise ValueError("Not gonna happen.")
        return

        self.__balance -= value

    def transfer(self, value, origin, destination):
        if origin == destination or origin.balance < value or value <= 0:
            print("Invalid transfer", "\n")
            return

        try:
            origin.withdraw(value)
            destination.deposit(value)
        except Exception as e:
            print("Transfer error: ", e)

    def is_delinquent(self):
        return self.balance < 0

    def what_to_do_with_client(self):
        if self.balance > 0:
            print(f"{self.holder}'s in good standing.")
        if self.balance < -abs(self.limit):
            print("Looks like we're gonna have to throw him in a dungeon.")
        elif abs(self.balance) == -abs(self.limit):
            print("Living dangerously, are we?")
        else:
            print("Let him go... for now...")

    # class methods
    @classmethod
    def print_client_list(cls):
        print("Here's a list of all our clients:\n")
        for index, account in enumerate(cls.accounts.values(), start=1):
            print(f"{index}) {account.holder}")
        print()

    @classmethod
    def print_delinquent_list(cls):
        print("Here's a list of all our delinquent clients:\n")
        for index, account in enumerate(cls.accounts.values(), start=1):
            if account.is_delinquent():
                print(f"{index}) {account.holder}")
                print()
                account.what_to_do_with_client()
                print()

    @classmethod
    def print_client_names(cls):
        accounts_list = list(cls.accounts.values())
        if len(accounts_list) > 2:
            first_two_names = ", ".join(account.holder.full_name
                                        for account in accounts_list[:2])
            last_name = accounts_list[-1].holder.full_name
            print(f"{first_two_names}, and {last_name}")
        elif len(accounts_list) == 2:
            print(f"{accounts_list[0].holder.full_name} and {accounts_list[1].holder.full_name}")
        elif accounts_list:
            print(accounts_list[0].holder.full_name)
        else:
            print("No account holders")

    @classmethod
    def total_balance(cls):
        total_balance = sum(account.balance
                            for account in cls.accounts.values())
        return cls.format_value(total_balance)

    @classmethod
    def total_limit(cls):
        total_limit = sum(account.limit for account in cls.accounts.values())
        return cls.format_value(total_limit)
