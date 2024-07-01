import allure
from locators.locators_login_page import LoginPageForm
from locators.locators_login_page import LoginPageButtons
from pages.base_page import BasePage


class LoginPageBurger(BasePage):  # создали класс страницы входа в сервис

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Метод ожидания формы входа в сервис')
    def wait_form_login(self):
        return BasePage.wait_element_page(self, LoginPageForm.FORM_LOG)

    @allure.step('Метод клика на кнопку "Восстановить пароль"')
    def click_on_button_password_recovery(self):
        BasePage.click_element_page(self, LoginPageButtons.PASS_REC)

    @allure.step('Метод клика на кнопку показать/скрыть пароль')
    def click_show_password(self):
        BasePage.click_element_page(self, LoginPageForm.SHOW_PASS_ICON)

    @allure.step('Метод отображения активного поля "Пароль"')
    def wait_active_password_field(self):
        return BasePage.wait_element_page(self, LoginPageForm.ACTIVE_PASS_FIELD)

    @allure.step('Метод входа в сервис нового пользователя')
    def completion_fields_login_and_password_and_log_user(self, data_user):
        BasePage.send_keys_element(self, LoginPageForm.FIELD_EMAIL_LOG, f'{data_user[1]}')
        BasePage.send_keys_element(self, LoginPageForm.FIELD_PASS_LOG, f'{data_user[2]}')
        BasePage.click_execute_element_page(self, LoginPageButtons.ENTER_ACC_USER)
