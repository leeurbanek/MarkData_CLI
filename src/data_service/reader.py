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
        self._ticker = ""
        self.key = os.getenv('TIINGO_KEY')

    # @property
    # def params(self):
    #     """Parameters to use in API calls"""
    #     return {
    #         "startDate": self.start.strftime("%Y-%m-%d"),
    #         "endDate": self.end.strftime("%Y-%m-%d"),
    #         "resampleFreq": self.freq,
    #         "format": "json",
    #     }

    @property
    def url(self):
        """API URL"""
        _url = f"https://api.tiingo.com/tiingo/daily/{self._ticker}/prices?"
        return _url

    def _read_one_data(self, params, url):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Token {self.key}',
        }

    def read(self):
        data_list = []
        for ticker in self.symbol:
            self._ticker = ticker
            # data_list.append(self._read_one_data(params=None, url=None))
            data_list.append(ticker)
        return data_list


# Historical Prices
# https://api.tiingo.com/tiingo/daily/<ticker>/prices?startDate=2012-1-1&endDate=2016-1-1

# import requests
# headers = {
#     'Content-Type': 'application/json'
# }
# requestResponse = requests.get("https://api.tiingo.com/tiingo/daily/aapl/prices?startDate=2019-01-02&token=Not logged-in or registered. Please login or register to see your API Token", headers=headers)
# print(requestResponse.json())
