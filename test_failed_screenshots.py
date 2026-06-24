from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
driver=webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/login")
    wait = WebDriverWait(driver,10)
    driver.find_element(By.ID, "username").send_keys("Wronguser")
    driver.find_element(By.ID,"password").send_keys("wrongpassword")
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    wait.until(EC.presence_of_element_located((By.ID, "flash")))
    assert "secure" in driver.current_url
except AssertionError:
    os.makedirs("screenshots",exist_ok=True)
    driver.save_screenshot("screenshots/failure.png")
    print("test failed! Screenshot saved to screenshots/failure.png")
    raise
finally:
    driver.quit()