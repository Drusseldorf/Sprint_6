import allure

from pages.order_page import OrderPage
from test_data import Url


class TestLogoRedirect:

    @allure.title('Проверка перехода по клику на лого Яндекс')
    def test_yandex_logo_redirect(self, driver):

        order_page = OrderPage(driver)

        order_page.open_page(Url.ORDER_PAGE_URL)

        order_page.click_yandex_logo()

        assert order_page.is_page_opened(Url.DZEN_URL)

    @allure.title('Проверка перехода по клику на лого Самоката')
    def test_scooter_logo_redirect(self, driver):

        order_page = OrderPage(driver)

        order_page.open_page(Url.ORDER_PAGE_URL)

        order_page.click_scooter_logo()

        assert order_page.is_page_opened(Url.MAIN_URL)
