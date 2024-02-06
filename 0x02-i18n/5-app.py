#!/usr/bin/env python3
"""
5-app.py
"""
from flask import Flask, request, render_template, g
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user(user_id):
    return users.get(user_id)

@app.before_request
def before_request():
    user_id = int(request.args.get('login_as', 0))
    g.user = get_user(user_id)
    print(f"before_request - User ID: {user_id}, User: {g.user}")

app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'fr']

@babel.localeselector
def get_locale():
    if g.user and g.user['locale'] in app.config['BABEL_SUPPORTED_LOCALES']:
        print(f"get_locale - User Locale: {g.user['locale']}")
        return g.user['locale']
    print("get_locale - Default Locale")
    return app.config['BABEL_DEFAULT_LOCALE']

@app.route('/')
def home():
    return render_template('5-index.html')

if __name__ == '__main__':
    app.run(debug=True)
