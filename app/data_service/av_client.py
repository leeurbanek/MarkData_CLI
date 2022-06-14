"""AlphaVantage Data Utilities.

See https://www.alphavantage.co/.Miscellaneous

Utility functions for creating, updating, and, working with an
Sqlite3 database that contains time series data from AlphaVantage.
See https://www.alphavantage.co/.

Requires that `pandas`, `pandas_datareader`, and `sqlalchemy`is
installed within the Python environment you are running this script.

Can also be imported as a module and contains the following functions:

    * add_new_column - Add a column to an Sqlite3 database table
    * add_timeseries_table - Create the tables Volume, Dividend, Split, etc.
    * update_database - Update the AlphaVantage time series database
"""
import json
import os
import unittest

from unittest.mock import Mock

import requests

from dotenv import load_dotenv


load_dotenv()  # take environment variables from .env

AV_API_KEY = os.getenv('AV_API_KEY')
AV_URL = 'https://www.alphavantage.co/query'


def get_time_series_daily(symbol, out_size=None):
    """"""
    out_size = 'compact' if not out_size else out_size
    param = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'outputsize': out_size,
        'apikey': AV_API_KEY,
    }
    r = requests.get(AV_URL, param)
    return json.loads(r.text)


class TestAlphaVantageClient(unittest.TestCase):
    def test_get_time_series_daily_returns_dict(self):
        pass
        # shipping_system_mock = Mock(get_status=Mock(return_value='SENT'))
        # result = can_cancel_order(1, shipping_system_mock)
        # self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
