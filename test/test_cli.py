import unittest
from unittest import runner
from unittest import result
from unittest.mock import mock_open, patch

from click.testing import CliRunner

from app import cli


class TestMarkData_CLI(unittest.TestCase):
    """"""
    def test_markdata_help_exists(self):
        runner = CliRunner()
        result = runner.invoke(cli.run, ['--help'])
        self.assertEqual(0, result.exit_code)
        self.assertIn(
            'MarkData_CLI: stock MARKet DATA Command Line Interface', result.output
            )

    def test_config_help_exists(self):
        runner = CliRunner()
        result = runner.invoke(cli.config, ['--help'])
        assert result.exit_code == 0
        self.assertIn(
            'Change the default settings', result.output
            )

    def test_config_option_help_exists(self):
        runner = CliRunner()
        result = runner.invoke(cli.config, ['--help'])
        assert result.exit_code == 0
        self.assertIn(  # --av_api_key
            'Your Alpha Vantage API key', result.output
            )
        self.assertIn(  # --adblock_link
            'Location or link to Adblockultimate', result.output
            )
        self.assertIn(  # --chart_dir
            'Path to the chart dir.', result.output
            )
        self.assertIn(  # --db_path
            'Path to the database.', result.output
            )
        self.assertIn(  # --gecko_drv
            'Path to Gecko driver (Windows users)', result.output
            )


class TestConfigOptions(unittest.TestCase):
    """"""
    def setUp(self) -> None:
        self.runner = CliRunner()
        self.mock_config_file = mock_open(read_data='''
            [default]
            ad_block = None
            av_api_key = None
            chart_dir = None
            db_path = None
            gecko_drv = None
            ''')

    def tearDown(self) -> None:
        del self.runner, self.mock_config_file

    def test_config_set_ad_block_path(self):
        with patch('builtins.open', self.mock_config_file):
            result = self.runner.invoke(cli.config, ['--ad_block', 'new_path'])
            assert result.exit_code == 0

    def test_config_set_av_api_key(self):
        with patch('builtins.open', self.mock_config_file):
            result = self.runner.invoke(cli.config, ['--av_api_key', 'new_key'])
            assert result.exit_code == 0

    @patch('app.cli.config')
    def test_config_set_chart_dir_path(self, mock_config):
        with patch('builtins.open', self.mock_config_file):
            result = self.runner.invoke(cli.config, ['--chart_dir', 'new_path'])
            assert result.exit_code == 0

    def test_config_set_db_dir_path(self):
        with patch('builtins.open', self.mock_config_file):
            result = self.runner.invoke(cli.config, ['--db_path', 'new_path'])
            assert result.exit_code == 0

    def test_config_set_gecko_drv_path(self):
        with patch('builtins.open', self.mock_config_file):
            result = self.runner.invoke(cli.config, ['--gecko_drv', 'new_path'])
            assert result.exit_code == 0


class TestDatabaseService(unittest.TestCase):
    """"""
    def setUp(self) -> None:
        self.runner = CliRunner()
        self.mock_config_file = mock_open(read_data='''
            [default]
            db_path = db.sqlite3
            ''')

    def tearDown(self) -> None:
        del self.runner, self.mock_config_file

    def test_initdb_warning_if_db_path_exists(self):
        with patch('app.cli.initdb') as initdb_mock:
            result = self.runner.invoke(initdb_mock, ['--db_path'])
            assert result.exit_code == 0


    # def test_function_a():
    #     # note that you must pass the name as it is imported on the application code
    #     with patch("myproject.main.complex_function") as complex_function_mock:

    #         # we dont care what the return value of the dependency is
    #         complex_function_mock.return_value = "foo"

    #         # we just want our function to work
    #         assert function_a() == "FOO"


if __name__ == '__main__':
    unittest.main()
