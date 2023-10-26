import allure

from data.users import USER_ELENA
from pages import OpenNewAccountPage


class TestLogin:

    @allure.title('Open New Account')
    def test_open_new_account(self, driver, login):
        open_new_account = OpenNewAccountPage(driver)
        open_new_account.open()
        open_new_account.click_on_submit()

        open_new_account.asser_that_account_was_created()


