import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from helpers import FormatLocator as fl


class MainPage(BasePage):

    @allure.step('Клик на вопрос FAQ и получение текста ответа')
    def click_on_question_get_answer(self, locator_number):

        question_locator = fl.format_locator(MainPageLocators.QUESTIONS, locator_number)
        answer_locator = fl.format_locator(MainPageLocators.ANSWERS, locator_number)

        self.click_element(question_locator)

        return self.get_element_text(answer_locator)
