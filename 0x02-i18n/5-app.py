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

@babel.localeselector
def get_locale():
    """
    Get the user's preferred locale.
    """
    url_locale = request.args.get('locale')
    if url_locale and url_locale in app.config['BABEL_SUPPORTED_LOCALES']:
        return url_locale

    if g.user and g.user.get('locale'):
        return g.user['locale']

    header_locale = request.headers.get('Accept-Language')
    if header_locale:
        for lang in header_locale.replace(' ', '').split(','):
            if lang in app.config['BABEL_SUPPORTED_LOCALES']:
                return lang

    return app.config['BABEL_DEFAULT_LOCALE']

@app.before_request
def before_request():
    """
    Function to be executed before handling each request.
    """
    user_id = int(request.args.get('login_as', 0))
    g.user = get_user(user_id)

def get_user(user_id):
    """
    Get user dictionary based on user ID.
    """
    return users.get(user_id, None)

@app.route('/')
def index():
    """
    Render the index template with the appropriate message.
    """
    if g.user:
        message = _("You are logged in as %(username)s.") % {"username": g.user['name']}
    else:
        message = _("You are not logged in.")
    
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
