import time
from pathlib import Path

import allure
import pytest
from playwright.sync_api import Page, sync_playwright

from src.pages.divar.download import DivarDownloadPage
from src.pages.duckduckgo.result import DuckDuckGoResultPage
from src.pages.duckduckgo.search import DuckDuckGoSearchPage


@pytest.fixture
def duckduckgo_result_page(page: Page) -> DuckDuckGoResultPage:
    return DuckDuckGoResultPage(page)


@pytest.fixture
def duckduckgo_search_page(page: Page) -> DuckDuckGoSearchPage:
    return DuckDuckGoSearchPage(page)


@pytest.fixture
def divar_download_page(page: Page) -> DivarDownloadPage:
    return DivarDownloadPage(page)


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(record_video_dir="videos/")
        page = context.new_page()
        yield page
        context.close()
        browser.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    report = outcome.get_result()

    # We only want to add attachments on failure
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page", None)

        if page:
            # Generate a unique name for the screenshot
            screenshot_name = f"screenshot_{int(time.time())}.png"
            screenshot_path = Path("screenshots") / screenshot_name

            # Take screenshot
            page.screenshot(path=str(screenshot_path))

            # Ensure the screenshot file exists and is not empty before attaching
            if screenshot_path.is_file() and screenshot_path.stat().st_size > 0:
                with open(screenshot_path, "rb") as image_file:
                    allure.attach(
                        image_file.read(),
                        name="Screenshot",
                        attachment_type=allure.attachment_type.PNG,
                    )

            # Attach video if it exists and is in the correct format
            video_path = Path(page.video.path())
            if video_path.is_file() and video_path.stat().st_size > 0:
                with open(video_path, "rb") as video_file:
                    allure.attach(
                        video_file.read(),
                        name="Video",
                        attachment_type=allure.attachment_type.WEBM,
                    )
