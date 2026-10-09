from selenium import webdriver
from selenium.webdriver.common.by import By
link = "https://suninjuly.github.io/"

class TestMainPage1():

    @classmethod
    def setup_class(self):
        print("\nstart browser for test suite..")
        self.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(self):
        print("quit browser for test suite..")
        self.browser.quit()

    def test_guest_should_see_h1(self):
        self.browser.get(link)
        self.browser.find_element(By.TAG_NAME, "h1")

    def test_guest_should_see_body(self):
        self.browser.get(link)
        self.browser.find_element(By.TAG_NAME, "body")


class TestMainPage2():

    def setup_method(self):
        print("start browser for test..")
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        print("quit browser for test..")
        self.browser.quit()

    def test_guest_should_see_h1(self):
        self.browser.get(link)
        self.browser.find_element(By.TAG_NAME, "h1")

    def test_guest_should_see_body(self):
        self.browser.get(link)
        self.browser.find_element(By.TAG_NAME, "body")

