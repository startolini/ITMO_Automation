import time
import pytest

from pages.modal_dialogs import ModalDialogs
import requests

def test_check_modal(browser):
    
    md = ModalDialogs(browser)
    md.visit()

    try:
        response = requests.get('https://demoqa.com/modal-dialogs')
        response.raise_for_status()  # Проверяем статус ответа HTTP
    except requests.exceptions.RequestException:
        pytest.skip("Страница недоступна, пропускаем тест")

    md.small_modal.click()
    time.sleep(2)
    md.close_small_modal.click()
    time.sleep(2)

    md.large_modal.click()
    time.sleep(2)
    md.close_large_modal.click()
    time.sleep(2)
