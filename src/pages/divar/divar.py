from playwright.sync_api import Page

from src.utilities.logger import Logger
from src.pages.base import BasePage


class Divar(BasePage):
    URL = "https://divar.ir/downloadm"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.page = page
        self.logger = Logger.get_logger(self.__class__.__name__)
        self.base_url = "https://divar.ir/"
