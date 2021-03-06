#!/usr/bin/python3
""" starts a Flask web app """

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ Display Hello HBNB! """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """ Display HBNB """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is(text):
    """ display C + <text>.replace('_', ' ') """
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>/', strict_slashes=False)
def python(text="is cool"):
    """ display Python  + <text>.replace('_', ' ') """
    return 'Python {}'.format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    return "{} is a number".format(n)


if __name__ == '__main__':
    """ port 5000 """
    app.run(host='0.0.0.0', port=5000)
