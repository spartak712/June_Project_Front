from base.base_page import BasePage


class StartPage(BasePage):

    PAGE_URL = 'https://demoqa.com/'
    ELEMENTS_TAB_LOCATOR = ('xpath', "//div[@class='card mt-4 top-card']")

    def click_on_element_tab(self):
        ELEMENTS_TAB = self.browser.find_element(*self.ELEMENTS_TAB_LOCATOR)
        ELEMENTS_TAB.click()
