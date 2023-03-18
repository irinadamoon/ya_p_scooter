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


class TestRegisterHeaderButton:


    @allure.title("Тест возможности регистрации по кн 'Заказать' в хедере")
    @allure.description("Заполнение полей ввода, подтверждение заказа, проверка, что заказ подтвержден")
    def test_register_using_header_order_button(self, driver):
        main_page = MainPage(driver)
        register_page = RegisterForm(driver)
        rent_page = RentPage(driver)

        main_page.go_to_register_page_using_footer_button()
        register_page.fill_in_registration_form()
        rent_page.rent_window_loaded()
        rent_page.order_grey_scooter_using_footer_order_button()

        assert rent_page.check_order_status()


    @allure.title("Проверка совпадения данных ИМЕНИ в заказе с введенными пользователем")
    @allure.description("Введено корректное имя 'Владимир'")
    def test_check_user_name(self, driver):
        main_page = MainPage(driver)
        register_page = RegisterForm(driver)
        rent_page = RentPage(driver)
        check_status = CheckStatusPage(driver)

        main_page.go_to_register_page_using_footer_button()
        register_page.fill_in_registration_form()
        rent_page.rent_window_loaded()
        rent_page.order_grey_scooter_using_footer_order_button()
        rent_page.wait_order_status()
        rent_page.go_to_check_status_page()

        assert check_status.check_user_name()


    @allure.title("Проверка совпадения данных ФАМИЛИИ в заказе с введенными пользователем")
    @allure.description("Введена корректная фамилия 'Ленин'")
    def test_check_user_family_name(self, driver):
        main_page = MainPage(driver)
        register_page = RegisterForm(driver)
        rent_page = RentPage(driver)
        check_status = CheckStatusPage(driver)

        main_page.go_to_register_page_using_footer_button()
        register_page.fill_in_registration_form()
        rent_page.rent_window_loaded()
        rent_page.order_grey_scooter_using_footer_order_button()
        rent_page.wait_order_status()
        rent_page.go_to_check_status_page()

        assert check_status.check_user_family_name()


    @allure.title("Проверка совпадения данных АДРЕСА в заказе с введенными пользователем")
    @allure.description("Введен корректный адрес 'РФ, Москва, Мавзолей'")
    def test_check_user_address(self, driver):
        main_page = MainPage(driver)
        register_page = RegisterForm(driver)
        rent_page = RentPage(driver)
        check_status = CheckStatusPage(driver)

        main_page.go_to_register_page_using_footer_button()
        register_page.fill_in_registration_form()
        rent_page.rent_window_loaded()
        rent_page.order_grey_scooter_using_footer_order_button()
        rent_page.wait_order_status()
        rent_page.go_to_check_status_page()

        assert check_status.check_user_address()

#   (есть баги)
    @allure.title("Проверка совпадения данных СТАНЦИИ МЕТРО в заказе с введенными пользователем")
    @allure.description("Выбор станции 'Площадь Революции' из выпадающего списка")
    def test_check_metro_station(self, driver):
        main_page = MainPage(driver)
        register_page = RegisterForm(driver)
        rent_page = RentPage(driver)
        check_status = CheckStatusPage(driver)

        main_page.go_to_register_page_using_footer_button()
        register_page.fill_in_registration_form()
        rent_page.rent_window_loaded()
        rent_page.order_grey_scooter_using_footer_order_button()
        rent_page.wait_order_status()
        rent_page.go_to_check_status_page()

        assert check_status.check_metro_station()


    @allure.title("Проверка совпадения данных ТЕЛЕФОНА в заказе с введенными пользователем")
    @allure.description("Номер введен в корректном формате +79995553311")
    def test_check_phone_number(self, driver):
        main_page = MainPage(driver)
        register_page = RegisterForm(driver)
        rent_page = RentPage(driver)
        check_status = CheckStatusPage(driver)

        main_page.go_to_register_page_using_footer_button()
        register_page.fill_in_registration_form()
        rent_page.rent_window_loaded()
        rent_page.order_grey_scooter_using_footer_order_button()
        rent_page.wait_order_status()
        rent_page.go_to_check_status_page()

        assert check_status.check_phone_number()

#   (есть баги)
    @allure.title("Проверка совпадения данных ДАТЫ ДОСТАВКИ в заказе с введенными пользователем")
    @allure.description("Выбор даты из текущего месяца, что б протестить возможность выбора даты, а не переключение календаря")
    def test_check_delivery_date_this_month(self, driver):
        main_page = MainPage(driver)
        register_page = RegisterForm(driver)
        rent_page = RentPage(driver)
        check_status = CheckStatusPage(driver)

        main_page.go_to_register_page_using_footer_button()
        register_page.fill_in_registration_form()
        rent_page.rent_window_loaded()
        rent_page.order_grey_scooter_using_footer_order_button()
        rent_page.wait_order_status()
        rent_page.go_to_check_status_page()

        assert check_status.check_delivery_date_this_month()


    @allure.title("Проверка совпадения данных СРОКА АРЕНДЫ в заказе с введенными пользователем")
    @allure.description("Срок аренды выбран 1 сутки что б не скроллить")
    def test_check_duration_1day(self, driver):
        main_page = MainPage(driver)
        register_page = RegisterForm(driver)
        rent_page = RentPage(driver)
        check_status = CheckStatusPage(driver)

        main_page.go_to_register_page_using_footer_button()
        register_page.fill_in_registration_form()
        rent_page.rent_window_loaded()
        rent_page.order_grey_scooter_using_footer_order_button()
        rent_page.wait_order_status()
        rent_page.go_to_check_status_page()

        assert check_status.check_duration_1day()


    @allure.title("Проверка совпадения данных ЦВЕТА САМОКАТА в заказе с введенными пользователем")
    @allure.description("Цвет самоката должен быть 'серая безысходность'")
    def test_check_scooter_color(self, driver):
        main_page = MainPage(driver)
        register_page = RegisterForm(driver)
        rent_page = RentPage(driver)
        check_status = CheckStatusPage(driver)

        main_page.go_to_register_page_using_footer_button()
        register_page.fill_in_registration_form()
        rent_page.rent_window_loaded()
        rent_page.order_grey_scooter_using_footer_order_button()
        rent_page.wait_order_status()
        rent_page.go_to_check_status_page()

        assert check_status.check_grey_color()


    @allure.title("Проверка совпадения данных КОММЕНТАРИЯ в заказе с введенными пользователем")
    @allure.description("Юзер оставил поле пустым, тест PASSED, если в данных заказа поле комментария отсутствует")
    def test_check_comment(self, driver):
        main_page = MainPage(driver)
        register_page = RegisterForm(driver)
        rent_page = RentPage(driver)
        check_status = CheckStatusPage(driver)

        main_page.go_to_register_page_using_footer_button()
        register_page.fill_in_registration_form()
        rent_page.rent_window_loaded()
        rent_page.order_grey_scooter_using_footer_order_button()
        rent_page.wait_order_status()
        rent_page.go_to_check_status_page()

        assert check_status.check_empty_comment()
