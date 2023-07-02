import datetime, logging, sqlite3
import os
import unittest
from unittest.mock import Mock, patch

from src import conf_obj, config_file
from src.ctx_mgr import DatabaseConnectionManager
from src.data_service import _BaseReader, _database_max_date, _sanitize_dates


conf_obj.read(config_file)


class SanitizeDateTest(unittest.TestCase):
    def setUp(self) -> None:
        logging.disable(logging.CRITICAL)
        self.db_table = 'data'

    def tearDown(self) -> None:
        logging.disable(logging.NOTSET)

    @patch('src.data_service._database_max_date')
    def test_db_max_date_used_if_gt_default_date(self, mock_db_max_date):
        db_date = datetime.date.today() - datetime.timedelta(days=3)
        start = datetime.date.today() - datetime.timedelta(days=30)
        end = datetime.date.today()
        mock_db_max_date.return_value = datetime.date.today() - datetime.timedelta(days=3)
        result = _sanitize_dates(db_date=db_date, start=start, end=end)
        self.assertEqual(result, (
            datetime.datetime.strftime(datetime.date.today() - datetime.timedelta(days=2), '%Y-%m-%d'),
            datetime.datetime.strftime(datetime.date.today(), '%Y-%m-%d')
        ))

    def test_iso_format_string_is_returned(self):
        db_date = None
        start = datetime.datetime.strptime('1999-12-31', '%Y-%m-%d').date()
        end = datetime.datetime.strptime('2000-1-1', '%Y-%m-%d').date()
        result = _sanitize_dates(db_date= db_date, start=start, end=end)
        self.assertEqual(result, ('1999-12-31', '2000-01-01'))

    def test_start_gt_end_raises_value_error(self):
        db_date = None
        start = datetime.datetime.strptime('2000-1-1', '%Y-%m-%d').date()
        end = datetime.datetime.strptime('1999-12-31', '%Y-%m-%d').date()
        self.assertRaises(ValueError, _sanitize_dates, db_date, start, end)


class DatabaseDateTest(unittest.TestCase):
    def setUp(self) -> None:
        logging.disable(logging.CRITICAL)
        self.db_path = 'test.sqlite'
        self.db_table = 'data'
        self.reader = _BaseReader()

    def tearDown(self) -> None:
        logging.disable(logging.NOTSET)
        del self.reader

    @patch('os.path.isfile')
    def test_database_date_with_no_database(self, mock_os_is_file):
        mock_os_is_file.return_value =  False
        result = self.reader.database_date()
        self.assertEqual(result, None)

    @patch('os.path.isfile')
    def test_database_date_with_database(self, mock_os_is_file):
        rows = [
            (datetime.date.today() - datetime.timedelta(days=2), 'R1'),
            (datetime.date.today() - datetime.timedelta(days=1), 'R2'),
            (datetime.date.today(), 'R3'),
        ]
        with DatabaseConnectionManager(db_path=self.db_path, mode='rwc') as db:
            db.cursor.execute(f'''
                CREATE TABLE {self.db_table} (
                    Date    DATE    NOT NULL,
                    Field   TEXT    NOT NULL,
                    PRIMARY KEY (Date)
                );
            ''')
            db.cursor.executemany('INSERT INTO data VALUES (?,?)', rows)
        mock_os_is_file.return_value =  True
        result = self.reader.database_date(db_path=self.db_path, db_table=self.db_table)
        self.assertEqual(result, datetime.date.today())
        os.remove(self.db_path)


class DefaultEndDateTest(unittest.TestCase):
    def setUp(self) -> None:
        logging.disable(logging.CRITICAL)
        self.reader = _BaseReader()

    def tearDown(self) -> None:
        logging.disable(logging.NOTSET)
        del self.reader

    @patch('src.data_service._value')
    def test_end_date_with_config_date_set(self, mock_value):
        mock_value.return_value = '2000-1-1'
        result = self.reader.default_end_date
        self.assertEqual(result, datetime.datetime.strptime('2000-1-1', '%Y-%m-%d').date())

    @patch('src.data_service._value')
    def test_end_date_with_no_config_date_set(self, mock_value):
        mock_value.return_value = None
        result = self.reader.default_end_date
        self.assertEqual(result, datetime.date.today())


class DefaultStartDateTest(unittest.TestCase):
    def setUp(self) -> None:
        logging.disable(logging.CRITICAL)
        self.days = int(conf_obj.get('Database', 'td_days'))
        self.reader = _BaseReader()

    def tearDown(self) -> None:
        logging.disable(logging.NOTSET)
        del self.reader

    @patch('src.data_service._value')
    def test_start_date_with_config_date_set(self, mock_value):
        mock_value.return_value = '1999-12-31'
        result = self.reader.default_start_date
        self.assertEqual(result, datetime.datetime.strptime('1999-12-31', '%Y-%m-%d').date())

    @patch('src.data_service._value')
    def test_start_date_with_no_config_date_set(self, mock_value):
        mock_value.return_value = None
        result = self.reader.default_start_date
        self.assertEqual(result, datetime.date.today() - datetime.timedelta(days=self.days))


class BaseReaderTest(unittest.TestCase):
    def setUp(self) -> None:
        logging.disable(logging.CRITICAL)
        self.reader = _BaseReader()

    def tearDown(self) -> None:
        logging.disable(logging.NOTSET)
        del self.reader

    def test_IsInstance_BaseReader(self):
        self.assertIsInstance(self.reader, _BaseReader)


class DatabaseMaxDateTest(unittest.TestCase):
    def setUp(self) -> None:
        logging.disable(logging.CRITICAL)
        self.db_table = 'data'

    def tearDown(self) -> None:
        return super().tearDown()

    def test_database_max_date_with_data_in_table(self):
        rows = [
            (datetime.date.today() - datetime.timedelta(days=2), 'R1'),
            (datetime.date.today() - datetime.timedelta(days=1), 'R2'),
            (datetime.date.today(), 'R3'),
        ]
        with DatabaseConnectionManager() as db:
            db.cursor.execute(f'''
                CREATE TABLE {self.db_table} (
                    Date    DATE    NOT NULL,
                    Field   TEXT    NOT NULL,
                    PRIMARY           KEY (Date)
                );
            ''')
            db.cursor.executemany('INSERT INTO data VALUES (?,?)', rows)
            db_date = _database_max_date(db.cursor, self.db_table)
            self.assertEqual(db_date, datetime.date.today())

    def test_database_max_date_with_no_data_in_table(self):
        with DatabaseConnectionManager() as db:
            db.cursor.execute(f'''
                CREATE TABLE {self.db_table} (
                    Date    DATE        NOT NULL,
                    Field   INTEGER     NOT NULL,
                    PRIMARY KEY (Date)
                );
            ''')
            db_date = _database_max_date(db.cursor, self.db_table)
            self.assertEqual(db_date, None)


if __name__ == '__main__':
    unittest.main()
