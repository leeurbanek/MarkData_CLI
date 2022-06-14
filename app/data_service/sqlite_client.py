import csv
import logging.config
import os
import sqlite3

from configparser import ConfigParser
from dotenv import load_dotenv


logger = logging.getLogger(__name__)

load_dotenv()  # take environment variables from .env
AV_API_KEY = os.getenv('AV_API_KEY')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CONFIG = os.path.join(BASE_DIR, 'config.ini')

conf_obj = ConfigParser()
conf_obj.read(CONFIG)

ETF_CSV = os.path.join(BASE_DIR, 'data/ETF.csv')


class DatabaseContextManager:
    """Context manager for Sqlite3 database connection.
    ------------------------------------------------
    Commits changes on exit.\n
    Parameters
    ----------
    `db_path` : string
        Path to an Sqlite3 database.\n
    `mode` : string
        determines if the new database is opened read-only 'ro',
        read-write 'rw', read-write and create 'rwc', or pure
        in-memory database 'memory' mode.\n
    Returns
    -------
    An Sqlite3 cursor object.\n
    """
    def __init__(self, db_path: str, mode: str=None):
        if mode == None: mode = 'ro'
        logger.info(f': class <DatabaseConnectionManager>, {db_path}, {mode}')
        self.db_path = db_path
        self.mode = mode

    def __enter__(self):
        logger.debug(f': DatabaseConnectionManager.__enter__()')
        try:
            self.connection = sqlite3.connect(
                f'file:{os.path.abspath(self.db_path)}?mode={self.mode}',
                detect_types=sqlite3.PARSE_DECLTYPES, uri=True
            )
            self.cursor = self.connection.cursor()
            print(f"connected {os.path.basename(self.db_path)}, mode: {self.mode}")
            return self.cursor
        except sqlite3.Error as e:
            print(f'{e}: {self.db_path}')

    def __exit__(self, exc_type, exc_value, exc_traceback):
        logger.debug(f': DatabaseConnectionManager.__exit__()')
        self.cursor.close()
        if isinstance(exc_value, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()
        self.connection.close()


def _create_daily_price_table(db_con):
    """Create the Open, High, Low, Close, AdjCl, Volume table.
    --------------------------------------------------------
    Data is adjusted daily historical from Alpha Vantage.\n
    See https://www.alphavantage.co/documentation/#dailyadj.\n
    Fields are Date, Open, High, Low, Close, Volume.\n
    Parameters
    ----------
    `db_con` : sqlite3.Connection object
        Connection to the time series database.\n
    """
    logger.debug(f"_create_daily_price_table('{db_con}')")
    db_con.execute(f'''
        CREATE TABLE IF NOT EXISTS daily_price (
            Date        DATE        PRIMARY KEY,
            Tick_id     INTEGER     NOT NULL,
            Open        INTEGER     NOT NULL,
            High        INTEGER     NOT NULL,
            Low         INTEGER     NOT NULL,
            Close       INTEGER     NOT NULL,
            Volume      INTEGER     NOT NULL,
            FOREIGN KEY (Tick_id)
                REFERENCES ticker (Symbol)
            );
        ''')


def _create_security_table(db_con, csv_file: str):
    """Create the security info table.
    -------------------------------
    Fields are Symbol, Issuer, Description, Structure, Inception, Portfolio, Updated.\n
    Parameters
    ----------
    `db_con` : sqlite3.Connection object
        Connection to the time series database.\n
    `csv_file` : str
        Path to the csv security info file.\n
    """
    logger.debug(f"._create_security_table('{db_con}, {csv_file}')")
    db_con.execute(f'''
        CREATE TABLE IF NOT EXISTS security (
            Symbol          TEXT    PRIMARY KEY,
            Issuer          TEXT,
            Description     TEXT,
            Structure       TEXT,
            Inception       DATE,
            Portfolio       TEXT,
            Updated         DATE
            );
        ''')
    db_con.executemany('''
        INSERT INTO ticker (Symbol, Issuer, Description, Structure, Inception, Portfolio)
        VALUES (?, ?, ?, ?, ?, ?);''', _get_etf_data(csv_file)
        )


def db_creator(db_path: str, mode: str=None, symbol: str=None) -> None:
    """"""
    logger.debug(f".db_creator({db_path}, {symbol})")
    if os.path.exists(ETF_CSV):
        with DatabaseContextManager(db_path, mode='rwc') as con:
            _create_security_table(con, ETF_CSV)

        # with open(ETF_CSV, 'r') as f:
        #     rows = csv.DictReader(f)
        #     [print(r) for r in rows]
    else:
        if not symbol:
            symbol = [s.strip() for s in conf_obj['data']['symbol'].split(',')]
        print(symbol)


def db_deleter(db_path: str, table: str) -> None:
    """"""
    logger.debug(f".db_deleter({db_path}, {table})")
    with DatabaseContextManager(db_path, mode='rwc') as con:
        print(f'{db_path}, {table}')


def _get_etf_data(csv_file: str) -> list:
    """"""
    with open(csv_file, 'r') as f:
        rows = csv.DictReader(f)
        etf_list = [(
            r['Symbol'],
            r['Issuer'],
            r['Description'],
            r['Structure'],
            r['Inception'],
            r['Portfolio']
        ) for r in rows]
        return etf_list
