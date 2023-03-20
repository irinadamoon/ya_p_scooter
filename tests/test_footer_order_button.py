import time

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


# тест возможности регистрации по кн "Заказать" в футере
class TestRegisterFooterButton:


    @allure.title("Тест возможности регистрации по кн 'Заказать' в футере")
    @allure.description("Заполнение полей ввода, подтверждение заказа, проверка, что заказ подтвержден")
    def test_register_using_footer_order_button(self, driver, data_base):
        main_page = MainPage(driver)
        register_page = RegisterForm(driver, data_base)
        rent_page = RentPage(driver, data_base)


        main_page.go_to_register_page_using_footer_button()
        register_page.fill_in_registration_form(data_base)
        rent_page.rent_window_loaded()
        rent_page.order_black_scooter_using_footer_order_button(data_base)

        assert rent_page.check_order_status()


    @allure.title("Проверка совпадения данных ИМЕНИ в заказе с введенными пользователем")
    @allure.description("Введено корректное имя 'Владимир'")
    def test_check_user_name(self, driver, data_base):
        main_page = MainPage(driver)
        register_page = RegisterForm(driver, data_base)
        rent_page = RentPage(driver, data_base)
        check_status = CheckStatusPage(driver, data_base)

        main_page.go_to_register_page_using_footer_button()
        register_page.fill_in_registration_form(data_base)
        rent_page.rent_window_loaded()
        rent_page.order_black_scooter_using_footer_order_button(data_base)
        rent_page.wait_order_status()
        rent_page.go_to_check_status_page()
        
        assert check_status.check_user_name(data_base)


    @allure.title("Проверка совпадения данных ФАМИЛИИ в заказе с введенными пользователем")
    @allure.description("Введена корректная фамилия 'Ленин'")
    def test_check_user_family_name(self, driver, data_base):
        main_page = MainPage(driver)
        register_page = RegisterForm(driver, data_base)
        rent_page = RentPage(driver, data_base)
        check_status = CheckStatusPage(driver, data_base)

        main_page.go_to_register_page_using_footer_button()
        register_page.fill_in_registration_form(data_base)
        rent_page.rent_window_loaded()
        rent_page.order_black_scooter_using_footer_order_button(data_base)
        rent_page.wait_order_status()
        rent_page.go_to_check_status_page()
        
        assert check_status.check_user_family_name(data_base)


    @allure.title("Проверка совпадения данных АДРЕСА в заказе с введенными пользователем")
    @allure.description("Введен корректный адрес 'РФ, Москва, Мавзолей'")
    def test_check_user_address(self, driver, data_base):
        main_page = MainPage(driver)
        register_page = RegisterForm(driver, data_base)
        rent_page = RentPage(driver, data_base)
        check_status = CheckStatusPage(driver, data_base)

        main_page.go_to_register_page_using_footer_button()
        register_page.fill_in_registration_form(data_base)
        rent_page.rent_window_loaded()
        rent_page.order_black_scooter_using_footer_order_button(data_base)
        rent_page.wait_order_status()
        rent_page.go_to_check_status_page()
        
        assert check_status.check_user_address(data_base)

#   (есть баги)
    @allure.title("Проверка совпадения данных СТАНЦИИ МЕТРО в заказе с введенными пользователем")
    @allure.description("Выбор станции 'Площадь Революции' из выпадающего списка")
    @allure.issue('https://irinadamoon.youtrack.cloud/issue/IK-36/YandeksSamokat.-V-statuse-zakaza-nazvanie-stancii-metro-v-veb-prilozhenii-ne-sootvetstvuet-id-stancii-v-mobilnom-prilozhenii', 'IK-36')
    def test_check_metro_station(self, driver, data_base):
        main_page = MainPage(driver)
        register_page = RegisterForm(driver, data_base)
        rent_page = RentPage(driver, data_base)
        check_status = CheckStatusPage(driver, data_base)

        main_page.go_to_register_page_using_footer_button()
        register_page.fill_in_registration_form(data_base)
        rent_page.rent_window_loaded()
        rent_page.order_black_scooter_using_footer_order_button(data_base)
        rent_page.wait_order_status()
        rent_page.go_to_check_status_page()
        
        assert check_status.check_metro_station(data_base)


    @allure.title("Проверка совпадения данных ТЕЛЕФОНА в заказе с введенными пользователем")
    @allure.description("Номер введен в корректном формате +79995553311")
    def test_check_phone_number(self, driver, data_base):
        main_page = MainPage(driver)
        register_page = RegisterForm(driver, data_base)
        rent_page = RentPage(driver, data_base)
        check_status = CheckStatusPage(driver, data_base)

        main_page.go_to_register_page_using_footer_button()
        register_page.fill_in_registration_form(data_base)
        rent_page.rent_window_loaded()
        rent_page.order_black_scooter_using_footer_order_button(data_base)
        rent_page.wait_order_status()
        rent_page.go_to_check_status_page()
        
        assert check_status.check_phone_number(data_base)

#   (есть баги)
    @allure.title("Проверка совпадения данных ДАТЫ ДОСТАВКИ в заказе с введенными пользователем")
    @allure.description("Выбор даты из следующего месяца, что б протестить возможность переключение календаря")
    @allure.issue('https://irinadamoon.youtrack.cloud/issue/IK-54/YandeksSamokat.-Verstka-ekrana-Status-zakaza.-Pole-data-dostavki-s-datoj-okonchaniya-arendy', 'IK-54')
    def test_check_delivery_date_next_month(self, driver, data_base):
        main_page = MainPage(driver)
        register_page = RegisterForm(driver, data_base)
        rent_page = RentPage(driver, data_base)
        check_status = CheckStatusPage(driver, data_base)

        main_page.go_to_register_page_using_footer_button()
        register_page.fill_in_registration_form(data_base)
        rent_page.rent_window_loaded()
        rent_page.order_black_scooter_using_footer_order_button(data_base)
        rent_page.wait_order_status()
        rent_page.go_to_check_status_page()
        
        assert check_status.check_delivery_date_next_month(data_base)


    @allure.title("Проверка совпадения данных СРОКА АРЕНДЫ в заказе с введенными пользователем")
    @allure.description("Срок аренды выбран 7 суток что б проверить скролл")
    def test_check_duration_7days(self, driver, data_base):
        main_page = MainPage(driver)
        register_page = RegisterForm(driver, data_base)
        rent_page = RentPage(driver, data_base)
        check_status = CheckStatusPage(driver, data_base)

        main_page.go_to_register_page_using_footer_button()
        register_page.fill_in_registration_form(data_base)
        rent_page.rent_window_loaded()
        rent_page.order_black_scooter_using_footer_order_button(data_base)
        rent_page.wait_order_status()
        rent_page.go_to_check_status_page()
        
        assert check_status.check_duration_7days(data_base)


    @allure.title("Проверка совпадения данных ЦВЕТА САМОКАТА в заказе с введенными пользователем")
    @allure.description("Цвет самоката должен быть 'чёрный жемчуг'")
    def test_check_scooter_color(self, driver, data_base):
        main_page = MainPage(driver)
        register_page = RegisterForm(driver, data_base)
        rent_page = RentPage(driver, data_base)
        check_status = CheckStatusPage(driver, data_base)

        main_page.go_to_register_page_using_footer_button()
        register_page.fill_in_registration_form(data_base)
        rent_page.rent_window_loaded()
        rent_page.order_black_scooter_using_footer_order_button(data_base)
        rent_page.wait_order_status()
        rent_page.go_to_check_status_page()
        
        assert check_status.check_black_color(data_base)


    @allure.title("Проверка совпадения данных КОММЕНТАРИЯ в заказе с введенными пользователем")
    @allure.description("Корректный текст 'Стучите громче, сплю крепко'")
    def test_check_comment(self, driver, data_base):
        main_page = MainPage(driver)
        register_page = RegisterForm(driver, data_base)
        rent_page = RentPage(driver, data_base)
        check_status = CheckStatusPage(driver, data_base)

        main_page.go_to_register_page_using_footer_button()
        register_page.fill_in_registration_form(data_base)
        rent_page.rent_window_loaded()
        rent_page.order_black_scooter_using_footer_order_button(data_base)
        rent_page.wait_order_status()
        rent_page.go_to_check_status_page()
       
        assert check_status.check_comment(data_base)
