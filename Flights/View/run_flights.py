from Flights.Controller.filghts_web_scraping import Scraping_Flights

"""
Run file for the system user with tests.
"""

with Scraping_Flights() as bot:
    print("The bot start..\n")
    bot.land_page()

    print("Start install all the flights information..\n")
    bot.install_flights()

    print("Starts looking for the word:'Blue' from all the flights information we downloaded..\n")
    bot.search_from_flights("Blue")
