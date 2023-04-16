import logging.config
import os
from configparser import ConfigParser
from dotenv import load_dotenv


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_file = os.path.join(base_dir, 'config.ini')

# Create getlist() converter, used in cmd_config.py for ticker symbols
# conf_obj = ConfigParser(allow_no_value=True, converters={'list': lambda x: [i.strip() for i in x.split(',')]})
conf_obj = ConfigParser(converters={'list': lambda x: [i.strip() for i in x.split(',')]})
conf_obj.read(config_file)

logger_conf = os.path.join(base_dir, 'logger.ini')
logging.config.fileConfig(fname=logger_conf)


try:
    load_dotenv()
    alpha_key = os.getenv('ALPHA_KEY')
    tiingo_key = os.getenv('TIINGO_KEY')
except:
    pass


__all__ = [
    "_none_value",
]


def _none_value(conf_obj, key='Default', value=None):
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
    print(f"\n\nkey={key}, value={value}")
    print(f"conf_obj: {conf_obj}")
    v = conf_obj.get(key, value)
    print(f"v = {v}")
    return None if v == ('None' or '') else v


if __name__ == '__main__':
    print(f"_none_value(): {_none_value(conf_obj, value='start')}, type: {type(_none_value(conf_obj,  value='start'))}")
