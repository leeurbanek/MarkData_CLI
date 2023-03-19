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
        self._read_one_price_data.return_value = {
            'date': '2023-03-09T00:00:00.000Z', 'close': 38.04, 'high': 38.58, 'low': 37.96, 'open': 38.51, 'volume': 40118857, 'adjClose': 38.04, 'adjHigh': 38.58, 'adjLow': 37.96, 'adjOpen': 38.51, 'adjVolume': 40118857, 'divCash': 0.0, 'splitFactor': 1.0
        }

    def tearDown(self) -> None:
        del self._read_one_price_data

    def test_parse_price_data(self):
        data_list = [
            datetime.date(2023, 3, 9), 3851, 3858, 3796, 3804, 40118857
        ]
        self.assertEqual(TiingoReader.parse_price_data(self, symbol=None), data_list)


if __name__ == '__main__':
    unittest.main()
