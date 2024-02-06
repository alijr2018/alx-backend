#!/usr/bin/env python3
"""
4-app.py
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


app = Flask(__name__)
babel = Babel(app)


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    requested_locale = request.args.get("locale")

    if requested_locale in app.config["LANGUAGES"]:
        return requested_locale

    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def index():
    return render_template('4-index.html', lang=str(get_locale()))


if __name__ == '__main__':
    app.run(debug=True)
