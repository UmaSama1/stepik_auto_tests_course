import os
from email._header_value_parser import get_attribute

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time
import math
import pyperclip

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/redirect_accept.html'
browser: WebDriver = webdriver.Chrome()
browser.get(link)
browser.find_element(By.XPATH, '//button[@type="submit"]').click()
browser.switch_to.window(browser.window_handles[1])
number = browser.find_element(By.XPATH, '//span[@id="input_value"]').text
y = calc(number)
browser.find_element(By.XPATH, '//input[@id="answer"]').send_keys(y)
browser.find_element(By.XPATH, '//button[contains(text(), "Submit")]').click()
# addToClipBoard = alert.split(': ')[-1]
# pyperclip.copy(addToClipBoard)
# alert.accept()
time.sleep(10)

# browser.find_element(By.XPATH, '//input[@name="firstname"]').send_keys('Uma')
# browser.find_element(By.XPATH, '//input[@name="lastname"]').send_keys('Sama')
# browser.find_element(By.XPATH, '//input[@name="email"]').send_keys('umasama1@gmail.com')
# file1 = browser.find_element(By.XPATH, '//input[@id="file"]').send_keys('/Users/umasama/Desktop/pythonProject/Lessons for automation/file.txt')
# browser.find_element(By.XPATH, '//button[@type="submit"]').click()
# time.sleep(15)
get_attribute
# y = calc(number)
# browser.find_element(By.XPATH, '//input[@id="answer"]').send_keys(y)
# browser.find_element(By.XPATH, '//input[@id="robotCheckbox"]').click()
# browser.find_element(By.XPATH, '//input[@id="robotsRule"]').click()
# browser.find_element(By.XPATH, '//button[contains(text(), "Submit")]').click()
# time.sleep(10)
