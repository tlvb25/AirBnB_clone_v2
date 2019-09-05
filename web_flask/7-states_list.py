#!/usr/bin/python3
"""Odd or even?"""
from flask import Flask, abort, render_template
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_betty():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello_hbnb():
    return 'HBNB'


@app.route('/c/<text>')
def c_isFun(text):
    text = 'C ' + text.replace('_', ' ')
    return text


@app.route('/python/<text>')
@app.route('/python')
def python_isFun(text='is cool'):
    text = 'Python {}'.format(text.replace('_', ' '))
    return text


@app.route('/number/<int:n>')
def check_ifNum(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def num_template(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def oddEven_template(n):
    return render_template('6-number_odd_or_even.html', n=n)


@app.route('/states_list')
def run_all_states():
    records = storage.all('State')
    return render_template('7-states_list.html', storage=records)


@app.teardown_appcontext
def run_teardown(self):
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
