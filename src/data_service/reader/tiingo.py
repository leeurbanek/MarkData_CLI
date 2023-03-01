import requests

from src import tiingo_key


# url = f"{BASE_URL}/prices?startDate={PERIOD}&token={API_KEY}"

# headers = {
#     'Content-Type': 'application/json'
# }

# # requestResponse = requests.get(url, headers=headers)
# requestResponse = requests.get("https://api.tiingo.com/tiingo/daily/aapl/prices?startDate=2019-01-02&token=Not logged-in or registered. Please login or register to see your API Token", headers=headers)
# print(requestResponse.json())

# =======

class TiingoReader():
    """"""
    def __init__(self) -> None:
        self.base_url = 'https://api.tiingo.com/tiingo'
        self.key = tiingo_key

# [
#     {
#         "date":"2019-01-02T00:00:00.000Z",
#         "close":157.92,
#         "high":158.85,
#         "low":154.23,
#         "open":154.89,
#         "volume":37039737,
#         "adjClose":157.92,
#         "adjHigh":158.85,
#         "adjLow":154.23,
#         "adjOpen":154.89,
#         "adjVolume":37039737,
#         "divCash":0.0,
#         "splitFactor":1.0
#     },
#     {
#         "date":"2019-01-03T00:00:00.000Z",
#         "close":142.19,
#         "high":145.72,
#         "low":142.0,
#         "open":143.98,
#         "volume":91312195,
#         "adjClose":142.19,
#         "adjHigh":145.72,
#         "adjLow":142.0,
#         "adjOpen":143.98,
#         "adjVolume":91312195,
#         "divCash":0.0,
#         "splitFactor":1.0
#     },
#     {
#         "date":"2019-01-04T00:00:00.000Z",
#         "close":148.26,
#         "high":148.5499,
#         "low":143.8,
#         "open":144.53,
#         "volume":58607070,
#         "adjClose":148.26,
#         "adjHigh":148.5499,
#         "adjLow":143.8,
#         "adjOpen":144.53,
#         "adjVolume":58607070,
#         "divCash":0.0,
#         "splitFactor":1.0
#     },
#     {
#         "date":"2019-01-07T00:00:00.000Z",
#         "close":147.93,
#         "high":148.83,
#         "low":145.9,
#         "open":148.7,
#         "volume":54777764,
#         "adjClose":147.93,
#         "adjHigh":148.83,
#         "adjLow":145.9,
#         "adjOpen":148.7,
#         "adjVolume":54777764,
#         "divCash":0.0,
#         "splitFactor":1.0
#     }
# ]
