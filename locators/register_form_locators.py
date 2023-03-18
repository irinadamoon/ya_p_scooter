from selenium.webdriver.common.by import By

class RegisterFormLocators:

    INPUT_NAME_REGISTER_FORM = [By.XPATH, "//input[@placeholder='* Имя']"]  # поле ввода имени
    INPUT_FAMILY_NAME_REGISTER_FORM = [By.XPATH, "//input[@placeholder='* Фамилия']"]  # поле ввода фамилии
    INPUT_ADDRESS_REGISTER_FORM = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]   # поле ввода адреса
    INPUT_METRO_ST_LIST_REGISTER_FORM = [By.XPATH, "//input[@placeholder='* Станция метро']"]  # поле выбора станции метро
    LIST_OF_METRO_STATIONS_REGISTER_FORM = [By.XPATH, "//div[@class='select-search__select']"]   # список станций
    ITEM_PLOSHYAD_REVOLUCII_IN_METRO_LIST = [By.XPATH, "//*[contains(text(), 'Площадь Революции')]"]   # станция площадь революции в списке
    INPUT_PHONE_NUMBER_REGISTER_FORM = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]  # поле ввода телефона
    BUTTON_NEX_REGISTER_FORM = [By.XPATH, "//button[contains(text(), 'Далее')]"]  # кн "Далее" под формой регистрации