# Import the requests library, which allows you to send HTTP requests in Python.
import requests
API_KEY = "fca_live_fnLXFPdd0F9YpkLS19H2ENhSDOhRXSlXx6BZ72OQ"

BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "EUR", "GBP", "JPY", "CNY", "INR", "AUD", "CAD", "CHF", "KRW", "MXN", "BRL", "ZAR"]



def currency_converter(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"

    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]

    except:
        print("Invalid Currency")
        return None 
while True:
    base = input("Enter the base currency (q for quit): ").upper()

    if base == "Q":

        break

    data = currency_converter(base)

    if not data:
        continue 
    del data[base]
    for count, value in data.items():
        print(f"{count}: {value}")
  
