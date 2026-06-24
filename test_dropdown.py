import select
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://The-Internet.herokuapp.com/dropdown")
wait = WebDriverWait(driver, 10)
dropdown = driver.find_element(By.ID, "dropdown")
select=Select(dropdown)
select.select_by_visible_text("Option 1")
print("Selected Option 1")
select.select_by_value("2")
print("Selected Option 2")
