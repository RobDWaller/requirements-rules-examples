'''
Module validates basic form data including names, emails, date of birth
and terms and conditions.
'''
import datetime
import re

# pylint: disable=no-self-use
class FormValidation:
    '''
    Form validation class contains four methods to validate application
    form data
    '''

    def name(self, name):
        '''
        Validate a name string, contain only alphanumeric characters, numbers,
        dashes and spaces. Returns boolean.
        '''

        if re.match(r'^[a-zA-Z0-9\s\-]+$', name):
            return True

        return False

    def email(self, email):
        '''
        Validate email string, returns boolean.
        '''

        if re.match(r'^[a-zA-Z0-9\-\.]+\@[a-zA-Z0-9\-\.]+\.[a-zA-Z0-9\-\.]+$', email):
            return True

        return False

    def date_of_birth(self, dob):
        '''
        Valdiate date of birth string, must be of format dd/mm/yyyy, no less
        than 1900 and no greater than today. Returns boolean.
        '''

        if re.match(r'^[0-9]{2}/[0-9]{2}/[0-9]{4}$', dob):

            dob_object = datetime.datetime.strptime(dob, '%d/%m/%Y')

            if dob_object.date() < datetime.datetime.strptime('01/01/1900', '%d/%m/%Y').date():
                return False

            if dob_object.date() > datetime.datetime.now().date():
                return False

            return True

        return False

    def terms_conditions(self, terms_conditions):
        '''
        Simple method to check if the terms and conditions were accepted.
        Returns boolean.
        '''

        return terms_conditions == 'on'
