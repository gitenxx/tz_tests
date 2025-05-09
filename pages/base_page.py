from playwright.sync_api import Page, Response

class BasePage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.page.set_default_timeout(timeout = 100000)

    def visit(self, url) -> Response | None:
        return self.page.goto(url, wait_until='networkidle')

    def reload(self) -> Response | None:
        return self.page.reload(wait_until='domcontentloaded')
        
    def status_check(self, link):
        return self.page.request.get(link)
        