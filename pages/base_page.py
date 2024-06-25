import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from seletools.actions import drag_and_drop


class BasePage:  # создали класс базовых методов selenium
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Метод получения текста элемента')
    def base_text_element(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Метод явного ожидания отображения элемента')
    def wait_element_page(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_all_elements_located(locator))

    @allure.step('Метод обратного ожидания(отсутствия элемента). Используется для отображения id заказа')
    def re_wait_element_page(self, locator, text):
        return WebDriverWait(self.driver, 10).until_not(expected_conditions.text_to_be_present_in_element(locator, text))

    @allure.step('Метод клика "ActionChains" по элементу страницы')
    def click_element_page(self, locator):
        element = BasePage.wait_element_page(self, locator)
        ActionChains(self.driver).move_to_element(*element).click().perform()

    @allure.step('Метод клика "ExecuteScript" по элементу. Используется для клика по кнопке "Вход" в форме входа user')
    def click_execute_element_page(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Метод ввода текста в поле элемента страницы')
    def send_keys_element(self, locator, text):
        return self.driver.find_element(*locator).send_keys(text)

    @allure.step('Метод перетаскивания ингредиента в заказ')
    def dragging_an_ingredient(self, locator_source, locator_target):
        source = self.driver.find_element(*locator_source)
        target = self.driver.find_element(*locator_target)
        drag_and_drop(self.driver, source, target)
