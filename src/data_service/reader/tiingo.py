import requests


API_KEY = None
BASE_URL = 'https://api.tiingo.com/tiingo'
FUNCTION = None
PERIOD = None
SYMBOL = None


url = f"{BASE_URL}/prices?startDate={PERIOD}&token={API_KEY}"

headers = {
    'Content-Type': 'application/json'
}

# requestResponse = requests.get(url, headers=headers)
requestResponse = requests.get("https://api.tiingo.com/tiingo/daily/aapl/prices?startDate=2019-01-02&token=Not logged-in or registered. Please login or register to see your API Token", headers=headers)
print(requestResponse.json())

# =======

class Tiingo():
    """"""
    def __init__(self) -> None:
        pass
