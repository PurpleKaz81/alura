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

        if isinstance(value, float):
            return "US${:,.2f}".format(value)
        elif isinstance(value, str):
            return value
        else:
            return "US${:,.2f}".format(value)

    def __str__(self):
        return f"Account: {self.number}, Holder: {self.holder}, Balance: {self.balance}, Limit: {self.limit}"

    def client_info(self, account):
        result = "Here's the client's information:\n"
        for index, (key, value) in enumerate(account.items(), start=1):
            result += f"{index}) {key}: {self.format_value(value, account['number'])}\n"
        return result

    def print_client_info(self):
        print(self.client_info(vars(self)))

    def print_client_list():
        print("Here's a list of all our clients:\n")
        for index, account in enumerate(accounts, start=1):
            print(f"{index}) {account.holder}")
        print()

    def total_balance(self, accounts):
        total_balance = sum(account.balance for account in accounts)
        return self.format_value(total_balance)

    def total_limit(self, accounts):
        total_limit = sum(account.limit for account in accounts)
        return self.format_value(total_limit)


account_1 = Account(123, "Nico", 1000)
account_2 = Account(321, "Marco", 100)
account_3 = Account(666, "Satan", 2679, 2000)

account_1.print_client_info()
account_2.print_client_info()
account_3.print_client_info()

accounts = [account_1, account_2, account_3]
Account.print_client_list()

print(
    f"The total balance and limit of their accounts is {accounts[0].total_balance(accounts)} and {accounts[0].total_limit(accounts)}, respectively."
)
