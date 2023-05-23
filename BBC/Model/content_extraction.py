import os
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from BBC.Model.article import Article
import constants as const
import json


class ContentExtraction:
    """
    This department is responsible for downloading
    the information of the article (title and content)
    """
    def __init__(self, link_art, driver=WebDriver):
        self._driver = driver
        self._art_items = Article(title=self._driver.title,
                                  link=link_art, category=None)
        self.remove_unnecessary_letters_from_name()

    def is_exit(self):
        """
        This function makes sure that we do not
        download an article that we already have in the folder.
        """
        file_name = self._art_items.get_title() + ".json"
        file_path = const.BBC_JSONS_PATH + str(file_name)
        if os.path.isfile(file_path):
            return True
        else:
            return False

    def pull_all_information_articles(self):
        """
        This function pulls the information from the HTML page
        with the help of tags common to the categories of the article.
        for example, I found that all the articles of the type News have
        a tag in common and thus I extracted the content of the article.
        """
        if not self.is_exit():
            if self._art_items.get_title().endswith('BBC News'):
                self._art_items.set_category("BBC News")
                self.extract_article_content('p[class^="ssrcss-1q0x1qg-Paragraph"]')
            elif self._art_items.get_title().endswith('BBC Sport'):
                self._art_items.set_category("BBC Sport")
                self.extract_article_content('p[data-reactid*="paragraph"]')
            elif self._art_items.get_title().endswith('BBC Food'):
                self._art_items.set_category("BBC Food")
                self.extract_article_content('p[class="blocks-text-block__paragraph"]')
            elif self._art_items.get_title().endswith('BBC Reel'):
                self._art_items.set_category("BBC Reel")
                return
            elif self._art_items.get_title().endswith('BBC Culture'):
                self._art_items.set_category("BBC Culture")
                self.extract_article_content('div[class="body-text-card b-reith-sans-font"]')
            elif self._art_items.get_title().endswith('BBC Travel'):
                self._art_items.set_category("BBC Travel")
                self.extract_article_content('div[class="body-text-card b-reith-sans-font"]')
            elif self._art_items.get_title().endswith('BBC Future'):
                self._art_items.set_category("BBC Future")
                self.extract_article_content('div[class="body-text-card b-reith-sans-font"]')
            elif self._art_items.get_title().endswith('BBC Worklife'):
                self._art_items.set_category("BBC Worklife")
                self.extract_article_content('div[class="body-text-card b-reith-sans-font"]')
            else:
                self._art_items.set_category("BBC other")
                self.extract_article_content('p')

    def extract_article_content(self, css_selector: str):
        """
        In this function we go line by line and look
        for the tag with the text attribute and concatenate
        the entire content of the article into a string object.
        :param css_selector: the tag with the text attribute
        """
        all_content = ""
        if css_selector == 'p':
            all_content_blocks = self._driver.find_elements(By.TAG_NAME, css_selector)
        else:
            all_content_blocks = self._driver.find_elements(By.CSS_SELECTOR, css_selector)
        for cur_block in all_content_blocks:
            cur_text = cur_block.get_attribute("innerText")
            all_content += cur_text + " "
        self._art_items.set_info(all_content)
        self.write_to_json()

    def write_to_json(self):
        """
        This function opens the JSON file and defines in it the name of the article,
         the link and the content of the article.
        """
        lower_info = self._art_items.get_info().lower()
        self._art_items.set_info(lower_info)
        article_json_obj = {
            "Title": self._art_items.get_title(),
            "Link": self._art_items.get_link(),
            "Info": self._art_items.get_info()
        }
        json_object = json.dumps(article_json_obj)
        file_name = self._art_items.get_title() + ".json"
        file_path = const.BBC_JSONS_PATH + str(file_name)

        try:
            with open(str(file_path), "w") as outfile:
                outfile.write(json_object)
        except:
            print("Can't open file")
            pass

    def remove_unnecessary_letters_from_name(self):
        art_name = self._art_items.get_title()
        art_name = art_name.replace(':', '')
        art_name = art_name.replace('?', '')
        art_name = art_name.replace('"', '')
        art_name = art_name.replace("'", "")
        art_name = art_name.replace('*', '')
        art_name = art_name.replace('<', '')
        art_name = art_name.replace('>', '')
        art_name = art_name.replace('|', '')
        art_name = art_name.replace('/', '')
        art_name = art_name.replace('\\', '')
        art_name = art_name.replace('\n', "")
        self._art_items.set_title(art_name)
