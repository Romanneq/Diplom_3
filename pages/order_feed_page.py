import allure
from pages.base_page import BasePage
from locators.locators_order_feed import OrderFeedElements


class OrderFeed(BasePage):  # Создали класс ленты заказов

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Метод отображения ленты заказов')
    def wait_order_feed_page(self):
        return BasePage.wait_element_page(self, OrderFeedElements.form_order_feed)

    @allure.step('Метод отображения id заказа в разделе: в работе')
    def re_wait_id_order_in_order_feed_page(self):
        return BasePage.re_wait_element_page(self, OrderFeedElements.sect_in_progress, 'Все текущие заказы готовы!')

    @allure.step('Метод клика на первый заказ в ленте заказов')
    def click_first_order_on_order_feed_page(self):
        return BasePage.click_element_page(self, OrderFeedElements.first_ord)

    @allure.step('Метод отображения окна с деталями заказа')
    def wait_window_with_details_order_on_order_feed_page(self):
        return BasePage.wait_element_page(self, OrderFeedElements.wind_details_ord)

    @allure.step('Метод возврата id заказа в ленте заказов')
    def return_id_order_in_order_feed_page(self):
        return BasePage.base_text_element(self, OrderFeedElements.last_id_ord)

    @allure.step('Метод возврата счетчика заказов за все время')
    def return_counter_orders_all_time_in_order_feed_page(self):
        return BasePage.base_text_element(self, OrderFeedElements.comp_all_time)

    @allure.step('Метод возврата счетчика заказов за сегодня')
    def return_counter_orders_today_in_order_feed_page(self):
        return BasePage.base_text_element(self, OrderFeedElements.comp_today)

    @allure.step('Метод возврата номера заказа в разделе в работе')
    def return_id_order_section_in_progress_in_order_feed_page(self):
        return BasePage.base_text_element(self, OrderFeedElements.sect_in_progress)


