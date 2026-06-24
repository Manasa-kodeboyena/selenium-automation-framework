from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class CheckboxPage:
    URL = "https://the-internet.herokuapp.com/checkboxes"
    def __init__(self,driver):
        self.driver = driver
        self.wait= WebDriverWait(driver,10)
    def open(self):
        self.driver.get(self.URL)

    def get_checkboxes(self):
        checkboxes=self.driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
        return checkboxes
        
    
    def check_checkbox(self,index):
        checkboxes = self.get_checkboxes()
        checkbox=checkboxes[index]
        if not checkbox.is_selected():
            checkbox.click()
            
    def uncheck_checkbox(self,index):
        checkboxes = self.get_checkboxes()
        checkbox = checkboxes[index]
        if checkbox.is_selected():
            checkbox.click()
            
    def is_checked(self, index):
        checkboxes = self.get_checkboxes()
        checkbox = checkboxes[index]
        return checkbox.is_selected()
    
    def checkbox(self,index):
        self.open()
        self.check_checkbox(index)