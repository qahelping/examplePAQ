import allure

from core.base_pages import BasePage
from data.urls import ACCOUNT_OVERVIEW
from pages.welcome_page import WelcomePage


class AccountOverviewPage(WelcomePage, BasePage):
    TITLE = '//*[@class="title"]'
    TABLE = '//*[@ng-app="OverviewAccountsApp"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Open "Accounts Overview" page')
    def open(self):
        self.driver.get(ACCOUNT_OVERVIEW)

    def asser_that_login_is_success(self, name):
        self.wait_for_visible(self.TITLE)
        self.wait_for_visible(self.TABLE)

        self.assert_text_in_element(self.TITLE, 'Accounts Overview')
        self.assert_actual_url(ACCOUNT_OVERVIEW)


