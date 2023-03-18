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

class MainPage:

    # конструктор класса
    def __init__(self, driver):
        self.driver = driver

    # действия c элементами

    @allure.step("Вход на главную страницу")
    def go_to_main_page(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru")

    @allure.step("Клик на кнопку согласия с куки")
    def click_cookie_confirm_button(self):
        self.driver.find_element(*MainPageLocators.COOKIE_CONFIRM_BUTTON).click()

    @allure.step("Клик 'Заказать' в шапке")
    def click_header_order_button(self):
        self.driver.find_element(*MainPageLocators.HEADER_ORDER_BUTTON).click()

    @allure.step("Клик 'Заказать' в футере")
    def click_footer_order_button(self):
        self.driver.find_element(*MainPageLocators.FOOTER_ORDER_BUTTON).click()

    @allure.step("Скролл до кн 'Заказать' в футере")
    def scroll_till_footer_order_button(self):
        elem = self.driver.find_element(*MainPageLocators.QUESTION_1)
        self.driver.execute_script("arguments[0].scrollIntoView();", elem)

    @allure.step("Переход на страницу регистрации кнопкой в шапке")
    def go_to_register_page_using_header_button(self):
        self.click_cookie_confirm_button()
        self.click_header_order_button()

    @allure.step("Переход на страницу регистрации кнопкой в футере")
    def go_to_register_page_using_footer_button(self):
        self.click_cookie_confirm_button()
        self.scroll_till_footer_order_button()
        self.click_footer_order_button()

    @allure.step("Клик на лого 'Яндекс'")
    def click_logo_yandex(self):
        self.driver.find_element(*MainPageLocators.LOGO_YANDEX).click()

    @allure.step("Проверка перехода на URL dzen по клику на лого 'Яндекс'")
    def check_yandex_url(self):
        original_window = self.driver.current_window_handle
        self.driver.find_element(*MainPageLocators.LOGO_YANDEX).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.number_of_windows_to_be(2))

        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
        WebDriverWait(self.driver, 10).until((expected_conditions.title_is('Дзен')))
        current_url = self.driver.current_url
        return current_url

    @allure.step("Клик на лого 'Самокат'")
    def click_logo_scooter(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((RegisterFormLocators.BUTTON_NEX_REGISTER_FORM)))
        self.driver.find_element(*MainPageLocators.LOGO_SCOOTER).click()

    @allure.step("Проверка загрузки главной страницы")
    def check_main_page_loaded(self):
        image = expected_conditions.visibility_of_element_located((MainPageLocators.SCOOTER_IMG))
        logo = expected_conditions.element_to_be_clickable((RegisterFormLocators.BUTTON_NEX_REGISTER_FORM))
        return image and logo

    @allure.step("Промотать вниз до последнего вопроса")
    def scroll_down_page(self):
        elem = self.driver.find_element(*MainPageLocators.QUESTION_8)
        self.driver.execute_script("arguments[0].scrollIntoView();", elem)

    @allure.step("Клик на вопрос 1")
    def click_question_1(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((MainPageLocators.QUESTION_1)))
        self.driver.find_element(*MainPageLocators.QUESTION_1).click()

    @allure.step("Клик на вопрос 2")
    def click_question_2(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((MainPageLocators.QUESTION_2)))
        self.driver.find_element(*MainPageLocators.QUESTION_2).click()

    @allure.step("Клик на вопрос 3")
    def click_question_3(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((MainPageLocators.QUESTION_3)))
        self.driver.find_element(*MainPageLocators.QUESTION_3).click()

    @allure.step("Клик на вопрос 4")
    def click_question_4(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((MainPageLocators.QUESTION_4)))
        self.driver.find_element(*MainPageLocators.QUESTION_4).click()

    @allure.step("Клик на вопрос 5")
    def click_question_5(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((MainPageLocators.QUESTION_5)))
        self.driver.find_element(*MainPageLocators.QUESTION_5).click()

    @allure.step("Клик на вопрос 6")
    def click_question_6(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((MainPageLocators.QUESTION_6)))
        self.driver.find_element(*MainPageLocators.QUESTION_6).click()

    @allure.step("Клик на вопрос 7")
    def click_question_7(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((MainPageLocators.QUESTION_7)))
        self.driver.find_element(*MainPageLocators.QUESTION_7).click()

    @allure.step("Клик на вопрос 8")
    def click_question_8(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((MainPageLocators.QUESTION_8)))
        self.driver.find_element(*MainPageLocators.QUESTION_8).click()

    @allure.step("Переход к вопросам внизу страницы")
    def go_to_questions_on_main_page(self):
        self.click_cookie_confirm_button()
        self.scroll_down_page()

    @allure.step("Проверка текста ответа 1")
    def check_answer_1(self):
        elem = self.driver.find_element(*MainPageLocators.ANSWER_1).text
        return elem == MainPageLocators.TEXT_ANSWER_1

    @allure.step("Проверка текста ответа 2")
    def check_answer_2(self):
        elem = self.driver.find_element(*MainPageLocators.ANSWER_2).text
        return elem == MainPageLocators.TEXT_ANSWER_2

    @allure.step("Проверка текста ответа 3")
    def check_answer_3(self):
        elem = self.driver.find_element(*MainPageLocators.ANSWER_3).text
        return elem == MainPageLocators.TEXT_ANSWER_3

    @allure.step("Проверка текста ответа 4")
    def check_answer_4(self):
        elem = self.driver.find_element(*MainPageLocators.ANSWER_4).text
        return elem == MainPageLocators.TEXT_ANSWER_4

    @allure.step("Проверка текста ответа 5")
    def check_answer_5(self):
        elem = self.driver.find_element(*MainPageLocators.ANSWER_5).text
        return elem == MainPageLocators.TEXT_ANSWER_5

    @allure.step("Проверка текста ответа 6")
    def check_answer_6(self):
        elem = self.driver.find_element(*MainPageLocators.ANSWER_6).text
        return elem == MainPageLocators.TEXT_ANSWER_6

    @allure.step("Проверка текста ответа 7")
    def check_answer_7(self):
        elem = self.driver.find_element(*MainPageLocators.ANSWER_7).text
        return elem == MainPageLocators.TEXT_ANSWER_7

    @allure.step("Проверка текста ответа 8")
    def check_answer_8(self):
        elem = self.driver.find_element(*MainPageLocators.ANSWER_8).text
        return elem == MainPageLocators.TEXT_ANSWER_8
