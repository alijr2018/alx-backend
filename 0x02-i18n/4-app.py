#!/usr/bin/env python3
"""
4-app.py
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _



@babel.localeselector
def get_locale():
    """
    get language form local
    """
    req_local = request.args.get('locale')

    if req_local and req_local in app.config['BABEL_SUPPORTED_LOCALES']:
        return req_local
    else:
        return request.accept_languages.best_match(app.config
                                                   ['BABEL_SUPPORTED_LOCALES'])


@app.route('/')
def index():
    """
    render templates
    """
    return render_template('4-index.html')


app = Flask(__name__)
babel = Babel(app)

app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'fr']

if __name__ == '__main__':
    app.run(debug=True)
