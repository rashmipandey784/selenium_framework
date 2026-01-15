from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# 1️⃣ First shadow host
shadow_host_1 = wait.until(
    EC.presence_of_element_located((By.ID, "shadow_host")))

shadow_root_1 = shadow_host_1.shadow_root

# 2️⃣ Second shadow host INSIDE first shadow root
shadow_host_2 = shadow_root_1.find_element(By.CSS_SELECTOR, "#nested_shadow_content")

shadow_root_2 = shadow_host_2.shadow_root

# 3️⃣ Target element inside second shadow root
nested_element1=shadow_root_2.find_element(By.CSS_SELECTOR,"#nested_shadow_content div")
print(nested_element1.text)

#nested_element2=shadow_root_2.find_element(By.CSS_SELECTOR,"a[href='https://www.pavantestingtools.com/']")
#nested_element2.click()