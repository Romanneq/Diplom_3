from selenium.webdriver.common.by import By


class LoginPageForm:
    form_log = [By.XPATH, ".//form[contains(@class, 'Auth_form__')]"]  # локатор формы входа в сервис
    show_pass_icon = [By.CSS_SELECTOR, ".input__icon > svg"]  # локатор иконки показать/скрыть пароль
    active_pass_field = [By.XPATH, ".//div[contains(@class, 'input_status_active')]"]  # локатор активного поля пароль
    field_email_log = [By.XPATH, ".//div[contains(@class, 'input_type_text ')]//child::input"]  # локатор поля email в форме входа в сервис
    field_pass_log = [By.XPATH, ".//div[contains(@class, 'input_type_password')]//child::input"]  # локатор поля password в форме входа в сервис


class LoginPageButtons:
    pass_rec = [By.XPATH, ".//a[text() = 'Восстановить пароль']"]  # локатор кнопки "Восстановить пароль"
    enter_acc_user = [By.XPATH, ".//button[contains(@class, 'button_button__')]"]  # локатор кнопки "Войти" в форме входа в сервис
