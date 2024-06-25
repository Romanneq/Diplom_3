import allure
from pages.main_page import MainPageBurger
from pages.login_page import LoginPageBurger
from pages.password_recovery_page import PasswordRecoveryPage


class TestPasswordRecovery:

    @allure.title('Тестирование перехода на страницу восстановление пароля кликом по кнопке "Восстановить пароль"')
    def test_go_to_the_password_recovery_page(self, web_driver):
        main_page_obj = MainPageBurger(web_driver)
        main_page_obj.wait_main_page()
        main_page_obj.click_on_button_sign_in_or_place_an_order()
        log_page_obj = LoginPageBurger(web_driver)
        log_page_obj.wait_form_login()
        log_page_obj.click_on_button_password_recovery()
        pas_rec_obj = PasswordRecoveryPage(web_driver)
        assert pas_rec_obj.wait_recovery_page()

    @allure.title('Тестирование клика по кнопке "Восстановить" в форме восстановления пароля')
    def test_click_on_button_recovery_in_password_recovery_page(self, web_driver, create_user_and_delete_user):
        main_page_obj = MainPageBurger(web_driver)
        main_page_obj.wait_main_page()
        main_page_obj.click_on_button_sign_in_or_place_an_order()
        log_page_obj = LoginPageBurger(web_driver)
        log_page_obj.wait_form_login()
        log_page_obj.click_on_button_password_recovery()
        pas_rec_obj = PasswordRecoveryPage(web_driver)
        pas_rec_obj.wait_recovery_page()
        pas_rec_obj.send_email_in_password_recovery_page(create_user_and_delete_user)
        pas_rec_obj.click_button_recovery()
        assert pas_rec_obj.wait_password_recovery_page()

    @allure.title('Клик по иконке показать/скрыть пароль делает поле пароль активным')
    def test_make_field_password_active_by_click_show_password(self, web_driver):
        main_page_obj = MainPageBurger(web_driver)
        main_page_obj.wait_main_page()
        main_page_obj.click_on_button_sign_in_or_place_an_order()
        log_page_obj = LoginPageBurger(web_driver)
        log_page_obj.wait_form_login()
        log_page_obj.click_show_password()
        assert log_page_obj.wait_active_password_field()
