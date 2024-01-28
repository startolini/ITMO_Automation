from pages.text_box import TextBox

def test_placeholder(browser):
    text_form = TextBox(browser)
    text_form.visit()
    assert text_form.full_name.get_dom_attribute('placeholder') == 'Full Name'

