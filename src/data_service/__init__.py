""""""

class _BaseReader():
    """"""
    def __init__(self, api_key=None, end=None, freq=None, start=None, symbol=None) -> None:
        self.api_key = api_key
        self.end = end
        self.freq = freq
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


# import datetime as dt


# def _sanitize_dates(start, end):
#     """
#     Return (timestamp_start, timestamp_end) tuple
#     if start is None - default is 5 years before the current date
#     if end is None - default is today

#     Parameters
#     ----------
#     start : str, int, date, datetime, Timestamp
#         Desired start date
#     end : str, int, date, datetime, Timestamp
#         Desired end date
#     """
#     if is_number(start):
#         # regard int as year
#         start = dt.datetime(start, 1, 1)
#     start = to_datetime(start)

#     if is_number(end):
#         end = dt.datetime(end, 1, 1)
#     end = to_datetime(end)

#     if start is None:
#         # default to 5 years before today
#         today = dt.date.today()
#         start = today - dt.timedelta(days=365 * 5)
#     if end is None:
#         # default to today
#         end = dt.date.today()
#     try:
#         start = to_datetime(start)
#         end = to_datetime(end)
#     except (TypeError, ValueError):
#         raise ValueError("Invalid date format.")
#     if start > end:
#         raise ValueError("start must be an earlier date than end")
#     return start, end
