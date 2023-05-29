class Account:

    def __init__(self, number, holder, balance, limit=1000):
        # print(f"Building object... {self}")
        self.number = number
        self.holder = holder
        self.balance = balance
        self.limit = limit

    def format_value(self, value, account_number=None):
        if account_number is not None and account_number == value:
            return str(value)

        if isinstance(value, float) or not isinstance(value, str):
            return "US${:,.2f}".format(value)
        else:
            return value

    def __str__(self):
        return f"Account: {self.number}, Holder: {self.holder}, Balance: {self.balance}, Limit: {self.limit}"

    def client_info(self, account):
        result = "Here's the client's information:\n"
        for index, (key, value) in enumerate(account.items(), start=1):
            result += f"{index}) {key}: {self.format_value(value, account['number'])}\n"
        return result

    def print_client_info(self):
        print(self.client_info(vars(self)))

    @classmethod
    def print_client_list(cls, accounts):
        print("Here's a list of all our clients:\n")
        for index, account in enumerate(accounts, start=1):
            print(f"{index}) {account.holder}")
        print()

    @classmethod
    def print_client_names(cls, accounts):
        if len(accounts) > 2:
            first_two_names = ", ".join(account.holder for account in accounts[:2])
            last_name = accounts[-1].holder
            print(f"{first_two_names}, and {last_name}")
        elif len(accounts) == 2:
            print(f"{accounts[0].holder} and {accounts[1].holder}")
        elif accounts:
            print(accounts[0].holder)
        else:
            print("No account holders")

    def total_balance(self, accounts):
        total_balance = sum(account.balance for account in accounts)
        return self.format_value(total_balance)

    def total_limit(self, accounts):
        total_limit = sum(account.limit for account in accounts)
        return self.format_value(total_limit)

    def deposit(self, value):
        self.balance += value if value > 0 else print(
            "You must deposit a positive value.")

    def withdraw(self, value):
        self.balance -= value if value > 0 else print(
            "You must withdraw a negative value.")


account_1 = Account(123, "Nico", 1000)
account_2 = Account(321, "Marco", 100)
account_3 = Account(666, "Satan", 2679, 2000)

account_1.print_client_info()
account_2.print_client_info()
account_3.print_client_info()

accounts = [account_1, account_2, account_3]
Account.print_client_list(accounts)

print(
    f"The total balance and limit of their accounts are {accounts[0].total_balance(accounts)} and {accounts[0].total_limit(accounts)}, respectively."
)

print()
print(f"Account 1's balance is {account_1.format_value(account_1.balance)}")
print()
print(f"Account 2's account number is {account_2.number}")
print()
print(f"Account 1's limit is {account_1.format_value(account_1.limit)}")
print()
print(
    f"{account_1.holder} would, of course, like to have {account_3.holder}'s limit of {account_3.format_value(account_3.limit)}"
)
print()
account_1.withdraw(500000)
print(f"{account_1.holder} went to hospital in NYC to get an aspirin for a minor headache. He now has US${account_1.balance} in his account. He's proper fucked.")
print()
account_3.deposit(1000000)
print(f"{account_3.holder} just made {account_3.format_value(100000)} selling shit T-shirts, cuz life's unfair, so he now has {account_3.format_value(account_3.balance)}.")
account_2.deposit(85.67)
print()
print(f"{account_2.holder} now has a balance of {account_2.format_value(account_2.balance)}")
print()
Account.print_client_names(accounts)
