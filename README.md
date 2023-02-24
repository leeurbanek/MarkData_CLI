# MarkData_CLI

> Stock ***MARK***et ***DATA*** ***C***ommand ***L***ine ***I***nterface

## Features

* Download daily or weekly stock charts

## Requirements

* [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [click](https://palletsprojects.com/p/click/)
* [colorlog](https://pypi.org/project/colorlog/)
* [Pillow](https://pillow.readthedocs.io/en/stable/)
* [pytest](https://pypi.org/project/pytest/)
* [requests](https://docs.python-requests.org/en/master/)
* [requests-html](https://pypi.org/project/requests-html/)
* [selenium](https://pypi.org/project/selenium/)

## Installation

Copy or clone this app to your computer. Use Python's built in venv module to create a virtual environment. In the directory where this app located enter `python3 -m venv venv` to create. Start the environment with `source venv/bin/activate` type `pip install --update pip setuptools wheel` to update. Finally `pip install -e .` installs the requirements and also installs the app in editable mode. Type `markdata-cli --help` and you should see:
``` shell
Usage: markdata [OPTIONS] COMMAND [ARGS]...

  MarkData_CLI: stock MARKet DATA Command Line Interface

Options:
  --debug / --no-debug  Enable/disable debug logging.
  --version             Show the version and exit.
  --help                Show this message and exit.

Commands:
  chart   Fetch online stockcharts from StockCharts.com
  config  Setup or change config settings in 'config.ini'
```

## Configuration

After successful install you will want to setup a few things. First, set the path to the where you are going to store your downloaded charts. Use `markdata-cli config --chart-dir`, follow the prompts and enter the absolute path to the directory. Next, if you want to have default ticker symbols to download set the `markdata-cli config --symbol` option too. Note that if you are going to use the Selenium version of the webscraper uncomment the line near the top of `src/chart_service/client.py` then [download the driver](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/) for chromium and save it to the install folder. Try `markdata-cli config --help` for help.

## Usage

Download stock charts from StockCharts.com see `markdata-cli chart --help`.
