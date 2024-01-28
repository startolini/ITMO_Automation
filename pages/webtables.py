from pages.base_page import BasePage
from components.components import WebElement


class WebTables(BasePage):
    # Здесь будет список элементов на конкретной странице WebTables
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.first_record_delete = WebElement(driver, '//*[contains(@id, "delete")]', 'xpath')
        self.no_rows = WebElement(driver, 'div.rt-noData')
        self.add_row = WebElement(driver, '#addNewRecordButton')
        self.window_add_modal = WebElement(driver, 'body > div.fade.modal.show > div > div')
        self.bth_add_modal = WebElement(driver, '#submit')
        self.modal_first_name = WebElement(driver, '#firstName')
        self.modal_last_name = WebElement(driver, '#lastName')
        self.modal_email = WebElement(driver, '#userEmail')
        self.modal_age = WebElement(driver, '#age')
        self.modal_salary = WebElement(driver, '#salary')
        self.modal_dept = WebElement(driver, '#department')

        self.forth_row_fn = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(1)')
        self.forth_row_edit = WebElement(driver, '#edit-record-4')
        self.forth_row_delete = WebElement(driver, '#delete-record-4')

        self.select_row = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-center > span.select-wrap.-pageSizeOptions > select')
        self.fifth_row = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-center > span.select-wrap.-pageSizeOptions > select > option:nth-child(1)')

        self.btn_next = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-next > button')
        self.btn_prev = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-previous > button')
        self.sec_page_first_cell = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(1) > div > div:nth-child(1)')
        self.page_num_div = WebElement(driver, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]/div[2]/div/div[2]/span[1]/div', 'xpath')
        self.page_num = WebElement(driver, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]/div[2]/div/div[2]/span[1]/div/input', 'xpath')
        self.total_page = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-center > span.-pageInfo > span')
        self.first_name_column = WebElement(driver, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[1]', 'xpath')
        self.last_name_column = WebElement(driver, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[2]', 'xpath')


