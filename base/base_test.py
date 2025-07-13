import pytest
from pages.start_page import StartPage
from pages.element_page import ElementPage


class BaseTest:

    start_page: StartPage
    element_page: ElementPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver_fixture):
        #request.cls.browser = driver_fixture
        request.cls.start_page = StartPage(driver_fixture)
        request.cls.element_page = ElementPage(driver_fixture)
