import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data
from locators import Locators


class TestLogin:

    def test_login_via_main_page(self, driver):
        """Вход через кнопку 'Войти в аккаунт' на главной странице."""
        driver.get(Data.STELLAR_BURGERS_URL)

        login_button = WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.element_to_be_clickable(Locators.LOGIN_BUTTON)
        )
        login_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.url_to_be(Data.STELLAR_BURGERS_URL + "login")
        )

        email_field = WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(Locators.EMAIL_FIELD)
        )
        email_field.send_keys(Data.AUTH_EMAIL)

        password_field = WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(Locators.PASSWORD_FIELD)
        )
        password_field.send_keys(Data.AUTH_PASSWORD)

        enter_button = WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.element_to_be_clickable(Locators.ENTER_BUTTON)
        )
        enter_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.url_to_be(Data.STELLAR_BURGERS_URL)
        )

        assert driver.current_url == Data.STELLAR_BURGERS_URL

    def test_login_via_personal_account_button(self, driver):
        """Вход через кнопку 'Личный кабинет' на главной странице."""
        driver.get(Data.STELLAR_BURGERS_URL)

        personal_account_button = WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT)
        )
        personal_account_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.url_to_be(Data.STELLAR_BURGERS_URL + "login")
        )

        email_field = WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(Locators.EMAIL_FIELD)
        )
        email_field.send_keys(Data.AUTH_EMAIL)

        password_field = WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(Locators.PASSWORD_FIELD)
        )
        password_field.send_keys(Data.AUTH_PASSWORD)

        enter_button = WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.element_to_be_clickable(Locators.ENTER_BUTTON)
        )
        enter_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.url_to_be(Data.STELLAR_BURGERS_URL)
        )

        assert driver.current_url == Data.STELLAR_BURGERS_URL

    def test_login_via_registration_form(self, driver):
        """Вход через кнопку 'Войти' в форме регистрации."""
        driver.get(Data.STELLAR_BURGERS_URL + "register")

        login_link = WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.element_to_be_clickable(Locators.LOGIN_LINK)
        )
        login_link.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.url_to_be(Data.STELLAR_BURGERS_URL + "login")
        )

        email_field = WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(Locators.EMAIL_FIELD)
        )
        email_field.send_keys(Data.AUTH_EMAIL)

        password_field = WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(Locators.PASSWORD_FIELD)
        )
        password_field.send_keys(Data.AUTH_PASSWORD)

        enter_button = WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.element_to_be_clickable(Locators.ENTER_BUTTON)
        )
        enter_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.url_to_be(Data.STELLAR_BURGERS_URL)
        )

        assert driver.current_url == Data.STELLAR_BURGERS_URL

    def test_login_via_password_recovery_form(self, driver):
        """Вход через кнопку 'Войти' в форме восстановления пароля."""
        driver.get(Data.STELLAR_BURGERS_URL + "forgot-password")

        login_link = WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.element_to_be_clickable(Locators.LOGIN_LINK)
        )
        login_link.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.url_to_be(Data.STELLAR_BURGERS_URL + "login")
        )

        email_field = WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(Locators.EMAIL_FIELD)
        )
        email_field.send_keys(Data.AUTH_EMAIL)

        password_field = WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(Locators.PASSWORD_FIELD)
        )
        password_field.send_keys(Data.AUTH_PASSWORD)

        enter_button = WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.element_to_be_clickable(Locators.ENTER_BUTTON)
        )
        enter_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.url_to_be(Data.STELLAR_BURGERS_URL)
        )

        assert driver.current_url == Data.STELLAR_BURGERS_URL
