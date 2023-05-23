from BBC.Controller.bcc_web_scraping import Scraping_BBC

"""
Run file for the system user with tests.
"""

with Scraping_BBC() as bot:
    print("The bot start..\n")
    bot.land_page()

    print("Start install all the article..\n")
    bot.install_articles()

    print("Starts looking for the word:'USA' from all the articles we downloaded..\n")
    bot.search_from_articles("USA")
    print("Starts looking for the combination of words:'UK businesses' from all the articles we downloaded..")
    bot.search_from_articles("UK businesses")
    print("Starts looking for the word:'a' from all the articles we downloaded..")
    bot.search_from_articles("a")

