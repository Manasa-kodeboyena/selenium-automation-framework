from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.common.by import By
import os
BASE_URL = "https://the-internet.herokuapp.com/"
def test_valid_login(driver):
    driver.get(f"{BASE_URL}/login")
    wait= WebDriverWait(driver,10)
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
    wait.until(EC.presence_of_element_located((By.ID,"flash")))
    assert "secure" in driver.current_url
    print("Valid login passed")
    
def test_invalid_login(driver):
    driver.get(f"{BASE_URL}/login")
    wait = WebDriverWait(driver, 10)
    driver.find_element(By.NAME,"username").send_keys("wronguser")
    driver.find_element(By.NAME, "password").send_keys("wrongpassword")
    driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
    wait.until(EC.presence_of_element_located((By.ID,"flash")))
    assert "secure" not in driver.current_url
    
    os.makedirs("screenshots",exist_ok = True)
    driver.save_screenshot("screenshots/invalid_login.png")
    print("invalid login test passed")
        