from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

"""
this class responsible for extracting all 
the article links on the main page of the site
"""


class ExtractLink:
    def __init__(self, driver=WebDriver):
        self._driver = driver
        self._articles = self._driver.find_elements(By.CSS_SELECTOR, 'a[class="block-link__overlay-link"]')
        self._reel_articles = self._driver.find_elements(By.CSS_SELECTOR, 'a[class="reel__link"]')
        self._links = []


    def pull_all_links_articles(self):
        """
        This function goes through the "children" of the tag
        we saved as the class object and looks for
        the 'href' attribute which is known in html to indicate a link.
        :return: A list of links to the articles
        """
        for article in self._articles:
            link = article.get_attribute('href').strip()
            self._links.append(link)

        for article in self._reel_articles:
            link = article.get_attribute('href').strip()
            self._links.append(link)

        return self._links

