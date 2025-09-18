from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright

#def test_check_page_title(page: Page):
 #   page.goto("https://seznam.cz")
  #  expect(page).to_have_title("Seznam – najdu tam, co neznám")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://seznam.cz")
    print("Page title:", page.title())
    browser.close()