from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class Testwebsite(unittest.TestCase):
    def test_web(self):
        self.browser = webdriver.Chrome()
        self.browser.get("http://suninjuly.github.io/registration1.html")
        input1 = self.browser.find_element(By.XPATH, '//input[contains(@class, "first") and @required]')
        input1.send_keys('Uma')
        input2 = self.browser.find_element(By.XPATH, '//input[contains(@class, "second") and @required]')
        input2.send_keys('Sama')
        input3 = self.browser.find_element(By.XPATH, '//input[contains(@class, "third") and @required]')
        input3.send_keys('umasama1@gmail.com')
        button = self.browser.find_element(By.CLASS_NAME, "btn")
        button.click()
        self.assertEquals('Congratulations! You have successfully registered!',
                          self.browser.find_element(By.XPATH, '//h1').text)

    def test_web2(self):
        self.browser = webdriver.Chrome()
        self.browser.get("http://suninjuly.github.io/registration2.html")
        input1 = self.browser.find_element(By.XPATH, '//input[contains(@class, "first") and @required]')
        input1.send_keys('Uma')
        input2 = self.browser.find_element(By.XPATH, '//input[contains(@class, "second") and @required]')
        input2.send_keys('Sama')
        input3 = self.browser.find_element(By.XPATH, '//input[contains(@class, "third") and @required]')
        input3.send_keys('umasama1@gmail.com')
        button = self.browser.find_element(By.CLASS_NAME, "btn")
        button.click()
        self.assertEquals('Congratulations! You have successfully registered!',
                          self.browser.find_element(By.XPATH, '//h1').text)

