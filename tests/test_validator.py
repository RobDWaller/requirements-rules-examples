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
        self.assertEqual(len(result['messages']), 0)

    def test_validate_invalid_firstname(self):

        validator = Validator(
            'firstname!',
            'lastname',
            'rob@test.com',
            '18/11/2018',
            'on'
        )

        result = validator.validate()

        self.assertFalse(result['result'])
        self.assertEqual(result['messages'][0], 'Please fill in a valid first name only alpha numeric characters, spaces and dashes allowed.')
        self.assertEqual(len(result['messages']), 1)

    def test_validate_invalid_lastname(self):

        validator = Validator(
            'firstname',
            'lastname!',
            'rob@test.com',
            '18/11/2018',
            'on'
        )

        result = validator.validate()

        self.assertFalse(result['result'])
        self.assertEqual(result['messages'][0], 'Please fill in a valid last name only alpha numeric characters, spaces and dashes allowed.')
        self.assertEqual(len(result['messages']), 1)

    def test_validate_invalid_email(self):

        validator = Validator(
            'firstname',
            'lastname',
            'robtest.com',
            '18/11/2018',
            'on'
        )

        result = validator.validate()

        self.assertFalse(result['result'])
        self.assertEqual(result['messages'][0], 'Please fill in a valid email.')
        self.assertEqual(len(result['messages']), 1)

    def test_validate_invalid_dob(self):

        validator = Validator(
            'firstname',
            'lastname',
            'rob@test.com',
            '2018/11/18',
            'on'
        )

        result = validator.validate()

        self.assertFalse(result['result'])
        self.assertEqual(result['messages'][0], 'Please fill in a valid date of birth, format day/month/year, after 1900 and before or equal to today.')
        self.assertEqual(len(result['messages']), 1)

    def test_validate_invalid_tscs(self):

        validator = Validator(
            'firstname',
            'lastname',
            'rob@test.com',
            '18/11/2018',
            ''
        )

        result = validator.validate()

        self.assertFalse(result['result'])
        self.assertEqual(result['messages'][0], 'Please agree to our terms and conditions and privacy policy.')
        self.assertEqual(len(result['messages']), 1)

    def test_validate_invalid_multiple(self):

        validator = Validator(
            'firstname',
            'lastname!',
            'robest.com',
            '18/11/2018',
            ''
        )

        result = validator.validate()

        self.assertFalse(result['result'])
        self.assertEqual(result['messages'][0], 'Please fill in a valid last name only alpha numeric characters, spaces and dashes allowed.')
        self.assertEqual(result['messages'][1], 'Please fill in a valid email.')
        self.assertEqual(result['messages'][2], 'Please agree to our terms and conditions and privacy policy.')
        self.assertEqual(len(result['messages']), 3)
