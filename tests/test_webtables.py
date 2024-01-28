import time
from pages.webtables import WebTables


def test_webtables(browser):

    wt = WebTables(browser)
    wt.visit()

    assert not wt.no_rows.exist()

    while wt.first_record_delete.exist():
        wt.first_record_delete.click()

    time.sleep(4)
    assert wt.no_rows.exist()





