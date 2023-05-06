"""src.data_service.__init__.py"""
import datetime
import os

from src import config_file, conf_obj, _value
from src.ctx_mgr import DatabaseConnectionManager


conf_obj.read(config_file)


class _BaseReader():
    """"""
    def __init__(self, api_key=None, end=None, freq=None, start=None, symbol=None) -> None:
        self.api_key = api_key
        self.freq = freq
        self.symbol = symbol
        start, end = _sanitize_dates(self.default_start_date, self.default_end_date)
        self.start = start
        self.end = end

    @property
    def params(self):
        """Parameters to use in API calls"""
        return None

    @property
    def base_url(self):
        """API URL"""
        # must be overridden in subclass
        raise NotImplementedError

    @property
    def default_end_date(self):
        """Default end date for reader
        ---------------------------
        Returns
        -------
        datetime.date object
        """
        end_date = _value(conf_obj.get('Default', 'start'))
        if end_date:
            try:
                default_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
            except TypeError as e:
                print(f"ERROR: {e}\nin src/data_service/__init__.py default_end_date()")
        else:
            default_date = datetime.date.today()
        return default_date

    @property
    def default_start_date(self):
        """Default start date for reader
        -----------------------------
        Returns
        -------
        datetime.date object
        """
        start_date = _value(conf_obj.get('Default', 'start'))
        if start_date:
            try:
                default_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
            except TypeError as e:
                print(f"ERROR: {e}\nin src/data_service/__init__.py default_start_date()")
        else:
            try:
                days = int(conf_obj.get('Default', 'td_days'))
                default_date = datetime.date.today() - datetime.timedelta(days=days)
            except Exception as e:
                print(f"{e} in config.ini file\nTry 'markdata config --help' for help.")
        return default_date


def _database_max_date(db_con, db_table):
    """Get the date of the last record in the table.
    ---------------------------------------------
    If table has no records return None.\n
    Parameters
    ----------
    `db_con` : sqlite3.Connection object
        Connection to the time series database.\n
    `table_name` : string
        Name of the table to check.\n
    Returns
    -------
    datetime.date object or None.\n
    """
    cursor = db_con.cursor()
    try:
        cursor.execute(f"SELECT Date FROM {db_table} WHERE ROWID IN (SELECT max(ROWID) FROM {db_table});")
    except Exception as e:
        print(f"{e}\nTry 'markdata config --help' for help.")
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return None


def _sanitize_dates(start: datetime.date, end: datetime.date) -> tuple:
    """Check that the start and end dates make sense
    ---------------------------------------------
    Parameters
    ----------
    `start` : datetime.date object\n
    `end` : datetime.date object\n
    Returns
    -------
    iso format date strings - (start, end) tuple\n
    """
    if start > end:
        raise ValueError('start must be earlier than end')
    return(
        datetime.datetime.strftime(start, '%Y-%m-%d'),
        datetime.datetime.strftime(end, '%Y-%m-%d')
    )

# =======

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

# =======

# self.ctx_obj = {
#     'Default': {
#         'database': 'db.sqlite',
#         'db_table': 'None',
#         'work_dir': 'temp',
#         'start': 'None',
#         'end': 'None'
#     },
#     'Scraper': {
#         'adblock': 'None',
#         'base_url': 'https://stockcharts.com/h-sc/ui?s=',
#         'driver': 'chromedriver'
#     },
#     'Ticker': {
#         'symbol': 'EEM, IWM'
#     },
#     'debug': True, 'opt_trans': 'alpha', 'symbol': ['EEM', 'IWM']
# }
