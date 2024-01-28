from pages.base_page import BasePage
from components.components import WebElement


class Alerts(BasePage):
    # Здесь будет список элементов на конкретной странице WebTables
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/alerts'
        super().__init__(driver, self.base_url)

        self.btn_al = WebElement(driver, '#alertButton')
        self.btn_cnf = WebElement(driver, '#confirmButton')
        self.btn_promt = WebElement(driver, '#promtButton')
        self.text_block = WebElement(driver, '#confirmResult')
        self.promt_result = WebElement(driver, '#promptResult')
        self.timer_alert = WebElement(driver, '#timerAlertButton')

