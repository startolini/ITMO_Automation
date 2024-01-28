from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from components.components import WebElement

class Koup(BasePage):
    # Здесь будет список элементов на конкретной странице Hero Kuapp

    def __init__(self, driver):
        self.base_url = 'https://the-internet.herokuapp.com/'
        super().__init__(driver, self.base_url)

        self.add_remove = WebElement(driver, '#content > ul > li:nth-child(2) > a')
        # self.btn_elements = WebElement(driver, '#app > div > div > div.home-body > div > div:nth-child(1)')
        # self.btn_elements1 = WebElement(driver, '//*[@id="app"]/div/div/div[2]/div/div[1]')
        # self.footer_text = WebElement(driver, '#app > footer > span')
