import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.homepage import HomePage


def test_example(page: Page) -> None:
    login_page = LoginPage(page)
    home_page = HomePage(page)
    
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()
    home_page.is_upgrade_button_visible()
    home_page.click_performance()
    home_page.click_dashboard()

    #page.get_by_role("textbox", name="Username").fill("Admin")
    #page.get_by_role("textbox", name="Password").fill("admin123")
    #page.get_by_role("button", name="Login").click()
    #expect(page.get_by_role("button", name="Upgrade")).to_be_visible()
    #page.get_by_role("link", name="Performance").click()
    #page.get_by_role("link", name="Dashboard").click()
