import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.dzen_page_locators import DzenPageLocators
from curl import Url

class DzenPage(BasePage):
    @allure.step('Проверка загрузки страницы "Дзен"')
    def waiting_loading_dzen(self):
        self.cross_url(Url.dzen_page)
    
    @allure.step('Проверка загрузки элемента страницы "Дзен"')
    def waiting_loading_research_dzen(self): 
        self.wait_element(DzenPageLocators.RESEARCH_BUTTON) 
