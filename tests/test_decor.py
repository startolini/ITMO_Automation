import time
import pytest
from pages.demoqa import DemoQA
from pages.radio_button import RadioButton

@pytest.mark.skip
def test_decor(browser):
    qa = DemoQA(browser)
    qa.visit()
    time.sleep(3)

    assert qa.headers.check_count_elements(6)

    # проверяем что есть какой-то текст в заголовках
    for element in qa.headers.find_elements():
        assert element.text != ''

@pytest.mark.skipif(True, reason='просто пропуск')
def test_radio(browser):
    rb = RadioButton(browser)
    rb.visit()

    rb.yes_radio.click_force()
    assert rb.text.get_text() == 'You have selected Yes'

    rb.imp_radio.click_force()
    assert rb.text.get_text() == 'You have selected Impressive'

    assert 'disabled' in rb.no_radio.get_dom_attribute('class')
