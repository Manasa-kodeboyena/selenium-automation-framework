import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--headless")           
    options.add_argument("--no-sandbox")         
    options.add_argument("--disable-dev-shm-usage")  
    options.add_argument("--start-maximized")
    
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()