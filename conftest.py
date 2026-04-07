from typing import Any, Generator

import pytest
from playwright.sync_api import sync_playwright, Browser, Page


@pytest.fixture
def browser_chrome() -> Generator[Browser, Any, None]:
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=["--no-proxy-server"]
        )
        yield browser
        browser.close()

@pytest.fixture
def page(browser_chrome) -> Generator[Page, Any, None]:
    page = browser_chrome.new_page()
    yield page
    page.close()

@pytest.fixture()
def page_quick_tour(browser_chrome) -> Generator[Page, Any, None]:
    page = browser_chrome.new_page(base_url="https://quick-tour.dprusakov.ru/")
    yield page
    page.close()

@pytest.fixture()
def url_quick_tour():
    return 'https://quick-tour.dprusakov.ru'