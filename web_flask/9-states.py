#!/usr/bin/python3
"""starts a Flask web application"""

from models import storage
from models.state import State
from models.city import City
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def cbs_list(id=None):
    states = storage.all('State')
    if id:
        id = '{}.{}'.format('State', id)
    return render_template('9-states.html',
                           states=states, id=id)


@app.teardown_appcontext
def teardown_db(Exception):
    storage.close()


if __name__ == "__main__":
    app.run()
