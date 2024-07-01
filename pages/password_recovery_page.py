import allure
from pages.base_page import BasePage
from locators.locators_password_recovery import PasswordRecoveryElements, PasswordRecoveryButton


class PasswordRecoveryPage(BasePage):  # Создали класс страницы восстановления пароля

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Метод отображения страницы восстановления пароля')
    def wait_recovery_page(self):
        return BasePage.wait_element_page(self, PasswordRecoveryElements.FORM_REC_EMAIL)

    @allure.step('Метод ввода почты в форму восстановления пароля')
    def send_email_in_password_recovery_page(self, data_user):
        BasePage.send_keys_element(self, PasswordRecoveryElements.FIELD_EMAIL_REC, f'{data_user[1]}')

    @allure.step('Метод клика по кнопке "Восстановить" в форме восстановить пароль')
    def click_button_recovery(self):
        BasePage.click_element_page(self, PasswordRecoveryButton.BUTTON_RECOVERY)

    @allure.step('Метод отображения формы восстановление пароля')
    def wait_password_recovery_page(self):
        return BasePage.wait_element_page(self, PasswordRecoveryElements.FORM_REC_PAS)
