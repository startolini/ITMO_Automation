import time
from pages.text_box import TextBox


def test_clear(browser):
    text_form = TextBox(browser)
    text_form.visit()
    text_form.full_name.send_keys('shilozhopik')
    time.sleep(3)
    text_form.full_name.clear()
    time.sleep(3)

    assert text_form.full_name.get_text() == ''