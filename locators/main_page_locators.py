from selenium.webdriver.common.by import By


class MainPageLocators:
    HEADER_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']") # Кнопка "заказать" в хедере
    FOOTER_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Home_FinishButton__1_cWm')]/button[text()='Заказать']") # Кнопка "заказать" внизу страницы
   
    QUESTION = (By.XPATH, '//div[@id="accordion__heading-{}"]') # Локатор строки вопроса
    LAST_QUESTION = (By.XPATH, '(//div[contains(@id, "accordion__heading-")])[last()]') # Локатор для последней строки вопроса
    ANSWER = (By.XPATH, '//div[@id="accordion__panel-{}"]/p') # Локатор спрятанной строки ответа
    COOKIE = (By.ID, "rcc-confirm-button") # Всплывающее сообщение "Куки": да все привыкли
   
    LOGO_SCOOTER = (By.XPATH, '//a[@href="/"]') # "Самокат" логотип    
    LOGO_YANDEX = (By.XPATH, '//a[@href="//yandex.ru"]') # "Яндекс" логотип
    