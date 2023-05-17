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


# import sys

# def write_lamb(outfile):
#     outfile.write("Mary had a little lamb.\n")

# if __name__ == '__main__':
#     with open(sys.argv[1], 'w') as outfile:
#         write_lamb(outfile)


##File test_lamb.py
# import unittest
# from io import StringIO

# import lamb


# class LambTests(unittest.TestCase):
#     def test_lamb_output(self):
#         outfile = StringIO()
#         lamb.write_lamb(outfile)
#         outfile.seek(0)
#         content = outfile.read()
#         self.assertEqual(content, "Mary had a little lamb.\n")


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
