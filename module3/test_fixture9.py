import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
link = "https://suninjuly.github.io/"

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestMainPage1():
    def test_guest_should_see_h1(self, browser):
        browser.get(link)
        browser.find_element(By.TAG_NAME, "h1")

    def test_guest_should_see_body(self, browser):
        browser.get(link)
        browser.find_element(By.TAG_NAME, "body")

    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_guest_should_see_search_button_on_the_main_page(self, browser): 
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "button.favorite")



