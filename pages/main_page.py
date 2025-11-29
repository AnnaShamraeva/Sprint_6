import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from curl import Url
from selenium.webdriver.support.ui import WebDriverWait
from conftest import driver

# Страница https://qa-scooter.praktikum-services.ru/


class MainPage(BasePage):

    @allure.step("Открыть главную страницу учебного тренажера Яндекс Самокат")
    def open_main_page(self):
        self.open_page(Url.main_page)    

    @allure.step("Принять куки")
    def accept_cookie(self):
        self.wait_element(MainPageLocators.COOKIE)
        self.click_on_element(MainPageLocators.COOKIE)

    @allure.step('Нажать кнопку "заказать" вверху страницы')
    def click_on_header_order_button(self):
        self.click_on_element(MainPageLocators.HEADER_ORDER_BUTTON)

    @allure.step('Нажать кнопку "заказать" внизу страницы')
    def click_on_footer_order_button(self):
        self.click_on_element(MainPageLocators.FOOTER_ORDER_BUTTON)

    @allure.step("Нажать на строку с вопросом в Вопросах о важном")
    def click_question(self, number):
        method, locator = MainPageLocators.QUESTION
        locator = locator.format(number) 
        return self.click_on_element((method, locator))

    
    @allure.step("Появление ответа на вопрос в Вопросах о важном")
    def get_answer(self, number):
        #WebDriverWait(self.driver, 10)
        method, locator = MainPageLocators.ANSWER
        locator = locator.format(number) 
        #WebDriverWait(self.driver, 10)
        return self.get_text((method, locator))

    @allure.step("Найти последний вопрос в Вопросах о важном")
    def find_last_question(self):
        self.find_element(MainPageLocators.LAST_QUESTION)
        
    @allure.step("Нажать на логотип Яндекс")
    def click_on_yandex_logo(self):
        self.click_on_element(MainPageLocators.LOGO_YANDEX)

    @allure.step("Проверить, что при нажатии на логотип Яндекс был совершен переход на Дзен страницу")
    def check_redirection_on_dzen_main_page(self):
        self.cross_url(Url.dzen_main_page)

    @allure.step("Нажать на логотип Самокат")
    def click_on_scooter_logo(self):
        self.click_on_element(MainPageLocators.LOGO_SCOOTER)

    @allure.step("Проверить, что при нажатии на логотип Самокат был совершен переход на главную страницу")
    def check_redirection_on_main_page(self):
        self.cross_url(Url.main_page)



    
