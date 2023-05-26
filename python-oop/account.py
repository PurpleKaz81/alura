class Account:
    def __init__(self, number, holder, balance, limit):
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
        for key, value in account.items():
            result += f"{key}, {self.format_value(value, account['number'])}\n"
        return result


account = Account(123, "Nico", 1000, 10000)
account_2 = Account(321, "Marco", 100, 1000)

print(account_2, "\n")
print(account_2.client_info(account_2.__dict__))
