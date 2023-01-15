#!/usr/bin/python3
"""..."""

from flask import Flask
from models import storage
from flask import render_template
app = Flask(__name__)


@app.route('/states')
@app.route('/states/<id>')
def states(id=None):
    """..."""
    from models.state import State
    states = storage.all(State)
    return render_template('9-states.html', states=states, id=id)


@app.teardown_appcontext
def teardown(arg=None):
    storage.close()

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
