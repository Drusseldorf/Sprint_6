from selenium.webdriver.common.by import By


class MainPageLocators:

    QUESTIONS = By.ID, 'accordion__heading-{}'
    ANSWERS = By.ID, 'accordion__panel-{}'
    COOKIES = By.ID, 'rcc-confirm-button'
    ORDER_TOP = By.XPATH, '//div[contains(@class, "Header_Nav")]/button[text()="Заказать"]'
    ORDER_BOTTOM = By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button[text()="Заказать"]'


class Header:

    SAMOKAT_LOGO = By.CSS_SELECTOR, '[href="/"]'
    YANDEX_LOGO = By.CSS_SELECTOR, '[href="//yandex.ru"]'
