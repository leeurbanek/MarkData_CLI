""""""

class _BaseReader():
    """"""
    def __init__(self, symbol, end=None, freq=None, key=None, start=None) -> None:
        self.end = end
        self.freq = freq
        self.key = key
        self.start = start
        self.symbol = symbol

    @property
    def params(self):
        """Parameters to use in API calls"""
        return None

    @property
    def base_url(self):
        """API URL"""
        # must be overridden in subclass
        raise NotImplementedError
