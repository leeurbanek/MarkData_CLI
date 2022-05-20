import unittest
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

    def test_database_help_exists(self):
        runner = CliRunner()
        result = runner.invoke(cli.config, ['--help'])
        assert result.exit_code == 0
        self.assertIn(
            'Database create, update, delete actions', result.output
            )


class TestConfigChartDir(unittest.TestCase):
    """"""
    def test_config_set_chart_dir_path(self):
        runner = CliRunner()

        mock_config_file = mock_open(read_data='[default]\nchart_dir = None\n')
        with patch('builtins.open', mock_config_file):
            result = runner.invoke(cli.config, ['--chart_dir', 'new_path'])
            assert result.exit_code == 0


class TestConfigDataBase(unittest.TestCase):
    """"""
    def test_config_set_database_path(self):
        pass


if __name__ == '__main__':
    unittest.main()
