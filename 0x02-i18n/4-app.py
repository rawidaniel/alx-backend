#!/usr/bin/env python3
"""
Module 2-app
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


@babel.localeselector
def get_locale():
    """select a language translation to use for the request
    """
    loc = request.args.get("locale")
    if loc in app.config['LANGUAGES']:
        return loc
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index() -> str:
    """Display Hello World message
    """
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run(debug=True)
