from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class DropdownPage:
    URL = "https://the-internet.herokuapp.com/dropdown"
    DROPDOWN = (By.ID, "dropdown")
    
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  
        
    def select_dropdown(self):  
        dropdown=self.driver.find_element(*self.DROPDOWN)
        return Select(dropdown)
        
    def open(self):
        self.driver.get(self.URL)  
          
    def select_option(self,option_no):
        select = self.select_dropdown()
        select.select_by_value(str(option_no))
        
    def get_selected_option(self):
        select = self.select_dropdown()
        return select.first_selected_option.text
        
    def dropdown(self,option_on):
        self.open()
        self.select_dropdown()
        self.select_option(option_on)
        
         