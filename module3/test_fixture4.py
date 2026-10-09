import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
link = "https://suninjuly.github.io/"

@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestMainPage1():
    def test_guest_should_see_h1(self, browser):
        print("start test1")
        browser.get(link)
        browser.find_element(By.TAG_NAME, "h1")
        print("finish test1")

    def test_guest_should_see_body(self, browser):
        print("start test2")
        browser.get(link)
        browser.find_element(By.TAG_NAME, "body")
        print("finish test2")




