from playwright.sync_api import Page

from src.pages.divar.divar import Divar


class DivarDownloadPage(Divar):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.path = "download"
        self.title = "دانلود اپلیکیشن دیوار | به جمع میلیونی کاربرهای دیوار بپیوندید"
        self.full_url = self.base_url + self.path
