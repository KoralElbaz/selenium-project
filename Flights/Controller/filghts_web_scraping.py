import os
from Flights.Controller.filghts_interface import FlightsInterface
from selenium import webdriver
import constants as const
from Flights.Model.flights_access_tables import AccessExtractTables
from Flights.Model.search_words_flights import SearchWordsFlights

import hashlib
from urllib.request import urlopen, Request

"""
 Full details about the functions can be found in interface..
"""
""" for Real-Time i read this tutorial: https://www.geeksforgeeks.org/python-script-to-monitor-website-changes/ """


class Scraping_Flights(FlightsInterface, webdriver.Chrome):
    def __init__(self, driver_path=const.FLIGHTS_DRIVER_PATH, teardown=False):
        self._driver_path = driver_path
        self._teardown = teardown

        # real-time part:
        # setting the URL you want to monitor
        self._url = Request(const.FLIGHTS_URL,
                            headers={'User-Agent': 'Mozilla/5.0'})

        # to perform a GET request and load the
        # content of the website and store it in a var
        self._response = urlopen(self._url).read()

        # to create the initial hash
        self._Hash = hashlib.sha224(self._response).hexdigest()
        print("running")

        os.environ['PATH'] += self._driver_path
        super(Scraping_Flights, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._teardown:
            self.quit()

    def land_page(self):
        self.get(const.FLIGHTS_URL)

    def install_flights(self):
        self._response = urlopen(self._url).read()
        currentHash = hashlib.sha224(self._response).hexdigest()
        # check if the current hush is the most updated
        if self._Hash != currentHash:
            print("something changed...")
            self._Hash = currentHash
            self.land_page()
            AccessExtractTables(driver=self)

    def search_from_flights(self, sub_text: str):
        SearchWordsFlights(sub_text)
