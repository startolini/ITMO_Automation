from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')

# поиск элемента
username = driver.find_element(By.CSS_SELECTOR, '#user-name')
password = driver.find_element(By.CSS_SELECTOR, '#password')
submit = driver.find_element(By.CSS_SELECTOR, '#login-button')

if username and password and submit:
    print('Элементы найдены')
else:
    print('Не найдено ничего')