from selenium.webdriver import Remote as RemoteWebDriver
# импортируем класс для удобства работы с методами webdriver


class BasePage():
    def __init__(self, browser: RemoteWebDriver, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
