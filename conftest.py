import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver_fixture(request):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    #options.add_argument('--window-size=1920,1080')
    options.add_argument('--no-sandbox')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--disable-blink-features=AutomationControlled")
    browser = webdriver.Chrome(options=options)
    #request.cls.browser = browser
    yield browser
    browser.quit()
