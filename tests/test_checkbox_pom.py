from pages.checkbox_page import CheckboxPage
def test_check_checkbox_pom(driver):
    page = CheckboxPage(driver)
    page.open()
    page.get_checkboxes()
    page.check_checkbox(1)
    assert page.is_checked(1)
    print("checkbox 2 is checked")
    
def test_uncheck_checkbox_pom(driver):
    page = CheckboxPage(driver)
    page.open()
    page.uncheck_checkbox(1)
    assert not page.is_checked(1)
    print("checkbox 2 is unselected")