#!/usr/bin/python3
""" starts a Flask web app """

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ Display Hello HBNB! """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_world():
    """ Display Hello HBNB! """
    return 'Hello HBNB!'


if __name__ == '__main__':
    """ port 5000 """
    app.run(host='0.0.0.0', port=5000)
