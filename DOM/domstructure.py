from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()

shadow_host = driver.find_element(By.XPATH, "//h1[text()='Simple template']")
print(shadow_host.text)



