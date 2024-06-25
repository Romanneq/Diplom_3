import allure
from locators.locators_login_page import LoginPageForm
from locators.locators_login_page import LoginPageButtons
from pages.base_page import BasePage


class LoginPageBurger(BasePage):  # создали класс страницы входа в сервис

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Метод ожидания формы входа в сервис')
    def wait_form_login(self):
        return BasePage.wait_element_page(self, LoginPageForm.form_log)

    @allure.step('Метод клика на кнопку "Восстановить пароль"')
    def click_on_button_password_recovery(self):
        BasePage.click_element_page(self, LoginPageButtons.pass_rec)

    @allure.step('Метод клика на кнопку показать/скрыть пароль')
    def click_show_password(self):
        BasePage.click_element_page(self, LoginPageForm.show_pass_icon)

    @allure.step('Метод отображения активного поля "Пароль"')
    def wait_active_password_field(self):
        return BasePage.wait_element_page(self, LoginPageForm.active_pass_field)

    @allure.step('Метод входа в сервис нового пользователя')
    def completion_fields_login_and_password_and_log_user(self, data_user):
        BasePage.send_keys_element(self, LoginPageForm.field_email_log, f'{data_user[1]}')
        BasePage.send_keys_element(self, LoginPageForm.field_pass_log, f'{data_user[2]}')
        BasePage.click_execute_element_page(self, LoginPageButtons.enter_acc_user)



