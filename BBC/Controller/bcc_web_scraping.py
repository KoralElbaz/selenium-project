import os
import constants as const
from selenium import webdriver
from BBC.Controller.bbc_interface import BbcInterface
from BBC.Model.extract_link import ExtractLink
from BBC.Model.content_extraction import ContentExtraction
from BBC.Model.search_words_article import SearchWords


"""
 Full details about the functions can be found in interface..
"""


class Scraping_BBC(BbcInterface,webdriver.Chrome):
    def __init__(self, driver_path=const.BBC_DRIVER_PATH, teardown=False):
        self._driver_path = driver_path
        self._teardown = teardown
        self._articles_list = []
        self._articles_links = []

        os.environ['PATH'] += self._driver_path
        super(Scraping_BBC, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._teardown:
            self.quit()

    def land_page(self):
        self.get(const.BBC_URL)

    def install_articles(self):
        list_of_links = ExtractLink(driver=self).pull_all_links_articles()

        for link in list_of_links:
            self.get(link)
            content_article = ContentExtraction(link, driver=self)
            content_article.pull_all_information_articles()
        self.close()

    def search_from_articles(self, sub_text: str):
        SearchWords(sub_text)
