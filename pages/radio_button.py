from components.components import WebElement
from pages.base_page import BasePage


class RadioButton(BasePage):
    # Здесь будет список элементов на конкретной странице Radio Button

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/radio-button'
        super().__init__(driver, self.base_url)

        self.yes_radio = WebElement(driver, '#yesRadio')
        self.imp_radio = WebElement(driver, '#impressiveRadio')
        self.no_radio = WebElement(driver, '#noRadio')
        self.text = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div:nth-child(2) > p')
