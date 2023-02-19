import logging
import os
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


class Spinner:
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
    with Spinner():
        # ... some long-running operations
        time.sleep(3)
    with WebDriverManager(debug=True) as driver:
        pass
    with WebDriverManager(debug=False) as driver:
        pass
