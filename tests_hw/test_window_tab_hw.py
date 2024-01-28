import time
from pages.links import Links

def test_browser_tab(browser):
    page_links = Links(browser)
    page_links.visit()
    time.sleep(3)

    assert page_links.home.get_text() == 'Home'
    assert page_links.home.get_dom_attribute('href') == 'https://demoqa.com'

    page_links.home.click()
    time.sleep(2)

    # winflow_handes возвращает список list активных вкладок
    assert len(browser.window_handles) == 2

