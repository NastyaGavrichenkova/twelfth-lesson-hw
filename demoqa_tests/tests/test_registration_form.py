from demoqa_tests.data import users
from demoqa_tests.model.registration_page import RegistrationPage


def test_successful_registration():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.registration(users.test_user)
    registration_page.should_registration_user_with(users.test_user)
