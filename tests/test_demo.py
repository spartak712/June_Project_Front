from base.base_test import BaseTest


class TestDemo(BaseTest):

    def test_open_element_tab(self):
        self.start_page.open()
        self.start_page.is_opened()
        self.start_page.click_on_element_tab()
        self.element_page.is_opened()
        self.start_page.browser.get("https://yandex.ru")
        print(self.start_page.browser.current_url)


