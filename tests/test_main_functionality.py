import allure
from pages.main_page import MainPageBurger
from pages.login_page import LoginPageBurger
from pages.order_feed_page import OrderFeed


class TestMainFunctionality:

    @allure.title('Тестирование перехода на страницу ленты заказов кликом на кнопку "Лента заказов"')
    def test_click_on_button_order_feed_sends_to_the_order_feed_page(self, web_driver):
        main_page_obj = MainPageBurger(web_driver)
        main_page_obj.wait_main_page()
        main_page_obj.click_on_button_order_feed()
        order_feed = OrderFeed(web_driver)
        assert order_feed.wait_order_feed_page()

    @allure.title('Тестирование перехода на основную страницу кликом по кнопке "Конструктор"')
    def test_click_on_button_constructor_sends_to_the_main_page(self, web_driver):
        main_page_obj = MainPageBurger(web_driver)
        main_page_obj.wait_main_page()
        main_page_obj.click_on_button_order_feed()
        order_feed = OrderFeed(web_driver)
        order_feed.wait_order_feed_page()
        main_page_obj.click_on_button_constructor()
        assert main_page_obj.wait_main_page()

    @allure.title('Клик по ингредиенту открывает всплывающее окно с деталями ингредиента')
    def test_click_on_ing_spicy_x_open_popup_window_with_details(self, web_driver):
        main_page_obj = MainPageBurger(web_driver)
        main_page_obj.wait_main_page()
        main_page_obj.click_on_ingredient_bul()
        assert main_page_obj.wait_open_popup_window_ing()

    @allure.title('Клик по крестику закрывает окно с деталями ингредиента')
    def test_click_on_cross_in_popup_window_close_popup_window(self, web_driver):
        main_page_obj = MainPageBurger(web_driver)
        main_page_obj.wait_main_page()
        main_page_obj.click_on_ingredient_bul()
        main_page_obj.wait_open_popup_window_ing()
        main_page_obj.click_on_cross_in_popup_window_ing()
        assert main_page_obj.wait_open_popup_window_ing() != True

    @allure.title('Тест: при перетаскивании ингредиента в корзину заказов, счетчик этого ингредиента увеличивается')
    def test_when_dragging_ingredient_in_order_basket_icon_counter_this_ing_increases(self, web_driver):
        main_page_obj = MainPageBurger(web_driver)
        main_page_obj.wait_main_page()
        main_page_obj.dragging_an_ingredient_bul_in_order_basket()
        main_page_obj.wait_ingredient_in_order_basket()
        assert main_page_obj.displayed_counter_ingredient_in_form_assemble_burger() == '2'

    @allure.title('Тест: авторизованный пользователь может оформить заказ')
    def test_authorized_user_can_place_an_order(self, web_driver, create_user_and_delete_user):
        main_page_obj = MainPageBurger(web_driver)
        main_page_obj.wait_main_page()
        main_page_obj.click_on_button_sign_in_or_place_an_order()
        log_page_obj = LoginPageBurger(web_driver)
        log_page_obj.wait_form_login()
        log_page_obj.completion_fields_login_and_password_and_log_user(create_user_and_delete_user)
        main_page_obj.wait_main_page()
        main_page_obj.dragging_an_ingredient_bul_in_order_basket()
        main_page_obj.wait_ingredient_in_order_basket()
        main_page_obj.click_on_button_sign_in_or_place_an_order()
        assert main_page_obj.wait_displayed_window_with_order_id()

