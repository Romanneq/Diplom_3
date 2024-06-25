from selenium.webdriver.common.by import By


class OrderFeedElements:
    form_order_feed = [By.XPATH, ".//div[contains(@class, 'OrderFeed_orderFeed__')]"]  # локатор страницы ленты заказов
    first_ord = [By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem__')][1]"]  # локатор первого заказа на странице лента заказов
    wind_details_ord = [By.XPATH, ".//div[contains(@class, 'Modal_orderBox__1xWdi Modal_modal__contentBox__')]"]  # локатор окна с деталями заказа
    last_id_ord = [By.XPATH, ".//ul[contains(@class, 'OrderFeed_list__')]//li[1]//a/div[1]/p[1]"]  # локатор первого id заказа в ленте заказов
    comp_all_time = [By.XPATH, ".//p[text()='Выполнено за все время:']//following-sibling::p"]  # локатор счетчика выполненных заказов за всё время
    comp_today = [By.XPATH, ".//p[text()='Выполнено за сегодня:']//following-sibling::p"]  # локатор счетчика выполненных заказов за сегодня
    sect_in_progress = [By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady__')]//child::li"]  # локатор раздела: в работе
