import allure

from data.users import USER_ELENA
from pages import LoginPage


class TestLogin:

    @allure.title('Login as user')
    def test_success_login(self, driver):
        login = LoginPage(driver)

        login.open()
        login.fill_name(USER_ELENA['login'])
        login.fill_password(USER_ELENA['password'])
        login.click_on_login()

        login.asser_that_login_is_success(USER_ELENA)
