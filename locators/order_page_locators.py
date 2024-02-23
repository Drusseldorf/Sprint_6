from selenium.webdriver.common.by import By


class OrderPageLocators:

    SELECT_METRO_STATION = By.CSS_SELECTOR, 'li.select-search__row[data-index="{}"]'
    NAME_INPUT = By.CSS_SELECTOR, 'input[placeholder="* Имя"]'
    LAST_NAME_INPUT = By.CSS_SELECTOR, 'input[placeholder="* Фамилия"]'
    ADDRESS_INPUT = By.CSS_SELECTOR, 'input[placeholder="* Адрес: куда привезти заказ"]'
    STATION_INPUT = By.CSS_SELECTOR, 'input[placeholder="* Станция метро"]'
    PHONE_INPUT = By.CSS_SELECTOR, 'input[placeholder="* Телефон: на него позвонит курьер"]'
    BUTTON_NEXT = By.XPATH, '//button[text()="Далее"]'

    DELIVERY_TIME = By.CSS_SELECTOR, 'input[placeholder="* Когда привезти самокат"]'
    RENTAL_PERIOD_DAY = By.XPATH, '//div[text()="сутки"]'
    RENTAL_PERIOD_FIELD = By.CLASS_NAME, 'Dropdown-control'

    MAKE_ORDER_BUTTON = By.XPATH, '//div[contains(@class, "Order_Buttons")]//button[text()="Заказать"]'

    CONFIRM_BUTTON = By.XPATH, '//button[text()="Да"]'

    DELIVERY_CONFIRM = By.XPATH, '//div[text()="Заказ оформлен"]'
