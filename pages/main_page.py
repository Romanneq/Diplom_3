import allure
from locators.locators_main_page import MainPageButtons
from pages.base_page import BasePage
from locators.locators_main_page import MainPageElements


class MainPageBurger(BasePage):  # Создали класс главной страницы cервиса

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Метод отображения главной страницы сервиса')
    def wait_main_page(self):
        return BasePage.wait_element_page(self, MainPageElements.form_assemble_burger)

    @allure.step('Метод клика по кнопке "Войти в аккаунт" или "Оформить заказ"')
    def click_on_button_sign_in_or_place_an_order(self):
        BasePage.click_element_page(self, MainPageButtons.butt_main_page)

    @allure.step('Метод клика на кнопку "Личный кабинет"')
    def click_on_button_personal_acc(self):
        BasePage.click_element_page(self, MainPageButtons.pers_accoount)

    @allure.step('Метод клика на логотип сервиса')
    def click_on_logo_main_page(self):
        BasePage.click_element_page(self, MainPageElements.logo_burger)

    @allure.step('Метод клика на кнопку "Лента заказов"')
    def click_on_button_order_feed(self):
        BasePage.click_element_page(self, MainPageButtons.order_feed)

    @allure.step('Метод клика на кнопку "Конструктор"')
    def click_on_button_constructor(self):
        BasePage.click_element_page(self, MainPageButtons.constructor)

    @allure.step('Метод клика на ингредиент булки')
    def click_on_ingredient_bul(self):
        BasePage.click_element_page(self, MainPageElements.ing_bul)

    @allure.step('Метод ожидания отображения всплывающего окна с деталями ингредиента')
    def wait_open_popup_window_ing(self):
        return BasePage.wait_element_page(self, MainPageElements.popup_window)

    @allure.step('Метод клика на крестик во всплывающем окне с деталями ингредиента')
    def click_on_cross_in_popup_window_ing(self):
        BasePage.click_element_page(self, MainPageElements.cross_in_win_ing)

    @allure.step('Метод перетаскивания ингредиента булки в корзину')
    def dragging_an_ingredient_bul_in_order_basket(self):
        BasePage.dragging_an_ingredient(self, MainPageElements.ing_bul, MainPageElements.order_basket)

    @allure.step('Метод отображения булки в корзине')
    def wait_ingredient_in_order_basket(self):
        return BasePage.wait_element_page(self, MainPageElements.ing_in_ord_bul)

    @allure.step('Метод отображения счетчика добавленного ингредиента в корзину заказа')
    def displayed_counter_ingredient_in_form_assemble_burger(self):
        return BasePage.base_text_element(self, MainPageElements.count_ing)

    @allure.step('Метод отображения окна с индентификатором заказа')
    def wait_displayed_window_with_order_id(self):
        return BasePage.wait_element_page(self, MainPageElements.win_ord_id)

    @allure.step('Метод отображения id заказа в окне оформленного заказа')
    def wait_displayed_id_order_in_window_order(self):
        return BasePage.re_wait_element_page(self, MainPageElements.id_ord, '9999')

    @allure.step('Метод возврата id заказа на главной странице')
    def return_id_order_in_window_order(self):
        return BasePage.base_text_element(self, MainPageElements.id_ord)
