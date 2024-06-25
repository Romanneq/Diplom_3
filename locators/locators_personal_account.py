from selenium.webdriver.common.by import By


class PersonalAccountElements:
    form_pers_acc = [By.XPATH, ".//ul[contains(@class, 'Profile_profileList__')]"]  # локатор формы отображения данных в персональном аккаунте
    hist_ord_form = [By.XPATH, ".//div[contains(@class, 'Account_contentBox__')]"]  # локатор формы отображения истории заказов в персональном кабинете
    first_order = [By.XPATH, ".//ul[contains(@class, 'OrderHistory_profileList__374GU OrderHistory_list')]/li[1]/a"]  # локатор первого заказа в истории заказов
    id_ord_in_hist_ord = [By.XPATH, ".//p[contains(@class, 'default mb-10 mt-5')]"]  # локатор id заказа в истории заказов


class PersonalAccountButtons:
    history_order = [By.XPATH, ".//a[text()='История заказов']"]  # локатор кнопки "История заказов"
    log_out = [By.XPATH, ".//button[text()='Выход']"]  # локатор кнопки "Выход" в персональном аккаунте

