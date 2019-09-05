#!/usr/bin/python3
""" 3. Python is cool! """
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_betty():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello_hbnb():
    return 'HBNB'

@app.route('/c/<text>')
def c_isfun(text):
    text = 'C ' + text.replace('_', ' ')
    return text

@app.route('/python/(<text>)')
@app.route('/python')
def python_isCool(text='is cool'):
    text = 'Python {}'.format(text.replace('_', ' '))
    return text

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
