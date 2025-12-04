import allure
import pytest
from data import MainPageAnswersForQuestions
from conftest import driver
from pages.main_page import MainPage
from curl import Url

class TestAnswersForQuestionsr:
    @allure.title('Тест: ')
    @pytest.mark.parametrize('number, answer', MainPageAnswersForQuestions.answers)
    def test_important_questions(self, driver, number, answer):
        # Arrange
        main_page = MainPage(driver)

        # Act
        main_page.open_main_page()
        main_page.accept_cookie()
        main_page.find_last_question()
        main_page.click_question(number)

        # Assert
        assert main_page.get_answer(number) == answer