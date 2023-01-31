#!/usr/bin/env python3
"""
Module 1-app
Set up basic Flask application
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    A class that represent available languages in our app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/")
def index():
    """Display Hello World message
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(debug=True)
