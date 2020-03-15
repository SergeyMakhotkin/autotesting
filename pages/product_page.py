import math
import re
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException



class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def solve_quiz_and_get_code(self):
        prompt = self.browser.switch_to.alert
        x = prompt.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        prompt.send_keys(answer)
        prompt.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f'Code: {alert_text}')
            alert.accept()
        except NoAlertPresentException:
            print('No second alert presented')


    def should_be_basket_price_eq_product_price(self):
        product_price_text = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        price_pattern = re.compile('[0-9.,]+')
        product_price = price_pattern.findall(product_price_text)[0]
        basket_price_text = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        basket_price = price_pattern.findall(basket_price_text)[0]
        assert basket_price == product_price, 'Basket price and product price are different'
