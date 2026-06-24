from pages.dropdown_page import DropdownPage
def test_dropdown_pom (driver):
    page = DropdownPage(driver)
    page.open()
    page.select_option(2)
    selected_option = page.get_selected_option()
    assert selected_option == "Option 2"
    print(f"Selected {selected_option}")