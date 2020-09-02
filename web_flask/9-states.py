#!/usr/bin/python3
""" starts a Flask web app """

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    st = storage.all(State).values()
    return render_template('7-states_list.html', states=st)


@app.route('/cities_by_states', strict_slashes=False)
def list_cities_states():
    st = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=st)


@app.route('/states', strict_slashes=False)
def states():
    st = storage.all(State).values()
    return render_template('7-states_list.html', states=st)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    flag = 0
    st = None
    all_states = storage.all(State).values()
    for state in all_states:
        if id in state.id:
            flag = 1
            st = state
            break
    return render_template('9-states.html', states=st, flag=flag)


@app.teardown_appcontext
def close_db(db):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
