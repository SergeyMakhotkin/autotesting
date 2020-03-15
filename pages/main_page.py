from .base_page import BasePage
# from .login_page import LoginPage
from .locators import MainPageLocators
from selenium.common.exceptions import NoAlertPresentException


class MainPage(BasePage):

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)
        # обработка всплывающих окон типа 'Alert'
        try:
            alert = self.browser.switch_to.alert
            alert.accept()
            print('There is some alert message. It has been closed.')
        except NoAlertPresentException:
            print('There is no any alert. Go ahead.')


    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), \
            'Login link is not present'
