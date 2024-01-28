import time

import pytest

from pages.accordian import Accordian
from pages.alerts import Alerts
from pages.browser_tab import BrowserTab
from pages.demoqa import DemoQA


@pytest.mark.skip('НЕ НУЖЕН ТК ТАКАЯ ЖЕ ПРОВЕРКА ЕСТЬ В СЛЕДУЮЩЕМ ТЕСТЕ')
def test_seo(browser):
    demo_qa_page = DemoQA(browser)
    demo_qa_page.visit()
    actual_seo = demo_qa_page.get_title()
    expected_seo = 'DEMOQA'

    assert actual_seo == expected_seo


@pytest.mark.parametrize('pages', [Accordian, Alerts, DemoQA, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)
    assert page.get_title() == 'DEMOQA'
