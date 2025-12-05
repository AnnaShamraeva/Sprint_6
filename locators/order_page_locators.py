from selenium.webdriver.common.by import By


class OrderPageLocators:
    # На странице https://qa-scooter.praktikum-services.ru/order
    # Форма "Для кого самокат"
    NAME_FIELD = (By.XPATH, '//input[@placeholder="* Имя"]') # Поле для ввода имени
    LAST_NAME_FIELD = (By.XPATH, '//input[@placeholder="* Фамилия"]') # Поле для ввода фамилии
    ADDRES_FIELD = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]') # Поле для ввода адреса
    METRO_FIELD = (By.XPATH, '//input[@placeholder="* Станция метро"]') # Поле для ввода станции метро
    STATION_FIELD = (By.XPATH, '//div[text()="Молодёжная"]') # Поле для ввода станции метро содержит в себе выпадающий список "Dropdown-placeholder" 
    PHONE_FIELD = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]') # Поле для ввода телефона
    FURTHER_BUTTON = (By.XPATH, '//button[text()="Далее"]') # Кнопка "Далее"
    # Форма "Про аренду"
    DATA_FIELD = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]') # Поле для ввода даты содержит в себе выпадающий список "Dropdown-placeholder"
    DATA = (By.XPATH, '//div[@class="react-datepicker__day react-datepicker__day--027 react-datepicker__day--weekend"]') # ВЫбираем суббота, 27-е декабря 2025 г.
    PERIOD_FIELD = (By.XPATH, '//div[text()="* Срок аренды"]') # Поле для ввода срока аренды

    PERIOD = (By.XPATH, '//div[text()="сутки"]') # Выбираем срок аренды "сутки"  
    COLOR = (By.XPATH, '//label[@for="black"]')  # Выбираем цвет "чёрный жемчуг"
    COMMENT_FIELD = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')  # Поле для ввода "Комментарий для курьера"
    ORDER_BUTTON = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Заказать"]') # Кнопка "Заказать"
    
    YES_BUTTON = (By.XPATH, "//button[text() ='Да']") # В появившейся форме выбираем кнопку "Да"
    
    BUTTON_MODAL_SCREEN_SUCCESS = (By.XPATH, '//button[text()="Посмотреть статус"]') # Всплывающее окно "Заказ оформлен"
   