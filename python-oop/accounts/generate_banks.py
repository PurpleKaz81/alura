import requests
import json

response = requests.get("https://brasilapi.com.br/api/banks/v1")
data = response.json()

banks = {item['code']: item.get('name', 'Unknown') for item in data}

with open("accounts/bank_list.py", "w") as f:
    f.write(f"banks = {json.dumps(banks, indent=4)}")
