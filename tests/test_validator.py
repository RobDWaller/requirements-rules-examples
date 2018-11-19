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

    def test_validate(self):

        validator = Validator(
            'firstname',
            'lastname',
            'rob@test.com',
            '18/11/2018',
            'on'
        )

        result = validator.validate()

        self.assertTrue(result['result'])
