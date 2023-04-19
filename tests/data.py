import datetime


ctx_obj = {
    'Default': {
        'database': 'db.sqlite',
        'db_table': 'None',
        'work_dir': 'temp',
        'start': 'None',
        'end': 'None'
    },
    'Scraper': {
        'adblock': 'None',
        'base_url': 'https://stockcharts.com/h-sc/ui?s=',
        'driver': 'chromedriver'
    },
    'Ticker': {
        'symbol': 'EEM, IWM, LQD'
    },
    'debug': True,
    'opt_trans': 'alpha',
    'symbol': ['EEM', 'IWM', 'LQD']
}

json_eem = [
    {'date': '2023-04-12T00:00:00.000Z', 'close': 39.39, 'high': 39.83, 'low': 39.31, 'open': 39.8, 'volume': 29882231, 'adjClose': 39.39, 'adjHigh': 39.83, 'adjLow': 39.31, 'adjOpen': 39.8, 'adjVolume': 29882231, 'divCash': 0.0, 'splitFactor': 1.0},
    {'date': '2023-04-13T00:00:00.000Z', 'close': 39.93, 'high': 40.0, 'low': 39.805, 'open': 39.85, 'volume': 28752750, 'adjClose': 39.93, 'adjHigh': 40.0, 'adjLow': 39.805, 'adjOpen': 39.85, 'adjVolume': 28752750, 'divCash': 0.0, 'splitFactor': 1.0},
    {'date': '2023-04-14T00:00:00.000Z', 'close': 39.72, 'high': 39.92, 'low': 39.53, 'open': 39.75, 'volume': 26673227, 'adjClose': 39.72, 'adjHigh': 39.92, 'adjLow': 39.53, 'adjOpen': 39.75, 'adjVolume': 26673227, 'divCash': 0.0, 'splitFactor': 1.0}
]

list_eem = [
    [datetime.date(2023, 4, 12), 'EEM', 3980, 3983, 3931, 3939, 29882231],
    [datetime.date(2023, 4, 13), 'EEM', 3985, 4000, 3980, 3993, 28752750],
    [datetime.date(2023, 4, 14), 'EEM', 3975, 3992, 3953, 3972, 26673227]
]

json_iwm = [
    {'date': '2023-04-12T00:00:00.000Z', 'close': 175.84, 'high': 178.98, 'low': 175.58, 'open': 178.82, 'volume': 27018113, 'adjClose': 175.84, 'adjHigh': 178.98, 'adjLow': 175.58, 'adjOpen': 178.82, 'adjVolume': 27018113, 'divCash': 0.0, 'splitFactor': 1.0},
    {'date': '2023-04-13T00:00:00.000Z', 'close': 178.17, 'high': 178.685, 'low': 175.93, 'open': 176.54, 'volume': 23259875, 'adjClose': 178.17, 'adjHigh': 178.685, 'adjLow': 175.93, 'adjOpen': 176.54, 'adjVolume': 23259875, 'divCash': 0.0, 'splitFactor': 1.0},
    {'date': '2023-04-14T00:00:00.000Z', 'close': 176.51, 'high': 179.22, 'low': 175.34, 'open': 178.33, 'volume': 29600374, 'adjClose': 176.51, 'adjHigh': 179.22, 'adjLow': 175.34, 'adjOpen': 178.33, 'adjVolume': 29600374, 'divCash': 0.0, 'splitFactor': 1.0}
]

list_iwm = [
    [datetime.date(2023, 4, 12), 'IWM', 17882, 17898, 17558, 17584, 27018113],
    [datetime.date(2023, 4, 13), 'IWM', 17654, 17868, 17593, 17817, 23259875],
    [datetime.date(2023, 4, 14), 'IWM', 17833, 17922, 17534, 17651, 29600374]
]

json_lqd = [
    {'date': '2023-04-12T00:00:00.000Z', 'close': 109.56, 'high': 110.31, 'low': 109.39, 'open': 110.26, 'volume': 20049150, 'adjClose': 109.56, 'adjHigh': 110.31, 'adjLow': 109.39, 'adjOpen': 110.26, 'adjVolume': 20049150, 'divCash': 0.0, 'splitFactor': 1.0},
    {'date': '2023-04-13T00:00:00.000Z', 'close': 109.75, 'high': 110.045, 'low': 109.55, 'open': 109.9, 'volume': 18589080, 'adjClose': 109.75, 'adjHigh': 110.045, 'adjLow': 109.55, 'adjOpen': 109.9, 'adjVolume': 18589080, 'divCash': 0.0, 'splitFactor': 1.0},
    {'date': '2023-04-14T00:00:00.000Z', 'close': 109.39, 'high': 109.57, 'low': 109.03, 'open': 109.44, 'volume': 16218945, 'adjClose': 109.39, 'adjHigh': 109.57, 'adjLow': 109.03, 'adjOpen': 109.44, 'adjVolume': 16218945, 'divCash': 0.0, 'splitFactor': 1.0}
]

list_lqd = [
    [datetime.date(2023, 4, 12), 'LQD', 11026, 11031, 10939, 10956, 20049150],
    [datetime.date(2023, 4, 13), 'LQD', 10990, 11004, 10955, 10975, 18589080],
    [datetime.date(2023, 4, 14), 'LQD', 10944, 10957, 10903, 10939, 16218945]
]
