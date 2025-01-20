from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration2.html")
    input1 = browser.find_element(By.XPATH, '//input[contains(@class, "first") and @required]')
    input1.send_keys('Uma')
    input2 = browser.find_element(By.XPATH, '//input[contains(@class, "second") and @required]')
    input2.send_keys('Sama')
    input3 = browser.find_element(By.XPATH, '//input[contains(@class, "third") and @required]')
    input3.send_keys('umasama1@gmail.com')

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

    time.sleep(2)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    assert 'Congratulations! You have successfully registered!' == welcome_text



finally:
    time.sleep(10)
    browser.quit()
