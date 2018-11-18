import datetime
import re

class FormValidation:

    def name(self, name):

        if re.match('^[a-zA-Z0-9\s\-]+$', name):
            return True

        return False

    def email(self, email):

        if re.match('^[a-zA-Z0-9\-\.]+\@[a-zA-Z0-9\-\.]+\.[a-zA-Z0-9\-\.]+$', email):
            return True

        return False

    def date_of_birth(self, dob):

        if re.match('^[0-9]{2}/[0-9]{2}/[0-9]{4}$', dob):

            dob_object = datetime.datetime.strptime(dob, '%d/%m/%Y')

            if dob_object.date() < datetime.datetime.strptime('01/01/1900', '%d/%m/%Y').date():
                return False

            if dob_object.date() > datetime.datetime.now().date():
                return False

            return True

        return False
