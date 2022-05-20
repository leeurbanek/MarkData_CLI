import logging.config
import os
import sqlite3


logger = logging.getLogger(__name__)
logger.debug(f'Hello {__name__}')



def creator(db_path, ticker=None):
    """"""
    logger.debug(f'creator({db_path})')
    print('creator() Not Implemented')


def updater(db_path):
    """"""
    logger.debug(f'updater({db_path})')
    print('updater() Not Implemented')


def deleter(db_path):
    """"""
    logger.debug(f'deleter({db_path})')
    print('deleter() Not Implemented')


class DatabaseConnectionManager:
    """Context manager for Sqlite3 databases.
    -----------------------------------------
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
    def __init__(self, db_path, mode='memory'):
        self.db_path = db_path
        self.mode = mode

    def __enter__(self):
        logger.debug(f'DatabaseConnectionManager.__enter__()')
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
        logger.debug(f'DatabaseConnectionManager.__exit__()')
        self.cursor.close()
        if isinstance(exc_value, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()
        self.connection.close()
