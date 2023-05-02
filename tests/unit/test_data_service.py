import datetime
import logging
import unittest
from unittest.mock import Mock, patch

from src.data_service import _BaseReader
from src.data_service.reader import TiingoReader


class ClientTest(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test__write_data_to_sqlite_db(self):
        pass


class _BaseReaderTest(unittest.TestCase):

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
        self.reader = _BaseReader()
        # self._value = Mock()

    def tearDown(self) -> None:
        logging.disable(logging.NOTSET)
        del self.ctx_obj, self.reader

    def test_IsInstance_BaseReader(self):
        self.assertIsInstance(self.reader, _BaseReader)

# >>> from unittest.mock import Mock
# >>> m = Mock()
# >>> m.side_effect = ['foo', 'bar', 'baz']
# >>> m()
# 'foo'
# >>> m()
# 'bar'
# >>> m()
# 'baz'

    # @patch('src.data_service._value')
    # @patch('src.data_service._database_max_date')
    # def test_start_date_if_no_config_date_no_db_date(self, _value, _database_max_date):
    #     _value.return_value = None
    #     _database_max_date.return_value = None
    #     self.assertEqual(self.reader.default_start_date, None)

    # @patch('src.data_service._value')
    # @patch('src.data_service._database_max_date')
    # def test_start_date_if_config_date_no_db_date(self, _value, _database_max_date):
    #     config_date = _value.return_value = datetime.datetime.strptime('2000-1-1','%Y-%m-%d').date()
    #     _database_max_date.return_value = None
    #     self.assertEqual(self.reader.default_start_date, datetime.datetime.strptime('2000-1-1','%Y-%m-%d').date())

    # @patch('src.data_service._value')
    # @patch('src.data_service._database_max_date')
    def test_start_date_if_db_date_no_config_date(self):
        # _value.return_value = None
        _database_max_date = Mock()
        _database_max_date.return_value = datetime.date.today()
        # self.assertEqual(self.reader.default_start_date, datetime.date.today())
        # del _value, _database_max_date

    # def test_default_end_date(self):
    #     pass

    # def test_sanitize_dates(self):
    #     sanitize =_sanitize_dates(start=None, end=None)
    #     self.assertEqual(sanitize, (None, None))


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
        logging.disable(logging.CRITICAL)
        del self._read_one_price_data

    def test_parse_price_data(self):
        data_list = [datetime.date(2023, 3, 31), 'IWM', 17640, 17864, 17637, 17840, 39602850]
        self.assertEqual(next(TiingoReader.parse_price_data(self, symbol='iwm')), data_list)


if __name__ == '__main__':
    unittest.main()
