
"""
This class it's the main class in implementing the system on the BBC website.
"""

class BbcInterface:
    def land_page(self):
        """Loads the BBC website in the driver."""
        raise NotImplementedError

    def install_articles(self):
        """
            First, the function saves in a list all the links
            to all the articles on the site.
            Second, she goes through every link she enters
            into the article and takes the necessary information.
            (The necessary information: title, link, and content of the article)

            :return: JSON files containing all the
                    necessary information from the articles.
            """
        raise NotImplementedError


    def search_from_articles(self, sub_text: str):
        """
            We will go through all the JSON files (each file = an article)
            and search if it exists The word/combination will then be added to the list.
            Finally we will print the list.

            :return: prints a table containing the name of the article
            and the link where the word or combination of words is found.
            """
        raise NotImplementedError

