from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    URL = "https://the-internet.herokuapp.com/login"
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME,"password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH_MESSAGE = (By.ID,"flash")
    def __init__(self,driver):
         self.driver = driver
         self.wait = WebDriverWait(driver,10)
    def open(self):
        self.driver.get(self.URL)
    def enter_username(self,username):
        self.driver.find_element(*self.USERNAME).send_keys(username)
    def enter_password(self,password):
        self.driver.find_element(*self.PASSWORD).send_keys(password)
    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
    def login(self,username,password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        self.wait.until(EC.presence_of_element_located(self.FLASH_MESSAGE))