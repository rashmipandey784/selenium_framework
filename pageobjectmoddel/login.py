from selenium import webdriver
from selenium.webdriver.common.by import By

from util.browserutil import Browser_Util
class Login_Browser(Browser_Util):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        self.user=(By.ID,"username")
        self.password=(By.ID,"password")
        self.submit=(By.ID,"signInBtn")
    def Login(self,user,password):
        self.driver.find_element(*self.user).send_keys(user)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.submit).click()



