import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data
from locators import Locators
from helpers import get_sign_up_data, get_random_email


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get(Data.STELLAR_BURGERS_URL)
    yield driver
    driver.quit()


@pytest.fixture
def login_user(driver):
    """Фикстура авторизует пользователя."""
    driver.get(Data.STELLAR_BURGERS_URL + "login")

    WebDriverWait(driver, Data.WAIT_TIME).until(
        EC.visibility_of_element_located(Locators.EMAIL_FIELD)
    ).send_keys(Data.AUTH_EMAIL)

    WebDriverWait(driver, Data.WAIT_TIME).until(
        EC.visibility_of_element_located(Locators.PASSWORD_FIELD)
    ).send_keys(Data.AUTH_PASSWORD)

    WebDriverWait(driver, Data.WAIT_TIME).until(
        EC.element_to_be_clickable(Locators.ENTER_BUTTON)
    ).click()

    WebDriverWait(driver, Data.WAIT_TIME).until(
        EC.url_to_be(Data.STELLAR_BURGERS_URL)
    )


@pytest.fixture
def go_to_account(driver, login_user):
    """Фикстура переходит в ЛК после авторизации."""
    WebDriverWait(driver, Data.WAIT_TIME).until(
        EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT)
    ).click()

    WebDriverWait(driver, Data.WAIT_TIME).until(
        EC.url_to_be(Data.STELLAR_BURGERS_URL + "account/profile")
    )
