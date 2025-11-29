import allure
import pytest

from curl import Url
from pages.main_page import MainPage

class TestClickOnLogo:
    @allure.title("Тест: при нажатии на логотип Яндекс был совершен переход на Дзен страницу")
    def test_click_on_yandex_logo(self, driver):
        # Arrange
        main_page = MainPage(driver)
        main_page.open_main_page()
        # Act
        main_page.click_on_yandex_logo()
        main_page.tab_switch(driver) 
        main_page.check_redirection_on_dzen_main_page()
        # Assert
        assert main_page.get_current_url() == Url.dzen_main_page

    @allure.title("Тест: при нажатии на логотип Самокат был совершен переход на главную страницу")
    def test_click_on_scooter_logo(self, driver):
        # Arrange
        main_page = MainPage(driver) 
        main_page.open_main_page()
        # Act
        main_page.click_on_header_order_button()
        main_page.click_on_scooter_logo()
        main_page.check_redirection_on_main_page()
        # Assert
        assert main_page.get_current_url() == Url.main_page