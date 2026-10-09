import time


def test_item_has_add_to_basket_button(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(30)  

    button = browser.find_element(
        'css selector', 'button.btn-add-to-basket'
    )

    assert button is not None, 'Кнопка добавления в корзину не найдена'