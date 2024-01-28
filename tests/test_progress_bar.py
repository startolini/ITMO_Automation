import time
from pages.progress_bar import ProgressBar

def test_progress_bar(browser):
    pb = ProgressBar(browser)
    pb.visit()
    time.sleep(3)

    pb.start_stop_btn.click()

    while True:
        if pb.progress_bar.get_dom_attribute('aria-valuenow') == '51':
            pb.start_stop_btn.click()
            break

    time.sleep(2)
    assert pb.progress_bar.get_dom_attribute('aria-valuenow') == '51'