import unittest

from click.testing import CliRunner

from src.data_service import client, reader
from src.run import main_cli


class DownloadTest(unittest.TestCase):

    def setUp(self) -> None:
        self.eem = [{'date': '2023-03-09T00:00:00.000Z', 'close': 38.04, 'high': 38.58, 'low': 37.96, 'open': 38.51, 'volume': 40118857, 'adjClose': 38.04, 'adjHigh': 38.58, 'adjLow': 37.96, 'adjOpen': 38.51, 'adjVolume': 40118857, 'divCash': 0.0, 'splitFactor': 1.0}, {'date': '2023-03-10T00:00:00.000Z', 'close': 37.84, 'high': 38.25, 'low': 37.8, 'open': 38.02, 'volume': 49316671, 'adjClose': 37.84, 'adjHigh': 38.25, 'adjLow': 37.8, 'adjOpen': 38.02, 'adjVolume': 49316671, 'divCash': 0.0, 'splitFactor': 1.0}]
        self.iwm = [{'date': '2023-03-09T00:00:00.000Z', 'close': 181.41, 'high': 187.27, 'low': 181.28, 'open': 186.73, 'volume': 33546890, 'adjClose': 181.41, 'adjHigh': 187.27, 'adjLow': 181.28, 'adjOpen': 186.73, 'adjVolume': 33546890, 'divCash': 0.0, 'splitFactor': 1.0}, {'date': '2023-03-10T00:00:00.000Z', 'close': 176.18, 'high': 180.39, 'low': 174.255, 'open': 180.39, 'volume': 67388021, 'adjClose': 176.18, 'adjHigh': 180.39, 'adjLow': 174.255, 'adjOpen': 180.39, 'adjVolume': 67388021, 'divCash': 0.0, 'splitFactor': 1.0}]
        self.reader = reader.TiingoReader(ticker_list=['EEM', 'IWM'])
        self.runner = CliRunner()

    def tearDown(self) -> None:
        del self.runner

    def test_convert_json_data_to_list(self):
        data_list = self.reader._convert_json_to_list()

    def test_write_data_list_to_db(self):
        pass


if __name__ == '__main__':
    unittest.main()
