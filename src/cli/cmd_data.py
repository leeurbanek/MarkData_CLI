import logging
from configparser import ConfigParser

import click

from src import config_file, conf_obj
from src.ctx_mgr import DatabaseConnectionManager
from src.data_service import client

conf_obj.read(config_file)

logger = logging.getLogger(__name__)


def _add_ohlc_table(ctx_obj, db_con):
    """"""
    if ctx_obj['debug']:
        logger.debug(f"_add_ohlc_table(db_con={db_con})")

# def add_ohlc_table(db_con, table_name):
#     """Create the Open, High, Low, Close, AdjCl, Volume table.
#     --------------------------------------------------------
#     Data is adjusted daily historical from Alpha Vantage.\n
#     See https://www.alphavantage.co/documentation/#dailyadj.\n
#     Fields are Date, Open, High, Low, Close, AdjCl, Volume.\n
#     Parameters
#     ----------
#     `db_con` : sqlite3.Connection object
#         Connection to the time series database.\n
#     `table_name` : string
#         Name of the table to create.\n
#     """
#     db_con.execute(f'''
#         CREATE TABLE IF NOT EXISTS {table_name} (
#             Date     DATE     NOT NULL,
#             Open     INTEGER  NOT NULL,
#             High     INTEGER  NOT NULL,
#             Low      INTEGER  NOT NULL,
#             Close    INTEGER  NOT NULL,
#             AdjCl    INTEGER  NOT NULL,
#             Volume   INTEGER  NOT NULL,
#             PRIMARY  KEY (Date));
#         ''')
# =======

# # create table in database
# createTable = '''CREATE TABLE ASSIGNMENT (
# 	StudentId INTEGER,
# 	StudentName VARCHAR(100),
# 	SubmissionDate TIMESTAMP);'''
# cursor.execute(createTable)


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
        # check if defaults are set
        if ctx.obj['Default']['work_dir'] == 'None':
            click.echo("Error: Work directory not set\nTry 'markdata config --help' for help.")
            return
        if ctx.obj['Default']['database'] == 'None':
            click.echo("Error: The database name is not set\nTry 'markdata config --help' for help.")
            return
        # create database and add talbe if not exist
        with DatabaseConnectionManager(db_path=f"{ctx.obj['Default']['work_dir']}/{ctx.obj['Default']['database']}", mode='rwc') as db_con:
            _add_ohlc_table(ctx_obj=ctx.obj, db_con=db_con)

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
            client.get_tiingo_data(conf_obj=conf_obj, ctx_obj=ctx.obj)

    else:  # print default message
        click.echo(f"""Usage: markdata data [OPTIONS] [SYMBOL]...
Try 'markdata data --help' for help.""")

# subprocess.run(['open', filename], check=True)
