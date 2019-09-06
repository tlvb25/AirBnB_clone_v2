#!/usr/bin/python3
"""12. HBNB is alive!"""
from flask import Flask, abort, render_template
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb')
def show_cityState():
    stateRec = storage.all('State')
    amenRec = storage.all('Amenity')
    return render_template('100-hbnb.html', states=stateRec, amenities=amenRec)


@app.teardown_appcontext
def tear_down(self):
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
