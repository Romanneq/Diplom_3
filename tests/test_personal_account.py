import allure


class TestPersonalAccount:

    @allure.title('Тестирование перехода по клику на кнопку "Личный кабинет"')
    def test_go_to_the_personal_account(self, instance_main_page, instance_login_page, instance_per_acc_page,
                                        create_user_and_delete_user):
        instance_main_page.wait_main_page()
        instance_main_page.click_on_button_sign_in_or_place_an_order()
        instance_login_page.wait_form_login()
        instance_login_page.completion_fields_login_and_password_and_log_user(create_user_and_delete_user)
        instance_main_page.wait_main_page()
        instance_main_page.click_on_button_personal_acc()
        assert instance_per_acc_page.wait_personal_account_page()

    @allure.title('Тестирование отображения истории заказов в личном кабинете')
    def test_go_to_the_order_history_in_personal_account(self, instance_main_page, instance_login_page,
                                                         instance_per_acc_page, create_user_and_delete_user):
        instance_main_page.wait_main_page()
        instance_main_page.click_on_button_sign_in_or_place_an_order()
        instance_login_page.wait_form_login()
        instance_login_page.completion_fields_login_and_password_and_log_user(create_user_and_delete_user)
        instance_main_page.wait_main_page()
        instance_main_page.click_on_button_personal_acc()
        instance_per_acc_page.wait_personal_account_page()
        instance_per_acc_page.click_history_order_on_personal_account()
        assert instance_per_acc_page.wait_history_order_on_personal_account()

    @allure.title('Тестирование выхода из аккаунта')
    def test_log_out_from_personal_account(self, instance_main_page, instance_login_page, instance_per_acc_page,
                                           create_user_and_delete_user):
        instance_main_page.wait_main_page()
        instance_main_page.click_on_button_sign_in_or_place_an_order()
        instance_login_page.wait_form_login()
        instance_login_page.completion_fields_login_and_password_and_log_user(create_user_and_delete_user)
        instance_main_page.wait_main_page()
        instance_main_page.click_on_button_personal_acc()
        instance_per_acc_page.wait_personal_account_page()
        instance_per_acc_page.click_log_out_on_personal_account()
        assert instance_login_page.wait_form_login()
