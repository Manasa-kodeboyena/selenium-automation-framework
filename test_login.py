from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
wait = WebDriverWait(driver,10)
print("Page loaded successfully!")
driver.find_element(By.NAME,"username").send_keys("tomsmith")
driver.find_element(By.NAME, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
wait.until(EC.presence_of_element_located((By.ID, "flash")))
print(f"Currevt URL: {driver.current_url}")
print(f"Page Title: {driver.title}")
assert "The Internet" in driver.title
print(f"Page tile : {driver.title}")
print("Login is successful!")
input("Press Enter to close")
driver.quit()