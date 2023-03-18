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
from pages.main_page import MainPage
from pages.register_form_page import RegisterForm
from pages.rent_page import RentPage
from pages.check_status_page import CheckStatusPage


class TestLogos:

    @allure.title("Проверка перехода на главную страницу сайта по клику на логотип 'Самокат'")
    @allure.description("Переход с гл.страницы в форму заказа по клику кн. 'Заказать' в шапке сайта и обратно по клику на логотип 'Самокат'")
    def test_logo_scooter(self, driver):
        main_page = MainPage(driver)

        main_page.go_to_register_page_using_header_button()
        main_page.click_logo_scooter()

        assert main_page.check_main_page_loaded()


    @allure.title("Проверка перехода на 'Дзен' по клику на логотип 'Яндекс'")
    @allure.description("Переход с гл.страницы на сайт 'Дзен' по клику на логотип 'Яндекс'")
    def test_logo_yandex(self, driver):
        main_page = MainPage(driver)

        assert main_page.check_yandex_url() == MainPageLocators.URL_DZEN



