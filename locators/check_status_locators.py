from selenium.webdriver.common.by import By

class CheckStatusLocators:

    BUTTON_CANCEL_ORDER_STATUS_PAGE = [By.XPATH, "//button[contains(@class, 'Button_Inverted__3IF-i')]"]  # кн "Отменить заказ" на странице статусов заказа
    DATA_FIELD = [By.XPATH, "//div[@class='Track_OrderInfo__2fpDL']"]   # поле с данными
    CHECK_NAME = [By.XPATH, "//div[@class='Track_OrderInfo__2fpDL']/div[1]/div[2]"]   # имя
    CHECK_FAMILY_NAME = [By.XPATH, "//div[@class='Track_OrderInfo__2fpDL']/div[2]/div[2]"]   # фамилия
    CHECK_ADDRESS = [By.XPATH, "//div[@class='Track_OrderInfo__2fpDL']/div[3]/div[2]"]   # адрес
    CHECK_METRO_STATION = [By.XPATH, "//div[@class='Track_OrderInfo__2fpDL']/div[4]/div[2]"]   # станция метро
    CHECK_PHONE_NUMBER = [By.XPATH, "//div[@class='Track_OrderInfo__2fpDL']/div[5]/div[2]"]   # телефон
    CHECK_DELIVERY_DATE = [By.XPATH, "//div[@class='Track_OrderInfo__2fpDL']/div[7]/div[2]"]   # дата доставки
    CHECK_DURATION_DAYS = [By.XPATH, "//div[@class='Track_OrderInfo__2fpDL']/div[8]/div[2]"]   # срок аренды
    CHECK_COLOR = [By.XPATH, "//div[@class='Track_OrderInfo__2fpDL']/div[10]/div[2]"]   # цвет
    CHECK_COMMENT = [By.XPATH, "//div[@class='Track_OrderInfo__2fpDL']/div[11]/div[2]"]   # комментарий

    DATE = '11 апреля'
