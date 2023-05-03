"""src.data_service.__init__.py"""
import datetime
import logging
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
    def default_start_date(self):
        """Default start date for reader"""
        date_list = []
        config_date = _value(conf_obj.get('Default', 'start'))
        if config_date:
            date_list.append(datetime.datetime.strptime(config_date, '%Y-%m-%d').date())
        if _database_max_date():
            date_list.append(_database_max_date())
        if date_list:
            return max(date_list)
        else:
            return None

        # try:
        #     # datetime.strptime('2011-03-07', '%Y-%m-%d')
        #     dates.append(datetime.date.strftime(conf_obj.get('Default', 'start'), '%Y-%m-%d'))
        #     # dates.append(datetime.date.today() - datetime.timedelta(days=30))
        #     # dates.append(_database_max_date() + datetime.timedelta(days=1))
        # except Exception as e:
        #     print(f"{e} in config.ini file\nTry 'markdata config --help' for help.")
        # return dates

    """
    if database date:
        use most recent date
    if config date:
    """

    @property
    def default_end_date(self):
        """Default end date for reader"""
        try:
            config_date = conf_obj.get('Default', 'end')
            default_date = datetime.date.today()
            return default_date if _value(config_date) is None else config_date
        except Exception as e:
            print(f"{e} in config.ini file\nTry 'markdata config --help' for help.")


def _database_max_date():
    """Get the date of the first/last record in the table.
    ---------------------------------------------------
    If table has no records return None.\n
    `db_connection()` is needed for database connection.\n
    Parameters
    ----------
    `db_con` : sqlite3.Connection object
        Connection to the time series database.\n
    `table_name` : string
        Name of the table to check.\n
    `extreme` : string
        MIN/MAX (first/last) date to return.\n
    Returns
    -------
    'YYYY-MM-DD' string or None.\n
    """
    try:
        db_path = f"{conf_obj.get('Default', 'work_dir')}/{conf_obj.get('Default', 'database')}"
        db_table = 'ohlc' if _value(conf_obj.get('Default', 'db_table')) is None else conf_obj.get('Default', 'db_table')
        if os.path.isfile(db_path):
            with DatabaseConnectionManager(db_path=db_path, mode='ro') as cursor:
                cursor.execute(f"SELECT Date FROM {db_table} WHERE ROWID IN (SELECT max(ROWID) FROM {db_table});")
                return cursor.fetchone()
    except Exception as e:
        print(f"{e}\nTry 'markdata config --help' for help.")


def _sanitize_dates(start, end):
    """
    Return (datetime start, datetime end) tuple
    -------------------------------------------
    Parameters
    `start` : datetime.date,
    `end` : datetime.date,
    """
    try:
        db_path = f"{conf_obj.get('Default', 'work_dir')}/{conf_obj.get('Default', 'database')}"
        db_table = 'ohlc' if _value(conf_obj.get('Default', 'db_table')) is None else conf_obj.get('Default', 'db_table')
        if os.path.isfile(db_path):
            with DatabaseConnectionManager(db_path=db_path, mode='ro') as cursor:
                cursor.execute(f"SELECT Date FROM {db_table} WHERE ROWID IN (SELECT max(ROWID) FROM {db_table});")
                db_date = cursor.fetchone()
    except Exception as e:
        print(f"{e}\nTry 'markdata config --help' for help.")

    # if db_date:
    #     start = db_date if (db_date > start) else start
    # if start > end:
    #     raise ValueError("start must be an earlier date than end")

    return start, end


if __name__ == '__main__':
    import unittest

    class _BaseReaderTest(unittest.TestCase):

        def setUp(self) -> None:
            logging.disable(logging.CRITICAL)
            self.reader = _BaseReader()

        def tearDown(self) -> None:
            logging.disable(logging.NOTSET)
            del self.reader

        def test_IsInstance_BaseReader(self):
            self.assertIsInstance(self.reader, _BaseReader)

    class _database_max_date_Test(unittest.TestCase):
        pass

    class default_end_date_Test(unittest.TestCase):
        pass

            # @patch('src.data_service._value')
    # @patch('src.data_service._database_max_date')
        # def test_start_date_if_db_date_no_config_date(self):
        #     # _value.return_value = None
        #     _database_max_date = Mock()
        #     _database_max_date.return_value = datetime.date.today()
        #     print(f"\n+++++++ _database_max_date() = {_database_max_date()}, type: {type(_database_max_date())}")
        #     self.assertEqual(self.reader.default_start_date, datetime.date.today())
        #     del _database_max_date

    #     def test_value_with_None_string_returns_None(self):
    #         assert _value('None') == None

    #     def test_value_with_empty_string_returns_None(self):
    #         assert _value('') == None

    #     def test_value_with_string_returns_string(self):
    #         assert _value('2000-1-1') == '2000-1-1'

    unittest.main()

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
