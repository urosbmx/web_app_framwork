import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield p, browser
        browser.close()


@pytest.fixture()
def mobile_page(browser):
    p, browser = browser
    device = p.devices["Pixel 5"]

    context = browser.new_context(**device)
    page = context.new_page()
    yield page
    context.close()
