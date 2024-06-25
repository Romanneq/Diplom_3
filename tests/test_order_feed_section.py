import allure
from pages.main_page import MainPageBurger
from pages.login_page import LoginPageBurger
from pages.order_feed_page import OrderFeed
from pages.personal_account_page import PersonalAccount


class TestOrderFeedSection:

    @allure.title('Если кликнуть на заказ в ленте заказов, отобразятся детали этого заказа')
    def test_click_on_first_order_in_order_feed_page_and_display_details_order(self, web_driver):
        main_page_obj = MainPageBurger(web_driver)
        main_page_obj.wait_main_page()
        main_page_obj.click_on_button_order_feed()
        order_feed = OrderFeed(web_driver)
        order_feed.wait_order_feed_page()
        order_feed.click_first_order_on_order_feed_page()
        assert order_feed.wait_window_with_details_order_on_order_feed_page()

    @allure.title('Заказы пользователя из раздела "История заказов" в личном кабинете отображаются в Ленте заказов')
    def test_orders_user_displayed_in_history_orders_and_order_feed(self, web_driver, create_user_and_delete_user):
        # Логинимся пользователем
        main_page_obj = MainPageBurger(web_driver)
        main_page_obj.wait_main_page()
        main_page_obj.click_on_button_sign_in_or_place_an_order()
        log_page_obj = LoginPageBurger(web_driver)
        log_page_obj.wait_form_login()
        log_page_obj.completion_fields_login_and_password_and_log_user(create_user_and_delete_user)
        main_page_obj.wait_main_page()
        # Создаем заказ
        main_page_obj.dragging_an_ingredient_bul_in_order_basket()
        main_page_obj.wait_ingredient_in_order_basket()
        main_page_obj.click_on_button_sign_in_or_place_an_order()
        main_page_obj.wait_displayed_window_with_order_id()
        main_page_obj.wait_displayed_id_order_in_window_order()
        main_page_obj.click_on_button_personal_acc()
        main_page_obj.wait_main_page()
        # Получаем id заказа в персональном аккаунте в истории заказов
        main_page_obj.click_on_button_personal_acc()
        pers_acc_obj = PersonalAccount(web_driver)
        pers_acc_obj.wait_personal_account_page()
        pers_acc_obj.click_history_order_on_personal_account()
        pers_acc_obj.wait_history_order_on_personal_account()
        pers_acc_obj.click_order_in_history_orders()
        id_ord_pers_acc = pers_acc_obj.return_id_order_in_history_order_on_presonal_account()
        # Получаем id заказа в ленте заказов и сравниваем все id
        main_page_obj.click_on_button_order_feed()
        main_page_obj.click_on_button_order_feed()
        order_feed = OrderFeed(web_driver)
        order_feed.wait_order_feed_page()
        id_ord_feed_page = order_feed.return_id_order_in_order_feed_page()
        assert id_ord_pers_acc == id_ord_feed_page

    @allure.title('При создании заказа счетчик выполнено за все время в ленте заказов увеличивается')
    def test_when_create_order_counter_completed_all_the_time_increasing(self, web_driver, create_user_and_delete_user):
        # Логинимся новым пользователем
        main_page_obj = MainPageBurger(web_driver)
        main_page_obj.wait_main_page()
        main_page_obj.click_on_button_sign_in_or_place_an_order()
        log_page_obj = LoginPageBurger(web_driver)
        log_page_obj.wait_form_login()
        log_page_obj.completion_fields_login_and_password_and_log_user(create_user_and_delete_user)
        main_page_obj.wait_main_page()
        # получаем счетчик до создания заказа
        main_page_obj.click_on_button_order_feed()
        order_feed = OrderFeed(web_driver)
        order_feed.wait_order_feed_page()
        counter_before_order = order_feed.return_counter_orders_all_time_in_order_feed_page()
        # создаем заказ
        main_page_obj.click_on_logo_main_page()
        main_page_obj.wait_main_page()
        main_page_obj.dragging_an_ingredient_bul_in_order_basket()
        main_page_obj.wait_ingredient_in_order_basket()
        main_page_obj.click_on_button_sign_in_or_place_an_order()
        main_page_obj.wait_displayed_window_with_order_id()
        main_page_obj.wait_displayed_id_order_in_window_order()
        main_page_obj.click_on_button_order_feed()
        main_page_obj.wait_main_page()
        # получаем счетчик после создания заказа и сравниваем их
        main_page_obj.click_on_button_order_feed()
        order_feed = OrderFeed(web_driver)
        order_feed.wait_order_feed_page()
        counter_after_order = order_feed.return_counter_orders_all_time_in_order_feed_page()
        assert int(counter_after_order) == int(counter_before_order) + 1

    @allure.title('При создании заказа счетчик выполнено за сегодня в ленте заказов увеличивается')
    def test_when_create_order_counter_completed_today_increasing(self, web_driver, create_user_and_delete_user):
        # Логинимся новым пользователем
        main_page_obj = MainPageBurger(web_driver)
        main_page_obj.wait_main_page()
        main_page_obj.click_on_button_sign_in_or_place_an_order()
        log_page_obj = LoginPageBurger(web_driver)
        log_page_obj.wait_form_login()
        log_page_obj.completion_fields_login_and_password_and_log_user(create_user_and_delete_user)
        main_page_obj.wait_main_page()
        # получаем счетчик до создания заказа
        main_page_obj.click_on_button_order_feed()
        order_feed = OrderFeed(web_driver)
        order_feed.wait_order_feed_page()
        counter_before_order = order_feed.return_counter_orders_today_in_order_feed_page()
        # создаем заказ
        main_page_obj.click_on_logo_main_page()
        main_page_obj.wait_main_page()
        main_page_obj.dragging_an_ingredient_bul_in_order_basket()
        main_page_obj.wait_ingredient_in_order_basket()
        main_page_obj.click_on_button_sign_in_or_place_an_order()
        main_page_obj.wait_displayed_window_with_order_id()
        main_page_obj.wait_displayed_id_order_in_window_order()
        main_page_obj.click_on_button_order_feed()
        main_page_obj.wait_main_page()
        # получаем счетчик после создания заказа и сравниваем их
        main_page_obj.click_on_button_order_feed()
        order_feed = OrderFeed(web_driver)
        order_feed.wait_order_feed_page()
        counter_after_order = order_feed.return_counter_orders_today_in_order_feed_page()
        assert int(counter_after_order) == int(counter_before_order) + 1

    @allure.title('После создания заказа его номер отображается в разделе: в работе')
    def test_when_create_order_id_order_displayed_in_section_in_progress(self, web_driver, create_user_and_delete_user):
        # Логинимся новым пользователем
        main_page_obj = MainPageBurger(web_driver)
        main_page_obj.wait_main_page()
        main_page_obj.click_on_button_sign_in_or_place_an_order()
        log_page_obj = LoginPageBurger(web_driver)
        log_page_obj.wait_form_login()
        log_page_obj.completion_fields_login_and_password_and_log_user(create_user_and_delete_user)
        main_page_obj.wait_main_page()
        # получаем id заказa
        main_page_obj.dragging_an_ingredient_bul_in_order_basket()
        main_page_obj.wait_ingredient_in_order_basket()
        main_page_obj.click_on_button_sign_in_or_place_an_order()
        main_page_obj.wait_displayed_window_with_order_id()
        main_page_obj.wait_displayed_id_order_in_window_order()
        id_order = main_page_obj.return_id_order_in_window_order()
        main_page_obj.click_on_button_order_feed()
        main_page_obj.wait_main_page()
        main_page_obj.click_on_button_order_feed()
        # Проверяем, что номер заказа отображается в разделе: в работе
        order_feed = OrderFeed(web_driver)
        order_feed.wait_order_feed_page()
        order_feed.re_wait_id_order_in_order_feed_page()
        section_in_progress = order_feed.return_id_order_section_in_progress_in_order_feed_page()
        assert id_order == section_in_progress[:0] + section_in_progress[0+1:]
