import unittest

from click.testing import CliRunner

from src.run import main_cli


class TestChartMainCLI(unittest.TestCase):

    def setUp(self) -> None:
        self.runner = CliRunner()

    def tearDown(self) -> None:
        del self.runner

    def test_chart_help_exists(self):
        result = self.runner.invoke(main_cli, 'chart --help')
        self.assertEqual(0, result.exit_code)
        self.assertIn('Usage: main-cli chart', result.output)

    def test_chart_cmd_without_opts_args(self):
        result = self.runner.invoke(main_cli, 'chart')
        self.assertEqual(0, result.exit_code)
        self.assertIn('Usage: markdata chart', result.output)

    # def test_chart_cmd_with_option(self):
    #     result = self.runner.invoke(main_cli, 'chart -d')
    #     self.assertEqual(0, result.exit_code)

    # def test_chart_cmd_with_argument(self):
    #     result = self.runner.invoke(main_cli, 'chart IWM')
    #     self.assertEqual(0, result.exit_code)
    #     self.assertIn('Usage: md-cli chart', result.output)

    # def test_chart_cmd_with_opt_and_arg(self):
    #     result = self.runner.invoke(main_cli, 'chart -d IWM')
    #     self.assertEqual(0, result.exit_code)


if __name__ == '__main__':
    unittest.main()
