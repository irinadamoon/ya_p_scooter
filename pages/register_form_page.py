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

class RegisterForm:

    # конструктор класса
    def __init__(self, driver):
        self.driver = driver


    # действия c элементами

    @allure.step("Заполнить поле имени")
    def input_name(self):
        self.driver.find_element(*RegisterFormLocators.INPUT_NAME_REGISTER_FORM).send_keys("Владимир")

    @allure.step("Заполнить поле фамилии")
    def input_family_name(self):
        self.driver.find_element(*RegisterFormLocators.INPUT_FAMILY_NAME_REGISTER_FORM).send_keys("Ленин")

    @allure.step("Заполнить поле адреса")
    def input_address(self):
        self.driver.find_element(*RegisterFormLocators.INPUT_ADDRESS_REGISTER_FORM).send_keys("РФ, Москва, Мавзолей")

    @allure.step("Выбрать станцию метро")
    def input_metro_station(self):
        self.driver.find_element(*RegisterFormLocators.INPUT_METRO_ST_LIST_REGISTER_FORM).send_keys("Площадь Революции")
        self.driver.find_element(*RegisterFormLocators.ITEM_PLOSHYAD_REVOLUCII_IN_METRO_LIST).click()

    @allure.step("Заполнить поле номера телефона")
    def input_phone_number(self):
        self.driver.find_element(*RegisterFormLocators.INPUT_PHONE_NUMBER_REGISTER_FORM).send_keys("+79995553311")

    @allure.step("Нажать кнопку 'Далее'")
    def click_nex_button_register_page(self):
        self.driver.find_element(*RegisterFormLocators.BUTTON_NEX_REGISTER_FORM).click()


    @allure.step("Заполнить форму регистрации")
    def fill_in_registration_form(self):
        self.input_name()
        self.input_family_name()
        self.input_address()
        self.input_metro_station()
        self.input_phone_number()
        self.click_nex_button_register_page()





