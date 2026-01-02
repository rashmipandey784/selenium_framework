from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.window import WindowTypes

from util.browserutil import Browser_Util
from conftest import browser_Instance
class Check_box(Browser_Util):
    def __init__(self,driver):
        super().__init__(driver)
        self.male_checkbox=(By.ID,"male")
    def Checked(self):
        window = self.driver.window_handles
        self.driver.switch_to.new_window(WindowTypes.WINDOW)
        self.driver.get("https://testautomationpractice.blogspot.com/")
        self.driver.find_element(*self.male_checkbox).click()
        #self.driver.switch_to.window(window[0])
        sleep(5)


