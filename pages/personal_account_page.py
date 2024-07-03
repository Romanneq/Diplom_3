import allure
from pages.base_page import BasePage
from locators.locators_personal_account import PersonalAccountElements, PersonalAccountButtons


class PersonalAccount(BasePage):  # Создали класс страницы персонального аккаунта

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Метод отображения главной страницы персонального аккаунта')
    def wait_personal_account_page(self: BasePage):
        return self.wait_element_page(PersonalAccountElements.FORM_PERS_ACC)

    @allure.step('Метод клика по кнопке "История заказов" в личном кабинете')
    def click_history_order_on_personal_account(self: BasePage):
        self.click_element_page(PersonalAccountButtons.HISTORY_ORDER)

    @allure.step('Метод отображения истории заказов')
    def wait_history_order_on_personal_account(self: BasePage):
        return self.wait_element_page(PersonalAccountElements.HIST_ORD_FORM)

    @allure.step('Метод клика по кнопке "Выход"')
    def click_log_out_on_personal_account(self: BasePage):
        self.click_element_page(PersonalAccountButtons.LOG_OUT)

    @allure.step('Метод возврата id заказа в истории заказов персонального аккаунта')
    def return_id_order_in_history_order_on_presonal_account(self: BasePage):
        return self.base_text_element(PersonalAccountElements.ID_ORD_IN_HIST_ORD)

    @allure.step('Метод клика по заказу в истории заказов в персональном аккаунте')
    def click_order_in_history_orders(self: BasePage):
        return self.click_element_page(PersonalAccountElements.FIRST_ORDER)
