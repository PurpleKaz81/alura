def create_account(number, name, balance, limit):
    return {
        "number": number,
        "holder": name,
        "balance": balance,
        "limit": limit,
    }


def deposit(account, value):
    account["balance"] += value
    return account["balance"]


def withdrawal(account, value):
    account["balance"] -= value
    return account["balance"]


def format_value(value):
    return "{:,.2f}".format(value)


def format_balance(account):
    return "{:,.2f}".format(account["balance"])


def format_limit(account):
    return "{:,.2f}".format(account["limit"])


account = create_account(123, "Nico", 55.0, 10000.0)
print(
    f"{account['holder']}'s account number is {account['number']}, where he has a balance of US${format_balance(account)} and a limit of US${format_limit(account)}.",
    end="\n\n")

print(
    f"After a deposit of US${format_value(100)}, {account['holder']}'s account is now worth US${format_value(deposit(account, 100.0))}.",
    end="\n\n")

print(
    f"However, after a withdrawal of US${format_value(2000)}, Nico's pretty fucked and only has US${format_value(withdrawal(account, 2000))} left.",
    end="\n\n")

print(
    f"Here's Nico's account info: Account {account['number']}. Account Holder: {account['holder']}. Balance: US${format_balance(account)}, limit: US${format_limit(account)}",
    end="\n\n")
