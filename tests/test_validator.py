import unittest
from form.src.validator import Validator

class TestValidator(unittest.TestCase):

    def test_validator(self):

        validator = Validator(
            'firstname',
            'lastname',
            'email',
            'dob',
            'on'
        )

        self.assertIsInstance(validator, Validator)
