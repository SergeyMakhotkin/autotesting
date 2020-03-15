from selenium.webdriver import Remote as RemoteWebDriver
from .pages.product_page import ProductPage
from time import sleep


def test_guest_can_add_product_to_basket(browser: RemoteWebDriver):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    # if '?promo=newYear' in page.browser.current_url:
    page.solve_quiz_and_get_code()
    page.should_be_basket_price_eq_product_price()
