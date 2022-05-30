from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def setUp(browser):  # 'browser' is passed here from browser method below

    if browser == "edge":
        serv_obj = Service("C:\Browser_Drivers_for_Testing\msedgedriver.exe")
        driver = webdriver.Edge(service=serv_obj)
        print("Launching Edge Browser...")
    elif browser == "firefox":
        serv_obj = Service("C:\Browser_Drivers_for_Testing\geckodriver.exe")
        driver = webdriver.Firefox(service=serv_obj)
        print("Launching Firefox Browser...")
    else:
        serv_obj = Service("C:\Browser_Drivers_for_Testing\chromedriver.exe")
        driver = webdriver.Chrome(service=serv_obj)
    return driver


def pytest_addoption(parser):  # this will get value from Command line-CLI
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # this will return the browser value to setUp method so pass 'browser' in setup
    return request.config.getoption("--browser")

# ################################# to Generate html report ###############################################33
# this is hook to add environment info in html report::
def pytest_configure(config):
    config._metadata['Project name'] = "nop Commerce"
    config._metadata['Module name'] = "Customers"
    config._metadata['Tester'] = "Ali"

# this is hook to delete/modify environment info in html report::
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)