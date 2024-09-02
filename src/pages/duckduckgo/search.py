from playwright.sync_api import Page

from src.pages.duckduckgo.duckduckgo import DuckDuckGo


class DuckDuckGoSearchPage(DuckDuckGo):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.search_input = page.locator("#searchbox_input")

    def search(self, phrase: str) -> None:
        self.search_input.fill(phrase)
        self.logger.info(f"enter {phrase} in search input")
        self.page.keyboard.press("Enter")
        self.logger.info(f"click on search button")
