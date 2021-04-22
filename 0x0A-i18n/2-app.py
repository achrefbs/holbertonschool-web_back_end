#!/usr/bin/env python3
"""
a single / route and an index.html template that simply outputs
“Welcome to Holberton” as page title (<title>) and “Hello world”
as header (<h1>).
"""


from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    determine the best match with our supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """index"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
