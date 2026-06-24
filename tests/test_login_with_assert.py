from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("https://The-Internet.herokuapp.com/login")
wait = WebDriverWait(driver, 10)
driver.find_element(By.NAME, "username").send_keys("wronguser")
driver.find_element(By.ID, "password").send_keys("wrongpassword")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='flash']")))
print("upto here evrything is loaded")
element = driver.find_element(By.ID, "flash")
print(element.text)
assert "invalid" in element.text.lower()
print("Error message verified!")
driver.quit()
