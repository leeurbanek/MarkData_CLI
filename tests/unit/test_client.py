import unittest

from click.testing import CliRunner

from src.chart_service import client
from src.run import main_cli


class GetChartDownloadTest(unittest.TestCase):

    def setUp(self) -> None:
        self.ctx = {
            'Default': {'opt_one': 'None'},
            'Ticker': {'symbol': 'IYR, IYZ'},
            'debug': False,
            'opt_trans': 'daily',
            'period': ['Daily'],
            'symbol': ['IWM']
            }
        self.runner = CliRunner()

    def tearDown(self) -> None:
        del self.runner

    def test_get_chart_ctx(self):
        pass

    def test_download(self):
        pass


if __name__ == '__main__':
    unittest.main()
