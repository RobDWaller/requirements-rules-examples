import re

class FormValidation:

    def name(self, name):

        if re.match('^[a-zA-Z0-9\s\-]+$', name):
            return True

        return False

    def email(self, email):

        return email
