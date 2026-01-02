import os.path
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
start_date = "2026-01-25"
driver.execute_script("window.scrollBy(0,2300);")
date_element = driver.find_element(By.ID, "start-date")
#driver.execute_script("window.scrollBY(0,500);")
driver.execute_script("arguments[0].setAttribute('value',arguments[1])", date_element, start_date)
end_date="2026-01-26"
end_element=driver.find_element(By.ID,"end-date")
driver.execute_script("arguments[0].setAttribute('value',arguments[1])",end_element,end_date)
driver.find_element(By.XPATH,"//button[text()='Submit']").click()
path = os.path.abspath("sel.txt")
if not os.path.exists(path):
    print(f"file not found at {path}")
    with open(path,"w") as f:
        f.write("write something for selenium")
    print(f"file is created {path}")
file=driver.find_element(By.ID,"singleFileInput")

file.send_keys(path)
driver.find_element(By.XPATH,"//button[text()='Upload Single File']").click()
wait=WebDriverWait(driver,5)
upload_txt=wait.until(EC.visibility_of_element_located((By.ID,"singleFileStatus")))
assert "sel.txt" in upload_txt.text
print(f"file upload successfully:{path}")

txt=driver.find_element(By.XPATH,"//table[@id='taskTable']//tr[2]/td[3]")
print(txt.text)
chrome_cpu=driver.find_element(By.XPATH,"//div[@id='displayValues']//p[3]")
print(chrome_cpu.text)

table_item=driver.find_elements(By.XPATH,"//table[@id='taskTable']//tr[2]")
for item in table_item:
    print(item.text)
#driver.find_element(By.XPATH,"//table[@id='productTable']//tr[2]/td[4]/input[@type='checkbox']").click()
#sleep(10)
checkboxes=driver.find_elements(By.XPATH,"//table[@id='productTable']//td/input")
for box in checkboxes:
    box.click()
    assert box.is_selected()

action=ActionChains(driver)
drag_btn=driver.find_element(By.ID,"draggable")
drop_btn=driver.find_element(By.ID,"droppable")
action.drag_and_drop(drag_btn,drop_btn)
dblick=driver.find_element(By.XPATH,"//button[text()='Copy Text']")
action.double_click(dblick)
sleep(7)
