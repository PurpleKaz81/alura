class CheckingAccount:

    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0

    def deposit(self, value):
        self.balance += value

    def __str__(self):
        return (
            f"Account number {self.account_number} has a balance of {self.format_values(self.balance)}."
            " He's rich, biatch!" if self.balance >= 5000 else
            f"Account number {self.account_number} has a balance of {self.format_values(self.balance)}."
        )

    @staticmethod
    def format_values(value):
        return f"US${value:,.2f}"

    @staticmethod
    def deposit_all_accounts(accounts):
        for account in accounts:
            account.deposit(100)

    @staticmethod
    def fix_name(users):
        return [
            ("Rafael Kasinski", ) + user[1:] if user[0] == "Rafael" else user
            for user in users
        ]


account_1 = CheckingAccount("616")
account_1.deposit(6666.66)
account_2 = CheckingAccount("1818")
account_2.deposit(1818.18)

accounts = [account_1, account_2]

for account in accounts:
    # print(f"Account {account.account_number} has a balance of {CheckingAccount.format_values(account.balance)}.")
    print(account)
    print()

CheckingAccount.deposit_all_accounts(accounts)
for account in accounts:
    print(account)
    print()

rick = ("Richard", 67, 1956)
rafael = ("Rafael", 42, 1981)
print(rafael)
print()
rafael = CheckingAccount.fix_name([rafael])[0]
print(rafael)
print()

paul = ("Paul", 22, 2002)
users = (rick, rafael, paul)
for user in users:
    print(', '.join(map(str, user)))
    print()

print(', '.join(map(str, users[0])))
