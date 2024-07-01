from selenium.webdriver.common.by import By


class PasswordRecoveryElements:
    FORM_REC_EMAIL = [By.XPATH, ".//div[contains(@class, 'Auth_login__')]"]  # локатор формы "Восстановления пароля" с полем email
    FIELD_EMAIL_REC = [By.XPATH, ".//input[contains(@class, 'text input__textfield')]"]  # локатор поля ввода email в форме восстановления пароля
    FORM_REC_PAS = [By.XPATH, ".//div[contains(@class, 'Auth_login_')]"]  # локатор формы восстановления пароля c полем пароль и кодом


class PasswordRecoveryButton:
    BUTTON_RECOVERY = [By.XPATH, ".//button[contains(@class, 'button_button__')]"]  # локатор кнопки "Восстановить" в форме восстановления пароля
