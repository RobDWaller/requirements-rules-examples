from form.src.form_validation import FormValidation
import unittest

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
