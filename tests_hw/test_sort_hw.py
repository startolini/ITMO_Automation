import time
import pytest

from components.components import WebElement
from pages.webtables import WebTables

def test_sort(browser):
    wt = WebTables(browser)
    wt.visit()

    wt.first_name_column.click()
    time.sleep(2)

    assert wt.first_name_column.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    time.sleep(2)

    wt.first_name_column.click()
    time.sleep(2)

    assert wt.first_name_column.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-desc -cursor-pointer'
    time.sleep(2)

    wt.last_name_column.click()
    time.sleep(2)

    assert wt.last_name_column.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    time.sleep(2)

    wt.last_name_column.click()
    time.sleep(2)

    assert wt.last_name_column.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-desc -cursor-pointer'
