from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from components.components import WebElement

class DemoQA(BasePage):
    # Здесь будет список элементов на конкретной странице DemoQA

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)

        self.icon = WebElement(driver, '#app > header > a')
        self.btn_elements = WebElement(driver, '#app > div > div > div.home-body > div > div:nth-child(1)')
        self.btn_elements1 = WebElement(driver, '//*[@id="app"]/div/div/div[2]/div/div[1]')
        self.footer_text = WebElement(driver, '#app > footer > span')
        self.headers = WebElement(driver, '#app > div > div > div.home-body > div > div > div > div.card-body > h5')
