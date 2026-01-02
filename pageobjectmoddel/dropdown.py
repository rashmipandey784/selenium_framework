from util.browserutil import Browser_Util
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select

class Window_handle(Browser_Util):
    def __init__(self,driver):
        super().__init__(driver)
    def Drop_and_down(self):
        window=self.driver.window_handles
        self.driver.get("https://testautomationpractice.blogspot.com/")
        drp_dwn=Select(self.driver.find_element(By.ID,"country"))
        drp_dwn.select_by_index(3)
        drp_dwn.select_by_visible_text("Germany")
        drp_dwn.select_by_value("usa")







