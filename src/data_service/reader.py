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
        self.end = '2023-04-04'
        self.freq = 'daily'
        self.start = '2023-03-31'

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
        # data = requests.get(f"{self.base_url}/{self.freq}/{symbol}/prices?startDate={self.start}&endDate={self.end}&token={self.api_key}", headers=headers)
        # return data.json()
        json_data = [  # IWM
            {'date': '2023-03-31T00:00:00.000Z', 'close': 178.4, 'high': 178.64, 'low': 176.37, 'open': 176.4, 'volume': 39602850, 'adjClose': 178.4, 'adjHigh': 178.64, 'adjLow': 176.37, 'adjOpen': 176.4, 'adjVolume': 39602850, 'divCash': 0.0, 'splitFactor': 1.0},
            {'date': '2023-04-03T00:00:00.000Z', 'close': 178.48, 'high': 179.78, 'low': 176.49, 'open': 178.95, 'volume': 27608982, 'adjClose': 178.48, 'adjHigh': 179.78, 'adjLow': 176.49, 'adjOpen': 178.95, 'adjVolume': 27608982, 'divCash': 0.0, 'splitFactor': 1.0},
            {'date': '2023-04-04T00:00:00.000Z', 'close': 175.35, 'high': 179.1, 'low': 174.32, 'open': 178.92, 'volume': 33487181, 'adjClose': 175.35, 'adjHigh': 179.1, 'adjLow': 174.32, 'adjOpen': 178.92, 'adjVolume': 33487181, 'divCash': 0.0, 'splitFactor': 1.0}
        ]
        return json_data

    # def parse_price_data(self, symbol):
    #     """Returns a list of lists"""
    #     data_list = []
    #     for item in self._read_one_price_data(symbol):
    #         data = [
    #             date(*map(int, item.get('date')[:10].split('-'))),
    #             symbol.upper(),
    #             round(item.get('adjOpen')*100),
    #             round(item.get('adjHigh')*100),
    #             round(item.get('adjLow')*100),
    #             round(item.get('adjClose')*100),
    #             item.get('adjVolume'),
    #         ]
    #         data_list.append(data)
    #     return data_list

    def parse_price_data(self, symbol):
        """Returns a generator object"""
        for item in self._read_one_price_data(symbol):
            data = [
                date(*map(int, item.get('date')[:10].split('-'))),
                symbol.upper(),
                round(item.get('adjOpen')*100),
                round(item.get('adjHigh')*100),
                round(item.get('adjLow')*100),
                round(item.get('adjClose')*100),
                item.get('adjVolume'),
            ]
            yield data

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
