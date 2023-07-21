#!/usr/bin/python3
"""Creating my first flask file"""

from flask import Flask

# creating an instance of Flask
app = Flask(__name__)

@app.route("/", strict_slashes=False)
def home():
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def value(text):
    return "C {}".format(text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

