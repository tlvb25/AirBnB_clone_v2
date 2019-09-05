#!/usr/bin/python3
""" List of states """

from flask import Flask
from flask import render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def tear_down(self):
    """ Method takes care of removal of SQLAlchemy Session """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def list_states():
    return render_template('7-states_list.html',
                           storage=storage.all("State").values())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
