import datetime
import logging
import unittest
from unittest.mock import Mock

from src.data_service.reader import TiingoReader


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

    def test_read_one_price_data(self):
        pass
    
    def test_parse_price_data(self):
        data_list = [datetime.date(2023, 3, 31), 'IWM', 17640, 17864, 17637, 17840, 39602850]
        self.assertEqual(next(TiingoReader.parse_price_data(self, symbol='iwm')), data_list)


if __name__ == '__main__':
    unittest.main()
