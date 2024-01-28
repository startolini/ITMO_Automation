import time

from pages.browser_tab import BrowserTab

def test_browser_tab(browser):
    page_browser = BrowserTab(browser)
    page_browser.visit()

    assert len(browser.window_handles) == 1
    # winflow_handes возвращает список list активных вкладок

    page_browser.new_tab.click()
    time.sleep(2)

    assert len(browser.window_handles) == 2

    # обращаемся к объекту browser и передаем как аргумент объект вкладки
    # на которую хотим переместиться, в данном случае 1ая вкладка
    browser.switch_to.window(browser.window_handles[0])
    time.sleep(2)

