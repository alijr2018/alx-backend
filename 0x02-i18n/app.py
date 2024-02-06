#!/usr/bin/env python3
"""
app.py
"""
from flask import Flask, render_template, g, request
from flask_babel import Babel, _

import pytz
import datetime

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

@babel.timezoneselector
def get_timezone():
    """
    Get the user's timezone.
    """
    url_timezone = request.args.get('timezone')
    if url_timezone:
        try:
            pytz.timezone(url_timezone)
            return url_timezone
        except pytz.UnknownTimeZoneError:
            pass

    if g.user and g.user.get('timezone'):
        return g.user['timezone']

    return 'UTC'

@app.before_request
def before_request():
    """
    Function to be executed before handling each request.
    """
    user_id = int(request.args.get('login_as', 0))
    g.user = users.get(user_id, None)

app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'fr']

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

@app.route('/')
def index():
    """
    Render the index template with the current time.
    """
    user_timezone = get_timezone()
    current_time_user = datetime.datetime.now(pytz.timezone(user_timezone))

    current_time = current_time_user.strftime("%b %d, %Y, %I:%M:%S %p")
    return render_template('index.html', current_time=current_time)

if __name__ == '__main__':
    app.run(debug=True)
