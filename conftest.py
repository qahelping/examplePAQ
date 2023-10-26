import time
from datetime import datetime

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOption
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.webdriver.firefox.options import Options as FirefoxOption
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from allure_commons.types import AttachmentType

from data import USER_ELENA
from pages import LoginPage


def pytest_addoption(parser):
    parser.addoption('--headless',
                     default='False',
                     help='headless options: "yes" or "no"')
    parser.addoption('--browser',
                     default='chrome',
                     help='option to define type of browser')


def create_chrome(headless=True):
    chrome_option = ChromeOption()
    if headless:
        chrome_option.add_argument('--headless')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_option)
    return driver


def create_firefox(headless=True):
    ff_option = FirefoxOption()
    if headless == 'True':
        ff_option.add_argument('--headless')
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=ff_option)
    return driver


@pytest.fixture(autouse=True)
def driver(request):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.implicitly_wait(5)
    driver.maximize_window()

    yield driver
    driver.quit()


# set up a hook to be able to check if a test has failed
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"

    setattr(item, "rep_" + rep.when, rep)


# check if a test has failed
@pytest.fixture(scope="function", autouse=True)
def test_failed_check(request):
    yield
    # request.node is an "item" because we use the default
    # "function" scope
    if request.node.rep_setup.failed:
        print("setting up a test failed!", request.node.nodeid)
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            driver = request.node.funcargs['driver']
            take_screenshot(driver, request.node.nodeid)
            print("executing test failed", request.node.nodeid)


# make a screenshot with a name of the test, date and time
def take_screenshot(driver, nodeid):
    time.sleep(1)
    file_name = f'{datetime.today().strftime("%Y-%m-%d_%H:%M")}.png'.replace("/", "_").replace("::", "__")
    driver.save_screenshot('failed_screenshot/' + file_name)
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


@pytest.fixture(autouse=False)
def login(request):
    login = LoginPage(request.node.funcargs['driver'])
    login.login(USER_ELENA)
