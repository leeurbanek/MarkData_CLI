import unittest

from src.cli import cmd_config


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
