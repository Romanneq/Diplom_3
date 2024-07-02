import allure
from locators.locators_main_page import MainPageButtons
from pages.base_page import BasePage
from locators.locators_main_page import MainPageElements


class MainPageBurger(BasePage):  # Создали класс главной страницы cервиса

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Метод отображения главной страницы сервиса')
    def wait_main_page(self: BasePage):
        return self.wait_element_page(MainPageElements.FORM_ASSEMBLE_BURGER)

    @allure.step('Метод клика по кнопке "Войти в аккаунт" или "Оформить заказ"')
    def click_on_button_sign_in_or_place_an_order(self: BasePage):
        self.click_element_page(MainPageButtons.BUTT_MAIN_PAGE)

    @allure.step('Метод клика на кнопку "Личный кабинет"')
    def click_on_button_personal_acc(self: BasePage):
        self.click_element_page(MainPageButtons.PERS_ACCOUNT)

    @allure.step('Метод клика на логотип сервиса')
    def click_on_logo_main_page(self: BasePage):
        self.click_element_page(MainPageElements.LOGO_BURGER)

    @allure.step('Метод клика на кнопку "Лента заказов"')
    def click_on_button_order_feed(self: BasePage):
        self.click_element_page(MainPageButtons.ORDER_FEED)

    @allure.step('Метод клика на кнопку "Конструктор"')
    def click_on_button_constructor(self: BasePage):
        self.click_element_page(MainPageButtons.CONSTRUCTOR)

    @allure.step('Метод клика на ингредиент булки')
    def click_on_ingredient_bul(self: BasePage):
        self.click_element_page(MainPageElements.ING_BUL)

    @allure.step('Метод ожидания отображения всплывающего окна с деталями ингредиента')
    def wait_open_popup_window_ing(self: BasePage):
        return self.wait_element_page(MainPageElements.POPUP_WINDOW)

    @allure.step('Метод клика на крестик во всплывающем окне с деталями ингредиента')
    def click_on_cross_in_popup_window_ing(self: BasePage):
        self.click_element_page(MainPageElements.CROSS_IN_WIN_ING)

    @allure.step('Метод перетаскивания ингредиента булки в корзину')
    def dragging_an_ingredient_bul_in_order_basket(self: BasePage):
        self.dragging_an_ingredient(MainPageElements.ING_BUL, MainPageElements.ORDER_BASKET)

    @allure.step('Метод отображения булки в корзине')
    def wait_ingredient_in_order_basket(self: BasePage):
        return self.wait_element_page(MainPageElements.ING_IN_ORD_BUL)

    @allure.step('Метод отображения счетчика добавленного ингредиента в корзину заказа')
    def displayed_counter_ingredient_in_form_assemble_burger(self: BasePage):
        return self.base_text_element(MainPageElements.COUNT_ING)

    @allure.step('Метод отображения окна с индентификатором заказа')
    def wait_displayed_window_with_order_id(self: BasePage):
        return self.wait_element_page(MainPageElements.WIN_ORD_ID)

    @allure.step('Метод отображения id заказа в окне оформленного заказа')
    def wait_displayed_id_order_in_window_order(self: BasePage):
        return self.re_wait_element_page(MainPageElements.ID_ORD, '9999')

    @allure.step('Метод возврата id заказа на главной странице')
    def return_id_order_in_window_order(self: BasePage):
        return self.base_text_element(MainPageElements.ID_ORD)
