import time
from pages.alerts import Alerts


def test_alert(browser):

    al_page = Alerts(browser)
    al_page.visit()

    assert not al_page.alert()

    al_page.btn_al.click()
    time.sleep(3)

    assert al_page.alert()


def test_alert_text(browser):

    al_page = Alerts(browser)
    al_page.visit()
    time.sleep(3)


    al_page.btn_al.click()
    time.sleep(3)

    assert al_page.alert().text == 'You clicked a button'
    al_page.alert().accept()

    assert not al_page.alert()

def test_confirm(browser):
    al_page = Alerts(browser)
    al_page.visit()

    al_page.btn_cnf.click()
    time.sleep(2)
    al_page.alert().dismiss()

    assert al_page.text_block.get_text() == 'You selected Cancel'

def test_prompt(browser):
    al_page = Alerts(browser)
    al_page.visit()
    name = 'Ilya'

    al_page.btn_promt.click()
    time.sleep(2)

    al_page.alert().send_keys(name)
    al_page.alert().accept()

    assert al_page.promt_result.get_text() == f'You entered {name}'
