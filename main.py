from flask import Flask, render_template, request

APP = Flask(__name__)

@APP.route('/', methods=['GET', 'POST'])
def form():

    if request.method == 'POST':
        return render_template('form.html', form = request.form)

    return render_template('form.html')
