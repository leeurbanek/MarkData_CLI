import unittest

from src import _value


class HelperFunctionTest(unittest.TestCase):

    def test_value_with_empty_string_returns_None(self):
        value = ''
        self.assertEqual(_value(value), None)

    def test_value_with_None_string_returns_None(self):
        value = 'None'
        self.assertEqual(_value(value), None)

    def test_value_with_string_returns_string(self):
        value = 'string'
        self.assertEqual(_value(value), 'string')


if __name__ == '__main__':
    unittest.main()
