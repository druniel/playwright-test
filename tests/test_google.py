import re
from playwright.sync_api import expect

def test_google_search(page):
    page.goto("https://www.google.com/ncr")
    
    try:
        page.get_by_role("button", name="Accept all").click(timeout=3000)
    except:
        print("No popoup")
        
    page.get_by_role("combobox", name="Search").fill("Playwright Python")
    page.keyboard.press("Enter")