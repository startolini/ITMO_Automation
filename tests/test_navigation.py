import time

from pages.demoqa import DemoQA
from pages.elements import Elements


def test_navigation(browser):
    demo_qa_page = DemoQA(browser)
    el_page = Elements(browser)

    demo_qa_page.visit()
    demo_qa_page.btn_elements.click()
    el_page.refresh()
    el_page.back()
    demo_qa_page.forward()

    assert el_page.equal_url()
