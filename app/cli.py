import os
from configparser import ConfigParser

import click

from app.service import database


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG = os.path.join(BASE_DIR, 'config.ini')

conf_obj = ConfigParser()
conf_obj.read(CONFIG)

DB_PATH = conf_obj.get('default', 'db_path')


@click.group()
def run():
    """MarkData_CLI: stock MARKet DATA Command Line Interface"""
    pass


# Config settings
# ===============

@run.command()
@click.argument('new_default', nargs=1, default=None, required=True, type=str)

# Set path to your chart directory
@click.option(
    '--chart_dir', 'transform', flag_value='chart_dir',
    help='Set path to your chart directory'
    )

# Set path to the default database
@click.option(
    '--db_path', 'transform', flag_value='db_path',
    help='Set path to the default database'
    )

def config(transform, new_default):
    """Change the default configuration settings"""
    default = conf_obj['default']
    default[transform] = new_default
    with open(CONFIG, 'w') as conf:
        conf_obj.write(conf)


# Database service
# ================

@run.command()
@click.argument('symbol', nargs=-1, default=None, type=str)
@click.option(
    '-db', '--db_path', default=DB_PATH,
    help=f"Location of the database. Default set in '.env' file. Current default: {DB_PATH}.",
    )
def initdb(db_path, symbol):
    """Create an sqlite3 database.\n
    Data is from Alpha Vantage daily open/high/low/close/volume adjusted close values.
    Defaults to equities in your symbols_list.
    """
    if os.path.exists(db_path):
        print(f'WARNING: the database {db_path} already exists!')
        click.confirm('  This operation will overwrite your database. Proceed?', abort=True)

    if symbol:
        symbol = [s.upper() for s in list(symbol)]
    database.creator(db_path, symbol)


@run.command()
def dropdb(db_path):
    """Not Implemented"""
    pass


@run.command()
@click.option(
    '-u', '--update', default=DB_PATH,
    help=f"Location of the database. Default set in '.env' file. Current default: {DB_PATH}.",
    )
def update(db_path):
    """Update an sqlite3 database.\n
    Data is from Alpha Vantage daily open/high/low/close/volume adjusted close values.
    Defaults to equities in your symbols_list.
    """
    if not os.path.exists(db_path):
        print(
            f"INFO: the database {db_path} does not exist."
            "\n Try 'marcli create --help' for help.\n"
            )
        return
    database.updater(db_path)
