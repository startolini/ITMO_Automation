import time
from selenium.webdriver import Keys
from pages.slider import Slider

def test_browser_tab(browser):
    page_slider = Slider(browser)
    page_slider.visit()
    assert page_slider.slider.exist()
    assert page_slider.inp.exist()

    while not page_slider.inp.get_dom_attribute('value') == '50':
        page_slider.slider.send_keys(Keys.ARROW_RIGHT)

    assert page_slider.slider.get_dom_attribute('value') == '50'