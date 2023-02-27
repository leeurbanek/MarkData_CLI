import requests


API_KEY = None
BASE_URL = 'https://www.alphavantage.co'
FUNCTION = None
SYMBOL = None


# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = f"{BASE_URL}/query?function={FUNCTION}&symbol={SYMBOL}&apikey={API_KEY}"
# url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey=demo'
r = requests.get(url)
data = r.json()
print(data)

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
# url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol=IBM&apikey=demo'
r = requests.get(url)
data = r.json()
print(data)

# =======

class Alpha():
    """"""
    def __init__(self) -> None:
        pass
