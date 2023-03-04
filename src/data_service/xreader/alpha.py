import requests

from src import alpha_key


API_KEY = None
BASE_URL = 'https://www.alphavantage.co'
FUNCTION = None
SYMBOL = None


# # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
# url = f"{BASE_URL}/query?function={FUNCTION}&symbol={SYMBOL}&apikey={API_KEY}"
# # url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey=demo'
# r = requests.get(url)
# data = r.json()
# print(data)

# # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
# # url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol=IBM&apikey=demo'
# r = requests.get(url)
# data = r.json()
# print(data)

# Fetches last 100 data points
# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey=demo

# Fetches 20+ years
# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&outputsize=full&apikey=demo

# =======

class AlphaReader():
    """"""
    def __init__(self) -> None:
        self.key = alpha_key

# =======

# https://dev.to/kamranakhan/python-convert-json-to-sqlite-4a5n

# import json
# import urllib.request
# import sqlite3
# from os import path

# stocks = ['AAPL', "MSFT"]

# connection = sqlite3.connect("C:\\Projects\\AIFX\\Spikes\\Data\\Stocks.db")
# cursor = connection.cursor()

# for stock in stocks:

#     url = "https://financialmodelingprep.com/api/v3/historical-price-full/" + stock
#     data = urllib.request.urlopen(url).read().decode()

#     obj = json.loads(data)

#     for child in obj['historical']:
#         print(child)

#         cursor.execute("Insert into StockPrices values (?, ?, ?, ?, ?, ?, ?)",
#                        (child['date'], child['close'], child['high'], child['low'],
#                        child['open'], child['volume'], stock))
#         connection.commit()

# CREATE TABLE "StockPrices" (
#     "date"  TEXT,
#     "close" INTEGER,
#     "high"  INTEGER,
#     "low"   INTEGER,
#     "open"  INTEGER,
#     "volume"    INTEGER,
#     "symbol"    TEXT
# );

# =======

# {
#     "Meta Data": {
#         "1. Information": "Daily Time Series with Splits and Dividend Events",
#         "2. Symbol": "IBM",
#         "3. Last Refreshed": "2023-02-27",
#         "4. Output Size": "Full size",
#         "5. Time Zone": "US/Eastern"
#     },
#     "Time Series (Daily)": {
#         "2023-02-27": {
#             "1. open": "131.42",
#             "2. high": "131.87",
#             "3. low": "130.13",
#             "4. close": "130.49",
#             "5. adjusted close": "130.49",
#             "6. volume": "2761326",
#             "7. dividend amount": "0.0000",
#             "8. split coefficient": "1.0"
#         },
#         "2023-02-24": {
#             "1. open": "129.62",
#             "2. high": "130.67",
#             "3. low": "129.22",
#             "4. close": "130.57",
#             "5. adjusted close": "130.57",
#             "6. volume": "3015907",
#             "7. dividend amount": "0.0000",
#             "8. split coefficient": "1.0"
#         },
#       .
#       .
#       .
#         "1999-11-01": {
#             "1. open": "98.5",
#             "2. high": "98.81",
#             "3. low": "96.37",
#             "4. close": "96.75",
#             "5. adjusted close": "52.6607098328961",
#             "6. volume": "9551800",
#             "7. dividend amount": "0.0000",
#             "8. split coefficient": "1.0"
#         }
#     }
# }
