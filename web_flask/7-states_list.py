#!/usr/bin/python3
"""Python script for Airbnb flask"""

from flask import Flask
from models import storage

app = Flask(__name__)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
