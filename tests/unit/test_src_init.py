import unittest

from src import _value


class ValueFunctionTest(unittest.TestCase):

    def test_value_with_None_string_returns_None(self):
        self.assertEqual(_value('None'), None)

    def test_value_with_empty_string_returns_None(self):
        self.assertEqual(_value(''), None)

    def test_value_with_string_returns_string(self):
        self.assertEqual(_value('2000-1-1'), '2000-1-1')


if __name__ == '__main__':
    unittest.main()
