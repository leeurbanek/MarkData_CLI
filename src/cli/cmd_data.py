import logging
from configparser import ConfigParser

import click

from src import config_file, conf_obj
from src.data_service import client


conf_obj.read(config_file)

logger = logging.getLogger(__name__)


@click.command('data', short_help="Fetch online OHLC price and volume data", help="""
\b
NAME
    data -- Retrieve OHLC data from various online sources
\b
SYNOPSIS
    data [Options] [ticker1 ticker2 ticker3 ...]
\b
DESCRIPTION
    The data utility attempts to retrieve OHLC data from various
    online sources.  If no ticker symbols are provided the default
    symbols from the config settings are used.  Try 'data --help'
    for help with config settings.
""")

@click.argument('symbol', nargs=-1, default=None, required=False, type=str)

@click.option('-a', '--alpha', 'opt_trans', flag_value='alpha', help='Fetch data from https://www.alphavantage.co/')
@click.option('-t', '--tiingo', 'opt_trans', flag_value='tiingo', help='Fetch data from https://api.tiingo.com/')

@click.pass_context
def cli(ctx, opt_trans, symbol):
    """Run chart command"""
    if ctx.obj['debug']:
        logger.debug(f"cli(ctx, opt_trans={opt_trans}, symbol={symbol })")

    if opt_trans:

        if symbol:  # use symbols from command line input
            symbol = [s.upper() for s in list(symbol)]
        else:  # use symbols from config.ini
            symbol = conf_obj.getlist('Ticker', 'symbol')

        # add parameters to context object
        ctx.obj['opt_trans'] = opt_trans
        ctx.obj['symbol'] = symbol

        # select data provider
        if opt_trans == 'alpha':
            client.get_alpha_data(ctx.obj)
        elif opt_trans == 'tiingo':
            client.get_tiingo_data(ctx.obj)

    else:  # print default message
        click.echo(f"""Usage: markdata data [OPTIONS] [SYMBOL]...
Try 'markdata data --help' for help.""")

# subprocess.run(['open', filename], check=True)
