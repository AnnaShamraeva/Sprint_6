import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from conftest import driver
from curl import Url
from conftest import driver
 
# страница заказа https://qa-scooter.praktikum-services.ru/order   

class OrderPage(BasePage):
    @allure.step('Заполнить поле "Имя"')
    def set_name(self, name):
        self.send_keys(OrderPageLocators.NAME_FIELD, name)

    @allure.step('Заполнить поле "Фамилия"')
    def set_last_name(self, last_name):
        self.send_keys(OrderPageLocators.LAST_NAME_FIELD, last_name)

    @allure.step('Заполнить поле "Адрес куда привезти заказ"')
    def set_address(self, address):        
        self.send_keys(OrderPageLocators.ADDRES_FIELD, address)
  
    @allure.step('Заполнить поле "Выбрать станцию метро"')
    def set_metro(self, station_metro):        
        self.click_on_element(OrderPageLocators.METRO_FIELD)
        self.click_on_element(station_metro)
 
    @allure.step('Заполнить поле "Телефон: на него позвонит курьер"')
    def set_phone(self, phone):        
        self.send_keys(OrderPageLocators.PHONE_FIELD, phone)

    @allure.step('Нажать кнопку "Далее"')
    def click_further_button(self):
        self.click_on_element(OrderPageLocators.FURTHER_BUTTON)

    @allure.step('Заполнить поле "Выбрать дату доставки"')
    def set_data(self, data):
        self.click_on_element(OrderPageLocators.DATA_FIELD)
        self.click_on_element(data)

    @allure.step('Заполнить поле "Выбрать срок аренды"')
    def set_period(self, period):
        self.click_on_element(OrderPageLocators.PERIOD_FIELD)
        self.click_on_element(period)

    @allure.step('Заполнить поле "Выбрать цвет"')
    def set_color(self, color):
        self.click_on_element(color)

    @allure.step('Заполнить поле "Комментарий для курьера"')
    def set_comment(self, comment):        
        self.send_keys(OrderPageLocators.COMMENT_FIELD, comment)

    @allure.step('Нажать кнопку "Заказать"')
    def click_order_button(self):
        self.click_on_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step('Нажать кнопку "Да"')
    def click_yes_button(self):
        self.click_on_element(OrderPageLocators.YES_BUTTON)

    @allure.step('Оформить заказ')
    def do_order(self, user):
        self.set_name(user['name'])
        self.set_last_name(user['last_name'])
        self.set_address(user['address'])
        self.set_metro(OrderPageLocators.STATION_FIELD)
        self.set_phone(user['phone'])
        self.click_further_button()
        self.set_data(OrderPageLocators.DATA)
        self.set_phone(OrderPageLocators.PERIOD)
        self.set_color(OrderPageLocators.COLOR)
        self.set_comment(user['comment'])
        self.click_order_button()
        self.click_yes_button()
           
    @allure.step('Проверить появление окна "Заказ оформлен"')
    def check_order_was_do_screen(self): 
        self.get_text(OrderPageLocators.MODAL_SCREEN_SUCCESS)