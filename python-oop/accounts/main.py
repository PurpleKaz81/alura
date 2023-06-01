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

print(
    f"Account 1's balance is {Account.accounts[123].format_value(Account.accounts[123].balance)}",
    "\n")
print(f"Account 2's account number is {Account.accounts[321].number}", "\n")
print(
    f"Account 3's limit is {Account.accounts[666].format_value(Account.accounts[666].limit)}",
    "\n")
print(
    f"{Account.accounts[123].holder} would, of course, like to have {Account.accounts[666].holder}'s limit of {Account.accounts[666].format_value(Account.accounts[666].limit)}",
    "\n")
Account.accounts[123].withdraw(500000)
print(
    f"{Account.accounts[123].holder} went to hospital in NYC to get an aspirin for a minor headache. He now has {Account.accounts[123].format_value(Account.accounts[123].balance)} in his account. He's now a bit short on change.",
    "\n")
Account.accounts[666].deposit(1000000)

date_1 = Date(12, 5, 2023)
print(
    f"{Account.accounts[666].holder} made {Account.accounts[666].format_value(100000)} selling shit T-shirts on {date_1.formatted_date()}, cuz life's unfair, so he now has {Account.accounts[666].format_value(Account.accounts[666].balance)}.",
    "\n")
Account.accounts[321].deposit(85.67)
print(
    f"{Account.accounts[321].holder} now has a balance of {Account.accounts[321].format_value(Account.accounts[321].balance)}",
    "\n")
Account.print_client_names()
print()

Account.accounts[123].print_client_info()
Account.accounts[321].print_client_info()
Account.accounts[666].print_client_info()

date_2 = Date(17, "08", 2017)
print(
    f"On {date_2.formatted_date()}, {Account.accounts[666].holder} came to visit and never really went back home.",
    "\n")

transfer_value = 30000
transfer = Account.accounts[123].transfer(transfer_value,
                                          Account.accounts[666],
                                          Account.accounts[123])
print(
    f"{Account.accounts[123].holder} received a transfer of {Account.accounts[666].format_value(transfer_value)} from {Account.accounts[666].holder}, who now owns the title to {Account.accounts[123].holder}'s soul.",
    "\n")
Account.accounts[123].print_client_info()
Account.accounts[666].print_client_info()

Account.print_delinquent_list()

print(Account.accounts[123].format_value(Account.accounts[123].limit), "\n")
Account.accounts[123].limit = 2000000
print(
    f"{Account.accounts[123].holder} needs a new limit. We'll give him {Account.accounts[123].format_value(Account.accounts[123].limit)}.",
    "\n")

Account.accounts[123].print_client_info()
Account.print_delinquent_list()

print(Account.accounts[123].format_value(Account.accounts[123].limit), "\n")

balance_difference = Account.accounts[123].balance - Account.accounts[
    321].balance
print(
    f"Now, {Account.accounts[321].holder} has {Account.accounts[123].format_value(balance_difference)} less than {Account.accounts[123].holder}.",
    "\n")

date_3 = Date(25, 12, 1996)
print(f"Coincidentally, {Account.accounts[222].holder} arrived in town on {date_3.formatted_date()}.")
