import allure

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from locators.main_page_locators import Header
from helpers import FormatLocator as fl
from helpers import FutureDate as fd
from test_data import OrderSuccess


class OrderPage(BasePage):

    @allure.step('Заполнение данных о заказчике')
    def fill_customer_info(self, name, last_name, address, station_number, phone_number):
        self.input_text(OrderPageLocators.NAME_INPUT, name)

        self.input_text(OrderPageLocators.LAST_NAME_INPUT, last_name)

        self.input_text(OrderPageLocators.ADDRESS_INPUT, address)

        self.click_element(OrderPageLocators.STATION_INPUT)
        station_locator = fl.format_locator(OrderPageLocators.SELECT_METRO_STATION, station_number)
        self.click_element(station_locator)

        self.input_text(OrderPageLocators.PHONE_INPUT, phone_number)

    @allure.step('Нажатие кнопки Далее')
    def click_next(self):
        self.click_element(OrderPageLocators.BUTTON_NEXT)

    @allure.step('Заполнение данных об аренде')
    def fill_delivery_info(self):
        delivery_time = fd.future_date()
        self.input_text(OrderPageLocators.DELIVERY_TIME, delivery_time)
        self.press_enter(OrderPageLocators.DELIVERY_TIME)

        self.click_element(OrderPageLocators.RENTAL_PERIOD_FIELD)
        self.click_element(OrderPageLocators.RENTAL_PERIOD_DAY)

    @allure.step('Подтверждение заказа')
    def confirm_delivery(self):
        self.click_element(OrderPageLocators.MAKE_ORDER_BUTTON)
        self.click_element(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step('Нажатие логотипа Яндекс и переход в Дзен')
    def click_yandex_logo(self):
        self.click_element(Header.YANDEX_LOGO)
        self.switch_tab()

    @allure.step('Нажатие логотипа Самокат и переход на главную страницу')
    def click_scooter_logo(self):
        self.click_element(Header.SAMOKAT_LOGO)

    def is_order_success(self):
        return OrderSuccess.ORDER_SUCCESS in self.get_element_text(OrderPageLocators.DELIVERY_CONFIRM)

    @allure.step('Подтверждение куки')
    def accept_cookies(self):
        self.click_element(OrderPageLocators.COOKIES)
