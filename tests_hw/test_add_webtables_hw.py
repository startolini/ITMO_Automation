import time
from pages.webtables import WebTables


def test_add_webtables(browser):

    wt = WebTables(browser)
    wt.visit()
    wt.add_row.click()

    assert wt.window_add_modal.exist()
    wt.bth_add_modal.click()

    assert wt.window_add_modal.exist()
    time.sleep(2)

    wt.modal_first_name.send_keys('Gendalf')
    wt.modal_last_name.send_keys('Wizard')
    wt.modal_email.send_keys('gen@dalf.wz')
    wt.modal_age.send_keys('97')
    wt.modal_salary.send_keys('150000')
    wt.modal_dept.send_keys('Mordor')
    wt.bth_add_modal.click()
    time.sleep(2)

    assert wt.forth_row_fn.get_text() == 'Gendalf'

    wt.forth_row_edit.click()
    wt.modal_first_name.clear()
    wt.modal_first_name.send_keys('Sauron')
    wt.bth_add_modal.click()
    time.sleep(2)

    assert wt.forth_row_fn.get_text() == 'Sauron'

    wt.forth_row_delete.click()

    assert wt.forth_row_fn.get_text() == ' '







