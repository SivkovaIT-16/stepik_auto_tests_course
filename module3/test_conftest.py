from selenium.webdriver.common.by import By
link = "https://suninjuly.github.io/"

def test_guest_should_see_h1(browser):
    browser.get(link)
    browser.find_element(By.TAG_NAME, "h1")

