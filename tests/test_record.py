from playwright.sync_api import Page, expect

# testing of playwright recording
def test_example(page: Page) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    expect(page.get_by_role("textbox", name="Password")).to_be_visible()
    expect(page.locator("form")).to_contain_text("Password")
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()