import pytest
from playwright.sync_api import Playwright


@pytest.fixture(scope='session')
def launch(playwright: Playwright):
    chrome = playwright.chromium.launch(headless=False, args=["--start-maximized"])
    context = chrome.new_context(no_viewport=True)
    page = context.new_page()
    yield page
    context.close()
    chrome.close()


@pytest.fixture(scope='session')
def view_pc(playwright: Playwright):
    chrome = playwright.chromium.launch(headless=False)
    context = chrome.new_context(viewport={'width': 1920, 'height': 1080})
    page = context.new_page()
    yield page
    context.close()
    chrome.close()


@pytest.fixture(scope='session')
def view_mobile(playwright: Playwright):
    chrome = playwright.chromium.launch(headless=False, channel='msedge')
    context = chrome.new_context(viewport={'width': 390, 'height': 1080})
    page = context.new_page()
    yield page
    context.close()
    chrome.close()
