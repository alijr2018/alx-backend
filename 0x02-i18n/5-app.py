#!/usr/bin/env python3
"""
5-app.py
"""
from flask import Flask, render_template, g, request
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.before_request
def before_request():
    user_id = int(request.args.get('login_as', 0))

    g.user = users.get(user_id, None)


app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'fr']


@babel.localeselector
def get_locale():
    if g.user and g.user['locale'] in app.config['BABEL_SUPPORTED_LOCALES']:
        return g.user['locale']
    return app.config['BABEL_DEFAULT_LOCALE']


@app.route('/')
def home():
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)
