import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data
from locators import Locators


class TestConstructor:

    def test_go_to_sauces_section(self, driver):
        """Проверка перехода к разделу «Соусы» для незалогиненного пользователя."""
        driver.get(Data.STELLAR_BURGERS_URL)

        sauces_button = WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.element_to_be_clickable(Locators.SAUCES_SECTION)
        )
        sauces_button.click()

        active_section = WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(Locators.ACTIVE_SECTION_SAUCES)
        )

        assert "Соусы" in active_section.text, "Раздел 'Соусы' не активен"

    def test_go_to_buns_section(self, driver):
        """Проверка перехода к разделу «Булки» для незалогиненного пользователя."""
        driver.get(Data.STELLAR_BURGERS_URL)

        buns_button = WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.element_to_be_clickable(Locators.BUNS_SECTION)
        )
        buns_button.click()

        active_section = WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(Locators.ACTIVE_SECTION_BUNS)
        )

        assert "Булки" in active_section.text, "Раздел 'Булки' не активен"

    def test_go_to_fillings_section(self, driver):
        """Проверка перехода к разделу «Начинки» для незалогиненного пользователя."""
        driver.get(Data.STELLAR_BURGERS_URL)

        fillings_button = WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.element_to_be_clickable(Locators.FILLINGS_SECTION)
        )
        fillings_button.click()

        active_section = WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(Locators.ACTIVE_SECTION_FILLINGS)
        )

        assert "Начинки" in active_section.text, "Раздел 'Начинки' не активен"
