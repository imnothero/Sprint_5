import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from data import Data
from locators import Locators
from helpers import get_sign_up_data

class TestRegistration:

    def fill_registration_form(self, driver: WebDriver, name: str, email: str, password: str):  # заполнение формы регистрации
        # ожидание и ввод имени
        name_field = WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(Locators.REGISTER_NAME_FIELD)
        )
        name_field.send_keys(name)

        # ожидание и ввод email
        email_field = WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(Locators.REGISTER_EMAIL_FIELD)
        )
        email_field.send_keys(email)

        # ожидание и ввод пароля
        password_field = WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(Locators.REGISTER_PASSWORD_FIELD)
        )
        password_field.send_keys(password)

        # клик по кнопке "Зарегистрироваться"
        register_button = WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.element_to_be_clickable(Locators.REGISTER_BUTTON)
        )
        register_button.click()

    def test_successful_registration(self, driver: WebDriver):  # успешная регистрация нового пользователя
        driver.get(Data.STELLAR_BURGERS_URL + "register")

        # генерация уникальных email и пароля
        from helpers import get_random_email

        email = get_random_email(cohort_number=19)
        password = "Qwerty123"

        # заполнение формы регистрации
        self.fill_registration_form(driver, "Nikita Melekhin", email, password)

        # ожидание перехода на страницу логина
        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.url_to_be(Data.STELLAR_BURGERS_URL + "login")
        )

        # проверка, что редирект успешен
        assert driver.current_url == Data.STELLAR_BURGERS_URL + "login"

    def test_invalid_password_registration(self, driver: WebDriver):  # ошибка при коротком пароле
        driver.get(Data.STELLAR_BURGERS_URL + "register")

        # генерация уникального email
        email, _ = get_sign_up_data(cohort_number=19)

        # заполнение формы регистрации с некорректным паролем
        self.fill_registration_form(driver, "Nikita Melekhin", email, "12345")

        # ожидание появления сообщения об ошибке
        error_message = WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(Locators.PASSWORD_ERROR_MESSAGE)
        )

        # проверка отображения сообщения об ошибке
        assert error_message.is_displayed(), "Ошибка при коротком пароле не отображается"
