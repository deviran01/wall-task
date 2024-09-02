from typing import List

from playwright.sync_api import Page

from src.pages.duckduckgo.duckduckgo import DuckDuckGo


class DuckDuckGoResultPage(DuckDuckGo):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.page = page
        self.result_links = page.locator('a[data-testid="result-title-a"]')
        self.search_input = page.locator("#search_form_input")
        self.title = " at DuckDuckGo"  # +query

    def result_link_titles(self) -> List[str]:
        self.logger.info("Waiting for search results to load.")
        self.result_links.nth(2).wait_for()
        self.logger.info("Retrieving all search result titles.")
        return self.result_links.all_text_contents()

    def result_link_titles_contain_phrase(self, phrase: str, minimum: int = 1) -> bool:
        titles = self.result_link_titles()
        matches = [t for t in titles if phrase.lower() in t.lower()]
        self.logger.info(
            f'Checking if at least {minimum} search results contain the phrase "{phrase}".'
        )
        return len(matches) >= minimum

    def navigate_to_search_result(self, search_result: str):
        self.logger.info(
            f'Opening search result containing the text: "{search_result}".'
        )
        return self.page.get_by_text(search_result).click()
