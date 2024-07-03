from selenium.webdriver.common.by import By


class LoginPageForm:
    FORM_LOG = [By.XPATH, ".//form[contains(@class, 'Auth_form__')]"]  # локатор формы входа в сервис
    SHOW_PASS_ICON = [By.CSS_SELECTOR, ".input__icon > svg"]  # локатор иконки показать/скрыть пароль
    ACTIVE_PASS_FIELD = [By.XPATH, ".//div[contains(@class, 'input_status_active')]"]  # локатор активного поля пароль
    FIELD_EMAIL_LOG = [By.XPATH, ".//div[contains(@class, 'input_type_text ')]//child::input"]  # локатор поля email в форме входа в сервис
    FIELD_PASS_LOG = [By.XPATH, ".//div[contains(@class, 'input_type_password')]//child::input"]  # локатор поля password в форме входа в сервис


class LoginPageButtons:
    PASS_REC = [By.XPATH, ".//a[text() = 'Восстановить пароль']"]  # локатор кнопки "Восстановить пароль"
    ENTER_ACC_USER = [By.XPATH, ".//button[contains(@class, 'button_button__')]"]  # локатор кнопки "Войти" в форме входа в сервис
