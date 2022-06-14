import json
import unittest

import pandas as pd


def convert_to_cent(df: pd.DataFrame) -> pd.DataFrame:
    ohlc = ('open', 'high', 'low', 'close')
    df = df.apply(
        lambda x: (x.astype(float) * 100).astype(int) if x.name in ohlc else x
        )
    return df


class CentEncoder(json.JSONEncoder):
    """"""
    def default(self, obj):
        print(obj)


class TestDatabase(unittest.TestCase):
    """"""
    def setUp(self) -> None:
        with open('test/IWM.json', 'r') as in_file:
            self.IWM = json.load(in_file)
        with open('test/TIP.json', 'r') as in_file:
            self.TIP = json.load(in_file)

    def tearDown(self) -> None:
        del self.IWM, self.TIP

    def test_IWM(self):
        df = pd.DataFrame(self.IWM['Time Series (Daily)']).transpose()
        df.columns = ['open', 'high', 'low', 'close', 'volume']
        df = convert_to_cent(df)
        print(df)

    def test_TIP(self):
        df = pd.DataFrame(self.TIP['Time Series (Daily)']).transpose()
        df.columns = ['open', 'high', 'low', 'close', 'volume']
        df = convert_to_cent(df)
        print(df)


if __name__ == '__main__':
    unittest.main()
