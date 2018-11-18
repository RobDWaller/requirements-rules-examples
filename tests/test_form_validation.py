import unittest
from datetime import timedelta, date
from form.src.form_validation import FormValidation

class TestFormValidation(unittest.TestCase):

    def test_form_validation(self):

        validation = FormValidation()

        self.assertIsInstance(validation, FormValidation)

    def test_name_empty(self):

        validation = FormValidation()

        self.assertFalse(validation.name(''))

    def test_name_filled(self):

        validation = FormValidation()

        self.assertTrue(validation.name('James'))

    def test_name_filled_two(self):

        validation = FormValidation()

        self.assertTrue(validation.name('James Christopher'))

    def test_name_filled_three(self):

        validation = FormValidation()

        self.assertTrue(validation.name('James-Christopher'))

    def test_name_filled_four(self):

        validation = FormValidation()

        self.assertTrue(validation.name('James-Christopher 3'))

    def test_name_invalid(self):

        validation = FormValidation()

        self.assertFalse(validation.name('James!!'))

    def test_last_name_filled(self):

        validation = FormValidation()

        self.assertTrue(validation.name('Johnson'))

    def test_last_name_filled_two(self):

        validation = FormValidation()

        self.assertTrue(validation.name('Jo Johnson'))

    def test_last_name_filled_three(self):

        validation = FormValidation()

        self.assertTrue(validation.name('Jo-Johnson'))

    def test_last_name_filled_four(self):

        validation = FormValidation()

        self.assertTrue(validation.name('Johnson 3rd'))

    def test_last_name_invalid(self):

        validation = FormValidation()

        self.assertFalse(validation.name('Johnson$'))

    def test_email_fail(self):

        validation = FormValidation()

        self.assertFalse(validation.email(''))

    def test_email_filled(self):

        validation = FormValidation()

        self.assertTrue(validation.email('jessica.smith@gmail.com'))

    def test_email_filled_two(self):

        validation = FormValidation()

        self.assertTrue(validation.email('jessica@myemail.co.uk'))

    def test_email_filled_three(self):

        validation = FormValidation()

        self.assertTrue(validation.email('jessica123@big-email.co'))

    def test_email_invalid(self):

        validation = FormValidation()

        self.assertFalse(validation.email('jessica.smith.outlook.com'))

    def test_email_invalid_two(self):

        validation = FormValidation()

        self.assertFalse(validation.email('jessica@outlook'))

    def test_email_invalid_three(self):

        validation = FormValidation()

        self.assertFalse(validation.email('jessica@out look.com'))

    def test_date_of_birth(self):

        validation = FormValidation()

        self.assertTrue(validation.date_of_birth('24/05/1995'))

    def test_date_of_birth_invalid(self):

        validation = FormValidation()

        self.assertFalse(validation.date_of_birth('1995/05/24'))

    def test_date_of_birth_invalid_two(self):

        validation = FormValidation()

        self.assertFalse(validation.date_of_birth('24-5-1995'))

    def test_date_of_birth_invalid_three(self):

        validation = FormValidation()

        self.assertFalse(validation.date_of_birth('24/5/1995'))

    def test_date_of_birth_low_range(self):

        validation = FormValidation()

        self.assertFalse(validation.date_of_birth('31/12/1899'))

    def test_date_of_birth_high_range(self):

        validation = FormValidation()

        date_string = date.today() + timedelta(days=1)

        self.assertFalse(validation.date_of_birth(date_string.strftime('%d/%m/%Y')))
