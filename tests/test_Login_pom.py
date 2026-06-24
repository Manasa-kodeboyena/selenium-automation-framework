from pages.login_page import LoginPage

def test_valid_Login_pom(driver):
    page = LoginPage(driver)
    page.open()
    page.login("tomsmith", "SuperSecretPassword!")
    assert "secure" in driver.current_url
    print("Valid login passed")
    
def test_invalid_login_pom(driver):
    page=LoginPage(driver)
    page.open()
    page.login("wronguser","wrongpassword")
    assert "secure" not in driver.current_url
    print("invalid login passed!")