from selenium.webdriver.common.by import By

class MainPageLocators:

    COOKIE_CONFIRM_BUTTON = [By.XPATH, "//button[@id='rcc-confirm-button']"]  # кн "да все привыкли"
    SCOOTER_IMG = [By.XPATH, "//img[@src='/assets/scooter.png']"]   # картинка самоката
    HEADER_ORDER_BUTTON = [By.XPATH, "//button[@class='Button_Button__ra12g']"]  # общ # кн "Заказать" в шапке
    FOOTER_ORDER_BUTTON = [By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM')]"]  # общ # кн "Заказать" в футере
    LOGO_SCOOTER = [By.XPATH, "//*[@alt='Scooter']"]   # лого самокат
    LOGO_YANDEX = [By.XPATH, "//*[@alt='Yandex']"]   # лого яндекс
    INPUT_DZEN = [By.XPATH, "//input[@aria-label='Запрос']"]   # поиск строка яндекса
    # локаторы вопросов о важном
    QUESTION_1 = [By.XPATH, "//*[@id='accordion__heading-0']"]   # 1-вопрос
    ANSWER_1 = [By.XPATH, "//*[@id='accordion__panel-0']"]   # 1-ответ
    QUESTION_2 = [By.XPATH, "//*[@id='accordion__heading-1']"]   # 2-вопрос
    ANSWER_2 = [By.XPATH, "//*[@id='accordion__panel-1']"]   # 2-ответ
    QUESTION_3 = [By.XPATH, "//*[@id='accordion__heading-2']"]   # 3-вопрос
    ANSWER_3 = [By.XPATH, "//*[@id='accordion__panel-2']"]   # 3-ответ
    QUESTION_4 = [By.XPATH, "//*[@id='accordion__heading-3']"]   # 4-вопрос
    ANSWER_4 = [By.XPATH, "//*[@id='accordion__panel-3']"]   # 4-ответ
    QUESTION_5 = [By.XPATH, "//*[@id='accordion__heading-4']"]   # 5-вопрос
    ANSWER_5 = [By.XPATH, "//*[@id='accordion__panel-4']"]   # 5-ответ
    QUESTION_6 = [By.XPATH, "//*[@id='accordion__heading-5']"]   # 6-вопрос
    ANSWER_6 = [By.XPATH, "//*[@id='accordion__panel-5']"]   # 6-ответ
    QUESTION_7 = [By.XPATH, "//*[@id='accordion__heading-6']"]   # 7-вопрос
    ANSWER_7 = [By.XPATH, "//*[@id='accordion__panel-6']"]   # 7-ответ
    QUESTION_8 = [By.XPATH, "//*[@id='accordion__heading-7']"]  # 8-вопрос
    ANSWER_8 = [By.XPATH, "//*[@id='accordion__panel-7']"]   # 8-ответ

    # переменные
    TEXT_ANSWER_1 = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    TEXT_ANSWER_2 = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
    TEXT_ANSWER_3 = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
    TEXT_ANSWER_4 = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    TEXT_ANSWER_5 = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
    TEXT_ANSWER_6 = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
    TEXT_ANSWER_7 = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
    TEXT_ANSWER_8 = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
    URL_DZEN = 'https://dzen.ru/?yredirect=true'

