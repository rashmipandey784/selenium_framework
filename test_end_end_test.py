from idlelib.parenmatch import CHECK_DELAY
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from util.browserutil import Browser_Util
from pageobjectmoddel.login import Login_Browser
from pageobjectmoddel.checkbox import Check_box
from pageobjectmoddel.alert import Window_alert
from pageobjectmoddel.dropdown import Window_handle
from conftest import browser_Instance
import json

data_path="data/test_e2eTestFramework.json"
with open(data_path)as f:
    test_data=json.load(f)
    test=test_data["data"]
#@pytest.mark.parametrize("testlist",test)
def test_e_e(browser_Instance):
    driver=browser_Instance
    l=Login_Browser(driver)
    for item in range(len(test)):
        email=test[0]["user_email"]
        Password=test[0]["userPassword"]
    l.Login(email,Password)
    c=Check_box(driver)
    c.Checked()
    al=Window_alert(driver)
    al.display_alert()
    dd=Window_handle(driver)
    dd.Drop_and_down()









