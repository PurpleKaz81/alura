class Account:

    def __init__(self, account_number):
        self._account_number = account_number
        self._balance = 0

    def deposit(self, value):
        self._balance += value

    def __str__(self):
        return (
            f"Account number {self._account_number} has a balance of {self.format_values(self._balance)}."
            " He's rich, biatch!" if self._balance >= 5000 else
            f"Account number {self._account_number} has a balance of {self.format_values(self._balance)}."
        )

    @staticmethod
    def format_values(value):
        return f"US${value:,.2f}"


class CheckingAccount(Account):

    def month_over(self):
        self._balance -= 2
        return self.__str__()


class SavingsAccount(Account):

    def month_over(self):
        self._balance += 1.01
        self._balance -= 3
        return self.__str__()


account_16 = CheckingAccount(16)
account_16.deposit(1000)
account_16.month_over()

account_17 = SavingsAccount(17)
account_17.deposit(1000)
account_17.month_over()

accounts = [account_16, account_17]

accounts_list = [(account.month_over()) for account in accounts]
for account in accounts_list:
    print(account)
