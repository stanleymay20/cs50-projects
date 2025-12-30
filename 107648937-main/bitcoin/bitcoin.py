import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get(
        "https://api.coincap.io/v2/assets/bitcoin",
        headers={"Authorization": "Bearer 6f6965eb9714e8cccdfe88570d72b389485a8e917b5f5d315ac60a2075edb33c"}
    )
    response.raise_for_status()
    data = response.json()
    price = float(data["data"]["priceUsd"])
    amount = n * price
    print(f"${amount:,.4f}")

except requests.RequestException:
    sys.exit("Error fetching Bitcoin price")
