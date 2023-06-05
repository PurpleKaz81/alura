import requests
import json

print("Sending request to API...")
response = requests.get("https://brasilapi.com.br/api/banks/v1")
data = response.json()

print("Creating banks dictionary...")
banks = { item['code']: item.get('name', 'Unknown') for item in data }

print("Writing banks dictionary to banks.py...")
with open("banks_data.py", "w") as f:
    f.write(f"banks ={json.dumps(banks, indent=4)}")

print("Done!")
