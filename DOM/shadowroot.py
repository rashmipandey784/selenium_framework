from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# 1️⃣ Shadow host
shadow_host = wait.until(
    EC.presence_of_element_located((By.ID, "shadow_host"))
)

shadow_root = shadow_host.shadow_root
shadow_element=shadow_root.find_element(By.CSS_SELECTOR,".info")
print(shadow_element.text)

