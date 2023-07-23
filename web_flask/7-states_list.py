#!/usr/bin/python3
"""Python script for Airbnb flask"""

from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def all_states():
    list_states = storage.all(State).values()
    return render_template("7-states_list.html", list_states=list_states)


@app.teardown_appcontext
def close_session():
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

# Coded by EnGentech
