from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
BASE_URL = "https://the-internet.herokuapp.com"
def test_dropdown(driver):
    driver.get(f"{BASE_URL}/dropdown")
    dropdown=driver.find_element(By.ID,"dropdown")
    select=Select(dropdown)
    select.select_by_visible_text("Option 1")
    print("Option-1 is selected!")
    select.select_by_value("2")
    print("option-2 is selected!")
    selected_option=select.first_selected_option
    assert selected_option.text == "Option 2"
    print(f"confirm selected {selected_option.text}")
 