from faker import Faker
import random

def get_sign_up_data(cohort_number=1):
    fake = Faker("ru_RU")
    first_name = fake.first_name().lower()
    last_name = fake.last_name().lower()
    random_digits = ''.join([str(random.randint(0, 9)) for _ in range(3)])
    email = f"{first_name}_{last_name}_{cohort_number}_{random_digits}@yandex.ru"
    password = fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return email, password

def get_random_email(cohort_number=1):
    fake = Faker()
    first_name = fake.first_name().lower()
    last_name = fake.last_name().lower()
    random_digits = ''.join([str(random.randint(0, 9)) for _ in range(3)])
    return f"{first_name}.{last_name}{cohort_number}{random_digits}@yandex.ru"
