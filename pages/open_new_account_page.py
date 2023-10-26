import allure

from core.base_pages import BasePage
from data import DOMAIN


class OpenNewAccountPage(BasePage):
    SUBMIT = '//*[@type="submit"]'

    TITLE = '//*[@class="title"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.OPEN_NEW_ACCOUNT = f'{DOMAIN}/parabank/openaccount.htm'

    @allure.step('Open login page')
    def open(self):
        self.driver.get(self.OPEN_NEW_ACCOUNT)

    @allure.step('Click on submit')
    def click_on_submit(self):
        self.click_on(self.SUBMIT)

    def asser_that_account_was_created(self):

        self.assert_text_in_element(self.TITLE, f"Account Opened!")
