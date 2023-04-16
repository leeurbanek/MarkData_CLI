import logging.config
import os
from configparser import ConfigParser
from dotenv import load_dotenv


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_file = os.path.join(base_dir, 'config.ini')

# Create getlist() converter, used in cmd_config.py for ticker symbols
# conf_obj = ConfigParser(allow_no_value=True, converters={'list': lambda x: [i.strip() for i in x.split(',')]})
conf_obj = ConfigParser(converters={'list': lambda x: [i.strip() for i in x.split(',')]})

logger_conf = os.path.join(base_dir, 'logger.ini')
logging.config.fileConfig(fname=logger_conf)


try:
    load_dotenv()
    alpha_key = os.getenv('ALPHA_KEY')
    tiingo_key = os.getenv('TIINGO_KEY')
except:
    pass


__all__ = [
    "_value",
]


# def _value(conf_obj, key='Default', value=None):
def _value(v):
    """Convert string 'None' to None type
    ----------------------------------
    Parse 'None' strings in config.ini to Python None type.\n
    Parameters
    ----------
    `ctx_obj` : dictionary
        Python Click context object.\n
    `key` : string
        config.ini section name.\n
    `value` : string
        Config parameter name.\n
    """
    # v = conf_obj.get(key, value)
    # return None if v == ('None' or '') else v
    return None if v == ('None' or '') else v
