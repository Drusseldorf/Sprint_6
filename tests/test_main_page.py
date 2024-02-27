import allure
import pytest

from test_data import AnswersFAQ, Url
from pages.main_page import MainPage


class TestFaqDropDown:

    @allure.title('Проверка наличия ожидаемого текста в ответе FAQ')
    @pytest.mark.parametrize('question_number, expected_answer', [('0', AnswersFAQ.ANSWER_0),
                                                                  ('1', AnswersFAQ.ANSWER_1),
                                                                  ('2', AnswersFAQ.ANSWER_2),
                                                                  ('3', AnswersFAQ.ANSWER_3),
                                                                  ('4', AnswersFAQ.ANSWER_4),
                                                                  ('5', AnswersFAQ.ANSWER_5),
                                                                  ('6', AnswersFAQ.ANSWER_6),
                                                                  ('7', AnswersFAQ.ANSWER_7)])
    def test_faq_answers_match(self, driver, question_number, expected_answer):

        main_page = MainPage(driver)

        main_page.open_page(Url.MAIN_URL)
        main_page.accept_cookies()

        answer = main_page.click_on_question_get_answer(question_number)

        assert answer == expected_answer
