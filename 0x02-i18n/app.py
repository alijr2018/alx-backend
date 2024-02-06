#!/usr/bin/env python3
"""
7-app.py
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
    get timezone
    """
    url_timezone = request.args.get('timezone')
    if url_timezone:
        try:
            pytz.timezone(url_timezone)
            return url_timezone
        except pytz.UnknownTimeZoneError:
            pass

    if g.user and g.user['timezone']:
        try:
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except pytz.UnknownTimeZoneError:
            pass

    return 'UTC'


@app.before_request
def before_request():
    """
    function and use the app.before_request,
    decorator to make it be executed before al
    """
    user_id = int(request.args.get('login_as', 0))

    g.user = users.get(user_id, None)


app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'fr']


@babel.localeselector
def get_locale():
    """
    get language form local
    """
    url_locale = request.args.get('locale')
    if url_locale and url_locale in app.config['BABEL_SUPPORTED_LOCALES']:
        return url_locale

    if g.user and g.user['locale'] in app.config['BABEL_SUPPORTED_LOCALES']:
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
    render templates
    """
    current_time = datetime.datetime.now(
        pytz.timezone(get_timezone())).strftime("%b %d, %Y, %I:%M:%S %p")

    return render_template('index.html', current_time=current_time)


if __name__ == '__main__':
    app.run(debug=True)
