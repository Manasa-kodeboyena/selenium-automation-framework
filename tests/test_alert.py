from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
alert=driver.switch_to.alert
print(f"Alert text:{alert.text}")
alert.accept()
print("alert accepted")

driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
alert = driver.switch_to.alert
print(f"Confirm text: {alert.text}")
alert.accept()
print("Alert dismissed")

driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
alert = driver.switch_to.alert
alert.send_keys("Manasa")
alert.accept()
print("Prompt is accepted!")

input("Press Enter to close")
driver.quit()