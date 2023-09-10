import os

from selene import have, command, be
from selene.support.shared import browser

from demoqa_tests import tests
from demoqa_tests.data.users import User


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    def fill_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value)

    def fill_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value)

    def select_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element('..').click()

    def fill_number(self, value):
        browser.element('#userNumber').should(be.blank).type(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').send_keys(month)
        browser.element('.react-datepicker__year-select').click().send_keys(year)
        browser.element(f'.react-datepicker__day--0{day}').click()

    def select_subject(self, value):
        browser.element('#subjectsInput').should(be.blank).type(value).press_enter()

    def select_hobby(self, value):
        browser.all('[for^=hobbies-checkbox]').element_by(have.exact_text(value)).click()

    def upload_picture(self, image):
        browser.element("#uploadPicture").set_value(
            os.path.abspath(
                os.path.join(os.path.dirname(tests.__file__), f'resources/{image}')
            )
        )

    def fill_address(self, street):
        browser.element('#currentAddress').should(be.blank).type(street)

    def select_state(self, name):
        browser.element('#state').perform(command.js.scroll_into_view).click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(name)).click()

    def select_city(self, name):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(name)).click()

    def submit_form(self):
        browser.element('#submit').press_enter()

    def registration(self, user: User):
        self.fill_name(user.name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.email)
        self.select_gender(user.gender)
        self.fill_number(user.number)
        self.fill_date_of_birth(user.date_of_birth_year,
                                user.date_of_birth_month,
                                user.date_of_birth_day)
        self.select_subject(user.subject)
        self.select_hobby(user.hobby)
        self.upload_picture(user.picture)
        self.fill_address(user.address)
        self.select_state(user.state)
        self.select_city(user.city)

        self.submit_form()

    def should_registration_user_with(self, user: User):
        browser.element('.table').all('td').even.should(
            have.exact_texts(f'{user.name} {user.last_name}',
                             user.email,
                             user.gender,
                             user.number,
                             f'{user.date_of_birth_day} {user.date_of_birth_month},{user.date_of_birth_year}',
                             user.subject,
                             user.hobby,
                             user.picture,
                             user.address,
                             f'{user.state} {user.city}'
                             )
        )
