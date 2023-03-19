import json
import os
import requests
from datetime import date

from dotenv import load_dotenv

from src.data_service import _BaseReader


load_dotenv()


class AlphaReader(_BaseReader):
    """"""
    def __init__(self) -> None:
        super().__init__()
        self.api_key = os.getenv('ALPHA_KEY')


class TiingoReader(_BaseReader):
    """"""
    def __init__(self) -> None:
        super().__init__()
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
        return "https://api.tiingo.com/tiingo"

    def _read_one_price_data(self, symbol):
        """"""
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Token {self.api_key}',
        }
        # json_data = requests.get(f"{self.base_url}/{self.freq}/{symbol}/prices?startDate={self.start}&endDate={self.end}&token={self.api_key}", headers=headers)
        json_data = {'date': '2023-03-09T00:00:00.000Z', 'close': 38.04, 'high': 38.58, 'low': 37.96, 'open': 38.51, 'volume': 40118857, 'adjClose': 38.04, 'adjHigh': 38.58, 'adjLow': 37.96, 'adjOpen': 38.51, 'adjVolume': 40118857, 'divCash': 0.0, 'splitFactor': 1.0}
        return json_data

    def parse_price_data(self, symbol):
        """"""
        price_data = self._read_one_price_data(symbol)
        data_list = [
            date(*map(int, price_data.get('date')[:10].split('-'))),
            round(price_data.get('adjOpen')*100),
            round(price_data.get('adjHigh')*100),
            round(price_data.get('adjLow')*100),
            round(price_data.get('adjClose')*100),
            price_data.get('adjVolume'),
        ]
        return data_list

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
