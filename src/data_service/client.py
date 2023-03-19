import logging


logger = logging.getLogger(__name__)


def get_alpha_data(ctx_obj):
    """"""
    if ctx_obj['debug']:
        logger.debug(f"get_alpha_data(ctxj={ctx_obj})")
    from src.data_service.reader import AlphaReader
    reader = AlphaReader()
    print(f"reader: {reader}")


def get_tiingo_data(ctx_obj):
    """"""
    if ctx_obj['debug']:
        logger.debug(f"get_tiingo_data(ctx={ctx_obj})")
    from src.data_service.reader import TiingoReader

    reader = TiingoReader()
    for symbol in ctx_obj['symbol']:
        data_list = reader.parse_price_data(symbol)
        _write_data_to_sqlite_db(data_list)


def _write_data_to_sqlite_db(data_list):
    """"""
    print(f"data_list: {data_list}")
