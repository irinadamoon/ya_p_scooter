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

class RentPage:

    # конструктор класса
    def __init__(self, driver):
        self.driver = driver


    # действия c элементами

    @allure.step("Ожидание загрузки окна")
    def rent_window_loaded(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((RentPageLocators.RENT_FORM_ORDER_BUTTON)))

    @allure.step("Выбор даты доставки в текущем месяце")
    def choose_delivery_date_this_month(self):
        self.driver.find_element(*RentPageLocators.INPUT_DELIVERY_DATE_RENT_FORM).click()
        self.driver.find_element(*RentPageLocators.CHOOSE_DELIVERY_DATE_THIS_MONTH_RENT_FORM).click()

    @allure.step("Выбор даты доставки в след месяце")
    def choose_delivery_date_next_month(self):
        self.driver.find_element(*RentPageLocators.INPUT_DELIVERY_DATE_RENT_FORM).click()
        self.driver.find_element(*RentPageLocators.CHANGE_MONTH_BUTTON).click()
        self.driver.find_element(*RentPageLocators.CHOOSE_DELIVERY_DATE_NEXT_MONTH_RENT_FORM).click()

    @allure.step("Выбор срока аренды 'сутки'")
    def choose_rent_period_1day(self):
        self.driver.find_element(*RentPageLocators.CHOOSE_ARROW_DURATION_RENT_FORM).click()
        self.driver.find_element(*RentPageLocators.CHOOSE_DURATION_1DAY_RENT_FORM).click()

    @allure.step("Выбор срока аренды 7 дней")
    def choose_rent_period_7days(self):
        self.driver.find_element(*RentPageLocators.CHOOSE_ARROW_DURATION_RENT_FORM).click()
        elem = self.driver.find_element(*RentPageLocators.CHOOSE_DURATION_7DAYS_RENT_FORM)
        self.driver.execute_script("arguments[0].scrollIntoView();", elem)
        self.driver.find_element(*RentPageLocators.CHOOSE_DURATION_7DAYS_RENT_FORM).click()

    @allure.step("Выбор черного цвета самоката")
    def choose_black_color(self):
        self.driver.find_element(*RentPageLocators.CHECKBOX_BLACK_COLOR_RENT_FORM).click()

    @allure.step("Выбор серого цвета самоката")
    def choose_grey_color(self):
        self.driver.find_element(*RentPageLocators.CHECKBOX_GREY_COLOR_RENT_FORM).click()

    @allure.step("Ввeдeние текста в поле 'комментарий курьеру'")
    def input_comment(self):
        self.driver.find_element(*RentPageLocators.INPUT_COMMENT_RENT_FORM).send_keys('Стучите громче, сплю крепко')

    @allure.step("Клик по кнопке 'Заказать'")
    def click_order_button(self):
        self.driver.find_element(*RentPageLocators.RENT_FORM_ORDER_BUTTON).click()

    @allure.step("Клик на кнопку 'Да' в окне подтверждения")
    def click_yes_button_confirm_window(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((RentPageLocators.POP_UP_CONFIRM_WINDOW)))
        self.driver.find_element(*RentPageLocators.YES_BUTTON_CONFIRM_ORDER_WINDOW).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((RentPageLocators.BUTTON_CHECK_STATUS_POPUP_INFO_WINDOW)))

    @allure.step("Проверка оформлен ли заказ")
    def check_order_status(self):
        window = expected_conditions.visibility_of_element_located((RentPageLocators.POP_UP_INFO_ORDER_CONFIRMED_WINDOW))
        button = expected_conditions.element_to_be_clickable((RentPageLocators.BUTTON_CHECK_STATUS_POPUP_INFO_WINDOW))
        return window and button

    @allure.step("Ожидание загрузки всплывающего окна")
    def wait_order_status(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((RentPageLocators.POP_UP_INFO_ORDER_CONFIRMED_WINDOW)))
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((RentPageLocators.BUTTON_CHECK_STATUS_POPUP_INFO_WINDOW)))

    @allure.step("Оформление заказа на серый самокат с доставкой в этом месяце, сроком аренды 1 день и пустым полем 'комментарий'")
    def order_grey_scooter_using_footer_order_button(self):
        self.choose_delivery_date_this_month()
        self.choose_rent_period_1day()
        self.choose_grey_color()
        self.click_order_button()
        self.click_yes_button_confirm_window()

    @allure.step("Оформление заказа на черный самокат с доставкой в след.месяце, сроком аренды 7 дней и всеми заполненными полями")
    def order_black_scooter_using_footer_order_button(self):
        self.choose_delivery_date_next_month()
        self.choose_rent_period_7days()
        self.choose_black_color()
        self.input_comment()
        self.click_order_button()
        self.click_yes_button_confirm_window()

    @allure.step("Переход на страницу статуса заказа")
    def go_to_check_status_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((RentPageLocators.BUTTON_CHECK_STATUS_POPUP_INFO_WINDOW)))
        self.driver.find_element(*RentPageLocators.BUTTON_CHECK_STATUS_POPUP_INFO_WINDOW).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((CheckStatusLocators.DATA_FIELD)))
        elem = self.driver.find_element(*CheckStatusLocators.BUTTON_CANCEL_ORDER_STATUS_PAGE)
        self.driver.execute_script("arguments[0].scrollIntoView();", elem)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((CheckStatusLocators.BUTTON_CANCEL_ORDER_STATUS_PAGE)))














