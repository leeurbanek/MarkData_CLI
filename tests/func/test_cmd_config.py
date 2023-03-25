import unittest

from click.testing import CliRunner

from src.run import main_cli


class TestConfigMainCLI(unittest.TestCase):

    def setUp(self) -> None:
        self.runner = CliRunner()

    def tearDown(self) -> None:
        del self.runner

    def test_config_help_exists(self):
        result = self.runner.invoke(main_cli, 'config --help')
        self.assertIn('Usage: main-cli config', result.output)
        self.assertEqual(0, result.exit_code)

    def test_config_cmd_without_opts_args(self):
        result = self.runner.invoke(main_cli, 'config')
        # self.assertIn('Usage: main-cli config', result.output)
        self.assertIn('', result.output)
        self.assertEqual(0, result.exit_code)

    def test_config_chart_dir_aborted(self):
        result = self.runner.invoke(main_cli, 'config --work-dir', input='N')
        self.assertIn('Aborted!', result.output)
        self.assertEqual(1, result.exit_code)

    # def test_config_chart_dir_with_argument(self):
    #     result = self.runner.invoke(main_cli, 'config --chart-dir', input='y\nchart\n')
    #     self.assertIn('Enter a valid chart_dir:', result.output)
    #     self.assertEqual(0, result.exit_code)


if __name__ == '__main__':
    unittest.main()
