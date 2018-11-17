from form.src.form_validation import FormValidation
import unittest

class TestFormValidation(unittest.TestCase):

    def test_form_validation(self):

        validation = FormValidation()

        self.assertIsInstance(validation, FormValidation)
