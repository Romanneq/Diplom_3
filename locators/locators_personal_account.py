from selenium.webdriver.common.by import By


class PersonalAccountElements:
    FORM_PERS_ACC = [By.XPATH, ".//ul[contains(@class, 'Profile_profileList__')]"]  # локатор формы отображения данных в персональном аккаунте
    HIST_ORD_FORM = [By.XPATH, ".//div[contains(@class, 'Account_contentBox__')]"]  # локатор формы отображения истории заказов в персональном кабинете
    FIRST_ORDER = [By.XPATH, ".//ul[contains(@class, 'OrderHistory_profileList__')]/li[1]/a"]  # локатор первого заказа в истории заказов
    ID_ORD_IN_HIST_ORD = [By.XPATH, ".//div[contains(@class, 'Modal_orderBox__')]/p[contains(@class, 'text text_type_digits-default')]"]  # локатор id заказа в истории заказов


class PersonalAccountButtons:
    HISTORY_ORDER = [By.XPATH, ".//a[text()='История заказов']"]  # локатор кнопки "История заказов"
    LOG_OUT = [By.XPATH, ".//button[text()='Выход']"]  # локатор кнопки "Выход" в персональном аккаунте
