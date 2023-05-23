import unittest

from src.cli.cmd_config import update_ticker_symbol


class UpdateConfigFileTest(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_write_to_config_func(self):
        pass


class ChartDirConfigTest(unittest.TestCase):

    def setUp(self) -> None:
        self.ctx = {'Default': {'chart_dir': 'temp/', 'opt_one': 'None'},
                        'Scraper': {'adblock': 'None', 'base_url': 'https://stockcharts.com/h-sc/ui?s=', 'driver': 'chromedriver'},
                        'Ticker': {'symbol': 'IYR, IYZ'},
                        'debug': True,
                        'opt_trans': 'chart_dir',
                        'section': '<Section: Default>',
                        }
        self.config = """
            [Default]
                chart_dir = temp/
            """

    def tearDown(self) -> None:
        del self.config, self.ctx

    def test_download(self):
        pass


if __name__ == '__main__':
    unittest.main()

# =======

# self.ctx_obj = {
#     'Default': {
#         'database': 'db.sqlite',
#         'db_table': 'None',
#         'work_dir': 'temp',
#         'start': 'None',
#         'end': 'None'
#     },
#     'Scraper': {
#         'adblock': 'None',
#         'base_url': 'https://stockcharts.com/h-sc/ui?s=',
#         'driver': 'chromedriver'
#     },
#     'Ticker': {
#         'symbol': 'EEM, IWM'
#     },
#     'debug': True, 'opt_trans': 'alpha', 'symbol': ['EEM', 'IWM']
# }
