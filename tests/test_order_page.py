import allure
import pytest

from locators.main_page_locators import MainPageLocators
from test_data import Url, CustomerData
from pages.order_page import OrderPage


class TestOrderScooter:

    @allure.title('Тест заказа самоката через разные кнопки')
    @pytest.mark.parametrize('button, name, last_name, address,'
                             'station_number, phone_number',
                             [(MainPageLocators.ORDER_TOP,
                               CustomerData.NAMES[0],
                               CustomerData.LAST_NAMES[0],
                               CustomerData.ADDRESSES[0], '1',
                               CustomerData.PHONES[0]),
                              (MainPageLocators.ORDER_BOTTOM,
                               CustomerData.NAMES[1],
                               CustomerData.LAST_NAMES[1],
                               CustomerData.ADDRESSES[1], '2',
                               CustomerData.PHONES[1])])
    def test_order_scooter_top_and_bottom_buttons(self, driver, button, name, last_name,
                                                  address, station_number, phone_number):
        order_page = OrderPage(driver)
        order_page.open_page(Url.MAIN_URL)
        order_page.accept_cookies()

        order_page.click_element(button)

        order_page.fill_customer_info(name, last_name, address,
                                      station_number, phone_number)

        order_page.click_next()

        order_page.fill_delivery_info()

        order_page.confirm_delivery()

        assert order_page.is_order_success()
