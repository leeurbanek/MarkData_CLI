import logging

from configparser import ConfigParser

from src import alpha_key, config_file


conf_obj = ConfigParser(converters={'list': lambda x: [i.strip() for i in x.split(',')]})
conf_obj.read(config_file)

logger = logging.getLogger(__name__)


def get_data(ctx):
    """"""
    debug = ctx['debug']
    symbol = ctx['symbol']

    if debug: logger.debug(f"alpha_key={alpha_key}")
    if debug: logger.debug(f"get_data(ctx={ctx})")
    if not debug: print(f"Saving to '{conf_obj.get('Default', 'chart_dir')}'\nstarting download")

#     # count = len(period) * len(symbol)
#     [download(debug, p, s) for p in period for s in symbol]
#     if not debug: print('cleaning up... ', end='')
#     if not debug: print('\b finished.')


# def download(debug, period, symbol):
#     """"""
#     if debug: logger.debug(f"download(period={period} {type(period)}, symbol={symbol} {type(symbol)})")

#     start = WebScraper(debug, period, symbol)
#     try:
#         start.webscraper()
#     except:
#         pass
