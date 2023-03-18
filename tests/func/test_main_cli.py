import unittest

from click.testing import CliRunner

from src.run import main_cli


class TestClickBasicSetup(unittest.TestCase):

    def setUp(self) -> None:
        self.runner = CliRunner()

    def tearDown(self) -> None:
        del self.runner

    def test_main_help_exists(self):
        result = self.runner.invoke(main_cli, '--help')
        self.assertIn('Usage: main-cli', result.output)
        self.assertEqual(0, result.exit_code)

    def test_debug_no_debug(self):
        result = self.runner.invoke(main_cli, '--debug config')
        self.assertEqual(0, result.exit_code)
        result = self.runner.invoke(main_cli, '--no-debug config')
        self.assertEqual(0, result.exit_code)

    def test_version_option(self):
        result = self.runner.invoke(main_cli, '--version')
        self.assertIn('main-cli, version', result.output)
        self.assertEqual(0, result.exit_code)

    def test_chart_help_exists(self):
        result = self.runner.invoke(main_cli, 'chart --help')
        self.assertIn('Usage: main-cli chart', result.output)
        self.assertEqual(0, result.exit_code)

    def test_config_help_exists(self):
        result = self.runner.invoke(main_cli, 'config --help')
        self.assertIn('Usage: main-cli config', result.output)
        self.assertEqual(0, result.exit_code)

    def test_data_help_exists(self):
        result = self.runner.invoke(main_cli, 'data --help')
        self.assertIn('Usage: main-cli data', result.output)
        self.assertEqual(0, result.exit_code)


if __name__ == '__main__':
    unittest.main()
