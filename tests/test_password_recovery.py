import allure


class TestPasswordRecovery:

    @allure.title('Тестирование перехода на страницу восстановление пароля кликом по кнопке "Восстановить пароль"')
    def test_go_to_the_password_recovery_page(self, instance_main_page, instance_login_page, instance_pass_rec_page):
        instance_main_page.wait_main_page()
        instance_main_page.click_on_button_sign_in_or_place_an_order()
        instance_login_page.wait_form_login()
        instance_login_page.click_on_button_password_recovery()
        assert instance_pass_rec_page.wait_recovery_page()

    @allure.title('Тестирование клика по кнопке "Восстановить" в форме восстановления пароля')
    def test_click_on_button_recovery_in_password_recovery_page(self, instance_main_page,
                                                                instance_login_page,
                                                                instance_pass_rec_page,
                                                                create_user_and_delete_user):
        instance_main_page.wait_main_page()
        instance_main_page.click_on_button_sign_in_or_place_an_order()
        instance_login_page.wait_form_login()
        instance_login_page.click_on_button_password_recovery()
        instance_pass_rec_page.wait_recovery_page()
        instance_pass_rec_page.send_email_in_password_recovery_page(create_user_and_delete_user)
        instance_pass_rec_page.click_button_recovery()
        assert instance_pass_rec_page.wait_password_recovery_page()

    @allure.title('Клик по иконке показать/скрыть пароль делает поле пароль активным')
    def test_make_field_password_active_by_click_show_password(self, instance_main_page, instance_login_page):
        instance_main_page.wait_main_page()
        instance_main_page.click_on_button_sign_in_or_place_an_order()
        instance_login_page.wait_form_login()
        instance_login_page.click_show_password()
        assert instance_login_page.wait_active_password_field()
