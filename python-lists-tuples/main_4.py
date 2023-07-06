from main_3 import Account, CheckingAccount, SavingsAccount, InvestmentAccount
from operator import attrgetter


class WageAccount:

    _accounts = []

    def __init__(self, account_number):
        self._account_number = account_number
        self._balance = 0
        self.__class__._accounts.append(self)

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

    def __lt__(self, other):
        return self._balance < other._balance

    def __gt__(self, other):
        return self._balance > other._balance

    @property
    def get_balance(self):
        return self._balance

    @staticmethod
    def format_values(value):
        return f"US${value:,.2f}"

    @classmethod
    def richest_mf(cls):
        return max(cls._accounts, key=attrgetter("get_balance"))


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
print()

account_5 = WageAccount(5)
account_5.deposit(500)

account_6 = WageAccount(10)
account_6.deposit(10000)

account_7 = WageAccount(83)
account_7.deposit(879)

accounts = [account_5, account_6, account_7]

for account in sorted(accounts):
    print(account)

print()

print(
    f"Mirror mirror on the wall, who's the richest of them all? It's Account number {WageAccount.richest_mf()._account_number}!"
)
