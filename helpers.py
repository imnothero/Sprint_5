from faker import Faker
import random

fake = Faker()


def get_random_email(cohort_number: int = 0):
    """Генерация уникального email."""
    return f"{fake.user_name()}_{cohort_number}@example.com"


def get_sign_up_data(cohort_number: int = 0):
    """Генерация пары email и пароль."""
    email = get_random_email(cohort_number)
    password = "Qwerty123"
    return email, password
