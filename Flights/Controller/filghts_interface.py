
"""
This class it's the main class in implementing the system on the flights website.
"""

class FlightsInterface:

    def land_page(self):
        """Loads the flights website in the driver."""
        raise NotImplementedError


    def install_flights(self):
        """
        Downloading the flight details from
        the incoming and outgoing flight schedule on the website.
        :return:JSON files containing all the
                necessary information from the flights.
        """
        raise NotImplementedError


    def search_from_flights(self, sub_text: str):
        """
        We will go through all the JSON files (each file = an flight)
        and search if it exists The word/combination will then be added to the list.
        Finally we will print the list.
        :param sub_text: Text : string
        :return:
        """
        raise NotImplementedError
