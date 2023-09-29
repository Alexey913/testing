# Нужно написать сквозной тест с использованием Selenium, который авторизует пользователя на 
# сайте https://www.saucedemo.com/. 
# Данные для входа - логин: "standard_user", пароль: "secret_sauce". 
# Проверить, что авторизация прошла успешно и отображаются товары.
# Вам необходимо использовать WebDriver для открытия страницы и методы sendKeys() для ввода 
# данных в поля формы, и submit() для отправки формы. После этого, проверьте, что на странице 
# отображаются продукты (productsLabel.getText() = "Products").

import unittest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestSelenium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Edge(service=Service(executable_path='msedgedriver.exe'))
        self.username = 'standard_user'
        self.password = 'secret_sauce'
    def test_selenium(self):
        self.driver.get('https://www.saucedemo.com/')
        name = self.driver.find_element(By.NAME, 'user-name')
        name.send_keys(self.username)
        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(self.password)
        submit = self.driver.find_element(By.NAME, 'login-button')
        submit.click()
        self.assertIn('Products', self.driver.find_element(By.XPATH, '/html/body').text)

    def tearDown(self) -> None:
        self.driver.close()

if __name__ == "__main__":
    unittest.main()