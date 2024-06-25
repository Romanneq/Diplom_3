from selenium.webdriver.common.by import By


class PasswordRecoveryElements:
    form_rec_email = [By.XPATH, ".//div[contains(@class, 'Auth_login__')]"]  # локатор формы "Восстановления пароля" с полем email
    field_email_rec = [By.XPATH, ".//input[contains(@class, 'text input__textfield')]"]  # локатор поля ввода email в форме восстановления пароля
    form_rec_pas = [By.XPATH, ".//div[contains(@class, 'Auth_login_')]"]  # локатор формы восстановления пароля c полем пароль и кодом


class PasswordRecoveryButton:
    button_recovery = [By.XPATH, ".//button[contains(@class, 'button_button__')]"]  # локатор кнопки "Восстановить" в форме восстановления пароля