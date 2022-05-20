"""setup logging for app"""
import logging
import logging.config
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG = os.path.join(BASE_DIR, 'config.ini')

logging.config.fileConfig(fname=CONFIG, disable_existing_loggers=True)
