#!/usr/bin/env python3
"""
3-app.py
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)


@app.route('/')
def index() -> str:
    """
    route
    """
    return render_template('3-index.html')


class Config:
    """
    Config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    Use request.accept_languages to determine the best,
    match with our supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(debug=True)
