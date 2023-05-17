"""src.data_service.__init__.py"""
import datetime
import os
from typing import Union

from src import config_file, conf_obj, _value
from src.ctx_mgr import DatabaseConnectionManager


conf_obj.read(config_file)
try:
    db_path = f"{conf_obj.get('Default', 'work_dir')}/{conf_obj.get('Default', 'database')}"
    db_table = f"{conf_obj.get('Default', 'db_table')}"
except Exception as e:
    print(f"{e} in config.ini file\nTry 'markdata config --help' for help.")


class _BaseReader():
    """"""
    def __init__(self, api_key=None, db_date=None, end=None, start=None, symbol=None) -> None:
        self.api_key = api_key
        self.symbol = symbol
        self.db_date = self.database_date(db_path)
        start, end = _sanitize_dates(self.db_date, self.default_start_date, self.default_end_date)
        self.start = start
        self.end = end

    def __repr__(self) -> str:
        return (
            f'_BaseReader(api_key={self.api_key!r}, '
            f'db_date={self.db_date!r}, '
            f'end={self.end!r}, '
            f'start={self.start!r}, '
            f'symbol={self.symbol!r})'
        )

    @staticmethod
    def database_date(db_path=None, db_table=None):
        """
        Most recent date from database
        ------------------------------
        Returns
        -------
        datetime.date object
        """
        if os.path.isfile(db_path):
            with DatabaseConnectionManager(db_path=db_path, mode='ro') as db:
                db_cur = db.cursor
                return _database_max_date(db_cur=db_cur, db_table=db_table)
        else:
            return None

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


def _database_max_date(db_cur, db_table):
    """Get the date of the last record in the table.
    ---------------------------------------------
    If table has no records return None.\n
    Parameters
    ----------
    `db_cur` : sqlite3.Connection object
        Connection to the time series database.\n
    `db_table` : string
        Name of the table to check.\n
    Returns
    -------
    datetime.date object or None.\n
    """
    try:
        db_date = db_cur.execute(f"SELECT Date FROM {db_table} WHERE ROWID IN (SELECT max(ROWID) FROM {db_table})").fetchone()
        if db_date:
            return db_date[0]
    except Exception as e:
        print(f"{e}\nTry 'markdata config --help' for help.")
    return None


def _sanitize_dates(db_date: Union[datetime.datetime, None], start: datetime.date, end: datetime.date) -> tuple:
    """Check t1hat the start and end dates make sense
    ---------------------------------------------
    Parameters
    ----------
    `start` : datetime.date object\n
    `end` : datetime.date object\n
    Returns
    -------
    iso format date strings - (start, end) tuple\n
    """
    if db_date:
        start = db_date + datetime.timedelta(days=1)
    if start > end:
        raise ValueError('start must be earlier than end')
    return(
        datetime.datetime.strftime(start, '%Y-%m-%d'),
        datetime.datetime.strftime(end, '%Y-%m-%d')
    )

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
