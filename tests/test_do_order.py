import allure
import pytest
from data import Users
from curl import Url
from pages.order_page import OrderPage
from pages.main_page import MainPage

class TestDoOrder:
    @allure.title("Тест успешного заказа самоката с точкой входа кнопка «Заказать» вверху страницы")
    @allure.description("Нужно проверить весь флоу позитивного сценария с двумя наборами данных. Проверить точки входа в сценарий, их две: кнопка «Заказать» вверху страницы и внизу")
    def test_do_order_by_header_button(self, driver):
        # Arrange
        main_page = MainPage(driver)
        main_page.open_main_page()
        order_page = OrderPage(driver)
        # Act
        main_page.accept_cookie()
        main_page.click_on_header_order_button()
        order_page.do_order(Users.user_one)
        modal_screen_text = order_page.check_order_was_do_screen()
        # Assert
        assert modal_screen_text == "Посмотреть статус"
        

    @allure.title("Тест успешного заказа самоката с точкой входа кнопка «Заказать» внизу страницы")
    def test_do_order_by_footer_button(self, driver):
        # Arrange
        main_page = MainPage(driver)
        main_page.open_main_page()
        order_page = OrderPage(driver)
        # Act
        main_page.accept_cookie()
        main_page.click_on_footer_order_button()
        order_page.do_order(Users.user_two)
        modal_screen_text = order_page.check_order_was_do_screen()
        # Assert
        assert modal_screen_text == "Посмотреть статус"

