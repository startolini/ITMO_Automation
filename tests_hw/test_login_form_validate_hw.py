import time
from pages.form_page import FormPage


def test_login_validate(browser):
    reg_form = FormPage(browser)
    reg_form.visit()

    assert reg_form.first_name.get_dom_attribute('placeholder') == 'First Name'
    assert reg_form.last_name.get_dom_attribute('placeholder') == 'Last Name'
    assert reg_form.user_email.get_dom_attribute('pattern') == '^([a-zA-Z0-9_\\-\\.]+)@([a-zA-Z0-9_\\-\\.]+)\\.([a-zA-Z]{2,5})$'

    reg_form.btn_submit.click_force()
    assert reg_form.user_form.get_dom_attribute('class') == 'was-validated'
