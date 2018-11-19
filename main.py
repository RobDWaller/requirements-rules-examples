from flask import Flask, render_template, request

APP = Flask(__name__)

@APP.route('/', methods=['GET', 'POST'])
def form():

    return render_template('form.html')
