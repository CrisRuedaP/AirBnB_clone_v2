#!/usr/bin/python3
"""starts a Flask web application"""

from models import storage
from models import State
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(Exception):
    storage.close()


if __name__ == "__main__":
    app.run()
