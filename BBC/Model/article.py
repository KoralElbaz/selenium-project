class Article:

    """
    An article object containing the fields: link title and content.
    """

    def __init__(self, title, link, category, info=""):
        self._title = title
        self._link = link
        self._category = category
        self._info = info

    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def get_category(self):
        return self._category

    def set_category(self, category):
        self._category = category

    def get_info(self) -> str:
        return self._info

    def set_info(self, info):
        self._info = info

    def get_link(self) -> str:
        return self._link

    def set_link(self, link):
        self._link = link
