from pages.base_page import BasePage
from components.components import WebElement


class ModalDialogs(BasePage):
    # Здесь будет список элементов на конкретной странице Modal Dialogs
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.submenu_items = WebElement(driver, '#item-0')
        self.icon = WebElement(driver, '#app > header > a > img')
        self.small_modal = WebElement(driver, '#showSmallModal')
        self.large_modal = WebElement(driver, '#showLargeModal')
        self.close_small_modal = WebElement(driver, '#closeSmallModal')
        self.close_large_modal = WebElement(driver, '#closeLargeModal')
