import allure


class TestOrderFeedSection:

    @allure.title('Если кликнуть на заказ в ленте заказов, отобразятся детали этого заказа')
    def test_click_on_first_order_in_order_feed_page_and_display_details_order(self, instance_main_page,
                                                                               instance_order_feed_page):
        instance_main_page.wait_main_page()
        instance_main_page.click_on_button_order_feed()
        instance_order_feed_page.wait_order_feed_page()
        instance_order_feed_page.click_first_order_on_order_feed_page()
        assert instance_order_feed_page.wait_window_with_details_order_on_order_feed_page()

    @allure.title('Заказы пользователя из раздела "История заказов" в личном кабинете отображаются в Ленте заказов')
    def test_orders_user_displayed_in_history_orders_and_order_feed(self, instance_main_page,
                                                                    instance_login_page,
                                                                    instance_per_acc_page,
                                                                    instance_order_feed_page,
                                                                    create_user_and_delete_user):
        # Логинимся пользователем
        instance_main_page.wait_main_page()
        instance_main_page.click_on_button_sign_in_or_place_an_order()
        instance_login_page.wait_form_login()
        instance_login_page.completion_fields_login_and_password_and_log_user(create_user_and_delete_user)
        instance_main_page.wait_main_page()
        # Создаем заказ
        instance_main_page.dragging_an_ingredient_bul_in_order_basket()
        instance_main_page.wait_ingredient_in_order_basket()
        instance_main_page.click_on_button_sign_in_or_place_an_order()
        instance_main_page.wait_displayed_window_with_order_id()
        instance_main_page.wait_displayed_id_order_in_window_order()
        instance_main_page.click_on_button_personal_acc()
        instance_main_page.wait_main_page()
        # Получаем id заказа в персональном аккаунте в истории заказов
        instance_main_page.click_on_button_personal_acc()
        instance_per_acc_page.wait_personal_account_page()
        instance_per_acc_page.click_history_order_on_personal_account()
        instance_per_acc_page.wait_history_order_on_personal_account()
        instance_per_acc_page.click_order_in_history_orders()
        id_ord_pers_acc = instance_per_acc_page.return_id_order_in_history_order_on_presonal_account()
        # Получаем id заказа в ленте заказов и сравниваем все id
        instance_main_page.click_on_button_order_feed()
        instance_main_page.click_on_button_order_feed()
        instance_order_feed_page.wait_order_feed_page()
        id_ord_feed_page = instance_order_feed_page.return_id_order_in_order_feed_page()
        assert id_ord_pers_acc == id_ord_feed_page

    @allure.title('При создании заказа счетчик выполнено за все время в ленте заказов увеличивается')
    def test_when_create_order_counter_completed_all_the_time_increasing(self, instance_main_page,
                                                                         instance_login_page,
                                                                         instance_order_feed_page,
                                                                         create_user_and_delete_user):
        # Логинимся новым пользователем
        instance_main_page.wait_main_page()
        instance_main_page.click_on_button_sign_in_or_place_an_order()
        instance_login_page.wait_form_login()
        instance_login_page.completion_fields_login_and_password_and_log_user(create_user_and_delete_user)
        instance_main_page.wait_main_page()
        # получаем счетчик до создания заказа
        instance_main_page.click_on_button_order_feed()
        instance_order_feed_page.wait_order_feed_page()
        counter_before_order = instance_order_feed_page.return_counter_orders_all_time_in_order_feed_page()
        # создаем заказ
        instance_main_page.click_on_logo_main_page()
        instance_main_page.wait_main_page()
        instance_main_page.dragging_an_ingredient_bul_in_order_basket()
        instance_main_page.wait_ingredient_in_order_basket()
        instance_main_page.click_on_button_sign_in_or_place_an_order()
        instance_main_page.wait_displayed_window_with_order_id()
        instance_main_page.wait_displayed_id_order_in_window_order()
        instance_main_page.click_on_button_order_feed()
        instance_main_page.wait_main_page()
        # получаем счетчик после создания заказа и сравниваем их
        instance_main_page.click_on_button_order_feed()
        instance_order_feed_page.wait_order_feed_page()
        counter_after_order = instance_order_feed_page.return_counter_orders_all_time_in_order_feed_page()
        assert int(counter_after_order) == int(counter_before_order) + 1

    @allure.title('При создании заказа счетчик выполнено за сегодня в ленте заказов увеличивается')
    def test_when_create_order_counter_completed_today_increasing(self, instance_main_page,
                                                                  instance_login_page,
                                                                  instance_order_feed_page,
                                                                  create_user_and_delete_user):
        # Логинимся новым пользователем
        instance_main_page.wait_main_page()
        instance_main_page.click_on_button_sign_in_or_place_an_order()
        instance_login_page.wait_form_login()
        instance_login_page.completion_fields_login_and_password_and_log_user(create_user_and_delete_user)
        instance_main_page.wait_main_page()
        # получаем счетчик до создания заказа
        instance_main_page.click_on_button_order_feed()
        instance_order_feed_page.wait_order_feed_page()
        counter_before_order = instance_order_feed_page.return_counter_orders_today_in_order_feed_page()
        # создаем заказ
        instance_main_page.click_on_logo_main_page()
        instance_main_page.wait_main_page()
        instance_main_page.dragging_an_ingredient_bul_in_order_basket()
        instance_main_page.wait_ingredient_in_order_basket()
        instance_main_page.click_on_button_sign_in_or_place_an_order()
        instance_main_page.wait_displayed_window_with_order_id()
        instance_main_page.wait_displayed_id_order_in_window_order()
        instance_main_page.click_on_button_order_feed()
        instance_main_page.wait_main_page()
        # получаем счетчик после создания заказа и сравниваем их
        instance_main_page.click_on_button_order_feed()
        instance_order_feed_page.wait_order_feed_page()
        counter_after_order = instance_order_feed_page.return_counter_orders_today_in_order_feed_page()
        assert int(counter_after_order) == int(counter_before_order) + 1

    @allure.title('После создания заказа его номер отображается в разделе: в работе')
    def test_when_create_order_id_order_displayed_in_section_in_progress(self, instance_main_page,
                                                                         instance_login_page,
                                                                         instance_order_feed_page,
                                                                         create_user_and_delete_user):
        # Логинимся новым пользователем
        instance_main_page.wait_main_page()
        instance_main_page.click_on_button_sign_in_or_place_an_order()
        instance_login_page.wait_form_login()
        instance_login_page.completion_fields_login_and_password_and_log_user(create_user_and_delete_user)
        instance_main_page.wait_main_page()
        # получаем id заказa
        instance_main_page.dragging_an_ingredient_bul_in_order_basket()
        instance_main_page.wait_ingredient_in_order_basket()
        instance_main_page.click_on_button_sign_in_or_place_an_order()
        instance_main_page.wait_displayed_window_with_order_id()
        instance_main_page.wait_displayed_id_order_in_window_order()
        id_order = instance_main_page.return_id_order_in_window_order()
        instance_main_page.click_on_button_order_feed()
        instance_main_page.wait_main_page()
        instance_main_page.click_on_button_order_feed()
        # Проверяем, что номер заказа отображается в разделе: в работе
        instance_order_feed_page.wait_order_feed_page()
        instance_order_feed_page.re_wait_id_order_in_order_feed_page()
        section_in_progress = instance_order_feed_page.return_id_order_section_in_progress_in_order_feed_page()
        assert id_order == section_in_progress[:0] + section_in_progress[0+1:]
