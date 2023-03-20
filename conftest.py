import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    driver.get('https://qa-scooter.praktikum-services.ru')
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def data_base():
    data = {
        'name': 'Владимир',
        'family_name': 'Ленин',
        'address': 'РФ, Москва, Мавзолей',
        'metro_station': 'Площадь Революции',
        'phone_number': '+79995553311',
        'delivery_date_apr': '11 апреля',
        'delivery_date_mar': '28 марта',
        'duration_date_7': 'семеро суток',
        'duration_date_1': 'сутки',
        'color_black': 'чёрный жемчуг',
        'color_grey': 'серая безысходность',
        'comment': 'Стучите громче, сплю крепко'
    }

    return data