import allure
from locators.locators_login_page import LoginPageForm
from locators.locators_login_page import LoginPageButtons
from pages.base_page import BasePage


class LoginPageBurger(BasePage):  # создали класс страницы входа в сервис

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Метод ожидания формы входа в сервис')
    def wait_form_login(self: BasePage):
        return self.wait_element_page(LoginPageForm.FORM_LOG)

    @allure.step('Метод клика на кнопку "Восстановить пароль"')
    def click_on_button_password_recovery(self: BasePage):
        self.click_element_page(LoginPageButtons.PASS_REC)

    @allure.step('Метод клика на кнопку показать/скрыть пароль')
    def click_show_password(self: BasePage):
        self.click_element_page(LoginPageForm.SHOW_PASS_ICON)

    @allure.step('Метод отображения активного поля "Пароль"')
    def wait_active_password_field(self: BasePage):
        return self.wait_element_page(LoginPageForm.ACTIVE_PASS_FIELD)

    @allure.step('Метод входа в сервис нового пользователя')
    def completion_fields_login_and_password_and_log_user(self: BasePage, data_user):
        self.send_keys_element(LoginPageForm.FIELD_EMAIL_LOG, f'{data_user[1]}')
        self.send_keys_element(LoginPageForm.FIELD_PASS_LOG, f'{data_user[2]}')
        self.click_execute_element_page(LoginPageButtons.ENTER_ACC_USER)
