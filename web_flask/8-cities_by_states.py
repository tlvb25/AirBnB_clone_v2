#!/usr/bin/python3
""" Task 9 """

from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def tear_down(self):
    """ Method takes care of removal of SQLAlchemy Session """
    storage.close()


@app.route('/cities_by_states')
def show_cities_by_state():
    return render_template('8-cities_by_states.html',
                           storage=storage.all("State").values())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
