import time
from pages.koup import Koup
from pages.koup_add_remove import KoupAddRemove


def test_btn_add(browser):

    koup = Koup(browser)
    koup.visit()
    koup.add_remove.click()
    koup_add_rem = KoupAddRemove(browser)

    time.sleep(5)
    assert koup_add_rem.add_element.get_dom_attribute('onclick') == 'addElement()'

    for i in range(4):
        koup_add_rem.add_element.click()

    assert koup_add_rem.delete.check_count_elements(4)

    # проверка всех элементов
    for element in koup_add_rem.delete.find_elements():
        assert element.text == 'Delete'

    # проверка только для первого элемента !!! НЕПРАВИЛЬНО !!!
    assert koup_add_rem.delete.get_text() == 'Delete'

    """ When Кликнуть на каждую кнопку "Delete" """
    while koup_add_rem.delete.exist():
        koup_add_rem.delete.click()

    assert not koup_add_rem.delete.exist()





