from selenium.webdriver.common.by import By
import pytest

link = "https://suninjuly.github.io/"


@pytest.mark.parametrize('selector', ["h1", "body"])
class TestMainPage:
    def test_guest_should_see_element(self, browser, selector):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, selector)

    def test_guest_should_see_element_again(self, browser, selector):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, selector)