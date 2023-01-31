#!/usr/bin/env python3
"""
Module 0-app
Set up basic Flask application
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """Display Hello World message
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(debug=True)
