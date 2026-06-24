from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
driver= webdriver.Chrome()
driver.get("https://The-Internet.herokuapp.com/checkboxes")
wait = WebDriverWait(driver,10)
checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
print(len(checkboxes))
print(f"1st checkbox is selected {checkboxes[0].is_selected()}")
print(f"2nd checkbox is selected {checkboxes[1].is_selected()}")
if not checkboxes[0].is_selected() :
    checkboxes[0].click()
    print("1st checkbox is selected")
if not checkboxes[1].is_selected() :
    checkboxes[1].click()
    print("2nd checkbox is selected")
input("Press Enter to close")
driver.quit()