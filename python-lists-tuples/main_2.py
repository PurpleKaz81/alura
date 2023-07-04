class CheckingAccount:

    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0

    def deposit(self, value):
        self.balance += value

    def __str__(self):
        regular_return = f"Account number {self.account_number} has a balance of {self.format_values(self.balance)}."
        rich_return = f"Account number {self.account_number} has a balance of {self.format_values(self.balance)}. He's rich, biatch!"
        return regular_return if self.balance < 5000 else rich_return

    @staticmethod
    def format_values(value):
        return f"US${value:,.2f}"


account_1 = CheckingAccount("616")
account_1.deposit(6666.66)
# print(account_1)
# print()

account_2 = CheckingAccount("1818")
account_2.deposit(1818.18)
# print(account_2)
# print()

accounts = [account_1, account_2]

for account in accounts:
    # print(f"Account {account.account_number} has a balance of {CheckingAccount.format_values(account.balance)}.")
    print(account)
    print()
