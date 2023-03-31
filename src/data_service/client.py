import logging

from src.ctx_mgr import DatabaseConnectionManager


logger = logging.getLogger(__name__)


def _create_database(ctx_obj):
    """"""
    if ctx_obj['debug']:
        logger.debug(f"_create_database(ctx_obj={ctx_obj})")


def get_alpha_data(ctx_obj):
    """"""
    if ctx_obj['debug']:
        logger.debug(f"get_alpha_data(ctxj={ctx_obj})")
    from src.data_service.reader import AlphaReader
    reader = AlphaReader()
    print(f"reader: {reader}")


def get_tiingo_data(conf_obj, ctx_obj):
    """"""
    if ctx_obj['debug']:
        logger.debug(f"get_tiingo_data(ctx={ctx_obj})")
    from src.data_service.reader import TiingoReader

    reader = TiingoReader()
    for symbol in ctx_obj['symbol']:
        data_list = reader.parse_price_data(symbol)
        _write_data_to_sqlite_db(ctx_obj, data_list)


def _value(conf_obj, value):
    """"""
    v = conf_obj.get('Default', value)
    return None if v == 'None' else v


def _write_data_to_sqlite_db(ctx_obj, data_list):
    """"""
    if ctx_obj['debug']:
        logger.debug(f"_write_data_to_sqlite_db(data_list={data_list})")

    with DatabaseConnectionManager(
        db_path=f"{ctx_obj['Default']['work_dir']}/{ctx_obj['Default']['database']}", mode='rwc'
    ) as db_con:
        print(f"db_con={db_con}")
