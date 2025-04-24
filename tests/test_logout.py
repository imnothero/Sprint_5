import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data
from locators import Locators


class TestPersonalAccount:

    def test_go_to_personal_account(self, go_to_account, driver):
        """Переход в ЛК по клику на кнопку 'Личный кабинет'."""
        assert driver.current_url == Data.STELLAR_BURGERS_URL + "account/profile"

    def test_go_to_constructor_from_personal_account(self, go_to_account, driver):
        """Переход в конструктор из ЛК по кнопке 'Конструктор'."""
        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON)
        ).click()

        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.url_to_be(Data.STELLAR_BURGERS_URL)
        )

        assert driver.current_url == Data.STELLAR_BURGERS_URL

    def test_go_to_constructor_via_logo(self, go_to_account, driver):
        """Переход в конструктор из ЛК по логотипу Stellar Burgers."""
        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.element_to_be_clickable(Locators.LOGO_BUTTON)
        ).click()

        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.url_to_be(Data.STELLAR_BURGERS_URL)
        )

        assert driver.current_url == Data.STELLAR_BURGERS_URL

    def test_logout(self, go_to_account, driver):
        """Выход из аккаунта по кнопке 'Выйти' в ЛК."""
        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.element_to_be_clickable(Locators.LOGOUT_BUTTON)
        ).click()

        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.url_to_be(Data.STELLAR_BURGERS_URL + "login")
        )

        assert driver.current_url == Data.STELLAR_BURGERS_URL + "login"
