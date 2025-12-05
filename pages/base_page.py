import allure
from curl import Url
from conftest import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

        
    # Открыть страницу
    def open_page(self, url):
        self.driver.get(url)

    # Получить url текущей страницы
    def get_current_url(self):
        return self.driver.current_url
    
    # Ссылка работает - осуществляется переход
    def cross_url(self, url):
        WebDriverWait(self.driver, 15).until(EC.url_to_be(url))   
    
    # Найти элемент
    def find_element(self, locator):
        self.driver.find_element(*locator)

    # Подождать элемент
    def wait_element(self, locator):
       WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))

    # Нажать на элемент
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    # Получить текст
    def get_text(self, locator):
        return self.driver.find_element(*locator).text
    
    # Передать значения
    def send_keys(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    # Переключить окно
    def tab_switch(self, driver):
        self.driver.switch_to.window(driver.window_handles[1])







