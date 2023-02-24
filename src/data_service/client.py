import logging

from configparser import ConfigParser

from src import config_file


conf_obj = ConfigParser(converters={'list': lambda x: [i.strip() for i in x.split(',')]})
conf_obj.read(config_file)

logger = logging.getLogger(__name__)


def get_data(ctx):
    """"""
    debug = ctx['debug']

    if debug: logger.debug(f"get_data(ctx={ctx})")
    if not debug: print(f"Saving to '{conf_obj.get('Default', 'chart_dir')}'\nstarting download")
