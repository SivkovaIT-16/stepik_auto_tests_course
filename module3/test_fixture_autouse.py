import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
link = "https://suninjuly.github.io/"

@pytest.fixture()
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture(autouse=True)
def prepare_data():
    print()
    print("preparing some critical data for every test")

class TestMainPage1():
    def test_guest_should_see_h1(self, browser):
        browser.get(link)
        browser.find_element(By.TAG_NAME, "h1")

    def test_guest_should_see_body(self, browser):
        browser.get(link)
        browser.find_element(By.TAG_NAME, "body")




