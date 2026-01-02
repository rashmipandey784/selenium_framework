from time import sleep

from util.browserutil import Browser_Util
from selenium import webdriver
from selenium.webdriver.common.window import WindowTypes

from selenium.webdriver.common.by import By
class Window_alert(Browser_Util):
    def __init__(self,driver):
        super().__init__(driver)
        self.alertbutton=(By.ID,"alertBtn")


    def display_alert(self):

        self.driver.find_element(*self.alertbutton).click()
        alert_btn=self.driver.switch_to.alert
        sleep(5)
        alert_btn.accept()
        #self.driver.switch_to.window(window[1])







