#!/usr/bin/python3
""" Task 9 """

from flask import Flask, abort, render_template
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb_filters')
def hbnb_filters():
    """Filters Section"""
    stateRec = storage.all('State')
    amenityRec = storage.all('Amenity')
    return render_template('10-hbnb_filters.html', states=stateRec, amenities=amenityRec)


@app.teardown_appcontext
def do_teardown(self):
    """Closes session"""
    storage.close()
