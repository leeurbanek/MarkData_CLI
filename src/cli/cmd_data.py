import logging
from configparser import ConfigParser

import click

from src import config_file, conf_obj, _none_value
from src.ctx_mgr import DatabaseConnectionManager
from src.data_service import client

conf_obj.read(config_file)

logger = logging.getLogger(__name__)


def _add_ohlc_table(conf_obj, ctx_obj, db_con):
    """Create the Open, High, Low, Close, AdjCl, Volume table.
    --------------------------------------------------------
    Fields are Date, Symbol, Open, High, Low, Close, Volume.\n
    Parameters
    ----------
    `ctx_obj` : dictionary
        Python Click context object.\n
    `db_con` : sqlite3.Connection object
        Connection to the time series database.\n
    """
    if ctx_obj['debug']:
        logger.debug(f"_add_ohlc_table(db_con={db_con})")

    table_name = 'ohlc' if _none_value(conf_obj, value='db_table') else table_name

    db_con.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            Date    TIMESTAMP   NOT NULL,
            Symbol  TEXT        NOT NULL,
            Open    INTEGER     NOT NULL,
            High    INTEGER     NOT NULL,
            Low     INTEGER     NOT NULL,
            Close   INTEGER     NOT NULL,
            Volume  INTEGER     NOT NULL,
            PRIMARY KEY (Date, Symbol));
        ''')


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
            _add_ohlc_table(conf_obj=ctx.obj, ctx_obj=ctx.obj, db_con=db_con)

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
            # client.get_tiingo_data(conf_obj=conf_obj, ctx_obj=ctx.obj)
            client.get_tiingo_data(ctx_obj=ctx.obj)

    else:  # print default message
        click.echo(f"""Usage: markdata data [OPTIONS] [SYMBOL]...
Try 'markdata data --help' for help.""")

# subprocess.run(['open', filename], check=True)

# =======

# eem = [{'date': '2023-03-09T00:00:00.000Z', 'close': 38.04, 'high': 38.58, 'low': 37.96, 'open': 38.51, 'volume': 40118857, 'adjClose': 38.04, 'adjHigh': 38.58, 'adjLow': 37.96, 'adjOpen': 38.51, 'adjVolume': 40118857, 'divCash': 0.0, 'splitFactor': 1.0}, {'date': '2023-03-10T00:00:00.000Z', 'close': 37.84, 'high': 38.25, 'low': 37.8, 'open': 38.02, 'volume': 49316671, 'adjClose': 37.84, 'adjHigh': 38.25, 'adjLow': 37.8, 'adjOpen': 38.02, 'adjVolume': 49316671, 'divCash': 0.0, 'splitFactor': 1.0}]
# iwm = [{'date': '2023-03-09T00:00:00.000Z', 'close': 181.41, 'high': 187.27, 'low': 181.28, 'open': 186.73, 'volume': 33546890, 'adjClose': 181.41, 'adjHigh': 187.27, 'adjLow': 181.28, 'adjOpen': 186.73, 'adjVolume': 33546890, 'divCash': 0.0, 'splitFactor': 1.0}, {'date': '2023-03-10T00:00:00.000Z', 'close': 176.18, 'high': 180.39, 'low': 174.255, 'open': 180.39, 'volume': 67388021, 'adjClose': 176.18, 'adjHigh': 180.39, 'adjLow': 174.255, 'adjOpen': 180.39, 'adjVolume': 67388021, 'divCash': 0.0, 'splitFactor': 1.0}]

# =======

# connector.execute("insert into DATAGERMANY values (NULL,?,?,?,?,?)", *row)

# =======

# import datetime
# import sqlite3

# # get the current datetime and store it in a variable
# currentDateTime = datetime.datetime.now()

# # make the database connection with detect_types
# connection = sqlite3.connect(
#     'StudentAssignment.db',
#     detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES
# )
# cursor = connection.cursor()

# # create table in database
# createTable = '''CREATE TABLE ASSIGNMENT (
# 	StudentId INTEGER,
# 	StudentName VARCHAR(100),
# 	SubmissionDate TIMESTAMP);'''
# cursor.execute(createTable)

# # create query to insert the data
# insertQuery = """INSERT INTO ASSIGNMENT
# 	VALUES (?, ?, ?);"""

# # insert the data into table
# cursor.execute(insertQuery, (1, "Virat Kohli",
# 							currentDateTime))
# cursor.execute(insertQuery, (2, "Rohit Pathak",
# 							currentDateTime))
# print("Data Inserted Successfully !")

# # commit the changes,
# # close the cursor and database connection
# connection.commit()
# cursor.close()
# connection.close()

# =======

# import datetime
# import sqlite3

# make a database connection and cursor object
# connection = sqlite3.connect(
#     'StudentAssignment.db',
#     detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES
# )
# cursor = connection.cursor()

# # select query to retrieve data
# cursor.execute("SELECT * from ASSIGNMENT where StudentId = 2")
# fetchedData = cursor.fetchall()

# # to access specific fetched data
# for row in fetchedData:
# 	StudentID = row[0]
# 	StudentName = row[1]
# 	SubmissionDate = row[2]
# 	print(StudentName, ", ID -",
# 		StudentID, "Submitted Assignments")
# 	print("Date and Time : ",
# 		SubmissionDate)
# 	print("Submission date type is",
# 		type(SubmissionDate))

# # commit the changes,
# # close the cursor and database connection
# cursor.close()
# connection.close()
