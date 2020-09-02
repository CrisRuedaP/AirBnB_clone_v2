#!/usr/bin/python3
"""starts a Flask web application"""

from models import storage
from models.state import State
from models.city import City
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cbs_list():
    states = storage.all('State')
    cities = storage.all('City')
    return render_template('8-cities_by_states.html',
                           states=states, cities=cities)


@app.teardown_appcontext
def teardown_db(Exception):
    storage.close()


if __name__ == "__main__":
    app.run()
