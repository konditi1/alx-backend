#!/usr/bin/env python3
"""
A flask instsance with index.html route rendered
"""
from flask import Flask
from flask import request
from flask import render_template
from flask_babel import Babel


class Config(object):
    """
    Configuration
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

"""Wrap the application with Babel"""
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Gets locale from request object
    """
    locale = request.args.get('locale', '').strip()
    if locale and locale in Config.LANGUAGES:
        return locale
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders a index. html template
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
    