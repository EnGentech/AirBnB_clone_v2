#!/usr/bin/python3
"""My first flask script"""

from flask import Flask
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
