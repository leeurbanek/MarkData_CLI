import dataclasses
from datetime import date


@dataclasses.dataclass
class OHLC:
    Date: date
    Tick_id: int
    Open: int
    High: int
    Low: int
    Close: int
    Volume: int

    @classmethod
    def from_dict(self, d):
        return self(**d)

    def to_dict(self):
        return dataclasses.asdict(self)


@dataclasses.dataclass
class Ticker:
    Symbol: str
    Issuer: str
    Description: str
    Structure: str
    Inception: str
    Portfolio: str
    Updated: date

    @classmethod
    def from_dict(self, d):
        return self(**d)

    def to_dict(self):
        return dataclasses.asdict(self)


if __name__ == '__main__':
    t1 = Ticker('XAR', 'State Street', 'Aerospac & Defence', 'ETF', '2011-09-28', 'Speculate', '2022-05-27')
    print(t1)
    d = t1.to_dict()
    print(d)
    t2 = Ticker.from_dict(d)
    print(t2)
