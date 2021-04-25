#!/usr/bin/env python3
"""
a single / route and an index.html template that simply outputs
“Welcome to Holberton” as page title (<title>) and “Hello world”
as header (<h1>).
"""


from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
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
    determine the best match with our supported languages.
    """
    lg = request.args.get('locale')
    if lg is not None:
        return lg
    if g.user:
        lg = g.user.get("locale")
        if lg:
            return lg
    lg = request.headers.get('locale')
    if lg:
        return lg
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    userID = request.args.get('login_as')
    if not userID:
        return None
    else:
        return users[int(userID)]


@app.before_request
def before_request():
    g.user = get_user()


@app.route('/')
def index():
    """index"""
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run()
