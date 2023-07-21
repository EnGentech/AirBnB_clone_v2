#!/usr/bin/python3
"""My first flask script"""

from flask import Flask, redirect, url_for
import re
pattern = re.compile("_")

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>")
def name(text):
    new = pattern.sub(" ", text)
    return "C {}".format(new)


@app.route("/python", strict_slashes=False)
def python():
    return "Python is cool"


@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    if text == "is cool":
        return redirect(url_for("python"))
    else:
        new = pattern.sub(" ", text)
        return "Python {}".format(new)


@app.route("/number/<n>", strict_slashes=False)
def number(n):
    n = int(n)
    val = isinstance(n, int)
    if val:
        return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
