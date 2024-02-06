#!/usr/bin/env python3
"""
1-app.py
"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


@app.route('/')
def index():
    """
    route
    """
    return render_template('1-index.html')


class Config:
    """
    Config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel.init_app(app)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
