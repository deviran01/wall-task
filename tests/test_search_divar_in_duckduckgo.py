import allure
from playwright.sync_api import expect, Page

from src.pages.divar.download import DivarDownloadPage
from src.pages.duckduckgo.result import DuckDuckGoResultPage
from src.pages.duckduckgo.search import DuckDuckGoSearchPage
from tests.testdata import DIVAR_SEARCH_RESULT_TITLE, SEARCH_QUERY


@allure.tag("flaky", "search", "divar")
@allure.title("Test search divar keyword in duckduckgo search engine")
@allure.description(
    "This test verifies that searching for a specific keyword in DuckDuckGo results in the expected "
    "Divar download page being found and opened."
)
@allure.severity(allure.severity_level.TRIVIAL)
@allure.link("https://duckduckgo.com/", name="DuckDuckGo")
def test_search_divar_keyword_in_duckduckgo_search_engine(
    page: Page,
    duckduckgo_search_page: DuckDuckGoSearchPage,
    duckduckgo_result_page: DuckDuckGoResultPage,
    divar_download_page: DivarDownloadPage,
    phrase: str = SEARCH_QUERY,
) -> None:

    with allure.step("Load DuckDuckGo Homepage and Input Search Query"):
        duckduckgo_search_page.load()
        duckduckgo_search_page.search(phrase)
        expect(duckduckgo_result_page.search_input).to_have_value(phrase)
        expect(page).to_have_title(duckduckgo_result_page.get_title())

    with allure.step("Verify Search Results Contain the Expected Keyword"):
        assert duckduckgo_result_page.result_link_titles_contain_phrase(phrase)
        expect(page).to_have_title(SEARCH_QUERY + duckduckgo_result_page.title)

    with allure.step("Click on the Divar-Related Link from Search Results"):
        duckduckgo_result_page.navigate_to_search_result(DIVAR_SEARCH_RESULT_TITLE)
        expect(page).to_have_title(divar_download_page.title)

    with allure.step("Verify the Divar Download Page Content and URL"):
        expect(page).to_have_title(divar_download_page.title)
        expect(page).to_have_url(divar_download_page.full_url)
