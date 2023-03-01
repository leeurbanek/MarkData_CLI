import logging.config
import os
from dotenv import load_dotenv


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


config_file = os.path.join(BASE_DIR, 'config.ini')

logger_conf = os.path.join(BASE_DIR, 'logger.ini')
logging.config.fileConfig(fname=logger_conf)


try:
    load_dotenv()
    alpha_key = os.getenv('ALPHA_KEY')
    tiingo_key = os.getenv('TIINGO_KEY')
except:
    pass
