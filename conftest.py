import os
from time import sleep

from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.window import WindowTypes

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="Chrome", help="browser selection"
    )
@pytest.fixture(scope="function")
def browser_Instance(request):
    global driver
    browser_name=request.config.getoption("browser_name")
    #service_obj=Service()
    if browser_name=="Chrome" :
        driver=webdriver.Chrome()
    if browser_name=="firefox":
        driver=webdriver.Firefox()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    #driver.switch_to.new_window(WindowTypes.WINDOW)
    #driver.get("https://testautomationpractice.blogspot.com/")
    yield driver
    driver.quit()

