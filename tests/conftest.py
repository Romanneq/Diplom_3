from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import pytest
import requests
from data import URL, Endpoint
import random
import string


def get_driver():
    service = ChromeService(executable_path=ChromeDriverManager().install())
    return webdriver.Chrome(service=service)


@pytest.fixture
def web_driver():
    driver = get_driver()
    driver.maximize_window()
    driver.get(URL)
    yield driver

    driver.quit()


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

    cr = requests.post(f'{URL}{Endpoint.create_user}', data=payload)  # создание user
    yield new_user

    login_user = requests.post(f'{URL}{Endpoint.login_user}', data=payload)  # логин user
    token = login_user.json()['accessToken']  # получение accessToken
    del_user = requests.delete(f'{URL}{Endpoint.del_user}', headers={'Authorization': token})  # удаление user


