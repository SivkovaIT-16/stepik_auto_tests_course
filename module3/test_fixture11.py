from selenium.webdriver.common.by import By
import pytest

link = "https://suninjuly.github.io/"


@pytest.mark.parametrize('selector', ["h1", "body", "title"])
def test_guest_should_see_element(browser, selector):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, selector)