from core.base_pages import BasePage


class WelcomePage(BasePage):
    WELCOME = '//*[@class="title"]'
    MESSAGE = '//*[@id="rightPanel"]//p'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def asser_that_registration_is_success(self, name):
        self.wait_for_visible(self.WELCOME)
        self.wait_for_visible(self.MESSAGE)

        self.assert_text_in_element(self.WELCOME, name)

