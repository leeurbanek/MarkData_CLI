import datetime, logging, sqlite3

import unittest
from unittest.mock import patch

from src import conf_obj, config_file
from src.data_service import _BaseReader, _database_max_date


conf_obj.read(config_file)


class SanitizeDatesTest(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()



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
        self.days = int(conf_obj.get('Default', 'td_days'))
        self.reader = _BaseReader()

    def tearDown(self) -> None:
        logging.disable(logging.NOTSET)
        del self.days, self.reader

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

    def setUp(self) -> None:
        self.db_table = 'data'

    def test_database_max_date_with_data_in_table(self):
        db = sqlite3.connect("file::memory:?cache=shared", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES, uri=True)
        rows = [
            (datetime.date.today() - datetime.timedelta(days=1), 1),
            (datetime.date.today(), 2),
        ]
        with db as db_con:
            cursor = db_con.cursor()
            cursor.execute(f'''
                CREATE TABLE {self.db_table} (
                    Date    DATE        NOT NULL,
                    Row     INTEGER     NOT NULL,
                    PRIMARY KEY (Date)
                );
            ''')
            cursor.executemany('INSERT INTO data VALUES (?,?)', rows)
            db_date = _database_max_date(db_con, self.db_table)
            self.assertEqual(db_date, datetime.date.today())

    def test_database_max_date_with_no_data_in_table(self):
        db = sqlite3.connect("file::memory:?cache=shared", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES, uri=True)
        with db as db_con:
            cursor = db_con.cursor()
            cursor.execute(f'''
                CREATE TABLE {self.db_table} (
                    Date    DATE        NOT NULL,
                    Row     INTEGER     NOT NULL,
                    PRIMARY KEY (Date)
                );
            ''')
            db_date = _database_max_date(db_con, self.db_table)
            self.assertEqual(db_date, None)


if __name__ == '__main__':
    unittest.main()
