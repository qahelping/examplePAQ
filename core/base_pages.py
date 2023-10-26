from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, NoSuchElementException
from selenium.webdriver.support.ui import Select


class BasePage():
    def __init__(self, driver, WAIT_UNTIL=5):
        self.driver = driver
        self.WAIT_UNTIL = WAIT_UNTIL

    def wait_for_visible(self, locator):
        try:
            return WebDriverWait(self.driver, self.WAIT_UNTIL).until(EC.visibility_of_element_located((By.XPATH, locator)))
        except WebDriverException:
            assert False, f"Element {locator} not clicable"

    def wait_for_clickable(self, locator):
        try:
            return WebDriverWait(self.driver, self.WAIT_UNTIL).until(EC.element_to_be_clickable((By.XPATH, locator)))
        except WebDriverException:
            assert False, f"Element {locator} not clicable"

    def wait_until_disappear(self, locator):
        try:
            return WebDriverWait(self.driver, self.WAIT_UNTIL).until(EC.element_to_be_clickable((By.XPATH, locator)))
        except WebDriverException:
            assert False, f"Element {locator} not clicable"

    def click_on(self, locator):
        element = self.wait_for_visible(locator)
        element.click()

    def hard_click(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        self.driver.execute_script("arguments[0].click();", element)

    def get_current_url(self):
        return self.driver.current_url

    def fill(self, locator, text):
        element = self.wait_for_visible(locator)
        element.clear()
        element.send_keys(text)

    def clear(self, locator):
        element = self.wait_for_visible(locator)
        element.clear()

    def assert_text_in_element(self, locator, expected_result):
        element = self.wait_for_visible(locator)
        assert expected_result in element.text , f"Text not the same element.text = {element.text}, expected_result = {expected_result}"



    def select_by_value(self, select, value):
        element = self.wait_for_visible(select)
        select = Select(element)
        select.select_by_value(value)

    def switch_to_iframe(self):
        self.driver.switch_to.frame(self.wait_for_visible('//iframe'))

    def set_display_none(self, locator):
        element = self.wait_for_visible(locator)
        self.driver.execute_script('arguments[0].setAttribute("display", arguments[1])', element, 'none')

    def prompt_alert(self):
        alert = self.driver.switch_to.alert
        print(alert.text)
        alert.send_keys("Answer")
        alert.accept()

    def open_new_window(self):
        self.driver.execute_script("window.open()")
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        self.driver.close()

    def assert_value_in_element_attribute(self, locator, attribute, expected_result):
        element = self.wait_for_visible(locator)
        value = element.get_attribute(attribute)
        assert value == expected_result, "Attribute value not the same"

    def assert_actual_url(self, expected_url):
        actual_url = self.driver.current_url
        assert expected_url == actual_url, f"Expected URL: {expected_url}, Actual URL: {actual_url}"

    def assert_that_element_is_not_visible(self, element):
        try:
            self.driver.find_element(By.XPATH, element)
        except NoSuchElementException:
            assert True,  'Element is visible'

    def add_cookie(self, name, value):
        self.driver.add_cookie({'name': name, 'value': value})
        self.driver.refresh()

    def delete_cookies(self):
        self.driver.delete_cookies()
        self.driver.refresh()
