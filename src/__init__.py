import logging.config
import os


BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)
))

config_file = os.path.join(BASE_DIR, 'config.ini')

logger_conf = os.path.join(BASE_DIR, 'logger.ini')
logging.config.fileConfig(fname=logger_conf)
