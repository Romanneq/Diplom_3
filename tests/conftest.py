from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.service import Service as FirefoxService
import pytest
import requests
from data import URL, Endpoint
import random
import string
from pages.main_page import MainPageBurger
from pages.login_page import LoginPageBurger
from pages.order_feed_page import OrderFeed
from pages.password_recovery_page import PasswordRecoveryPage
from pages.personal_account_page import PersonalAccount


def get_driver(name):
    if name == 'Chrome':
        service = ChromeService(executable_path=ChromeDriverManager().install())
        return webdriver.Chrome(service=service)
    elif name == 'Firefox':
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        return webdriver.Firefox(service=service)
    else:
        raise TypeError('Driver is not found')


@pytest.fixture(params=['Chrome', 'Firefox'])
def web_driver(request):
    driver = get_driver(request.param)
    driver.maximize_window()
    driver.get(URL)
    yield driver

    driver.quit()


@pytest.fixture(scope='function')
def instance_main_page(web_driver):
    main_page_obj = MainPageBurger(web_driver)
    return main_page_obj


@pytest.fixture(scope='function')
def instance_order_feed_page(web_driver):
    order_feed = OrderFeed(web_driver)
    return order_feed


@pytest.fixture(scope='function')
def instance_login_page(web_driver):
    log_page_obj = LoginPageBurger(web_driver)
    return log_page_obj


@pytest.fixture(scope='function')
def instance_pass_rec_page(web_driver):
    pas_rec_obj = PasswordRecoveryPage(web_driver)
    return pas_rec_obj


@pytest.fixture(scope='function')
def instance_per_acc_page(web_driver):
    pers_acc_obj = PersonalAccount(web_driver)
    return pers_acc_obj


@pytest.fixture
def create_user_and_delete_user():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # создаём список, чтобы метод мог его вернуть
    new_user = []

    # генерируем имя, почту и логин пользователя
    name = generate_random_string(5)
    email = f'{generate_random_string(5)}@yandex.ru'
    password = generate_random_string(5)

    new_user.append(name)
    new_user.append(email)
    new_user.append(password)

    # собираем тело запроса
    payload = {
        "name": name,
        "email": email,
        "password": password
    }

    cr = requests.post(f'{URL}{Endpoint.CREATE_USER}', data=payload)  # создание user
    yield new_user

    login_user = requests.post(f'{URL}{Endpoint.LOGIN_USER}', data=payload)  # логин user
    token = login_user.json()['accessToken']  # получение accessToken
    del_user = requests.delete(f'{URL}{Endpoint.DEL_USER}', headers={'Authorization': token})  # удаление user
