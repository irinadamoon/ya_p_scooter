from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import allure

from locators.main_page_locators import MainPageLocators
from locators.register_form_locators import RegisterFormLocators
from locators.rent_page_locators import RentPageLocators
from locators.check_status_locators import CheckStatusLocators



class CheckStatusPage:

    # конструктор класса
    def __init__(self, driver):
        self.driver = driver

    # проверки

    @allure.step("Проверка что введенное юзером ИМЯ соответствует имени в заказе")
    def check_user_name(self):
        name = 'Владимир'
        elem = self.driver.find_element(*CheckStatusLocators.CHECK_NAME).text
        return name == elem

    @allure.step("Проверка что введенная юзером ФАМИЛИЯ соответствует фамилии в заказе")
    def check_user_family_name(self):
        name = 'Ленин'
        elem = self.driver.find_element(*CheckStatusLocators.CHECK_FAMILY_NAME).text
        return name == elem

    @allure.step("Проверка что введенный юзером АДРЕС соответствует адресу в заказе")
    def check_user_address(self):
        name = 'РФ, Москва, Мавзолей'
        elem = self.driver.find_element(*CheckStatusLocators.CHECK_ADDRESS).text
        return name == elem

    @allure.step("Проверка что выбранная юзером СТАНЦИЯ МЕТРО соответствует станции метро в заказе")
    def check_metro_station(self):
        name = 'Площадь Революции'
        elem = self.driver.find_element(*CheckStatusLocators.CHECK_METRO_STATION).text
        return name == elem

    @allure.step("Проверка что введенный юзером ТЕЛЕФОН соответствует телефону в заказе")
    def check_phone_number(self):
        name = '+79995553311'
        elem = self.driver.find_element(*CheckStatusLocators.CHECK_PHONE_NUMBER).text
        return name == elem

    @allure.step("Проверка что выбранная юзером ДАТА ДОСТАВКИ соответствует дате доставки в заказе")
    def check_delivery_date_next_month(self):
        name = '11 апреля'
        elem = self.driver.find_element(*CheckStatusLocators.CHECK_DELIVERY_DATE).text
        return name == elem

    @allure.step("Проверка что выбранный юзером СРОК АРЕНДЫ соответствует сроку аренды в заказе")
    def check_duration_7days(self):
        name = 'семеро суток'
        elem = self.driver.find_element(*CheckStatusLocators.CHECK_DURATION_DAYS).text
        return name == elem

    @allure.step("Проверка что выбранный юзером ЦВЕТ соответствует цвету в заказе")
    def check_black_color(self):
        name = 'чёрный жемчуг'
        elem = self.driver.find_element(*CheckStatusLocators.CHECK_COLOR).text
        return name == elem

    @allure.step("Проверка что введенный юзером КОММЕНТАРИЙ соответствует комментарию в заказе")
    def check_comment(self):
        name = 'Стучите громче, сплю крепко'
        elem = self.driver.find_element(*CheckStatusLocators.CHECK_COMMENT).text
        return name == elem

    @allure.step("Проверка что выбранная юзером ДАТА ДОСТАВКИ соответствует дате доставки в заказе")
    def check_delivery_date_this_month(self):
        name = '28 марта'
        elem = self.driver.find_element(*CheckStatusLocators.CHECK_DELIVERY_DATE).text
        return name == elem

    @allure.step("Проверка что выбранный юзером СРОК АРЕНДЫ соответствует сроку аренды в заказе")
    def check_duration_1day(self):
        name = 'сутки'
        elem = self.driver.find_element(*CheckStatusLocators.CHECK_DURATION_DAYS).text
        return name == elem

    @allure.step("Проверка что выбранный юзером ЦВЕТ соответствует цвету в заказе")
    def check_grey_color(self):
        name = 'серая безысходность'
        elem = self.driver.find_element(*CheckStatusLocators.CHECK_COLOR).text
        return name == elem

    @allure.step("Проверка что поле КОММЕНТАРИЯ, оставленный незаполненным юзером, отсутствует в заказе")
    def check_empty_comment(self):
        try:
            self.driver.find_element(*CheckStatusLocators.CHECK_COMMENT)
        except NoSuchElementException:
            return True
        return False

