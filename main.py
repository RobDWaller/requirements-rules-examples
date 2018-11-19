'''
Form application main route module, acts like the controller
'''
from flask import Flask, render_template, request
from form.src.validator import Validator

APP = Flask(__name__)

@APP.route('/', methods=['GET', 'POST'])
def form():
    '''
    Loads the form template or the success template. If post request data is
    validated if successful the success template is rendered if not the
    request data is returned to the form template. If get request the form
    template is rendered.
    '''
    if request.method == 'POST':

        validator = Validator(
            request.form.get('firstname', ''),
            request.form.get('lastname', ''),
            request.form.get('email', ''),
            request.form.get('dob', ''),
            request.form.get('tac', '')
        )

        result = validator.validate()

        if result['result'] is False:
            data = {'form': request.form, 'messages': result['messages']}
            return render_template('form.html', data=data)

        data = {'form': request.form}
        return render_template('success.html', data=data)

    data = {'form': '', 'messages': ''}
    return render_template('form.html', data=data)
