import logging
from configparser import ConfigParser

import click

from src import config_file


conf_obj = ConfigParser(
    converters={'list': lambda x: [i.strip() for i in x.split(',')]}
    )
conf_obj.read(config_file)

logger = logging.getLogger(__name__)


@click.command('data', short_help="Fetch online OHLC price and volume data", help="""
\b
NAME
    data -- Get online OHLC data from various online sources
\b
SYNOPSIS
    data [Options] [ticker1 ticker2 ticker3 ...]
\b
DESCRIPTION
    Try 'data --help' for help with data options.
""")

@click.pass_context
def cli(ctx):
    """Run data command"""
    if ctx.obj['debug']:
        logger.debug(f"cli(ctx)")
