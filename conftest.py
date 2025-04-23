import pytest
from selenium import webdriver
from data import Data
from helpers import get_sign_up_data, get_random_email  # импорт генераторов


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get(Data.STELLAR_BURGERS_URL)
    yield driver
    driver.quit()


@pytest.fixture
def random_signup_data():
    """Фикстура возвращает рандомные email и пароль."""
    return get_sign_up_data()


@pytest.fixture
def random_email():
    """Фикстура возвращает только email."""
    return get_random_email()
