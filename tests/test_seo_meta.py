import time

import pytest

from pages.accordian import Accordian
from pages.alerts import Alerts
from pages.browser_tab import BrowserTab
from pages.demoqa import DemoQA

@pytest.mark.parametrize('pages', [Accordian, Alerts, BrowserTab, DemoQA])
def test_seo_meta(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)

    assert page.meta_tag.exist()
    assert page.meta_tag.get_dom_attribute('name') == 'viewport'
    assert page.meta_tag.get_dom_attribute('content') == 'width=device-width,initial-scale=1'

