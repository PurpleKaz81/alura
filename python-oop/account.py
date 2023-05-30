from date import Date


class Account:
    accounts = []

    # initialization
    def __init__(self, number, holder, balance, limit=1000):
        self.__number = number
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit
        Account.accounts.append(self)

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
        if value > 0:
            self.__balance -= value
        else:
            print("The withdrawal amount must be a positive value.")

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
        for index, account in enumerate(cls.accounts, start=1):
            print(f"{index}) {account.holder}")
        print()

    @classmethod
    def print_delinquent_list(cls):
        print("Here's a list of all our delinquent clients:\n")
        for index, account in enumerate(cls.accounts, start=1):
            if account.is_delinquent():
                print(f"{index}) {account.holder}")
                print()
                account.what_to_do_with_client()
                print()

    @classmethod
    def print_client_names(cls):
        if len(cls.accounts) > 2:
            first_two_names = ", ".join(account.holder
                                        for account in cls.accounts[:2])
            last_name = cls.accounts[-1].holder
            print(f"{first_two_names}, and {last_name}")
        elif len(cls.accounts) == 2:
            print(f"{cls.accounts[0].holder} and {cls.accounts[1].holder}")
        elif cls.accounts:
            print(cls.accounts[0].holder)
        else:
            print("No account holders")

    @classmethod
    def total_balance(cls):
        total_balance = sum(account.balance for account in cls.accounts)
        return cls.format_value(total_balance)

    @classmethod
    def total_limit(cls):
        total_limit = sum(account.limit for account in cls.accounts)
        return cls.format_value(total_limit)


# creating accounts and adding to the list
account_1 = Account(123, "Nico", 1000)
account_2 = Account(321, "Marco", 100)
account_3 = Account(666, "Satan", 2679, 2000)

account_1.print_client_info()
account_2.print_client_info()
account_3.print_client_info()

# Printing the client list
Account.print_client_list()

print(
    f"The total balance and limit of their accounts are {Account.total_balance()} and {Account.total_limit()}, respectively.",
    "\n")

print(f"Account 1's balance is {account_1.format_value(account_1.balance)}",
      "\n")
print(f"Account 2's account number is {account_2.number}", "\n")
print(f"Account 1's limit is {account_1.format_value(account_1.limit)}", "\n")
print(
    f"{account_1.holder} would, of course, like to have {account_3.holder}'s limit of {account_3.format_value(account_3.limit)}",
    "\n")
account_1.withdraw(500000)
print(
    f"{account_1.holder} went to hospital in NYC to get an aspirin for a minor headache. He now has {account_1.format_value(account_1.balance)} in his account. He's proper fucked.",
    "\n")
account_3.deposit(1000000)

date_1 = Date(12, 5, 2023)
print(
    f"{account_3.holder} made {account_3.format_value(100000)} selling shit T-shirts on {date_1.formatted_date()}, cuz life's unfair, so he now has {account_3.format_value(account_3.balance)}.",
    "\n")
account_2.deposit(85.67)
print(
    f"{account_2.holder} now has a balance of {account_2.format_value(account_2.balance)}",
    "\n")
Account.print_client_names()
print()

account_1.print_client_info()
account_2.print_client_info()
account_3.print_client_info()

date_2 = Date(17, "08", 2017)
print(
    f"On {date_2.formatted_date()}, {account_3.holder} came to visit and never really went back home.",
    "\n")

transfer_value = 30000
transfer = account_1.transfer(transfer_value, account_3, account_1)
print(
    f"{account_1.holder} received a transfer of {account_3.format_value(transfer_value)} from {account_3.holder}, who now owns the title to {account_1.holder}'s soul.",
    "\n")
account_1.print_client_info()
account_3.print_client_info()

Account.print_delinquent_list()
