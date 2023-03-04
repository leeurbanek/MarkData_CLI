from src import alpha_key, tiingo_key


class AlphaReader():
    """"""
    def __init__(self) -> None:
        self.base_url = None
        self.key = alpha_key


class TiingoReader():
    """"""
    def __init__(self) -> None:
        self.base_url = 'https://api.tiingo.com/tiingo'
        self.key = tiingo_key
