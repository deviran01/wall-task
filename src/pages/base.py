from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def take_screenshot(self, name: str):
        path = f"screenshots/{name}.png"
        self.page.screenshot(path=path)
        return path

    def get_video_path(self):
        return self.page.video.path()

    def get_title(self):
        return self.page.title()
