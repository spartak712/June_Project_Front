from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver_fixture):
        self.EC = EC
        self.browser = driver_fixture
        self.wait = WebDriverWait(driver_fixture, 10, poll_frequency=1)

    def open(self):
        self.browser.get(self.PAGE_URL)

    def is_opened(self):
        self.wait.until(self.EC.url_to_be(self.PAGE_URL))
        print(self.browser.current_url)
        print(f'{self.__class__.__name__} is opened')








