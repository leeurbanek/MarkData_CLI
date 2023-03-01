import logging

from configparser import ConfigParser

from src import config_file


conf_obj = ConfigParser(converters={'list': lambda x: [i.strip() for i in x.split(',')]})
conf_obj.read(config_file)

logger = logging.getLogger(__name__)


def choose_data_provider(ctx):
    """"""
    if ctx['debug']: logger.debug(f"choose_data_provider(ctx={ctx})")

    if ctx['opt_trans'] == 'alpha':
        get_alphavantage_data(conf_obj, ctx)

    elif ctx['opt_trans'] == 'tiingo':
        get_tiingo_data(conf_obj, ctx)


def get_alphavantage_data(conf_obj, ctx_obj):
    from src.data_service.reader.alpha import AlphaReader
    data = AlphaReader()

    if ctx_obj['debug']:
        logger.debug(f"get_alphavantage_data(ctx_obj={ctx_obj})")
        logger.debug(f"alphavantage key: {data.key}")


def get_tiingo_data(conf_obj, ctx_obj):
    from src.data_service.reader.tiingo import TiingoReader
    data = TiingoReader()

    if ctx_obj['debug']:
        logger.debug(f"get_tiingo_data(ctx_obj={ctx_obj})")
        logger.debug(f"tiingo key: {data.key}")


def write_to_database():
    pass
