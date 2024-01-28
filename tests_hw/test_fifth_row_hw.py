import time
from pages.webtables import WebTables


def test_fifth_row(browser):

    wt = WebTables(browser)
    wt.visit()

    wt.select_row.scroll_to_element()
    wt.select_row.click()
    wt.fifth_row.click()
    time.sleep(3)

    for i in range(3):
        wt.add_row.click()
        wt.modal_first_name.send_keys('Gendalf')
        wt.modal_last_name.send_keys('Wizard')
        wt.modal_email.send_keys('gen@dalf.wz')
        wt.modal_age.send_keys('97')
        wt.modal_salary.send_keys('150000')
        wt.modal_dept.send_keys('Mordor')
        wt.bth_add_modal.click()
        time.sleep(4)

    assert wt.forth_row_fn.get_text() == 'Gendalf'

    wt.btn_next.click()
    time.sleep(3)

    assert wt.page_num.get_dom_attribute('value') == '2'

    wt.btn_prev.click()
    time.sleep(3)

    assert wt.page_num.get_dom_attribute('value') == '1'

