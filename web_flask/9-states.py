#!/usr/bin/python3
""" Task 9 """

from flask import Flask, render_template
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def tear_down(self):
    storage.close()


@app.route('/states')
def show_OnlyStates():
    records = storage.all("State").values()
    return render_template('7-states_list.html', records=records)


@app.route('/states/<id>')
def show_cities_of_state(id):
    records = storage.all('State')
    return render_template('9-states.html', id=id, records=records)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
