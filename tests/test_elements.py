from pages.elements import Elements

def test_elements(browser):
    el_page = Elements(browser)
    el_page.visit()
    assert el_page.btns_first_menu.check_count_elements(9)
