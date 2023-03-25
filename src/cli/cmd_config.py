import logging
import os

import click

from src import config_file, conf_obj


conf_obj.read(config_file)

logger = logging.getLogger(__name__)


def update_default_db_path(conf_obj, ctx_obj):
    """"""
    if ctx_obj['debug']:
        logger.debug(f"update_default_db_path(section={ctx_obj['section']}, opt_trans={ctx_obj['opt_trans']})")

    current = f"{conf_obj.get('Default', 'db_path')}"
    click.confirm(
        f"Current {ctx_obj['opt_trans']}: '{current}'\nDo you want to change this?", abort=True
        )
    new_value =  click.prompt(f"Please enter a valid {ctx_obj['opt_trans']}", type=str)
    if os.path.exists(f"{new_value}"):
        click.confirm(
            f"WARNING: '{new_value}' directory exists, cannot create.\n\tUse '{new_value}' anyway?", abort=True
            )
        return new_value
    else:
        try:
            os.makedirs(f"{new_value}")
            return new_value
        except:
            print(f"OSError '{new_value}': try using absolute path to chart directory.")


def update_default_work_dir(conf_obj, ctx_obj):
    """"""
    if ctx_obj['debug']:
        logger.debug(f"update_default_work_dir(section={ctx_obj['section']}, opt_trans={ctx_obj['opt_trans']})")

    current = f"{conf_obj.get('Default', 'work_dir')}"
    click.confirm(
        f"Current {ctx_obj['opt_trans']}: '{current}'\nDo you want to change this?", abort=True
        )
    new_value =  click.prompt(f"Please enter a valid {ctx_obj['opt_trans']}", type=str)
    if os.path.exists(f"{new_value}"):
        click.confirm(
            f"WARNING: '{new_value}' directory exists, cannot create.\n\tUse '{new_value}' anyway?", abort=True
            )
        return new_value
    else:
        try:
            os.makedirs(f"{new_value}")
            return new_value
        except:
            print(f"OSError '{new_value}': try using absolute path to chart directory.")


def update_ticker_symbol(conf_obj, ctx_obj):
    """"""
    if ctx_obj['debug']:
        logger.debug(f"update_ticker_symbol(conf_obj={conf_obj}, ctx_obj={ctx_obj})")

    current = f"{conf_obj.get('Ticker', 'symbol')}"
    click.echo(f"Current {ctx_obj['opt_trans']}: '{current}'\nTry 'markdata config --help' for help.")

    # Current ticker symbols from config.ini
    conf_symbol = conf_obj.getlist('Ticker', 'symbol')
    # ctx_obj symbols from command line arquments
    ctx_symbol = ctx_obj['symbol']

    extend, remove = [], []  # create lists

    # Add symbols to extend/remove list
    for v in ctx_symbol:
        v = v.upper().strip()
        if v in conf_symbol:
            remove.append(v)
        else:
            extend.append(v.strip())

    # Extend/remove items in symbol_list
    if extend:
        click.confirm(
            f"Adding symbols: {', '.join(extend)}\nDo you want to continue?", abort=True
            )
        conf_symbol.extend(extend)
    if remove:
        click.confirm(
            f"Removing symbols: {', '.join(remove)}\nDo you want to continue?", abort=True
            )
        for r in remove:
            conf_symbol.remove(r)

    # Convert symbol_list to new_value string
    new_value = ', '.join(conf_symbol)
    return new_value


def write_new_value_to_config():
    """Write new value to config.ini"""
    with open(config_file, 'w') as f:
        conf_obj.write(f)


@click.command('config', short_help="Setup or change config settings in 'config.ini'", help="""
\b
NAME
    config -- Setup or change config settings
\b
SYNOPSIS
    config [Options] [argument1 argument2 argument3 ...]
\b
DESCRIPTION
    The config utility writes any specified arguments, separated
    by single blank (' ') characters, to the config.ini file.
    Use absolute paths for directories, etc.  Quotes are not needed.
""")

@click.argument('arguments', nargs=-1, default=None, required=False, type=str)

# config Data
@click.option(
    '--create-db', 'opt_trans', flag_value='create_db',
    help=f"Create new database, current: {conf_obj.get('Default', 'database')}"
)
@click.option(
    '--db-path', 'opt_trans', flag_value='db_path',
    help=f"Change database path, current: '{conf_obj.get('Default', 'db_path')}"
)

# config Ticker
@click.option(
    '-s', '--symbol', 'opt_trans', flag_value='symbol',
    help=f"Add/remove ticker symbols, current: '{conf_obj.get('Ticker', 'symbol')}'"
)

# config Work directory
@click.option(
    '-w', '--work-dir', 'opt_trans', flag_value='work_dir',
    help=f"Change working directory, current: '{conf_obj.get('Default', 'work_dir')}'"
)



@click.pass_context
def cli(ctx, opt_trans, arguments):
    """Run config command"""
    if ctx.obj['debug']:
        logger.debug(f"cli(ctx, opt_trans={opt_trans}, arguments={arguments })")

    if opt_trans:
        ctx.obj['opt_trans'] = opt_trans  # add opt_trans to ctx

        if opt_trans == 'work_dir':
            section = conf_obj['Default']
            ctx.obj['section'] = section  # add section to ctx
            new_value = update_default_work_dir(conf_obj, ctx.obj)
            if new_value:
                section[opt_trans] = new_value
                write_new_value_to_config()

        elif opt_trans == 'db_path':
            section = conf_obj['Default']
            ctx.obj['section'] = section  # add section to ctx
            new_value = update_default_db_path(conf_obj, ctx.obj)
            if new_value:
                section[opt_trans] = new_value
                write_new_value_to_config()

        elif opt_trans == 'symbol':
            section = conf_obj['Ticker']
            ctx.obj['section'] = section  # add section to ctx
            ctx.obj['symbol'] = arguments
            new_value = update_ticker_symbol(conf_obj, ctx.obj)
            if new_value:
                section[opt_trans] = new_value
                write_new_value_to_config()
