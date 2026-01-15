from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://vinothqaacademy.com/alert-and-popup/")

wait = WebDriverWait(driver, 10)

# Click Alert Box button (NO frame switch)
wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='Alert Box']")
    )
).click()

# Handle alert
alert = driver.switch_to.alert
print(alert.text)
alert.accept()

driver.find_element(By.ID,"vfb-5").send_keys("rashmi")