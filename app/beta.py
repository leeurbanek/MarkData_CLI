import unittest
from io import StringIO


def write_lamb(outfile):
    outfile.write("Mary had a little lamb.\n")


class LambTests(unittest.TestCase):
    def test_lamb_output(self):
        outfile = StringIO()
        # NOTE: Alternatively, for Python 2.6+, you can use
        # tempfile.SpooledTemporaryFile, e.g.,
        #outfile = tempfile.SpooledTemporaryFile(10 ** 9)
        write_lamb(outfile)
        outfile.seek(0)
        content = outfile.read()
        self.assertEqual(content, "Mary had a little lamb.\n")


if __name__ == '__main__':
    unittest.main()
