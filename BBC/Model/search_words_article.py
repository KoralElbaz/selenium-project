import glob
import json
import os
from prettytable import PrettyTable
import constants as const


class SearchWords:
    """
    This Class is responsible for searching
    for a word/combination in all the articles we downloaded
    """
    def __init__(self, txt):
        self._words_to_check = txt
        self._art_list_with_the_words = []
        self.search_in_all_articles()

    def print_data(self):
        table = PrettyTable(field_names=["Article Name", "Article Link"])
        table.add_rows(self._art_list_with_the_words)
        print(table)

    def is_exit_in_art(self, art_info):
        """
        A function that checks whether
        a word/combination of words is found in a certain text
        :param art_info: Text : string
        :return:
        """
        if self._words_to_check.lower() in art_info.lower():
            return True
        else:
            return False

    def search_in_all_articles(self):
        """
        This function passes through all files that end with the json extension.
        in a specific folder and checks whether
        there is text containing a certain word/combination.
        If so, we will save all the files containing this in a list-type object.
        :return: print table with this word/words.
        """
        dir_jsons_path = const.BBC_JSONS_DIR
        for file_name in glob.glob(os.path.join(dir_jsons_path, '*.json')):  # Reading all json files
            with open(file_name, encoding='utf-8', mode='r') as file:
                json_data = json.loads(file.read())
                cur_content = json_data["Info"]  # Checking only the content of the article
                type(cur_content)
                if self.is_exit_in_art(cur_content):
                    article_info = [json_data["Title"], json_data["Link"]]
                    self._art_list_with_the_words.append(article_info)
        self.print_data()
