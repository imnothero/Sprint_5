import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data
from locators import Locators


def login(driver, email=Data.AUTH_EMAIL, password=Data.AUTH_PASSWORD):
    """Вспомогательный метод для входа в аккаунт."""
    driver.get(Data.STELLAR_BURGERS_URL + "login")

    email_field = WebDriverWait(driver, Data.WAIT_TIME).until(
        EC.visibility_of_element_located(Locators.EMAIL_FIELD)
    )
    email_field.send_keys(email)

    password_field = WebDriverWait(driver, Data.WAIT_TIME).until(
        EC.visibility_of_element_located(Locators.PASSWORD_FIELD)
    )
    password_field.send_keys(password)

    enter_button = WebDriverWait(driver, Data.WAIT_TIME).until(
        EC.element_to_be_clickable(Locators.ENTER_BUTTON)
    )
    enter_button.click()

    WebDriverWait(driver, Data.WAIT_TIME).until(
        EC.url_to_be(Data.STELLAR_BURGERS_URL)
    )


def go_to_personal_account(driver):
    """Вспомогательный метод для перехода в ЛК."""
    personal_account_button = WebDriverWait(driver, Data.WAIT_TIME).until(
        EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT)
    )
    personal_account_button.click()

    WebDriverWait(driver, Data.WAIT_TIME).until(
        EC.url_to_be(Data.STELLAR_BURGERS_URL + "account/profile")
    )


class TestPersonalAccount:

    def test_go_to_personal_account(self, driver):
        """Переход в ЛК по клику на кнопку 'Личный кабинет'."""
        login(driver)
        go_to_personal_account(driver)

        assert driver.current_url == Data.STELLAR_BURGERS_URL + "account/profile"

    def test_go_to_constructor_from_personal_account(self, driver):
        """Переход в конструктор из ЛК по кнопке 'Конструктор'."""
        login(driver)
        go_to_personal_account(driver)

        constructor_button = WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON)
        )
        constructor_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.url_to_be(Data.STELLAR_BURGERS_URL)
        )

        assert driver.current_url == Data.STELLAR_BURGERS_URL

    def test_go_to_constructor_via_logo(self, driver):
        """Переход в конструктор из ЛК по логотипу Stellar Burgers."""
        login(driver)
        go_to_personal_account(driver)

        logo_button = WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.element_to_be_clickable(Locators.LOGO_BUTTON)
        )
        logo_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.url_to_be(Data.STELLAR_BURGERS_URL)
        )

        assert driver.current_url == Data.STELLAR_BURGERS_URL

    def test_logout(self, driver):
        """Выход из аккаунта по кнопке 'Выйти' в ЛК."""
        login(driver)
        go_to_personal_account(driver)

        logout_button = WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.element_to_be_clickable(Locators.LOGOUT_BUTTON)
        )
        logout_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.url_to_be(Data.STELLAR_BURGERS_URL + "login")
        )

        assert driver.current_url == Data.STELLAR_BURGERS_URL + "login"
