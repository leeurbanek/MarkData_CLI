import logging
import os
import sqlite3
import sys
import threading
import time
from configparser import ConfigParser

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from src import config_file


conf_obj = ConfigParser()
conf_obj.read(config_file)

logging.getLogger('selenium').setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

ADBLOCK = conf_obj['Scraper']['adblock']
DRIVER = conf_obj['Scraper']['driver']


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
        logger.debug('DatabaseConnectionManager.__enter__()')
        try:
            self.connection = sqlite3.connect(
                f'file:{os.path.abspath(self.db_path)}?mode={self.mode}',
                detect_types=sqlite3.PARSE_DECLTYPES, uri=True
                # detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES, uri=True
            )
            self.cursor = self.connection.cursor()
            print(f"connected {os.path.basename(self.db_path)}, mode: {self.mode}")
            return self.cursor
        except sqlite3.Error as e:
            print(f'{e}: {self.db_path}')

    def __exit__(self, exc_type, exc_value, exc_traceback):
        logger.debug('DatabaseConnectionManager.__exit__()')
        self.cursor.close()
        if isinstance(exc_value, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()
        self.connection.close()


class SpinnerManager:
    """Manage a simple spinner object"""
    busy = False
    delay = 0.2

    @staticmethod
    def spinning_cursor():
        while 1:
            for cursor in '|/-\\': yield cursor

    def __init__(self, delay=None):
        self.spinner_generator = self.spinning_cursor()
        if delay and float(delay): self.delay = delay

    def spinner_task(self):
        while self.busy:
            sys.stdout.write(next(self.spinner_generator))
            sys.stdout.flush()
            time.sleep(self.delay)
            sys.stdout.write('\b')
            sys.stdout.flush()

    def __enter__(self):
        self.busy = True
        threading.Thread(target=self.spinner_task).start()

    def __exit__(self, exception, value, tb):
        self.busy = False
        time.sleep(self.delay)
        if exception is not None:
            return False


class WebDriverManager:
    """Manage Selenium web driver"""
    def __init__(self, debug: bool) -> None:
        self.debug = debug

    def __enter__(self):
        chrome_opts = webdriver.ChromeOptions()
        chrome_opts.headless = True  # don't display browser window
        s = Service(DRIVER)
        driver = webdriver.Chrome(service=s, options=chrome_opts)
        # Install ad blocker if used
        if os.path.exists(ADBLOCK):
            driver.install_addon(ADBLOCK)
            # pyautogui.PAUSE = 2.5
            # pyautogui.click()  # position browser window
            # pyautogui.hotkey('ctrl', 'w')  # close ADBLOCK page

        if self.debug: logger.debug(f'WebDriverManager.__enter__(session={driver.session_id})')
        return driver

    def __exit__(self, exc_type, exc_value, exc_traceback):
        driver.quit()
        if self.debug: logger.debug('WebDriverManager.__exit__()')


if __name__ == '__main__':
    with SpinnerManager():
        # ... some long-running operations
        time.sleep(3)
    with WebDriverManager(debug=True) as driver:
        pass
    with WebDriverManager(debug=False) as driver:
        pass
