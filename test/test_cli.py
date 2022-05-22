import unittest
from unittest import runner
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
            'Change the default configuration settings', result.output
            )

    def test_config_option_help_exists(self):
        runner = CliRunner()
        result = runner.invoke(cli.config, ['--help'])
        assert result.exit_code == 0
        self.assertIn(  # --adblock_link
            'Location or link to Adblockultimate', result.output
            )
        self.assertIn(  # --chart_dir
            'Set path to your chart directory', result.output
            )
        self.assertIn(  # --db_path
            'Set path to the default database', result.output
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
            chart_dir = None
            db_dir = None
            gecko_drv = None
            ''')

    def tearDown(self) -> None:
        del self.runner, self.mock_config_file

    def test_config_set_ad_block_path(self):
        with patch('builtins.open', self.mock_config_file):
            result = self.runner.invoke(cli.config, ['--chart_dir', 'new_path'])
            assert result.exit_code == 0

    def test_config_set_chart_dir_path(self):
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


if __name__ == '__main__':
    unittest.main()
