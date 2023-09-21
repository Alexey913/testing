# Напишите автоматизированный тест, который выполнит следующие шаги:
# 1. Открывает главную страницу Google.
# 2. Вводит "Selenium" в поисковую строку и нажимает кнопку "Поиск в Google".
# 3. В результатах поиска ищет ссылку на официальный сайт Selenium 
# (https://www.selenium.dev) и проверяет, что ссылка действительно присутствует среди 
# результатов поиска

import unittest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestSelenium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Edge(service=Service(executable_path='msedgedriver.exe'))

    def test_selenium(self):
        self.driver.get('https://www.google.ru/')
        elem = self.driver.find_element(By.NAME, 'q')
        elem.send_keys('Selenium')
        elem.send_keys(Keys.RETURN)
        self.assertIn('https://www.selenium.dev', self.driver.find_element(By.XPATH, '/html/body').text)

    def tearDown(self) -> None:
        self.driver.close()

if __name__ == "__main__":
    unittest.main()