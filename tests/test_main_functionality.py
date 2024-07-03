import allure


class TestMainFunctionality:

    @allure.title('Тестирование перехода на страницу ленты заказов кликом на кнопку "Лента заказов"')
    def test_click_on_button_order_feed_sends_to_the_order_feed_page(self, instance_main_page,
                                                                     instance_order_feed_page):
        instance_main_page.wait_main_page()
        instance_main_page.click_on_button_order_feed()
        assert instance_order_feed_page.wait_order_feed_page()

    @allure.title('Тестирование перехода на основную страницу кликом по кнопке "Конструктор"')
    def test_click_on_button_constructor_sends_to_the_main_page(self, instance_main_page, instance_order_feed_page):
        instance_main_page.wait_main_page()
        instance_main_page.click_on_button_order_feed()
        instance_order_feed_page.wait_order_feed_page()
        instance_main_page.click_on_button_constructor()
        assert instance_main_page.wait_main_page()

    @allure.title('Клик по ингредиенту открывает всплывающее окно с деталями ингредиента')
    def test_click_on_ing_spicy_x_open_popup_window_with_details(self, instance_main_page,):
        instance_main_page.wait_main_page()
        instance_main_page.click_on_ingredient_bul()
        assert instance_main_page.wait_open_popup_window_ing()

    @allure.title('Клик по крестику закрывает окно с деталями ингредиента')
    def test_click_on_cross_in_popup_window_close_popup_window(self, instance_main_page):
        instance_main_page.wait_main_page()
        instance_main_page.click_on_ingredient_bul()
        instance_main_page.wait_open_popup_window_ing()
        instance_main_page.click_on_cross_in_popup_window_ing()
        assert instance_main_page.wait_open_popup_window_ing() != True

    @allure.title('Тест: при перетаскивании ингредиента в корзину заказов, счетчик этого ингредиента увеличивается')
    def test_when_dragging_ingredient_in_order_basket_icon_counter_this_ing_increases(self, instance_main_page):
        instance_main_page.wait_main_page()
        instance_main_page.dragging_an_ingredient_bul_in_order_basket()
        instance_main_page.wait_ingredient_in_order_basket()
        assert instance_main_page.displayed_counter_ingredient_in_form_assemble_burger() == '2'

    @allure.title('Тест: авторизованный пользователь может оформить заказ')
    def test_authorized_user_can_place_an_order(self, instance_main_page, instance_login_page,
                                                create_user_and_delete_user):
        instance_main_page.wait_main_page()
        instance_main_page.click_on_button_sign_in_or_place_an_order()
        instance_login_page.wait_form_login()
        instance_login_page.completion_fields_login_and_password_and_log_user(create_user_and_delete_user)
        instance_main_page.wait_main_page()
        instance_main_page.dragging_an_ingredient_bul_in_order_basket()
        instance_main_page.wait_ingredient_in_order_basket()
        instance_main_page.click_on_button_sign_in_or_place_an_order()
        assert instance_main_page.wait_displayed_window_with_order_id()
