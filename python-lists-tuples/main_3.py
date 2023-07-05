try:
    import warnings
    warnings.filterwarnings("ignore")
    import numpy as np
    from abc import ABCMeta, abstractmethod
    print("Module loaded.")
    print()
except ImportError:
    print("Module not loaded.")
    print()


class Account(metaclass=ABCMeta):

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

    @abstractmethod
    def month_over(self):
        print("Subclasses must implement this method!")
        raise NotImplementedError("Subclasses must implement this method!")


class CheckingAccount(Account):

    def month_over(self):
        self._balance -= 2
        return self.__str__()


class SavingsAccount(Account):

    def month_over(self):
        self._balance += 1.01
        self._balance -= 3
        return self.__str__()


class InvestmentAccount(Account):

    def month_over(self):
        self._balance += 1.10
        self._balance -= 5
        return self.__str__()


account_16 = CheckingAccount(16)
account_16.deposit(1000)
account_16.month_over()

account_17 = SavingsAccount(17)
account_17.deposit(1000)
account_17.month_over()

account_18 = InvestmentAccount(18)
account_18.deposit(100000)
account_18.month_over()

accounts = [account_16, account_17, account_18]

accounts_list = [(account.month_over()) for account in accounts]
for account in accounts_list:
    print(account)
    print()

numbers = np.array([1, 3.5])
for number in numbers:
    print(f"{number:.2f}")
    print()

new_numbers = [(number + 3.74) for number in numbers]
for new_number in new_numbers:
    print(f"{new_number:.2f}")
    print()
