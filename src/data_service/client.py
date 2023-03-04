import logging


logger = logging.getLogger(__name__)


def select_data_provider(ctx_obj):
    """"""
    if ctx_obj['debug']: logger.debug("select_data_provider(ctx_obj)")

    if ctx_obj['opt_trans'] == 'alpha':
        get_alpha_data(ctx_obj)

    elif ctx_obj['opt_trans'] == 'tiingo':
        get_tiingo_data(ctx_obj)


def get_alpha_data(ctx_obj):
    from src.data_service.reader import AlphaReader
    reader = AlphaReader()

    if ctx_obj['debug']:
        logger.debug(f"get_alpha_data(ctxj={ctx_obj})")
        logger.debug(f"{reader}")


def get_tiingo_data(ctx_obj):
    from src.data_service.reader import TiingoReader
    reader = TiingoReader()

    if ctx_obj['debug']:
        logger.debug(f"get_tiingo_data(ctx={ctx_obj})")
        logger.debug(f"{reader}")


def write_to_database():
    pass
