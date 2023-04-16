"""src.data_service.__init__.py"""
import datetime
import logging
import os

from src import config_file, conf_obj, _none_value
from src.ctx_mgr import DatabaseConnectionManager


conf_obj.read(config_file)

logging.getLogger('unittest').setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


class _BaseReader():
    """"""
    def __init__(self, api_key=None, end=None, freq=None, start=None, symbol=None) -> None:
        self.api_key = api_key
        self.freq = freq
        self.symbol = symbol

        # start, end = _sanitize_dates(start or self.default_start_date, end)
        start, end = _sanitize_dates()
        self.start = self.default_start_date()
        self.end = datetime.date.today()

    @property
    def params(self):
        """Parameters to use in API calls"""
        return None

    @property
    def base_url(self):
        """API URL"""
        # must be overridden in subclass
        raise NotImplementedError

    # @property
    def default_start_date(self):
        """Default start date for reader"""
        default = datetime.date.today() - datetime.timedelta(days=90)
        # return default
        print(f"_none_value: {_none_value(conf_obj, value='start')}, type: {type(_none_value(conf_obj, value='start'))}")
        value = default if _none_value(conf_obj, value='start') is None else conf_obj.get('Default', 'start')
        return value

# table_name = 'ohlc' if _none_value(conf_obj, value='db_table') else table_name

    @property
    def default_end_date(self):
        """Default end date for reader"""
        if not _none_value(conf_obj, 'Default', 'end'):
            return conf_obj.get('Default', 'end')
        else:
            return datetime.date.today()

ctx={
    'Default': {
        'database': 'db.sqlite',
        'db_table': 'None',
        'work_dir': 'temp',
        'start': 'None',
        'end': 'None'
        },
    'Scraper': {
        'adblock': 'None',
        'base_url': 'https://stockcharts.com/h-sc/ui?s=',
        'driver': 'chromedriver'
        },
    'Ticker': {
        'symbol': 'EEM, IWM'
        },
    'debug': True,
    'opt_trans': 'tiingo',
    'symbol': ['EEM', 'IWM']
    }

def _sanitize_dates(ctx_obj=ctx, start=None, end=None):
    """"""
    if ctx_obj['debug']:
        logger.debug(f"_sanitize_dates(ctx_obj={ctx_obj})")

    db_path = f"{ctx_obj['Default']['work_dir']}/{ctx_obj['Default']['database']}"
    table_name = 'ohlc'
    if os.path.exists(db_path):
        with DatabaseConnectionManager(db_path=db_path, mode='ro') as cursor:
            cursor.execute(f"SELECT Date FROM {table_name} WHERE ROWID IN (SELECT max(ROWID) FROM {table_name});")
            date = cursor.fetchone()[0]
            print(f"db.sqlite last date: {date}")


# fetchedData = cursor.fetchall()

# # to access specific fetched data
# for row in fetchedData:
# 	StudentID = row[0]
# 	StudentName = row[1]
# 	SubmissionDate = row[2]
# 	print(StudentName, ", ID -",
# 		StudentID, "Submitted Assignments")
# 	print("Date and Time : ",
# 		SubmissionDate)
# 	print("Submission date type is",
# 		type(SubmissionDate))

    start, end = 'start', 'end'
    return start, end

# =======

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
