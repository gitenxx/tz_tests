from playwright.sync_api import Page

from pages.base_page import BasePage
from components.request_a_quote_form import RequestAQuoteForm


class MainPage(BasePage):
    '''Главная страница — https://qatest.datasub.com/.'''
    def __init__(self, page: Page) -> None:
        self.request_a_quote = RequestAQuoteForm(page)
        super().__init__(page)