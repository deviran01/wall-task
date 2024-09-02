from playwright.sync_api import Page

from src.utilities.logger import Logger
from src.pages.base import BasePage


class DuckDuckGo(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.page = page
        self.logger = Logger.get_logger(self.__class__.__name__)
        self.base_url = "https://www.duckduckgo.com/"
        self.title = "DuckDuckGo — Privacy, simplified."

    def load(self) -> None:
        self.page.goto(self.base_url)
        self.logger.info(f"load duckduckgo page")
