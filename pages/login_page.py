import allure

from core.base_pages import BasePage
from pages.welcome_page import WelcomePage


class LoginPage(BasePage):
    USERNAME = '//*[@name="username"]'
    PASSWORD = '//*[@name="password"]'
    LOGIN = '//*[@type="submit"]'
    FORGOT_LOGIN_INFO = '//*[href="lookup.htm"]'
    REGISTRATION = '//*[href="register.htm"]'

    USER = '//*[@class="smallText"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Open login page')
    def open(self):
        self.driver.get('https://parabank.parasoft.com/parabank/index.htm')

    @allure.step('Fill name')
    def fill_name(self, name):
        self.fill(self.USERNAME, name)

    @allure.step('Fill password')
    def fill_password(self, password):
        self.fill(self.PASSWORD, password)

    @allure.step('Click on submit')
    def click_on_login(self):
        self.click_on(self.LOGIN)

    def asser_that_login_is_success(self, user):
        self.assert_that_element_is_not_visible(self.USERNAME)
        self.assert_that_element_is_not_visible(self.PASSWORD)
        self.assert_that_element_is_not_visible(self.LOGIN)
        self.assert_that_element_is_not_visible(self.FORGOT_LOGIN_INFO)
        self.assert_that_element_is_not_visible(self.REGISTRATION)

        self.assert_text_in_element(self.USER, f"Welcome {user['name']} {user['surname']}")

    @allure.step('Login as user')
    def login(self, user):
        self.open()
        self.fill_name(user['login'])
        self.fill_password(user['password'])

        self.click_on_login()

        self.asser_that_login_is_success(user)
