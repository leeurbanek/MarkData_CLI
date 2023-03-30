import logging

import click

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
        _write_data_to_sqlite_db(conf_obj, ctx_obj, data_list)


def _write_data_to_sqlite_db(conf_obj, ctx_obj, data_list):
    """"""
    if ctx_obj['debug']:
        logger.debug(f"_write_data_to_sqlite_db(data_list={data_list})")

    if not conf_obj.get('Default', 'database'):
        if not conf_obj.get('Default', 'work_dir'):
            click.echo("Error: Work directory not set\nTry 'markdata config --help' for help.")
            return
        else:
            _create_database(ctx_obj)

    db_path = f"{conf_obj.get('Default', 'work_dir')}/db.sqlite"
    with DatabaseConnectionManager(db_path=db_path, mode='rwc') as db_con:
        print(f"db_con: {db_con}")
