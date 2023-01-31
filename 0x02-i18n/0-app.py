#!/usr/bin/env python3
"""
Module 0-app
Set up basic Flask application
"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = "en"
app.config['BABEL_DEFAULT_TIMEZONE'] = "UTC"
babel = Babel(app)


class config:
    """
    A class that represent available languages in our app
    """
    LANGUAGES = ["en", "fr"]


@app.route("/")
def index():
    """Display Hello World message
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(debug=True)
