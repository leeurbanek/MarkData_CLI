import json
import os
import requests

from dotenv import load_dotenv

from src.data_service import _BaseReader


load_dotenv()


class AlphaReader(_BaseReader):
    """"""
    def __init__(self, ticker_list) -> None:
        super().__init__(ticker_list)
        self.api_key = os.getenv('ALPHA_KEY')


class TiingoReader(_BaseReader):
    """"""
    def __init__(self, ticker_list) -> None:
        super().__init__(ticker_list)
        self.api_key = os.getenv('TIINGO_KEY')
        self.end = '2023-03-10'
        self.freq = 'daily'
        self.start = '2023-03-09'


    @property
    def params(self):
        """Parameters to use in API calls"""
        return {
            'startDate'
            # "startDate": self.start.strftime("%Y-%m-%d"),
            # "endDate": self.end.strftime("%Y-%m-%d"),
            # "resampleFreq": self.freq,
            # "format": "json",
        }

    @property
    def base_url(self):
        """API URL"""
        url = "https://api.tiingo.com/tiingo"
        return url

    def _read_one_price_data(self):
        """"""
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Token {self.api_key}',
        }
        for ticker in self.ticker_list:
            # price = requests.get(f"{self.base_url}/{self.freq}/{ticker}/prices?startDate={self.start}&endDate={self.end}&token={self.api_key}", headers=headers)
            # yield price.json()
            price = f"{self.base_url}/{self.freq}/{ticker}/prices?startDate={self.start}&endDate={self.end}&token={self.api_key}"
            yield ticker, price

    def write_price_data_to_db(self):
        """"""
        price_data = self._read_one_price_data()

        while True:
            try:
                print(f"\n{next(price_data)}")
            except StopIteration:
                break

# =======

# Historical Prices
# https://api.tiingo.com/tiingo/daily/<ticker>/prices?startDate=2012-1-1&endDate=2016-1-1

# import requests
# headers = {
#     'Content-Type': 'application/json'
# }
# requestResponse = requests.get("https://api.tiingo.com/tiingo/daily/aapl/prices?startDate=2019-01-02&token=Not logged-in or registered. Please login or register to see your API Token", headers=headers)
# print(requestResponse.json())

eem = [{'date': '2023-03-09T00:00:00.000Z', 'close': 38.04, 'high': 38.58, 'low': 37.96, 'open': 38.51, 'volume': 40118857, 'adjClose': 38.04, 'adjHigh': 38.58, 'adjLow': 37.96, 'adjOpen': 38.51, 'adjVolume': 40118857, 'divCash': 0.0, 'splitFactor': 1.0}, {'date': '2023-03-10T00:00:00.000Z', 'close': 37.84, 'high': 38.25, 'low': 37.8, 'open': 38.02, 'volume': 49316671, 'adjClose': 37.84, 'adjHigh': 38.25, 'adjLow': 37.8, 'adjOpen': 38.02, 'adjVolume': 49316671, 'divCash': 0.0, 'splitFactor': 1.0}]
iwm = [{'date': '2023-03-09T00:00:00.000Z', 'close': 181.41, 'high': 187.27, 'low': 181.28, 'open': 186.73, 'volume': 33546890, 'adjClose': 181.41, 'adjHigh': 187.27, 'adjLow': 181.28, 'adjOpen': 186.73, 'adjVolume': 33546890, 'divCash': 0.0, 'splitFactor': 1.0}, {'date': '2023-03-10T00:00:00.000Z', 'close': 176.18, 'high': 180.39, 'low': 174.255, 'open': 180.39, 'volume': 67388021, 'adjClose': 176.18, 'adjHigh': 180.39, 'adjLow': 174.255, 'adjOpen': 180.39, 'adjVolume': 67388021, 'divCash': 0.0, 'splitFactor': 1.0}]


if __name__ == '__main__':
    from datetime import date

    price_data = eem
    for record in price_data:
        row = [
            'EEM',
            date(*map(int, record.get('date')[:10].split('-'))),
            round(record.get('adjOpen')*100),
            round(record.get('adjHigh')*100),
            round(record.get('adjLow')*100),
            round(record.get('adjClose')*100),
            record.get('adjVolume'),
        ]
        print(row)
        print([type(item) for item in row])

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
