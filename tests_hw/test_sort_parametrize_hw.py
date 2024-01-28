import time
import pytest

from components.components import WebElement
from pages.webtables import WebTables


@pytest.mark.parametrize("col_locator", [
    ('//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[1]', 'xpath'),
    # Локатор для первого столбца
    ('//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[2]', 'xpath'),
    # Локатор для второго столбца
    ('//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[3]', 'xpath'),
    # Локатор для третьего столбца
    ('//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[4]', 'xpath'),
    # Локатор для четвертого столбца
    ('//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[5]', 'xpath'),
    # Локатор для пятого столбца
    ('//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[6]', 'xpath'),
    # Локатор для шестого столбца
])

def test_table_sorting(browser, col_locator):
    locator, loc_style = col_locator

    wt = WebTables(browser)
    wt.visit()

    # Находим заголовок столбца и кликаем на него для сортировки
    col_header = WebElement(browser, locator, loc_style)
    col_header.click()

    # Ждем сортировки (можно добавить явные ожидания)
    time.sleep(2)

    # Получаем значения столбца после сортировки
    col_values = col_header.get_dom_attribute('class')
    actual_values = 'rt-th rt-resizable-header -sort-asc -cursor-pointer'

    # Проверяем, что столбец отсортирован по возрастанию
    assert actual_values == col_values

    # Кликаем на заголовок столбца еще раз для сортировки по убыванию
    col_header.click()

    # Ждем сортировки (можно добавить явные ожидания)
    time.sleep(2)

    # Получаем значения столбца после второй сортировки
    col_2_values = col_header.get_dom_attribute('class')
    actual_2_values = 'rt-th rt-resizable-header -sort-desc -cursor-pointer'

    # Проверяем, что столбец отсортирован по убыванию
    assert actual_2_values == col_2_values
