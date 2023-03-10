import os
import requests

from dotenv import load_dotenv

from src.data_service import _BaseReader


load_dotenv()


class AlphaReader(_BaseReader):
    """"""
    def __init__(self, symbol) -> None:
        super().__init__(symbol)
        self.ticker = ""
        self.key = os.getenv('ALPHA_KEY')


class TiingoReader(_BaseReader):
    """"""
    def __init__(self, symbol) -> None:
        super().__init__(symbol)
        self.ticker = ""
        self.key = os.getenv('TIINGO_KEY')


    @property
    def params(self):
        """Parameters to use in API calls"""
        return {
            'startDate'
            # "startDate": self.start.strftime("%Y-%m-%d"),
            # "endDate": self.end.strftime("%Y-%m-%d"),
            # "resampleFreq": self.freq,
            # "format": "json",
        }

    @property
    def base_url(self):
        """API URL"""
        # url = f"https://api.tiingo.com/tiingo/daily/{self.ticker}/prices?"
        url = "https://api.tiingo.com/tiingo"
        return url

    def _read_one_data(self):
        """"""
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Token {self.key}',
        }
        for ticker in self.symbol:
            self.ticker = ticker
            # data = requests.get(f"{self.base_url}startDate=2023-03-08&token={self.key}", headers=headers)
            url = f"{self.base_url}/{self.freq}/{ticker}/prices?startDate={self.start}&endDate={self.end}&token={self.key}"
            yield url

    def write_data(self):
        """"""
        data = self._read_one_data()

        while True:
            try:
                print(f"\nnext() = {next(data)}")
            except StopIteration:
                break

# =======

# Historical Prices
# https://api.tiingo.com/tiingo/daily/<ticker>/prices?startDate=2012-1-1&endDate=2016-1-1

# import requests
# headers = {
#     'Content-Type': 'application/json'
# }
# requestResponse = requests.get("https://api.tiingo.com/tiingo/daily/aapl/prices?startDate=2019-01-02&token=Not logged-in or registered. Please login or register to see your API Token", headers=headers)
# print(requestResponse.json())
