import datetime
import logging
import unittest
from unittest.mock import Mock

from src.data_service import _sanitize_dates
from src.data_service.client import _write_data_to_sqlite_db
from src.data_service.reader import TiingoReader


class ClientTest(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test__write_data_to_sqlite_db(self):
        pass


class DataServiceTest(unittest.TestCase):

    def setUp(self) -> None:
        logging.disable(logging.CRITICAL)
        self.ctx_obj = {
            'Default': {
                'database': 'db.sqlite',
                'db_table': 'None',
                'work_dir': 'temp',
                'start': 'None',
                'end': 'None'
            },
            'Scraper': {
                'adblock': 'None',
                'base_url': 'https://stockcharts.com/h-sc/ui?s=',
                'driver': 'chromedriver'
            },
            'Ticker': {
                'symbol': 'EEM, IWM'
            },
            'debug': True, 'opt_trans': 'alpha', 'symbol': ['EEM', 'IWM']
        }

    def tearDown(self) -> None:
        logging.disable(logging.NOTSET)

    def test_sanitize_dates(self):
        sanitize =_sanitize_dates(self.ctx_obj)
        # self.assertEqual(sanitize, (None, None))


class TiingoReaderTest(unittest.TestCase):

    def setUp(self) -> None:
        self._read_one_price_data = Mock()
        self._read_one_price_data.return_value = [
            {
                'date': '2023-03-31T00:00:00.000Z',
                'close': 178.4,
                'high': 178.64,
                'low': 176.37,
                'open': 176.4,
                'volume': 39602850,
                'adjClose': 178.4,
                'adjHigh': 178.64,
                'adjLow': 176.37,
                'adjOpen': 176.4,
                'adjVolume': 39602850,
                'divCash': 0.0,
                'splitFactor': 1.0
            },
        ]

    def tearDown(self) -> None:
        del self._read_one_price_data

    def test_parse_price_data(self):
        data_list = [datetime.date(2023, 3, 31), 'IWM', 17640, 17864, 17637, 17840, 39602850]
        self.assertEqual(next(TiingoReader.parse_price_data(self, symbol='iwm')), data_list)


if __name__ == '__main__':
    unittest.main()
