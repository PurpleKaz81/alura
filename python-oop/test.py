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
    if value == account['number']:
        return str(value)

    if isinstance(value, (int, float)):
        return "US${:,.2f}".format(value)
    else:
        return str(value)


def format_balance(account):
    return "{:,.2f}".format(account["balance"])

def format_limit(account):
    return "{:,.2f}".format(account["limit"])

def account_balance(account):
    return f"Here's Nico's account info: Account {account['number']}. Account Holder: {account['holder']}. Balance: US${format_balance(account)}, limit: US${format_limit(account)}"

def account_balance_keys(account):
    result = "Here's the client's information:\n"
    for key, value in account.items():
        result += f"{key}: {format_value(value)}\n"
    return result


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

print(account_balance(account))
print(f"US${format_balance(account)}", end="\n\n")

print(
    f"After a deposit of {format_value(3000)}, {account['holder']} now has a balance of US${format_value(deposit(account, 3000))} in account #{account['number']}.",
    end="\n\n")

deposit(account, 5000)

print(account_balance(account), end="\n\n")

print(account_balance_keys(account))
