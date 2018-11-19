'''
Wrapper for the FormValidation class
'''
from .form_validation import FormValidation

# pylint: disable=too-few-public-methods
class Validator:
    '''
    Simple class which validates a forms input. Contains one method validate.
    '''

    # pylint: disable=too-many-arguments
    def __init__(self, first_name, last_name, email, date_of_birth, terms_conditions):
        '''
        Accepts and sets first name string, last name string, email string,
        date of birth string, and terms and conditions string.
        '''

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.date_of_birth = date_of_birth
        self.terms_conditions = terms_conditions

    def validate(self):
        '''
        Method that validates all the inputted fields using the form validation
        class. Returns a dictionary containing boolean result and list of
        validation error messages.
        '''

        form_validation = FormValidation()

        result = {'result': True, 'messages': []}

        if form_validation.name(self.first_name) is False:
            result['result'] = False
            result['messages'].append('''
                Please fill in a valid first name only alpha numeric characters,
                spaces and dashes allowed.
            ''')

        if form_validation.name(self.last_name) is False:
            result['result'] = False
            result['messages'].append('''
                Please fill in a valid last name only alpha numeric characters,
                spaces and dashes allowed.
            ''')

        if form_validation.email(self.email) is False:
            result['result'] = False
            result['messages'].append('Please fill in a valid email.')

        if form_validation.date_of_birth(self.date_of_birth) is False:
            result['result'] = False
            result['messages'].append('''
                Please fill in a valid date of birth, format day/month/year,
                after 1900 and before or equal to today.
            ''')

        if form_validation.terms_conditions(self.terms_conditions) is False:
            result['result'] = False
            result['messages'].append('''
                Please agree to our terms and conditions and privacy policy.
            ''')

        return result
