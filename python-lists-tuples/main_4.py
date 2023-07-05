from main_3 import Account, CheckingAccount, SavingsAccount, InvestmentAccount


class WageAccount:

    def __init__(self, account_number):
        self._account_number = account_number
        self._balance = 0

    def deposit(self, value):
        self._balance += value

    def __str__(self):
        if self._balance >= 5000:
            return f"Account number {self._account_number} has a balance of {self.format_values(self._balance)}. He's rich, biatch!"
        elif self._balance <= 0:
            return f"Account number {self._account_number} has a balance of {self.format_values(self._balance)}. Damn!"
        else:
            return f"Account number {self._account_number} has a balance of {self.format_values(self._balance)}."

    def __eq__(self, other):
        if type(other) != WageAccount:
            return False

        return self._account_number == other._account_number and self._balance == other._balance

    @staticmethod
    def format_values(value):
        return f"US${value:,.2f}"


class WageMultiple(WageAccount):
    pass


account_1 = WageAccount(37)
print(account_1)

account_2 = WageAccount(37)
print(account_2)

print(account_1 == account_2)

all_accounts = [account_1]
print(account_2 in all_accounts)

account_1.deposit(1000)
print(account_1._balance == account_2._balance)
print(account_1 == account_2)

account_3 = WageAccount(88)
account_4 = CheckingAccount(88)

print(account_3 == account_4)

print()

print(isinstance(SavingsAccount(99), SavingsAccount))

print(isinstance(WageMultiple(81), Account))

print(isinstance(SavingsAccount(191), Account))
