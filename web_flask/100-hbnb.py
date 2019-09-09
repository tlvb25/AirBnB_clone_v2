#!/usr/bin/python3
"""12. HBNB is alive!"""
from flask import Flask, escape, render_template
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.route('/hbnb')
def hbnb():
    """ A route that displays the main hbnb page """
    states = storage.all('State')
    amenities = storage.all('Amenity')
    places = storage.all('Place')
    users = storage.all('User')
    return render_template('100-hbnb.html',
                           states=states, amenities=amenities,
                           places=places, users=users)


@app.teardown_appcontext
def tear_down(self):
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
