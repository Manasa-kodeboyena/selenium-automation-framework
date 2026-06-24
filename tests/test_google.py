from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
def test_google_search(driver):
    driver.get("https://www.google.com")
    wait = WebDriverWait(driver,10)
    search_box = wait.until(
        EC.elements_to_be_clickable((By.Name,"q"))
    )
    search_box.clear()
    search_box.send_keys("Selenium Python")
    search_box.send_keys(Keys.RETURN)
    wait.unit(EC.presence_of_element_located((By.ID,"search")))
    assert "Selenium" in driver.title
    print(f"Page title: {driver.title}")