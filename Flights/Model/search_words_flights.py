import glob
import json
import os
from prettytable import PrettyTable
import constants as const

"""
This class is similar to the BBC article search class, 
the only difference is that we will go through 
all the columns in the JSON file of a flight.
"""

class SearchWordsFlights:
    def __init__(self, txt):
        self._words_to_check = txt
        self._flights_list_with_the_words_arrival = []
        self._flights_list_with_the_words_depart = []
        self.search_in_arrival_articles()
        self.search_in_depart_articles()

    def print_data_depart(self):
        table = PrettyTable(field_names=["  Airline Name  ",
                                         "  Flight Num  ",
                                         " From -> Israel ",
                                         "   Terminal   ",
                                         "  schedule_time  ",
                                         "  updated_time  ",
                                         "  Status  "
                                         ])
        table.add_rows(self._flights_list_with_the_words_depart)
        print(table)

    def print_data_arrival(self):
        table = PrettyTable(field_names=["  Airline Name  ",
                                         "  Flight Num  ",
                                         " Israel -> To ",
                                         "   Terminal   ",
                                         "  schedule_time  ",
                                         "  updated_time  ",
                                         "  Status  "
                                         ])
        table.add_rows(self._flights_list_with_the_words_arrival)
        print(table)

    def is_exit_in_info(self, flight_info):
        for data in flight_info:
            if self._words_to_check.lower() in data.lower():
                return True
            else:
                return False

    def search_in_arrival_articles(self):
        dir_jsons_path = const.FLIGHTS_ARRIVAL_JSONS_DIR
        for file_name in glob.glob(os.path.join(dir_jsons_path, '*.json')):  # Reading all json files
            with open(file_name, encoding='utf-8', mode='r') as file:
                json_data = json.loads(file.read())
                cur_content = [json_data["Airline"],
                               json_data["Flight_Num"]+"            ",
                               json_data["Status"]+"   ",
                               json_data["Update_Time"]+"    ",
                               json_data["Schedule_Time"],
                               "  "+json_data["Terminal"]+"    ",
                               "       "+json_data["Came_From"]

                               ]
                if self.is_exit_in_info(cur_content):
                    self._flights_list_with_the_words_arrival.append(cur_content)
        self.print_data_arrival()

    def search_in_depart_articles(self):
        dir_jsons_path = const.FLIGHTS_DEPART_JSONS_DIR
        for file_name in glob.glob(os.path.join(dir_jsons_path, '*.json')):  # Reading all json files
            with open(file_name, encoding='utf-8', mode='r') as file:
                json_data = json.loads(file.read())
                cur_content = [json_data["Airline"],
                               json_data["Flight_Num"]+"            ",
                               json_data["Status"]+"   ",
                               json_data["Update_Time"]+"    ",
                               json_data["Schedule_Time"],
                               "  "+json_data["Terminal"]+"    ",
                               "       "+json_data["Came_To"]

                               ]
                if self.is_exit_in_info(cur_content):
                    self._flights_list_with_the_words_depart.append(cur_content)
        self.print_data_depart()
