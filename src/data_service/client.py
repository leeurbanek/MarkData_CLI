import logging


logger = logging.getLogger(__name__)


def select_data_provider(ctx_obj):
    """"""
    if ctx_obj['debug']: logger.debug("select_data_provider(ctx_obj)")

    if ctx_obj['opt_trans'] == 'alpha':
        _get_alpha_data(ctx_obj)

    elif ctx_obj['opt_trans'] == 'tiingo':
        _get_tiingo_data(ctx_obj)


def _get_alpha_data(ctx_obj):
    if ctx_obj['debug']:
        logger.debug(f"_get_alpha_data(ctxj={ctx_obj})")
    from src.data_service.reader import AlphaReader
    reader = AlphaReader(
        symbol=ctx_obj['symbol']
    )


def _get_tiingo_data(ctx_obj):
    if ctx_obj['debug']:
        logger.debug(f"_get_tiingo_data(ctx={ctx_obj})")
    from src.data_service.reader import TiingoReader

    reader = TiingoReader(
        symbol=ctx_obj['symbol']
    )
    reader.write_data()
