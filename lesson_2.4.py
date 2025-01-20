from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), "100"))
    # WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.XPATH, '//h5[@id="price"]'), '100'))
    browser.find_element(By.XPATH, '//button[@id="book"]').click()
    browser.execute_script("window.scrollBy(0, 100);")
    number = browser.find_element(By.XPATH, '//span[@id="input_value"]').text
    y = calc(number)
    browser.find_element(By.XPATH, '//input[@id="answer"]').send_keys(y)
    browser.find_element(By.XPATH, '//button[contains(text(), "Submit")]').click()
finally:
    time.sleep(5)