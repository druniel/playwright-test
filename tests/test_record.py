import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    page.locator("span").filter(has_text="овать логин страницу sdf").click()
    page.get_by_role("menuitem", name="Logout").click()
    expect(page.get_by_role("textbox", name="Password")).to_be_visible()
    expect(page.locator("form")).to_contain_text("Password")