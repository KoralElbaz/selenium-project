from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from Flights.Model.extract_tables import ExtractTables

"""
This class is responsible for extracting all flight details 
in the schedule of incoming and outgoing flights.
"""
class AccessExtractTables:
    def __init__(self, driver=WebDriver):
        self._driver = driver
        self.get_tables()

    def get_tables(self):
        self.get_arrival_table()
        ExtractTables(driver=self._driver, flight_type="arrival")
        self.get_depart_table()
        ExtractTables(driver=self._driver, flight_type="depart")

    def get_arrival_table(self):
        """
        This function opens the full flight schedule and displays
        all incoming flights.
        In addition, stops the automatic update.
        """
        button_next_flights = self._driver.find_element(By.CSS_SELECTOR, 'button[id="next"]')
        """ When we reach the end of the page the style="display" """
        style_state = button_next_flights.get_attribute("style")

        while style_state == "":
            button_next_flights.click()
            button_next_flights = self._driver.find_element(By.CSS_SELECTOR, 'button[id="next"]')
            style_state = button_next_flights.get_attribute("style")

        button_stop_update = self._driver.find_element(By.CSS_SELECTOR, 'a[id="toggleAutoUpdate"]')
        button_stop_update.click()

    def get_depart_table(self):
        """
            This function opens the full flight schedule and displays
            all outgoing flights.
            In addition, stops the automatic update.
            """
        button_depart_table = self._driver.find_element(By.CSS_SELECTOR, 'a[id="tab--departures_flights-label"]')
        button_depart_table.click()

        is_able = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[id="next"]')))

        button_next_flights = self._driver.find_element(By.CSS_SELECTOR, 'button[id="next"]')
        style_state = button_next_flights.get_attribute("style")

        while style_state == "":
            button_next_flights.click()
            button_next_flights = self._driver.find_element(By.CSS_SELECTOR, 'button[id="next"]')
            style_state = button_next_flights.get_attribute("style")

        # button_stop_update = self._driver.find_element(By.CSS_SELECTOR, 'a[id="toggleAutoUpdate"]')
        # button_stop_update.click()
