from account import Account
import accounts
from date import Date

for account in Account.accounts.values():
    account.print_client_info()

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

print(account_1.format_value(account_1.limit), "\n")
account_1.limit = 2000000
print(
    f"{account_1.holder} needs a new limit. We'll give him {account_1.format_value(account_1.limit)}.",
    "\n")

account_1.print_client_info()
Account.print_delinquent_list()
