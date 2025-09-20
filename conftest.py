#import pytest
#from pytest import FixtureRequest
#from playwright.sync_api import sync_playwright

#@pytest.fixture(params=["chromium", "firefox", "webkit"])
#def browser(request: FixtureRequest):
#    with sync_playwright() as p:
#        browser = getattr(p, request.param).launch()
#        #browser = p.chromium.launch(headless=True)
#        yield browser
#        browser.close()
        
#@pytest.fixture
#def page(browser):
#    page = browser.new_page()
#    yield page
#    page.close()