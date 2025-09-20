from playwright.sync_api import Page, expect
import pytest
import json

def get_json_data() -> list:
    with open('./test_data/data2.json', "r") as file:
        data = json.load(file)
    return [(item['username'], item['password']) for item in data]

@pytest.mark.parametrize("username,password", get_json_data())
def test_example(page: Page, username, password) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").fill(username)
    page.get_by_role("textbox", name="Password").fill(password)
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("link", name="Dashboard")).to_be_visible()