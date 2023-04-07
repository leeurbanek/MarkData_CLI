import datetime
import unittest
from unittest.mock import Mock

from src.data_service.client import _write_data_to_sqlite_db
from src.data_service.reader import TiingoReader


class ClientTest(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test__write_data_to_sqlite_db(self):
        pass


class ReaderTest(unittest.TestCase):

    def setUp(self) -> None:
        self._read_one_price_data = Mock()
        self._read_one_price_data.return_value = [
            {'date': '2023-03-31T00:00:00.000Z', 'close': 178.4, 'high': 178.64, 'low': 176.37, 'open': 176.4, 'volume': 39602850, 'adjClose': 178.4, 'adjHigh': 178.64, 'adjLow': 176.37, 'adjOpen': 176.4, 'adjVolume': 39602850, 'divCash': 0.0, 'splitFactor': 1.0},
        ]

    def tearDown(self) -> None:
        del self._read_one_price_data

    # def test_parse_price_data(self):
    #     data_list = [
    #         datetime.date(2023, 3, 31), 'IWM', 17640, 17864, 17637, 17840, 39602850
    #     ]
    #     self.assertEqual(TiingoReader.parse_price_data(self, symbol=None), data_list)


if __name__ == '__main__':
    unittest.main()
