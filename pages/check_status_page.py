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
from pages.register_form_page import RegisterForm



class CheckStatusPage:

    # конструктор класса
    def __init__(self, driver, data_base):
        self.driver = driver
        self.data_base = data_base

    # проверки

    @allure.step("Проверка что введенное юзером ИМЯ соответствует имени в заказе")
    def check_user_name(self, data_base):
        wait_res = self.data_base.get('name')
        act_res = self.driver.find_element(*CheckStatusLocators.CHECK_NAME).text
        return wait_res == act_res

    @allure.step("Проверка что введенная юзером ФАМИЛИЯ соответствует фамилии в заказе")
    def check_user_family_name(self, data_base):
        wait_res = self.data_base.get('family_name')
        act_res = self.driver.find_element(*CheckStatusLocators.CHECK_FAMILY_NAME).text
        return wait_res == act_res

    @allure.step("Проверка что введенный юзером АДРЕС соответствует адресу в заказе")
    def check_user_address(self, data_base):
        wait_res = self.data_base.get('address')
        act_res = self.driver.find_element(*CheckStatusLocators.CHECK_ADDRESS).text
        return wait_res == act_res

    @allure.step("Проверка что выбранная юзером СТАНЦИЯ МЕТРО соответствует станции метро в заказе")
    def check_metro_station(self, data_base):
        wait_res = self.data_base.get('metro_station')
        act_res = self.driver.find_element(*CheckStatusLocators.CHECK_METRO_STATION).text
        return wait_res == act_res

    @allure.step("Проверка что введенный юзером ТЕЛЕФОН соответствует телефону в заказе")
    def check_phone_number(self, data_base):
        wait_res = self.data_base.get('phone_number')
        act_res = self.driver.find_element(*CheckStatusLocators.CHECK_PHONE_NUMBER).text
        return wait_res == act_res

    @allure.step("Проверка что выбранная юзером ДАТА ДОСТАВКИ соответствует дате доставки в заказе")
    def check_delivery_date_next_month(self, data_base):
        wait_res = self.data_base.get('delivery_date_apr')
        act_res = self.driver.find_element(*CheckStatusLocators.CHECK_DELIVERY_DATE).text
        return wait_res == act_res

    @allure.step("Проверка что выбранный юзером СРОК АРЕНДЫ соответствует сроку аренды в заказе")
    def check_duration_7days(self, data_base):
        wait_res = self.data_base.get('duration_date_7')
        act_res = self.driver.find_element(*CheckStatusLocators.CHECK_DURATION_DAYS).text
        return wait_res == act_res

    @allure.step("Проверка что выбранный юзером ЦВЕТ соответствует цвету в заказе")
    def check_black_color(self, data_base):
        wait_res = self.data_base.get('color_black')
        act_res = self.driver.find_element(*CheckStatusLocators.CHECK_COLOR).text
        return wait_res == act_res

    @allure.step("Проверка что введенный юзером КОММЕНТАРИЙ соответствует комментарию в заказе")
    def check_comment(self, data_base):
        wait_res = self.data_base.get('comment')
        act_res = self.driver.find_element(*CheckStatusLocators.CHECK_COMMENT).text
        return wait_res == act_res

    @allure.step("Проверка что выбранная юзером ДАТА ДОСТАВКИ соответствует дате доставки в заказе")
    def check_delivery_date_this_month(self, data_base):
        wait_res = self.data_base.get('delivery_date_mar')
        act_res = self.driver.find_element(*CheckStatusLocators.CHECK_DELIVERY_DATE).text
        return wait_res == act_res

    @allure.step("Проверка что выбранный юзером СРОК АРЕНДЫ соответствует сроку аренды в заказе")
    def check_duration_1day(self, data_base):
        wait_res = self.data_base.get('duration_date_1')
        act_res = self.driver.find_element(*CheckStatusLocators.CHECK_DURATION_DAYS).text
        return wait_res == act_res

    @allure.step("Проверка что выбранный юзером ЦВЕТ соответствует цвету в заказе")
    def check_grey_color(self, data_base):
        wait_res = self.data_base.get('color_grey')
        act_res = self.driver.find_element(*CheckStatusLocators.CHECK_COLOR).text
        return wait_res == act_res

    @allure.step("Проверка что поле КОММЕНТАРИЯ, оставленный незаполненным юзером, отсутствует в заказе")
    def check_empty_comment(self, data_base):
        try:
            self.driver.find_element(*CheckStatusLocators.CHECK_COMMENT)
        except NoSuchElementException:
            return True
        return False

