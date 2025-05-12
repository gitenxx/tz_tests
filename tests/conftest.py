import pytest
from playwright.sync_api import Page, sync_playwright, expect

from pages.main_page import MainPage


@pytest.fixture(scope='function')
def chromium_page() -> Page:
    with sync_playwright() as playwright:
        chromium = playwright.chromium.launch(headless=True)
        context = chromium.new_context()
        yield context.new_page()

@pytest.fixture(scope='function')
def main_page(chromium_page: Page) -> MainPage:
    return MainPage(chromium_page)
