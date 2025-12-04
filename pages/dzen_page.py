import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.dzen_page_locators import DzenPageLocators

class DzenPage(BasePage):
    @allure.step('Проверка загрузки страницы "Дзен"')
    def waiting_loading_dzen(self):
        self.wait_element(DzenPageLocators.ALL_ABOUT_DZEN)  
    
    
    @allure.step('Проверка открытия страницы "Дзен"')
    def check_go_to_dzen(self):
        current_url = self.get_current_url()
        assert current_url == 'https://dzen.ru/?yredirect=true', 'Страница Дзен не открылась'

