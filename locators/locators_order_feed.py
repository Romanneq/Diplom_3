from selenium.webdriver.common.by import By


class OrderFeedElements:
    FORM_ORDER_FEED = [By.XPATH, ".//div[contains(@class, 'OrderFeed_orderFeed__')]"]  # локатор страницы ленты заказов
    FIRST_ORD = [By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem__')][1]"]  # локатор первого заказа на странице лента заказов
    WIND_DETAILS_ORD = [By.XPATH, ".//div[contains(@class, 'Modal_orderBox__')]"]  # локатор окна с деталями заказа
    LAST_ID_ORD = [By.XPATH, ".//ul[contains(@class, 'OrderFeed_list__')]//li[1]//a/div[1]/p[1]"]  # локатор первого id заказа в ленте заказов
    COMP_ALL_TIME = [By.XPATH, ".//p[text()='Выполнено за все время:']//following-sibling::p"]  # локатор счетчика выполненных заказов за всё время
    COMP_TODAY = [By.XPATH, ".//p[text()='Выполнено за сегодня:']//following-sibling::p"]  # локатор счетчика выполненных заказов за сегодня
    SECT_IN_PROGRESS = [By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady__')]//child::li"]  # локатор раздела: в работе
