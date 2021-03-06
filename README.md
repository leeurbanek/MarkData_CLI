# MarkData_CLI

> Stock ***Mark***et ***Data*** ***C***ommand ***L***ine ***I***nterface.

## Features

* Automaticaly update 'ohlc' database
* Create SQLite3 database for 'ohlc' data
* Download daily and weekly stock charts
* View charts in your default viewer

## Requirements

* [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [click](https://palletsprojects.com/p/click/)
* [colorlog](https://pypi.org/project/colorlog/)
* [Pillow](https://pillow.readthedocs.io/en/stable/)
* [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/index.html)
* [python-dotenv](https://pypi.org/project/python-dotenv/)
* [selenium](https://selenium-python.readthedocs.io/)
* [requests](https://docs.python-requests.org/en/master/)
* [tqdm](https://pypi.org/project/tqdm/)

## Installation

We are going to use the command line so open a terminal to get started. Linux and Mac users will probably have `bash` installed which will be fine, Windows users will have to make the necessary translations to follow along.

First let's check if Git is installed. At the `$` prompt type `git --version` and press enter. You should see something like `git version 2.xx.x`. If not go to [Installing Git – the easy way](https://gist.github.com/derhuerst/1b15ff4652a867391f03) and follow the installation instructions for your system.

Now create a clone of this Git repo on your computer. In the terminal enter `cd` to switch into your work directory then at the prompt type the following:

```
git clone <url of this repository> marcli_pkg && cd marcli_pkg
```

## Configuration

Install [AdBlocker Ultimate](https://adblockultimate.net/).  Next you need to find where adblockultimate was installed.  For example in Firefox:
1. Go to the url about:support.
2. In 'Application Basics' table, next to 'Profile Directory', click button 'Open Directory'.
3. Open extensions folder. The file you want ends with 'adblockultimate.net.xpi'.

Make a note of this file path or create a link to the file.  Now run `markdata config --ad_block` and add the path or link.

If you are using Windows set `markdata config --gecko_drv` to the location of the [Firefox driver](https://github.com/mozilla/geckodriver/releases) that Selenium will need.

## Usage

Open a terminal if it was closed and start the virtual environment you set up earlier.

Make sure you edited the `.env` and `config.ini` files to suit your preferences then type the following at the prompt to get started:

```
markdata --help
```

If all went well you should see something like this:

```
Usage: markdata [OPTIONS] COMMAND [ARGS]...

  Markdata_CLI: A stock MARket Command Line Interface data retrieval tool.

Options:
  --help  Show this message and exit.

Commands:
  chart   Retrieve sharp charts from Stockcharts.com.
  view    View charts saved in your default directory.
```
To view the `--help` text for the other commands, 'chart' for example, you can use:
```
markdata chart --help
```
## General Notes

To learn more about StockCharts.com and the exelect services they offer visit [StockCharts.com](https://stockcharts.com/) be sure to check out the ChartSchool tab too.

If you notice any errors, mistakes, or opportunities for improvement please let me know.
