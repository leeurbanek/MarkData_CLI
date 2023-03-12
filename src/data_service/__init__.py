""""""

class _BaseReader():
    """"""
    def __init__(self, ticker_list, api_key=None, end=None, freq=None, start=None) -> None:
        self.api_key = api_key
        self.end = end
        self.freq = freq
        self.start = start
        self.ticker_list = ticker_list

    @property
    def params(self):
        """Parameters to use in API calls"""
        return None

    @property
    def base_url(self):
        """API URL"""
        # must be overridden in subclass
        raise NotImplementedError
