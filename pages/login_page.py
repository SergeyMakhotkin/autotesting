from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.common.exceptions import NoSuchElementException


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        print("url check passed!")
        self.should_be_login_form()
        print("login form check passed!")
        self.should_be_register_form()
        print("register form check passed!")
        print("It's really login page!")

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'Wrong login URL'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            'Login form is not present'


    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            'Register form is not present'
