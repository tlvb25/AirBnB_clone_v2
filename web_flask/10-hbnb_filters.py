#!/usr/bin/python3
""" Task 9 """

from flask import Flask, abort, render_template
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb_filters')
def hbnb_filters():
    states = storage.all('State')
    amenities = storage.all('Amenity')
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


@app.teardown_appcontext
def do_teardown(self):
    """Closes session"""
    storage.close()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
