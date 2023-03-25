import logging.config
import os
from configparser import ConfigParser
from dotenv import load_dotenv


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


config_file = os.path.join(BASE_DIR, 'config.ini')
# Create getlist() converter, used in cmd_config.py for ticker symbols
conf_obj = ConfigParser(converters={'list': lambda x: [i.strip() for i in x.split(',')]})

logger_conf = os.path.join(BASE_DIR, 'logger.ini')
logging.config.fileConfig(fname=logger_conf)


try:
    load_dotenv()
    alpha_key = os.getenv('ALPHA_KEY')
    tiingo_key = os.getenv('TIINGO_KEY')
except:
    pass
