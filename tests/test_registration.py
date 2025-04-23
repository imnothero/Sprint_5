import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from data import Data
from locators import Locators
from helpers import get_sign_up_data, get_random_email


class TestRegistration:

    def fill_registration_form(self, driver: WebDriver, name: str, email: str, password: str):
        """Заполнение формы регистрации."""
        name_field = WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(Locators.REGISTER_NAME_FIELD)
        )
        name_field.send_keys(name)

        email_field = WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(Locators.REGISTER_EMAIL_FIELD)
        )
        email_field.send_keys(email)

        password_field = WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(Locators.REGISTER_PASSWORD_FIELD)
        )
        password_field.send_keys(password)

        register_button = WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.element_to_be_clickable(Locators.REGISTER_BUTTON)
        )
        register_button.click()

    def test_successful_registration(self, driver: WebDriver):
        """Успешная регистрация нового пользователя."""
        driver.get(Data.STELLAR_BURGERS_URL + "register")

        email = get_random_email(cohort_number=19)
        password = Data.REGISTRATION_PASSWORD_VALID

        self.fill_registration_form(driver, Data.REGISTRATION_NAME, email, password)

        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.url_to_be(Data.STELLAR_BURGERS_URL + "login")
        )

        assert driver.current_url == Data.STELLAR_BURGERS_URL + "login"

    def test_invalid_password_registration(self, driver: WebDriver):
        """Ошибка при коротком пароле."""
        driver.get(Data.STELLAR_BURGERS_URL + "register")

        email, _ = get_sign_up_data(cohort_number=19)

        self.fill_registration_form(driver, Data.REGISTRATION_NAME, email, Data.REGISTRATION_PASSWORD_INVALID)

        error_message = WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(Locators.PASSWORD_ERROR_MESSAGE)
        )

        assert error_message.is_displayed(), "Ошибка при коротком пароле не отображается"
