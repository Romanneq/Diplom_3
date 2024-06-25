import allure
from pages.base_page import BasePage
from locators.locators_personal_account import PersonalAccountElements, PersonalAccountButtons


class PersonalAccount(BasePage):  # Создали класс страницы персонального аккаунта

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Метод отображения главной страницы персонального аккаунта')
    def wait_personal_account_page(self):
        return BasePage.wait_element_page(self, PersonalAccountElements.form_pers_acc)

    @allure.step('Метод клика по кнопке "История заказов" в личном кабинете')
    def click_history_order_on_personal_account(self):
        BasePage.click_element_page(self, PersonalAccountButtons.history_order)

    @allure.step('Метод отображения истории заказов')
    def wait_history_order_on_personal_account(self):
        return BasePage.wait_element_page(self, PersonalAccountElements.hist_ord_form)

    @allure.step('Метод клика по кнопке "Выход"')
    def click_log_out_on_personal_account(self):
        BasePage.click_element_page(self, PersonalAccountButtons.log_out)

    @allure.step('Метод возврата id заказа в истории заказов персонального аккаунта')
    def return_id_order_in_history_order_on_presonal_account(self):
        return BasePage.base_text_element(self, PersonalAccountElements.id_ord_in_hist_ord)

    @allure.step('Метод клика по заказу в истории заказов в персональном аккаунте')
    def click_order_in_history_orders(self):
        return BasePage.click_element_page(self, PersonalAccountElements.first_order)





