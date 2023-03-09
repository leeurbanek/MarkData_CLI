""""""

class _BaseReader():
    """"""
    def __init__(self, symbol, start=None, end=None) -> None:
        self.end = end
        self.start = start
        self.symbol = symbol

    @property
    def params(self):
        """Parameters to use in API calls"""
        return None

    @property
    def url(self):
        """API URL"""
        # must be overridden in subclass
        raise NotImplementedError
