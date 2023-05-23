import time
import os, shutil

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
import constants as const

from Flights.Model.create_flights_json import CreateJson
from Flights.Model.flight_arrival import FlightArrival
from Flights.Model.flight_depart import FlightDepart


class ExtractTables:

    def __init__(self, driver: WebDriver, flight_type: str):
        self._driver = driver
        self._flight_type = flight_type
        self._all_flights = []
        self.extract_flights()

    def extract_flights(self):
        if self._flight_type == "arrival":
            self.emptying_folder(const.FLIGHTS_ARRIVAL_JSONS_DIR)
            time.sleep(0.5)
            self.pull_flight_arrival_information()
            CreateJson(self._all_flights, self._flight_type)

        elif self._flight_type == "depart":
            self.emptying_folder(const.FLIGHTS_DEPART_JSONS_DIR)
            time.sleep(0.5)
            self.pull_flight_depart_information()
            CreateJson(self._all_flights, self._flight_type)

    def pull_flight_arrival_information(self):
        """
        This function goes row by row in the table of incoming flights
        and sends to an auxiliary function that will extract the text from the row.
        """
        rows = self._driver.find_elements(By.CSS_SELECTOR, 'tr[class^="flight_row"]')
        for row in rows:
            self.get_arrival_row_data(row)

    def pull_flight_depart_information(self):
        """
        This function goes row by row in the table of outgoing flights
        and sends to an auxiliary function that will extract the text from the row.
        """
        table_rows = self._driver.find_element(By.CSS_SELECTOR, 'table[id="flight_board-departures_table"]')
        rows = table_rows.find_elements(By.CSS_SELECTOR, 'tr[role="row"][class^="flight_row"]')
        for row in rows:
            self.get_depart_row_data(row)

    def get_arrival_row_data(self, row):
        """
        Enter the information retrieved using
        the GET functions into the incoming/outgoing flight object.
        :param row: with the information of flight
        """
        flight_arrival = FlightArrival()
        flight_arrival.set_airline(self.get_airline(row))
        flight_arrival.set_flight_num(self.get_flight_num(row))
        flight_arrival.set_came_from(self.get_Country(row))
        flight_arrival.set_terminal(self.get_terminal(row))
        flight_arrival.set_schedule_time(self.get_schedule_time(row))
        flight_arrival.set_updated_time(self.get_update_time(row))
        flight_arrival.set_status(self.get_status(row))
        self._all_flights.append(flight_arrival)

    def get_depart_row_data(self, row):
        flight_depart = FlightDepart()
        flight_depart.set_airline(self.get_airline(row))
        flight_depart.set_flight_num(self.get_flight_num(row))
        flight_depart.set_came_to(self.get_Country(row))
        flight_depart.set_terminal(self.get_terminal(row))
        flight_depart.set_schedule_time(self.get_schedule_time(row))
        flight_depart.set_updated_time(self.get_update_time(row))
        flight_depart.set_status(self.get_status(row))
        self._all_flights.append(flight_depart)

    def get_airline(self, cur_row: WebElement):
        airline_box = cur_row.find_element(By.CSS_SELECTOR, 'div[class="td-airline"]')
        airline = airline_box.get_attribute("innerText")
        return airline

    def get_flight_num(self, cur_row: WebElement):
        flight_num = cur_row.find_element(By.CSS_SELECTOR, 'div[class="td-flight"]').get_attribute("innerText")
        return flight_num

    def get_Country(self, cur_row: WebElement):
        land = cur_row.find_element(By.CSS_SELECTOR, 'div[class="td-city"]').get_attribute("innerText")
        return land

    def get_terminal(self, cur_row: WebElement):
        terminal = cur_row.find_element(By.CSS_SELECTOR, 'div[class="td-terminal"]').get_attribute("innerText")
        return terminal

    def get_schedule_time(self, cur_row: WebElement):
        schedule_box = cur_row.find_element(By.CSS_SELECTOR, 'div[class="td-scheduledTime"]')
        time_schedule = schedule_box.find_element(By.TAG_NAME, 'time')
        hour_schedule = time_schedule.find_element(By.TAG_NAME, 'strong').get_attribute("innerText")
        date_schedule = time_schedule.find_element(By.TAG_NAME, 'div').get_attribute("innerText")
        total_schedule = hour_schedule + " " + date_schedule
        return total_schedule

    def get_update_time(self, cur_row: WebElement):
        updated_time = cur_row.find_element(By.CSS_SELECTOR, 'div[class="td-updatedTime"]').get_attribute("innerText")
        return updated_time

    def get_status(self, cur_row: WebElement):
        status = cur_row.find_element(By.CSS_SELECTOR, 'div[class="td-status"]').get_attribute("innerText")
        return status

    def emptying_folder(self, path):
        """
        When we check if flight information has changed
        we will want to empty the folder and add the latest information.
        :param path: of the folder with the json files
        """
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))
