import allure
from pages.main_page import MainPageBurger
from pages.login_page import LoginPageBurger
from pages.personal_account_page import PersonalAccount


class TestPersonalAccount:

    @allure.title('Тестирование перехода по клику на кнопку "Личный кабинет"')
    def test_go_to_the_personal_account(self, web_driver, create_user_and_delete_user):
        main_page_obj = MainPageBurger(web_driver)
        main_page_obj.wait_main_page()
        main_page_obj.click_on_button_sign_in_or_place_an_order()
        log_page_obj = LoginPageBurger(web_driver)
        log_page_obj.wait_form_login()
        log_page_obj.completion_fields_login_and_password_and_log_user(create_user_and_delete_user)
        main_page_obj.wait_main_page()
        main_page_obj.click_on_button_personal_acc()
        pers_acc_obj = PersonalAccount(web_driver)
        assert pers_acc_obj.wait_personal_account_page()

    @allure.title('Тестирование отображения истории заказов в личном кабинете')
    def test_go_to_the_order_history_in_personal_account(self, web_driver, create_user_and_delete_user):
        main_page_obj = MainPageBurger(web_driver)
        main_page_obj.wait_main_page()
        main_page_obj.click_on_button_sign_in_or_place_an_order()
        log_page_obj = LoginPageBurger(web_driver)
        log_page_obj.wait_form_login()
        log_page_obj.completion_fields_login_and_password_and_log_user(create_user_and_delete_user)
        main_page_obj.wait_main_page()
        main_page_obj.click_on_button_personal_acc()
        pers_acc_obj = PersonalAccount(web_driver)
        pers_acc_obj.wait_personal_account_page()
        pers_acc_obj.click_history_order_on_personal_account()
        assert pers_acc_obj.wait_history_order_on_personal_account()

    @allure.title('Тестирование выхода из аккаунта')
    def test_log_out_from_personal_account(self, web_driver, create_user_and_delete_user):
        main_page_obj = MainPageBurger(web_driver)
        main_page_obj.wait_main_page()
        main_page_obj.click_on_button_sign_in_or_place_an_order()
        log_page_obj = LoginPageBurger(web_driver)
        log_page_obj.wait_form_login()
        log_page_obj.completion_fields_login_and_password_and_log_user(create_user_and_delete_user)
        main_page_obj.wait_main_page()
        main_page_obj.click_on_button_personal_acc()
        pers_acc_obj = PersonalAccount(web_driver)
        pers_acc_obj.wait_personal_account_page()
        pers_acc_obj.click_log_out_on_personal_account()
        assert log_page_obj.wait_form_login()


