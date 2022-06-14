import os
from configparser import ConfigParser

import click

from app.data_service import sqlite_client


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG = os.path.join(BASE_DIR, 'config.ini')

conf_obj = ConfigParser()
conf_obj.read(CONFIG)


@click.group()
def run():
    """MarkData_CLI: stock MARKet DATA Command Line Interface"""
    pass


# Config options
# ==============

@run.command()
@click.argument('new_default', nargs=1, default=None, required=True, type=str)

# Alpha Vantage API key
@click.option(
    '--av_api_key', 'transform', flag_value='av_api_key',
    help='Your Alpha Vantage API key'
    )

# Path or symbolic link to Adblockultimate
@click.option(
    '--ad_block', 'transform', flag_value='ad_block',
    help='Location or link to Adblockultimate'
    )

# Path to the chart directory
@click.option(
    '--chart_dir', 'transform', flag_value='chart_dir',
    help=f"Path to the chart dir. Current default: '{conf_obj['default']['chart_dir']}'"
    )

# Path to the default database
@click.option(
    '--db_path', 'transform', flag_value='db_path',
    help=f"Path to the database. Current default: '{conf_obj['default']['db_path']}'"
    )

# Location of the browser driver for Selenium
@click.option(
    '--gecko_drv', 'transform', flag_value='gecko_drv',
    help='Path to Gecko driver (Windows users)'
    )

def config(transform, new_default):
    """Change the default settings"""
    default = conf_obj['default']
    default[transform] = new_default
    if transform == 'chart_dir':
        if not os.path.exists(default[transform]):
            os.makedirs(default[transform])
    with open(CONFIG, 'w') as conf:
        conf_obj.write(conf)


# Database service
# ================

@run.command()
@click.argument('symbol', nargs=-1, default=None, type=str)
@click.option(
    '--db_path', default=True, flag_value=conf_obj['default']['db_path'],
    help=f"Path to the database. Current default db is '{conf_obj['default']['db_path']}'"
    )

def initdb(db_path, symbol):
    """Create a new database"""
    if db_path == 'None':
        click.echo("Please set the default db first.")
        click.echo("Try 'markdata config --help' for help.")
        return
    if os.path.exists(db_path):
        print(f'WARNING: the database {db_path} already exists!')
        click.confirm('  This operation will overwrite your database. Proceed?', abort=True)
    if symbol:
        symbol = [s.upper() for s in list(symbol)]
    sqlite_client.db_creator(db_path, symbol)


# @run.command()
# @click.argument('table', nargs=-1, default=None, type=str)
# @click.option(
#     '--db_path', default=True, flag_value=conf_obj['default']['db_path'],
#     help=f"Path to the database. Current default db is '{conf_obj['default']['db_path']}'"
#     )

# @run.command()
# def drop_table(db_path, table):
#     """"""
#     pass


# @run.command()
# @click.option(
#     '-u', '--update', default=DB_PATH,
#     help=f"Location of the database. Default set in '.env' file. Current default: {DB_PATH}.",
#     )
# def update(db_path):
#     """Update Alpha Vantage price data\n
#     Data is from Alpha Vantage daily open/high/low/close/volume adjusted close values.
#     Defaults to equities in your symbols_list.
#     """
#     if not os.path.exists(db_path):
#         print(
#             f"INFO: the database {db_path} does not exist."
#             "\n Try 'marcli create --help' for help.\n"
#             )
#         return
#     database.updater(db_path)

if __name__ == '__main__':
    run()
