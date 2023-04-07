import logging

from src.ctx_mgr import DatabaseConnectionManager


logger = logging.getLogger(__name__)


def get_alpha_data(ctx_obj):
    """"""
    if ctx_obj['debug']:
        logger.debug(f"get_alpha_data(ctxj={ctx_obj})")
    from src.data_service.reader import AlphaReader
    reader = AlphaReader()
    print(f"reader: {reader}")


# def get_tiingo_data(conf_obj, ctx_obj):
def get_tiingo_data(ctx_obj):
    """"""
    if ctx_obj['debug']:
        logger.debug(f"get_tiingo_data(ctx={ctx_obj})")
    from src.data_service.reader import TiingoReader

    reader = TiingoReader()
    for symbol in ctx_obj['symbol']:
        data_list = reader.parse_price_data(symbol)
        _write_data_to_sqlite_db(ctx_obj, data_list)


def _write_data_to_sqlite_db(ctx_obj, data_list):
    """"""
    if ctx_obj['debug']:
        logger.debug(f"_write_data_to_sqlite_db(data_list={data_list})")

    db_path=f"{ctx_obj['Default']['work_dir']}/{ctx_obj['Default']['database']}"

    with DatabaseConnectionManager(db_path, mode='rw') as db_cur:
        for data in data_list:
            db_cur.execute("INSERT INTO ohlc VALUES (?,?,?,?,?,?,?);", data)


if __name__ == '__main__':
    ctx_obj = {'Default': {'work_dir': 'temp', 'database': 'db.sqlite'}, 'Scraper': {'adblock': 'None', 'base_url': 'https://stockcharts.com/h-sc/ui?s=', 'driver': 'chromedriver'}, 'Ticker': {'symbol': 'EEM, IWM'}, 'debug': True, 'opt_trans': 'tiingo', 'symbol': ['IWM']}
    get_tiingo_data(ctx_obj)
